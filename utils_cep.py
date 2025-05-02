import sys
import subprocess
import heapq

# Script original de leitura de CEPs
PARSER = "achar_cep.py"

# Lê e retorna a cidade correspondente ao CEP através do parser
def obter_cidade_por_cep(bloco_cidades: str, cep: int) -> str:
    entrada = bloco_cidades.strip() + "\n--\n" + f"{cep}\n" # Adicionado uma garantia de início e término de blocos com o "--"
    proc = subprocess.run(
        [sys.executable, PARSER],
        input = entrada,
        text = True,
        capture_output = True # Captura retorno bem sucedido ou erro se houver
    )
    if proc.returncode != 0:
        raise RuntimeError(f"Parser erro (status {proc.returncode})")
    saida = proc.stdout.strip()
    marcador = 'se encontra em' # Separador para strings como: "O CEP X se encontra em 'Nome da Cidade'"
    if marcador in saida:
        return saida.split(marcador)[1].strip().strip('.') # Retorna o que vem depois do marcador
    raise ValueError(f"CEP não encontrado: {cep}")

# Separa o input em blocos de cidades, ligações e linha de CEPs
def separar_blocos(texto: str):
    linhas = texto.strip().split('\n')

    # Encontra os índices onde aparecem os separadores "--"
    separadores = []
    for i in range(len(linhas)):
        linha = linhas[i]
        if linha.strip() == '--':
            separadores.append(i)

    if len(separadores) < 2:
        raise ValueError("Formato inválido: são necessários dois separadores '--'")

    # Divide o texto em três blocos: cidades, conexões e CEPs
    indice1 = separadores[0]
    indice2 = separadores[1]

    bloco_cidades = linhas[:indice1]               # Antes do primeiro separador
    bloco_conexoes = linhas[indice1 + 1 : indice2]   # Entre os dois separadores
    bloco_ceps = linhas[indice2 + 1:]              # Depois do segundo separador

    for linha in bloco_ceps:
        if linha:  # ignora linhas vazias
            return bloco_cidades, bloco_conexoes, linha

    raise ValueError("Não foi encontrada uma linha de CEPs no final")

def normalizar_linhas(linha):
    return [p.strip() for p in linha.split(',')]  # List comprehension

def linha_valida(infos):
    return len(infos) == 3

# Constrói intervalos de CEP para cada cidade
def construir_intervalos(bloco_cidades: list[str]):
    intervalos = []
    for linha in bloco_cidades:
        infos = normalizar_linhas(linha)
        if not linha_valida(infos):
            continue
        nome, inicio_txt, fim_txt = infos
        try:
            inicio, fim = int(inicio_txt), int(fim_txt)
        except ValueError:
            continue
        if inicio > fim: inicio, fim = fim, inicio
        intervalos.append((nome, inicio, fim))
    return intervalos

# Constrói grafo não-direcionado
def construir_grafo(bloco_conexoes: list[str]):
    grafo = {}
    for linha in bloco_conexoes:
        infos = normalizar_linhas(linha)
        if not linha_valida(infos):
            continue
        origem, destino, custo_txt = infos
        try:
            custo = float(custo_txt)
        except ValueError:
            continue
        grafo.setdefault(origem, []).append((destino, custo))
        grafo.setdefault(destino, []).append((origem, custo))
    return grafo

# Aplica o algoritmo de Dijkstra, considerando caminho bi-direcional
def dijkstra(grafo, inicio, destino):
    distancia = {inicio: 0.0}
    heap = [(0.0, inicio, [inicio])]
    while heap:
        custo, nodo, caminho = heapq.heappop(heap)
        if custo > distancia.get(nodo, float('inf')):
            continue
        if nodo == destino:
            return custo, caminho
        for vizinho, peso in grafo.get(nodo, []):
            novo_custo = custo + peso
            if novo_custo < distancia.get(vizinho, float('inf')):
                distancia[vizinho] = novo_custo
                heapq.heappush(heap, (novo_custo, vizinho, caminho + [vizinho]))
    return None, None