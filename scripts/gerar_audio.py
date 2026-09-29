#!/usr/bin/env python3
"""Gera o áudio de um roteiro do Radar IA com edge-tts (duas vozes) e ffmpeg.

Uso: gerar_audio.py ROTEIRO.md SAIDA.mp3 [--capa CAPA.png]
Lê as falas "**ANA:**" e "**LEO:**", sintetiza cada uma, concatena com pausas
e grava um MP3 mono a 64 kbps com tags ID3. Imprime a duração em segundos.
"""
import argparse, asyncio, hashlib, json, os, re, subprocess, sys, tempfile
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

DICIONARIO_FONETICO = [
    # Empresas, Laboratórios e Plataformas
    (r"\bHugging Face\b", "Ráguin Féiss"),
    (r"\bHuggingFace\b", "Ráguin Féiss"),
    (r"\bGitHub Copilot\b", "Guít Ráb Có-pilot"),
    (r"\bGitHub\b", "Guít Ráb"),
    (r"\bGitLab\b", "Guít Léb"),
    (r"\bGit\b", "Guít"),
    (r"\bOpenAI\b", "Open Ei-Ai"),
    (r"\bAnthropic\b", "Antrópic"),
    (r"\bDeepSeek\b", "Díp Sík"),
    (r"\bNvidia\b", "Envídia"),
    (r"\bGoogle\b", "Gúgol"),
    (r"\bMicrosoft\b", "Maikro soft"),
    (r"\bMeta\b", "Méta"),
    (r"\bAmazon\b", "Ámazon"),
    (r"\bApple\b", "Épol"),
    (r"\bMistral\b", "Mistral"),
    (r"\bPerplexity\b", "Perpléxiti"),
    (r"\bCohere\b", "Cohíre"),
    (r"\bxAI\b", "Ex-Ei-Ai"),
    (r"\bGroq\b", "Grók"),
    (r"\bCerebras\b", "Serébras"),
    (r"\bScale AI\b", "Scéil Ei-Ai"),
    (r"\bRunway\b", "Rán-uéi"),
    (r"\bMidjourney\b", "Mid-júrnei"),
    (r"\bCursor\b", "Cúrsor"),
    (r"\bReplit\b", "Réplit"),
    (r"\bCloudflare\b", "Cláud-flér"),
    (r"\bDatabricks\b", "Déta-briks"),
    (r"\bSnowflake\b", "Snóu-fléik"),
    (r"\bPalantir\b", "Palantír"),
    (r"\bSalesforce\b", "Séils-fórss"),
    (r"\bHubSpot\b", "Ráb-Spót"),
    (r"\bShopify\b", "Shópi-fai"),
    (r"\bSoftBank\b", "Sóft-Bénk"),
    (r"\bSpaceX\b", "Spéiss-Ex"),
    (r"\bTSMC\b", "TÉ ESSE ÉME CÉ"),
    (r"\bASML\b", "Á ESSE ÉME ÉLE"),
    (r"\bDocker\b", "Dóker"),
    (r"\bKubernetes\b", "Cuber-né-tis"),
    (r"\bVercel\b", "Ver-sél"),
    (r"\bFigma\b", "Fígma"),
    (r"\bSlack\b", "Slék"),
    (r"\bNotion\b", "Nóushon"),
    (r"\bLangChain\b", "Léng-Tchéin"),
    (r"\bOllama\b", "Oláma"),
    (r"\bComfyUI\b", "Cómfi Ú-Í"),
    (r"\bSentry\b", "Séntri"),
    (r"\bSGLang\b", "ÉSSE-GÉ-Léng"),

    # Pessoas Famosas do Setor
    (r"\bAltman\b", "Óltman"),
    (r"\bAmodei\b", "Amodéi"),
    (r"\bDemis Hassabis\b", "Démis Rassábis"),
    (r"\bHassabis\b", "Rassábis"),
    (r"\bSutskever\b", "Sútskever"),
    (r"\bLeCun\b", "Le-Cán"),
    (r"\bJensen Huang\b", "Jénsen Rúang"),
    (r"\bHuang\b", "Rúang"),
    (r"\bElon Musk\b", "Ílon Másk"),
    (r"\bMusk\b", "Másk"),
    (r"\bSatya Nadella\b", "Sátia Nadéla"),
    (r"\bNadella\b", "Nadéla"),
    (r"\bSundar Pichai\b", "Súndar Pitchái"),
    (r"\bPichai\b", "Pitchái"),
    (r"\bZuckerberg\b", "Zúker-berg"),

    # Modelos, Produtos e Linha de Comando
    (r"\bClaude Code\b", "Clód Cód"),
    (r"\bClaude\b", "Clód"),
    (r"\bSonnet\b", "Sónet"),
    (r"\bOpus\b", "Ópus"),
    (r"\bHaiku\b", "Ráiku"),
    (r"\bCopilot\b", "Có-pilot"),
    (r"\bDevin\b", "Dévin"),
    (r"\bDevDay\b", "Dév-Déi"),
    (r"\bChatGPT\b", "Tchét GÉ-PÉ-TÉ"),
    (r"\bGPT-([0-9.]+)\b", r"GÉ-PÉ-TÉ \1"),
    (r"\bGPT\b", "GÉ-PÉ-TÉ"),
    (r"\bGemini\b", "Djémini"),
    (r"\bFlash\b", "Flésh"),
    (r"\bPro\b", "Pró"),
    (r"\bUltra\b", "Últra"),
    (r"\bLlama\b", "Láma"),
    (r"\bQwen\b", "Kiú-uen"),
    (r"\bMixtral\b", "Mikstral"),
    (r"\bCodestral\b", "Cód-estral"),
    (r"\bGrok\b", "Grók"),
    (r"\bFlux\b", "Flúks"),
    (r"\bSora\b", "Sóra"),
    (r"\bVeo\b", "Vé-o"),
    (r"\bWhisper\b", "Wísper"),
    (r"\bGDPval\b", "GÉ-DÉ-PÉ val"),

    # Hardware, Siglas e Protocolos
    (r"\bGPUs\b", "Gê-Pê-Ús"),
    (r"\bGPU\b", "Gê-Pê-Ú"),
    (r"\bCPUs\b", "Cê-Pê-Ús"),
    (r"\bCPU\b", "Cê-Pê-Ú"),
    (r"\bTPUs\b", "Té-Pé-Ús"),
    (r"\bTPU\b", "Té-Pé-Ú"),
    (r"\bNPUs\b", "ÉNE-PÉ-Ús"),
    (r"\bNPU\b", "ÉNE-PÉ-Ú"),
    (r"\bVRAM\b", "VÉ-RÁM"),
    (r"\bAPIs\b", "A-PÉ-Ís"),
    (r"\bAPI\b", "A-PÉ-Í"),
    (r"\bLLMs\b", "Éli-Éli-Émis"),
    (r"\bLLM\b", "Éli-Éli-Émi"),
    (r"\bVLMs\b", "VÉ-ÉLE-ÉMis"),
    (r"\bVLM\b", "VÉ-ÉLE-ÉMi"),
    (r"\bSDKs\b", "ÉSSE-DÉ-CÁs"),
    (r"\bSDK\b", "ÉSSE-DÉ-CÁ"),
    (r"\bCLIs\b", "CÉ-ÉLE-Ís"),
    (r"\bCLI\b", "CÉ-ÉLE-Í"),
    (r"\bUI\b", "Ú-Í"),
    (r"\bUX\b", "Ú-ÉX"),
    (r"\bSaaS\b", "SÁSS"),
    (r"\bAGI\b", "A-GÉ-Í"),
    (r"\bASI\b", "A-ÉSSE-Í"),
    (r"\bRLHF\b", "ÉRE ÉLE HAGÁ ÉFE"),
    (r"\bDNS\b", "DÉ-ÉNE-ÉSSE"),
    (r"\bURLs\b", "Ú-ÉRE-ÉLEs"),
    (r"\bURL\b", "Ú-ÉRE-ÉLE"),
    (r"\bEUA\b", "E-U-A"),
    (r"\bSTF\b", "ÉSSE-TÉ-ÉFE"),
    (r"\bTCU\b", "TÉ-CÉ-Ú"),
    (r"\bLGPD\b", "ÉLE-GÉ-PÉ-DÉ"),
    (r"\bMCP\b", "ÉME-CÉ-PÉ"),
    (r"\bWebMCP\b", "Web ÉME-CÉ-PÊ"),
    (r"\bvLLM\b", "VÉ-Éli-Éli-Émi"),
    (r"\bXSS\b", "XÍSSE-ÉSSE-ÉSSE"),
    (r"\bYAML\b", "IÁ-MEL"),

    # Conceitos Técnicos e Anglicismos Frequentes
    (r"\bprompt injections\b", "prómpt indjécshons"),
    (r"\bprompt injection\b", "prómpt indjécshon"),
    (r"\bprompts\b", "prómpts"),
    (r"\bprompt\b", "prómpt"),
    (r"\bsandboxing\b", "sénd-bóksing"),
    (r"\bsandboxes\b", "sénd-bókses"),
    (r"\bsandbox\b", "sénd-bóks"),
    (r"\bsystem cards\b", "sístem cards"),
    (r"\bsystem card\b", "sístem card"),
    (r"\bbenchmarks\b", "béntch-marks"),
    (r"\bbenchmark\b", "béntch-mark"),
    (r"\bframeworks\b", "fréim-works"),
    (r"\bframework\b", "fréim-work"),
    (r"\bcheckpoints\b", "tchék-points"),
    (r"\bcheckpoint\b", "tchék-point"),
    (r"\bdatasets\b", "déta-sets"),
    (r"\bdataset\b", "déta-set"),
    (r"\bfine-tuning\b", "fain tiúning"),
    (r"\bfine tuning\b", "fain tiúning"),
    (r"\bopen-source\b", "ópen sórs"),
    (r"\bopen source\b", "ópen sórs"),
    (r"\bopen-weight\b", "ópen uéit"),
    (r"\bopen weights\b", "ópen uéits"),
    (r"\bhardware\b", "rárd-uér"),
    (r"\bsoftware\b", "sóft-uér"),
    (r"\bmiddleware\b", "mídol-uér"),
    (r"\bruntimes\b", "rán-taimes"),
    (r"\bruntime\b", "rán-taime"),
    (r"\breleases\b", "rilíses"),
    (r"\brelease\b", "rilís"),
    (r"\bdeployments\b", "diplói-ments"),
    (r"\bdeployment\b", "diplói-ment"),
    (r"\bdeploy\b", "diplói"),
    (r"\bcloud\b", "cláud"),
    (r"\btokens\b", "tókens"),
    (r"\btoken\b", "tóken"),
    (r"\bagentic\b", "eijéntic"),
    (r"\bagents\b", "éigents"),
    (r"\bagent\b", "éigent"),
    (r"\bharness\b", "rár-nes"),
    (r"\bevals\b", "eváls"),
    (r"\beval\b", "evál"),
    (r"\btrade-offs\b", "tréid-ófs"),
    (r"\btrade-off\b", "tréid-óf"),
    (r"\bfeedbacks\b", "fíd-béks"),
    (r"\bfeedback\b", "fíd-bék"),
    (r"\bbig techs\b", "bíg téks"),
    (r"\bbig tech\b", "bíg ték"),
    (r"\bstartups\b", "stárt-áps"),
    (r"\bstartup\b", "stárt-áp"),
    (r"\bred teaming\b", "réd tíming"),
    (r"\bmultimodality\b", "múlti-mo-dáliti"),
    (r"\bmultimodal\b", "múlti-modál"),
    (r"\bembeddings\b", "embédings"),
    (r"\bembedding\b", "embéding"),
    (r"\bRAG\b", "RÉG"),
]

