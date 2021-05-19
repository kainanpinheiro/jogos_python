class JogoDaVelha:
    def __init__(self, jogador1, jogador2):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        self.__ganhador = False
        self.lugares = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    def get_ganhador(self):
        return self.__ganhador

    def iniciar(self, jogada, jogador):
        print(self.velha())
        retorno = self.escolher_lugar(jogada, jogador)
        if retorno:
            print(self.velha())
            retorno = self.verificar_ganhador()
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

    def verificar_ganhador(self):
        ganhou = list()

        # Verifica valores na horizontal
        for lugar in self.lugares:
            ganhou.append(self.validar_valores(lugar))

        # Verifica valores na vertical
        for lugar in zip(*self.lugares):
            ganhou.append(self.validar_valores(list(lugar)))

        # Verifica valores na diagonal
        diagonal1 = [lugar[i] for i, lugar in enumerate(self.lugares)]
        diagonal2 = [lugar[i] for i, lugar in enumerate(self.lugares[::-1])]
        ganhou.append(self.validar_valores(diagonal1))
        ganhou.append(self.validar_valores(diagonal2))

        if any(ganhou):
            self.__ganhador = True

    def validar_valores(self, lugar):
        return all(i == lugar[0] for i in lugar)


if __name__ == "__main__":
    jogo = JogoDaVelha("X", "O")
    ganhador = jogo.get_ganhador()
    jogo.ganhador = True
    while not ganhador:
        jogo.iniciar(1, "O")
        jogo.iniciar(4, "O")
        jogo.iniciar(7, "O")
        ganhador = jogo.get_ganhador()
    print('FINALIZADO')
