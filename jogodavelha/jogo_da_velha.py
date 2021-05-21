class JogoDaVelha:
    def __init__(self, jogador1, jogador2):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        self.__ganhador = False
        self.__deu_velha = False
        self.lugares = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    def get_ganhador(self):
        return self.__ganhador

    def get_deu_velha(self):
        return self.__deu_velha

    def iniciar(self, jogada, jogador):
        retorno = self.escolher_lugar(jogada, jogador)
        self.deu_velha()
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

    def deu_velha(self):
        self.__deu_velha = all(
            isinstance(j, str) for i in self.lugares for j in i
        )


if __name__ == "__main__":
    jogador1 = input('Jogador1 escolha X ou O: ')
    if jogador1 == 'O' or jogador1 == 'X':
        jogador2 = 'X' if jogador1 == 'O' else 'O'
    print(f"Jogador1 -> {jogador1} \nJogador2 -> {jogador2}")
    jogo = JogoDaVelha(jogador1, jogador2)
    ganhador = jogo.get_ganhador()
    deu_velha = False
    print(jogo.velha())
    while not ganhador and not deu_velha:
        deu_velha = jogo.get_deu_velha()
        if deu_velha:
            print('DEU VELHA MANO!')
        lugar = input("Escolha um lugar (X): ")
        jogo.iniciar(int(lugar), jogador1)
        ganhador = jogo.get_ganhador()
        if not ganhador:
            lugar = input("Escolha um lugar (O): ")
            jogo.iniciar(int(lugar), jogador2)
            ganhador = jogo.get_ganhador()
    print('FINALIZADO')
