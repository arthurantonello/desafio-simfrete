import sys
from utils_cep import (
    separar_blocos,
    construir_grafo,
    obter_cidade_por_cep,
    dijkstra
)

def main():
    texto = sys.stdin.read()
    bloco_cidades, bloco_linhas, linha_ceps = separar_blocos(texto)
    grafo = construir_grafo(bloco_linhas)

    # Parse dos dois CEPs finais
    ceps = [int(x) for x in linha_ceps.replace(',', ' ').split()]
    cep1, cep2 = ceps

    cidade1 = obter_cidade_por_cep('\n'.join(bloco_cidades), cep1)
    cidade2 = obter_cidade_por_cep('\n'.join(bloco_cidades), cep2)

    custo, caminho = dijkstra(grafo, cidade1, cidade2)
    if caminho:
        print(' -> '.join(caminho))
        print(f'Custo total: {custo:.2f}')
    else:
        print(f'Não há caminho de {cidade1} até {cidade2}.')

if __name__ == '__main__':
    main()
