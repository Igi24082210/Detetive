import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('musicadetetive.mp3') #musica de fundo
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)
import random
from datetime import datetime, timedelta  # Relógio do jogo

print('''\033[33m
                                                    REGRAS DO JOGO
                            -Cada rodada você poderá receber uma pista ou fazer um palpite.
                            -Você poderá dar o palpite apenas uma vez, se acertar o local e o assassino você ganha, 
                            caso contrario o jogo acaba e você perde sem descobrir o verdadeiro culpado.
                            -Caso você acerte apenas uma das duas  perguntas (Local ou assassino), você ainda perderá.
                            -Se o tempo encerrar (06:00) e você não tenha consigo encontrar as respostas para as perguntas o jogo encerra e você perde. 
                            -Você poderá utilizar o mapa para ajudar na resolução  do caso.
                            -Tome cuidado com as pistas, nem todas são verdadeiras.
\033[0m''')
print('*'*160)
# Lista de nomes dos personagens e suas descrições
personagens = {
    "FURA-CÃO": "conheceu o Vovô Coxa durante um clássico do Atletiba, quando assumiu seu papel de mascote. Embora se encontrasse regularmente, Fura-Cão sempre acreditou que o Vovô Coxa, com sua fama, ofuscava seu próprio brilho. Ele queria ser o maior ícone do futebol paranaense, mas via o Vovô Coxa como um obstáculo.",
    "QUATI": "conheceu o Vovô Coxa há três anos, em um evento de mascotes. Embora respeitasse o Vovô Coxa, sempre manteve uma relação distante. Quati, ambicioso, acreditava que o Vovô Coxa favorecia os clubes maiores, o que impedia o crescimento de Foz do Iguaçu. Isso gerou ressentimento.",
    "DOGÃO": "se conheceram em um amistoso entre seus clubes e mantiveram respeito mútuo. Com o tempo, Dogão começou a se ressentir das opiniões de Vovô Coxa sobre o Maringá, acreditando que as interferências eram antiquadas e desnecessárias.",
    "TUBARÃO": "Tubarão e Vovô Coxa já compartilharam momentos de glória. Contudo, depois de Tubarão se envolver em escândalos de apostas, o Vovô Coxa decidiu ajudá-lo, dizendo que ele deveria enfrentar as consequências. Isso criou uma mágoa forte entre eles.",
    "GRALHA": "conheceu o Vovô Coxa em um evento de mascotes. Ansioso por reconhecimento, Gralha sentiu que o Vovô Coxa monopolizava as atenções, deixando pouco espaço para os mascotes mais novos. Ele via o Vovô Coxa como um obstáculo à sua ascensão.",
    "FANTASMA": "Fantasma e Vovô Coxa formaram uma amizade sólida quando o Operário começou a crescer no cenário estadual. No entanto, o Fantasma descobriu que o Vovô Coxa sabia de um segredo comprometido. Com medo de que o Vovô Coxa revelasse, Fantasma passou a vê-lo como uma ameaça."
}

# Locais possíveis da morte do Vovô Coxa
locais = ["Cozinha", "Banheiro", "Sala", "Jardim", "Piscina"]

# Seleciona um local da morte aleatório
local_morte = random.choice(locais)


def associar_personagens_aleatoriamente(personagens):
    numeros = list(range(6))
    random.shuffle(numeros)
    return dict(zip(personagens.keys(), numeros))

