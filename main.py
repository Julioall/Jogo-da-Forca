# BIBLIOTECAS NECESSARIAS
from os import system, name
import random

# FUNÇÃO PRINT COLORIDO


def colored_print(texto="Digite um texto!", cor="branco", fundo="preto", negrito=False, sublinhado=False, italico=False):
    # Padrões de cores
    padroes_cores = {
        "preto": "30",
        "vermelho": "31",
        "verde": "32",
        "amarelo": "33",
        "azul": "34",
        "magenta": "35",
        "ciano": "36",
        "branco": "37",
    }
    # Padrões de cores de fundo
    padroes_cores_fundo = {
        "preto": "40",
        "vermelho": "41",
        "verde": "42",
        "amarelo": "43",
        "azul": "44",
        "magenta": "45",
        "ciano": "46",
        "branco": "47",
    }

    # Verificar se a cor e o fundo especificados existem nos padrões de cores
    if cor not in padroes_cores:
        print("A cor especificada não existe.")
        return

    if fundo not in padroes_cores_fundo:
        print("A cor de fundo especificada não existe.")
        return

    # Obter o código ANSI das cores e do estilo
    codigo_cor = padroes_cores[cor]
    codigo_fundo = padroes_cores_fundo[fundo]
    codigo_estilo = ""

    if negrito:
        codigo_estilo += "1;"
    if italico:
        codigo_estilo += "3"
    if sublinhado:
        codigo_estilo += "4;"

    # Imprimir o texto colorido no terminal com o estilo aplicado
    print(f"\033[{codigo_estilo}{codigo_cor};{codigo_fundo}m{texto}\033[0m")

# LIMPAR A TELA


def limpar_tela():
    # Console do Windows
    if name == 'nt':
        _ = system('cls')
    # Console do mac ou linux
    else:
        _ = system('clear')

# TITULO DO JOGO


def titulo():
    colored_print("=" * 50, cor="amarelo")
    colored_print("Bem-vindo(a) ao Jogo da Forca!".center(50).upper(),
                  cor="verde", negrito=True)
    colored_print("Adivinhe a palavra abaixo:".center(50).upper(), cor="ciano")
    colored_print("=" * 50, cor="amarelo")
    print("\n")

# FUNÇÃO DE FRAMES


def inforcado(chances):
    # Lista de estágios da forca
    estagios = ["""
        ----------
        |        |
        |        
        |        
        |
        |________
    """,
                """
        ----------
        |        |
        |        O
        |        
        |
        |________
    """,
                """
        ----------
        |        |
        |        O
        |        |
        |
        |________
    """,
                """
        ----------
        |        |
        |        O
        |       /|
        |
        |________
    """,
                """
        ----------
        |        |
        |        O
        |       /|\\
        |
        |________
    """,
                """
        ----------
        |        |
        |        O
        |       /|\\
        |      _/ 
        |________
    """,
                """
        ----------
        |        |
        |        O
        |       /|\\
        |      _/ \_
        |________
    """]
    estagios = estagios[::-1]
    print(estagios[chances])

# FUNÇÃO LOOP DO JOGO


