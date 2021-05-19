class JogoDaVelha:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.ganhador = False
        self.lugares = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    def velha(self):
        tabuleiro = f"""
        _{self.lugares[0][0]}_|_{self.lugares[0][1]}_|_{self.lugares[0][2]}_
        _{self.lugares[1][0]}_|_{self.lugares[1][1]}_|_{self.lugares[1][2]}_
         {self.lugares[2][0]} | {self.lugares[2][1]} | {self.lugares[2][2]}

        """

        return tabuleiro

    def escolher_lugar(self, lugar, jogador):
        for i, k in enumerate(self.lugares):
            for j, l in enumerate(k):
                if lugar == l and isinstance(l, int):
                    self.lugares[i][j] = jogador
        return False



jogo = JogoDaVelha("X", "O")
print(jogo.velha())
jogo.escolher_lugar(1, "X")
jogo.escolher_lugar(2, "O")
jogo.escolher_lugar(3, "X")
print(jogo.velha())