associacoes = associar_personagens_aleatoriamente(personagens)
# Função para gerar pistas com base no local
def gerar_pistas(associacoes, local_morte):

    if local_morte == "Cozinha":
        return [
            f"{list(associacoes.keys())[0]} passou a noite no corredor",
            f"Se {list(associacoes.keys())[2]} estava no banheiro, então {list(associacoes.keys())[1]} estava no quarto",
            f"Ou {list(associacoes.keys())[1]} ou {list(associacoes.keys())[2]} estava no banheiro",
            f"Quem estava no banheiro viu {list(associacoes.keys())[3]} e {list(associacoes.keys())[4]} na piscina",
            f"Se e somente se {list(associacoes.keys())[4]} passou a festa inteira na parte externa, então {list(associacoes.keys())[3]} passou um tempo na parte interna.",
	        f"{list(associacoes.keys())[2]} viu {list(associacoes.keys())[4]} no jardim.",
	        f"Ninguém entrou ou saiu do corredor.",
	        f"{list(associacoes.keys())[3]} e {list(associacoes.keys())[5]} chegaram atrasados na festa.",
            f"{list(associacoes.keys())[0]} ouviu apenas alguém correndo na sala.",
	        f"{list(associacoes.keys())[4]} amanheceu na piscina.",
	        f"Não havia ninguém no escritório.",
            f"{list(associacoes.keys())[5]} e encontrou o corpo do vovô coxa na cozinha e {list(associacoes.keys())[3]} estava proximo."
	        # PISTAS EM CONTRADIÇÃO
            f"Se {list(associacoes.keys())[1]} não estava no banheiro então {list (personagens.keys())[2]} não estava no banheiro.",
	        f"{list(associacoes.keys())[0]} e {list(associacoes.keys())[3]} estavam na cozinha.",
	        f"{list(associacoes.keys())[5]} estava passeando pela casa.",
        ]
    elif local_morte == "Banheiro":
        return [
           f" {list(associacoes.keys())[0]} estava no jardim e viu {list(associacoes.keys())[1]} saindo do banheiro antes do crime.",
            f"Não foi encontrado sangue na sala .",
            f"{list(associacoes.keys())[3]} ou {list(associacoes.keys())[5]} estavam na piscina no momento do crime.",
            f"{list(associacoes.keys())[4]} foi visto entrando no banheiro com o Vovô Coxa pouco antes da morte.",
            f"{list(associacoes.keys())[5]} encontrou o corpo dentro do banheiro , e {list(associacoes.keys())[0]} e {list(associacoes.keys())[1]} estavam próximos .",
	        f"{list(associacoes.keys())[1]} ou  {list(associacoes.keys())[4]} ou {list(associacoes.keys())[5]} estavam conversando com o Vovô Coxa antes da morte no jardim.",
	        f"{list(associacoes.keys())[3]} e Vovô Coxa discutiram na noite anterior.",
	        f"{list(associacoes.keys())[1]} foi visto saindo rapidamente do banheiro.",
	        f"{list(associacoes.keys())[4]} foi visto irritado perto da sala.",	
	        f"{list(associacoes.keys())[0]} escutou {list(associacoes.keys())[1]} resmungando pelo corredor.",
	        f"Se {list(associacoes.keys())[3]} não estava na piscina no momento do crime {list(associacoes.keys())[5]} também não estava.",
	        f" Se {list(associacoes.keys())[1]} não estava conversando com o Vovô Coxa antes da morte no jardim {list(associacoes.keys())[5]} e {list(associacoes.keys())[4]} não estavam conversando também.",
            f"{list(associacoes.keys())[1]} jogou futebol ontem e discutiu com o vovô coxa.",
        ]
    elif local_morte == "Sala":
        return [
            f"Se {list(associacoes.keys())[0]} estava no jardim, então {list(associacoes.keys())[1]} foi visto saindo da sala.",
	        f"{list(associacoes.keys())[2]} encontrou o corpo do Vovô Coxa perto do corredor.",
	        f"{list(associacoes.keys())[5]} ou {list(associacoes.keys())[4]} foi visto na piscina.",
	        f"{list(associacoes.keys())[3]} ou {list(associacoes.keys())[5]} estavam na cozinha no momento do crime.",
	        f"{list(associacoes.keys())[0]} encontrou {list(associacoes.keys())[4]} discutindo com o Vovô Coxa na sala antes do crime.",
	        f"{list(associacoes.keys())[2]} encontrou o corpo dentro da sala, e {list(associacoes.keys())[0]} e {list(associacoes.keys())[1]} vieram.",
	        f"{list(associacoes.keys())[1]} e {list(associacoes.keys())[4]} ou {list(associacoes.keys())[3]} estavam conversando com o Vovô Coxa antes do crime.",
	        f"{list(associacoes.keys())[0]} discutiu com o Vovô Coxa na noite anterior, após um jogo de futebol.",
	        f"{list(associacoes.keys())[1]} foi visto saindo rapidamente da sala logo após uma discussão.",
	        f"{list(associacoes.keys())[1]} foi visto bebendo com o Vovô Coxa na sala antes do assasinato.",
	        f"{list(associacoes.keys())[5]} foi visto no escritório",
            f"{list(associacoes.keys())[1]} foi visto na sala",
	        f"Se {list(associacoes.keys())[5]} não foi visto na piscina, então {list(associacoes.keys())[4]} também não foi visto na piscina.",
	        f"Se {list(associacoes.keys())[3]} não estava na cozinha no momento do crime então {list(associacoes.keys())[5]} não estava na cozinha também.",
        ]
    elif local_morte == "Jardim":
        return [
            f"{list(associacoes.keys())[0]} estava no escritório quando viu {list(associacoes.keys())[1]} saindo do banheiro.",
            f"{list(associacoes.keys())[3]} estava discutindo com o Vovô minutos antes da morte.",
            f"Não havia nenhuma arma no local.",
            f"{list(associacoes.keys())[3]} ou {list(associacoes.keys())[1]} foram vistos perto do escritório durante a noite.",
            f"{list(associacoes.keys())[0]} encontrou {list(associacoes.keys())[4]} no  jardim com as mãos sujas de terra. ",
		    f"{list(associacoes.keys())[2]} estava na cozinha quando ouviu gritos vindos do jardim.",
		    f"{list(associacoes.keys())[1]}, {list(associacoes.keys())[3]} ou {list(associacoes.keys())[4]} estavam próximos ao jardim ao encontrar o corpo .",
		    f"{list(associacoes.keys())[3]} jogou futebol ontem com o Vovô Coxa , mas discutiram depois.",
		    f"{list(associacoes.keys())[1]} foi visto saindo correndo do jardim logo após uma discussão.",
		    f"{list(associacoes.keys())[4]} foi visto  bebendo com o Vovô Coxa no início da noite.",
		    f" {list(associacoes.keys())[5]} dormiu na sala.",
		    f"{list(associacoes.keys())[2]} viu {list(associacoes.keys())[4]} entrando na sala.",
		    f"Se {list(associacoes.keys())[1]} não estava próximos ao jardim ao encontrar o corpo, {list(associacoes.keys())[3]} e {list(associacoes.keys())[4]} também não estavam.",
		    f"Se {list(associacoes.keys())[0]} não encontrou {list(associacoes.keys())[4]} , {list(associacoes.keys())[4]} não estava com a mão suja.",
		    f"Se {list(associacoes.keys())[1]} não foi visto perto do escritorio {list(associacoes.keys())[3]} não foi visto perto do escritorio.",
        ]
    elif local_morte == "Piscina":
        return [
            f" {list(associacoes.keys())[0]}  foi a jardim e encontrou {list(associacoes.keys())[1]}.",
	        f" {list(associacoes.keys())[2]}  encontrou o corpo morto.",
	        f" Não foi encontrado sangue no banheiro.",
	        f" {list(associacoes.keys())[3]} ou {list(associacoes.keys())[5]} estavam na sala.",
 	        f" {list(associacoes.keys())[5]} foi a cozinha e avistou {list(associacoes.keys())[4]} com uma faca.",
            f" {list(associacoes.keys())[2]}  avistou o corpo da janela do banheiro.{list(associacoes.keys())[0]}  e {list(associacoes.keys())[1]} estavam próximos do local.",
            f" {list(associacoes.keys())[1]} ou {list(associacoes.keys())[4]} ou {list(associacoes.keys())[2]}  estavam conversando com o vovô antes da morte.",
            f" {list(associacoes.keys())[3]} jogou futebol ontem com vovô coxa e discutiu.",
            f" O culpado interagiu com Vovô Coxa na noite do crime ou na anterior.",
            f" {list(associacoes.keys())[4]} foi avistado bebendo com vovô coxa .",
            f" {list(associacoes.keys())[1]} antes de encontrar {list(associacoes.keys())[0]} estava na piscina.",
            f"  Se {list(associacoes.keys())[5]} estava na sala então {list(associacoes.keys())[1]} poderia estar no jardim",   
            f"  Se e somente se {list(associacoes.keys())[0]}  não estava no jardim então {list(associacoes.keys())[1]}  estava no jardim.",
            f" Se {list(associacoes.keys())[2]}  estava conversando  com Vovô Coxa e {list(associacoes.keys())[1]}  não estava conversando com o Vovô Coxa.",
        ]
    return []

