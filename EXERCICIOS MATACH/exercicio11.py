jogador1 = input("Jogador 1: ").lower()
jogador2 = input("Jogador 2: ").lower()

match (jogador1, jogador2):
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("Jogador 2 venceu")
    case _ if jogador1 == jogador2:
        print("Empate")
    case _:
        print("Jogada inválida")
