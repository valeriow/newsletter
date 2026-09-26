#!/usr/bin/env python3
"""Gera o áudio de um roteiro do Radar IA com edge-tts (duas vozes) e ffmpeg.

Uso: gerar_audio.py ROTEIRO.md SAIDA.mp3 [--capa CAPA.png]
Lê as falas "**ANA:**" e "**LEO:**", sintetiza cada uma, concatena com pausas
e grava um MP3 mono a 64 kbps com tags ID3. Imprime a duração em segundos.
"""
import argparse, asyncio, json, os, re, subprocess, sys, tempfile
from pathlib import Path

import edge_tts

VOZES = {
    "ANA": "pt-BR-FranciscaNeural",
    "LEO": "pt-BR-AntonioNeural",
}
RATE = "+4%"           # levemente mais rápido que o padrão, soa mais natural em conversa
PAUSA_FALA = 0.45      # segundos entre falas
PAUSA_BLOCO = 1.1      # segundos entre blocos (## títulos)
CONCORRENCIA = 4

def front_matter(texto):
    m = re.match(r"---\n(.*?)\n---\n(.*)", texto, re.S)
    if not m:
        return {}, texto
    meta = {}
    for linha in m.group(1).splitlines():
        if ":" in linha:
            k, v = linha.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, m.group(2)

def limpar(t):
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)   # links → texto
    t = re.sub(r"[*_`#>]+", "", t)                      # marcações
    t = t.replace("→", "").replace("·", ",")
    t = re.sub(r"\s+", " ", t).strip()
    return t

def falas(corpo):
    """Lista de ('ANA'|'LEO'|'PAUSA', texto)."""
    itens = []
    for bloco in re.split(r"\n\s*\n", corpo):
        b = bloco.strip()
        if not b:
            continue
        if b.startswith("#"):
            itens.append(("PAUSA", ""))
            continue
        m = re.match(r"\*\*(ANA|LEO)\s*:\*\*\s*(.*)", b, re.S | re.I)
        if m:
            texto = limpar(m.group(2))
            if texto:
                itens.append((m.group(1).upper(), texto))
    return itens

async def sintetizar(itens, pasta):
    sem = asyncio.Semaphore(CONCORRENCIA)
    async def um(i, quem, texto):
        destino = pasta / f"{i:04d}.mp3"
        for tentativa in range(4):
            try:
                async with sem:
                    await edge_tts.Communicate(texto, VOZES[quem], rate=RATE).save(str(destino))
                if destino.stat().st_size > 0:
                    return
            except Exception as e:  # noqa: BLE001
                print(f"[{i}] tentativa {tentativa+1} falhou: {e}", file=sys.stderr)
                await asyncio.sleep(2 * (tentativa + 1))
        raise RuntimeError(f"não foi possível sintetizar a fala {i}")
    await asyncio.gather(*(um(i, q, t) for i, (q, t) in enumerate(itens) if q != "PAUSA"))

def silencio(pasta, nome, seg):
    destino = pasta / nome
    if not destino.exists():
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                        "-t", str(seg), "-c:a", "libmp3lame", "-b:a", "64k", str(destino)], check=True)
    return destino

def concatenar(itens, pasta, saida, meta, capa):
    lista = pasta / "lista.txt"
    with open(lista, "w") as f:
        for i, (quem, _) in enumerate(itens):
            if quem == "PAUSA":
                f.write(f"file '{silencio(pasta, 'bloco.mp3', PAUSA_BLOCO)}'\n")
            else:
                f.write(f"file '{pasta / f'{i:04d}.mp3'}'\n")
                f.write(f"file '{silencio(pasta, 'fala.mp3', PAUSA_FALA)}'\n")
    cmd = ["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lista)]
    if capa:
        cmd += ["-i", capa, "-map", "0:a", "-map", "1:v", "-c:v", "copy", "-disposition:v", "attached_pic"]
    else:
        cmd += ["-map", "0:a"]
    cmd += ["-ac", "1", "-ar", "24000", "-c:a", "libmp3lame", "-b:a", "64k",
            "-metadata", f"title={meta.get('title', 'Radar IA')}",
            "-metadata", "artist=Radar IA", "-metadata", "album=Radar IA — podcast",
            "-metadata", f"date={meta.get('date', '')[:4]}", "-id3v2_version", "3", saida]
    subprocess.run(cmd, check=True)

def duracao(arquivo):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "json", arquivo], capture_output=True, text=True, check=True).stdout
    return float(json.loads(out)["format"]["duration"])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roteiro"); ap.add_argument("saida"); ap.add_argument("--capa")
    a = ap.parse_args()
    meta, corpo = front_matter(Path(a.roteiro).read_text(encoding="utf-8"))
    itens = falas(corpo)
    n = sum(1 for q, _ in itens if q != "PAUSA")
    if n == 0:
        sys.exit("nenhuma fala ANA/LEO encontrada no roteiro")
    print(f"{n} falas, {sum(len(t.split()) for _, t in itens)} palavras")
    with tempfile.TemporaryDirectory() as tmp:
        pasta = Path(tmp)
        asyncio.run(sintetizar(itens, pasta))
        concatenar(itens, pasta, a.saida, meta, a.capa)
    d = duracao(a.saida)
    print(f"duração: {int(d//60)}m{int(d%60):02d}s, {os.path.getsize(a.saida)//1024} KB")
    print(json.dumps({"duracao_seg": round(d), "bytes": os.path.getsize(a.saida)}))

if __name__ == "__main__":
    main()