def jogo():
    titulo()
    while True:
        # LISTA DE PALAVRAS DO JOGO
        palavras = [
            "abacate", "abacaxi", "acai", "acerola", "ameixa", "banana", "caju", "caqui", "carambola", "cereja",
            "cidra", "coco", "damasco", "figo", "framboesa", "groselha", "guava", "jabuticaba", "jaca", "kiwi",
            "laranja", "lima", "limao", "maca", "mamao", "manga", "maraqua", "melancia", "melao", "mexerica",
            "mirtilo", "morango", "nectarina", "pequi", "pera", "pessego", "pitanga", "pitaya", "romaa", "sapoti",
            "seriguela", "tamarindo", "tangerina", "uva", "abiu", "aceroleira", "atemoia", "bacaba", "bacuri",
            "buriti", "cabeludinha", "cacau", "cacauacu", "cagaita", "caja", "canastra", "caramuru", "carapeba",
            "casco-de-velho", "caxeta", "cedro", "centra", "ceriguela", "chorao", "coco-da-baia", "coco-do-mar",
            "coco-preto", "condessa", "coracao-de-negro", "cuba", "cuieira", "cujarana", "cumaru", "curua",
            "embauba", "embu", "endrin", "excalete", "feijoa", "fermiao", "frutadeira", "fava", "gabiroba",
            "gervao", "graviola", "genipapo", "gobo", "goyaba", "goiaba", "guabiroba", "guarana", "guariroba",
            "guiaba", "guaiba", "hera", "hidromele", "hipericao", "horseradish", "ibapoa", "imbauba", "ingu",
            "ipanema", "ipeca", "jacata", "jambolao", "jameri", "janipaba", "japota", "japura", "jatai", "jatoba",
            "jeriv", "juazeriro", "jucarazeiro", "jua", "jubeba", "jurubeba", "labrusca", "licuri", "limao-galego",
            "limao-rosa", "lipia", "macaa-paulista", "macaa-peruana", "magnolia", "mamoeiro", "mamoncillo", "mandarim",
            "maracaja", "maranha", "marolo", "mata-cabra", "mexerica-rio", "mirtilo", "mogno", "mognos", "molinillo",
            "murta", "nago", "nanjeira", "nespera", "nin", "oliveira", "orange", "orcina", "orelha-de-macaco",
            "orvalha", "oxalis", "pacovan", "palm", "paran", "pata-de-vaca", "peari", "perado", "piche",
            "pinhao", "pitombeira", "piuva", "pixirica", "planta-mel", "polpa", "poro-poro", "puaia", "pupunha",
            "queiui", "rasteira", "sapota", "sorva", "taperiba", "tatajuba", "tucuma", "tuiuba", "ucuuba",
            "urucum", "uvaia", "uvaiapura", "vasculaco", "vermut", "visgueiro", "xantelasma", "xat", "xinxim"]

        # ESCOLHER PALAVRA RANDOMICAMENTE
        palavra = random.choice(palavras)

        # LIST COMPREHENSION
        # Para cada letra da palavra ele adiciona um _ para mostra para o usuário quantas letras tem a palavra
        letras_descobertas = ['_' for letra in palavra]

        # LISTA DE LETRAS ERRADAS
        letras_erradas = []
        # LOOP ENQUANTO CHANCES FOR MAIOR QUE ZERO
        chances = 6
        while chances > 0:
            # IMPRIMIR LETRAS DESCOBERTAS
            print(" ".join(letras_descobertas))
            print("\nChances restantes: ", chances)
            print("Letras erradas:", " ".join(letras_erradas))
            # TENTATIVAS
            inforcado(chances)
            tentativa = input("Digite uma letra: ").lower()
            # VERIFICA SE O USUARIO DIGITOU APENAS UM CARACTER E SE ELE É UMA LETRA
            if len(tentativa) == 1 and tentativa.isalpha():
                if tentativa not in letras_erradas:
                    # VERIFICAR SE A LETRA EXISTE NA PALAVRA
                    if tentativa in palavra:
                        index = 0
                        # VERIFICA SE A LETRA EXISTE EM CADA INDICE DA PALAVRA
                        for letra in palavra:
                            # VERIFICAR SE A TENTATIVA É IGUAL A LETRA
                            if tentativa == letra:
                                # ADICIONA A LETRA NA POSIÇÃO DESCOBERTA DA PALAVRA NA LISTA letra_descoberta
                                letras_descobertas[index] = letra
                            # INCLEMENTA UM A CADA VERIFICAÇÃO
                            index += 1

                    # SE A LETRA NÃO FOR ENCONTRADA NA PALAVRA
                    else:
                        # PERDE UMA CHANCE
                        chances -= 1
                        # LETRA É ADICIONADA A LISTA DE LETRAS ERRADAS
                        letras_erradas.append(tentativa)

                    # VERIFICAR SE O JOGADOR COMPLETOU A PALAVRA
                    if "_" not in letras_descobertas:  # SE O _ NÃO ESTIVER MAIS PRESENTE A LISTA letra_descoberta
                        print("Você venceu, a palavra era:")
                        colored_print(f"{palavra.upper()}", cor="verde")
                        break
                else:
                    print(f"Você já escolheu essa letra: {tentativa}")
            else:
                print("Parece que você digitou algo errado!")
                print("Digite novamente!")
                continue

        if chances == 0:
            colored_print(
                f"Você gastou todas as suas chances!\nA palavra éra: {palavra}", cor="vermelho")
        jogar = input("Jogar novamente: 's' (Sim) ou 'n' (Não): ").lower()
        if jogar == "y" or "n":
            if jogar == "s":
                pass

            else:
                print("Jogo finalizado!")
                break
        else:
            colored_print("Opção invalida!", cor="vermelho")


# INICIANDO O JOGO
jogo()