# Gera as pistas baseadas no local da morte
pistas = gerar_pistas(associacoes, local_morte)


# Função para o jogo
def jogo_detetive(personagens,associacoes, locais, pistas, local_morte):
    print("                                                               \033[32mSuspeitos:\033[0m")
    for name, desc in personagens.items():
        print(f"{name}: {desc}")
        print("." * 150)
    suposicao_restante = 1  # Número de tentativas para adivinhar

    if local_morte == "Cozinha":
        assassino = list(associacoes.keys())[3]
    elif local_morte == "Banheiro":
        assassino = list(associacoes.keys())[1]
    elif local_morte == "Sala":
        assassino = list(associacoes.keys())[1]
    elif local_morte == "Jardim":
        assassino = list(associacoes.keys())[4]
    elif local_morte == "Piscina":
        assassino = list(associacoes.keys())[1]

    tempo_inicio = datetime.strptime("00:00", "%H:%M")
    tempo_final = datetime.strptime("06:00", "%H:%M")
    tempo_atual = tempo_inicio
    dicas_dadas = 0

    acertou_local = False
    acertou_assassino = False

    while suposicao_restante > 0:
        if tempo_atual >= tempo_final:
            print("\n\033[31mO tempo acabou. O jogo terminou.\033[0m")
            break

        tempo_restante = tempo_final - tempo_atual
        print(
            f"\n                                                       \033[32mHorário atual:\033[0m {tempo_atual.strftime('%H:%M')}")
        print(f"                                                       \033[31mTempo restante:\033[0m {tempo_restante}")

        print("\033[32m \nEcolha uma opção:\033[0m")
        print('-' * 10)
        print("\033[33m 0 \033[0m  — Dica")
        print(f"\033[33m 1 \033[0m  — Adivinhar ({suposicao_restante} tentativas restantes)")
        print("\033[33m 2 \033[0m  — Ver mapa")
        escolha = input("\033[33m Opção: \033[0m ").strip()
        print('-' * 10)

        if escolha == "0":  # Solicitar uma dica
            if dicas_dadas < len(pistas):
                print(f"\033[33m Dica\033[0m : {pistas[dicas_dadas]}")
                dicas_dadas += 1
                tempo_atual += timedelta(minutes=30)
            else:
                print("\033[31mNão há mais dicas disponíveis.\033[0m")

        elif escolha == "1":  # Fazer uma tentativa de adivinhação
            adivinhar_local = input("Local: ").strip().title()
            adivinhar_assassino = input("Assassino: ").strip().upper()

            if adivinhar_local == local_morte:
                acertou_local = True
            else:
                print(f"\033[31mLocal incorreto. {adivinhar_local} não é o local da morte.\033[0m")

            if adivinhar_assassino in personagens:
                if adivinhar_assassino == assassino:
                    acertou_assassino = True
                else:
                    print(f"\033[31m{adivinhar_assassino} não é o assassino.\033[0m")
            else:
                print("\033[31mSuspeito inválido. Tente novamente.\033[0m")

            if acertou_local and acertou_assassino:
                print("\033[32mParabéns! Você acertou o local e o assassino!\033[0m")
                print('_' * 30)
                break
            else:
                suposicao_restante -= 1
                tempo_atual += timedelta(minutes=30)
                if acertou_local:
                    print("\033[34mVocê acertou o local, mas errou o assassino.\033[0m")
                elif acertou_assassino:
                    print("\033[34mVocê acertou o assassino, mas errou o local.\033[0m")
        elif escolha == "2":  # seleciona o mapa
            print('''\033[32m
            ┌───────────────────────────────────────────────────────────┐
            │                                ┌─────────────┐            │
            │                       │        │   PISCINA   │            │
            │             ┌─────────┴────────┴─────◇───────┴────────────│                                              
            │             │                │           │                │
            │             ◇  QUARTO        │ BANHEIRO  │   ESCRITÓRIO   │
            │             │                                             │
            │             │                │           │                │
            │   JARDIM    │───   ──────────┴───────────┴────────   ─────│                                             
            │             │                CORREDOR                     │
            │             │─────────   ─────────────────────────────────│                                             
            │             │                               │             │
            │             │                               │             │
            │             │              SALA                           │
            │                                             │   COZINHA   │
            │             │                               │             │
            │             │                               │             │
            └─────────────┴───────────────────────────────┴─────────────┘\033[0m''')

        else:
            print("\033[31mOpção inválida. Escolha 0 para Dica, 1 para Adivinhar ou 2 para ver Mapa.\033[0m")

    if suposicao_restante == 0 or tempo_atual >= tempo_final:
        print("\033[34m\nO jogo terminou.\033[0m")
        print(f"\033[34mO assassino real era {assassino}\033[0m. \033[32m O local correto era {local_morte}.\033[0m")
        print('_' * 30)


# Executa o jogo
jogo_detetive(personagens,associacoes, locais, pistas, local_morte)