def aplicar_fonetica(t):
    for padrao, substituto in DICIONARIO_FONETICO:
        t = re.sub(padrao, substituto, t, flags=re.IGNORECASE)
    return t

def limpar(t):
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)   # links → texto
    t = re.sub(r"[*_`#>]+", "", t)                      # marcações
    t = t.replace("→", "").replace("·", ",")
    t = aplicar_fonetica(t)
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

def concatenar(itens, pasta, saida, meta, capa, intro=None, outro=None):
    lista = pasta / "lista.txt"
    with open(lista, "w") as f:
        if intro and Path(intro).exists():
            f.write(f"file '{Path(intro).resolve()}'\n")
            f.write(f"file '{silencio(pasta, 'pausa_intro.mp3', 0.5)}'\n")

        for i, (quem, _) in enumerate(itens):
            if quem == "PAUSA":
                f.write(f"file '{silencio(pasta, 'bloco.mp3', PAUSA_BLOCO)}'\n")
            else:
                f.write(f"file '{pasta / f'{i:04d}.mp3'}'\n")
                f.write(f"file '{silencio(pasta, 'fala.mp3', PAUSA_FALA)}'\n")

        if outro and Path(outro).exists():
            f.write(f"file '{silencio(pasta, 'pausa_outro.mp3', 0.5)}'\n")
            f.write(f"file '{Path(outro).resolve()}'\n")

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
    ap.add_argument("--intro", default="assets/audio/intro.mp3", help="Caminho da vinheta de introdução")
    ap.add_argument("--outro", default="assets/audio/outro.mp3", help="Caminho da vinheta de encerramento")
    a = ap.parse_args()
    texto = Path(a.roteiro).read_text(encoding="utf-8")
    meta, corpo = front_matter(texto)
    sha = hashlib.sha256(texto.encode("utf-8")).hexdigest()
    itens = falas(corpo)
    n = sum(1 for q, _ in itens if q != "PAUSA")
    if n == 0:
        sys.exit("nenhuma fala ANA/LEO encontrada no roteiro")
    print(f"{n} falas, {sum(len(t.split()) for _, t in itens)} palavras")
    with tempfile.TemporaryDirectory() as tmp:
        pasta = Path(tmp)
        asyncio.run(sintetizar(itens, pasta))
        concatenar(itens, pasta, a.saida, meta, a.capa, intro=a.intro, outro=a.outro)
    d = duracao(a.saida)
    print(f"duração: {int(d//60)}m{int(d%60):02d}s, {os.path.getsize(a.saida)//1024} KB")
    print(json.dumps({"duracao_seg": round(d), "bytes": os.path.getsize(a.saida), "sha256": sha}))

if __name__ == "__main__":
    main()
