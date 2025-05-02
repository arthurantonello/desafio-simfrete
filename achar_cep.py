import sys
from utils_cep import linha_valida

def main():
    cidades = []

    # Ler as cidades até encontrar o breakpoint
    for linha in sys.stdin:
        linha = linha.strip() # Para remover espaços e o \n do stdin
        if linha == '--':
            break
        
        infos = linha.split(',')
        if not linha_valida(infos):
            continue

        nome, inicio, fim  = infos[0].strip(), infos[1].strip(), infos[2].strip()

        # Assegura que inicio é menor que o fim
        if inicio > fim:
            inicio, fim = fim, inicio

        cidades.append((int(inicio), int(fim), nome))

    # Ordena por tamanho do intervalo (menor primeiro)
    cidades.sort(key=lambda intervalo: intervalo[1] - intervalo[0])

    # Caso queira manter a lista original inalterada, porém é menos eficiente
    #cidades_ordenadas = sorted(cidades, key=lambda intervalo: intervalo[1] - intervalo[0])

    # Ler o CEP alvo
    cep_alvo = None
    for linha in sys.stdin:
        if linha: # Ignora linhas vazias
            cep_alvo = int(linha.strip())
            break

    if cep_alvo is None:
        print('Nenhum CEP informado após o "--" para pesquisa.')
        return

    # Encontra o cep no intervalo
    for inicio, fim, nome in cidades:
        if inicio <= cep_alvo <= fim:
            print(f'O CEP alvo {cep_alvo} se encontra em {nome}.')
            return

    print('CEP não encontrado.')

if __name__ == '__main__':
    main()