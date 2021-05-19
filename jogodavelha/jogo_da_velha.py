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

    def iniciar(self, jogada, jogador):
        print(self.velha())
        while not self.ganhador:
            retorno = self.escolher_lugar(jogada, jogador)
            if retorno:
                print(self.velha())
                return True
            else:
                print(self.velha())
                return "Jogada inválida"

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
                    return True
        return False


jogo = JogoDaVelha("X", "O")
jogo.iniciar(1, "X")
