from jogo_da_velha import JogoDaVelha


if __name__ == "__main__":
    jogo = JogoDaVelha("X", "O")
    print(jogo.velha())
    jogo.escolher_lugar(1, "X")
    jogo.escolher_lugar(2, "O")
    jogo.escolher_lugar(3, "X")
    print(jogo.velha())
