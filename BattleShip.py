import random

class Battle(object):
    def __init__(self,nJogadas):
        self.matriz = [["A" for j in range(5)] for i in range(5)]
        self.nJogadas = nJogadas
        self.nBarcos = 2
        if self.jogoExiste():
            self.carregarmatriz()
            self.carregarJogadas()
        else:
            self.preenchermatriz()

    def preencherTabuleiro(self):
        for i in range(2):
            x = random.randint(0,4)
            y = random.randint(0,4)
            if self.matriz[x][y] == "B":
                i=-1
            else:
                print(str(x) + "-" + str(y))
                self.matriz[x][y] = "B"
                self.salvarTabuleiro(x,y,"B")

    def jogoExiste(self):
        arq = open("arquivoTabuleiro.txt", "r")
        if arq.readline() == "":
            existe = False
        else:
            existe = True
        return existe

    def salvarJogadas(self):
        self.arq = open("arquivoJogadas.txt", "w")
        self.arq.write(str(self.nJogadas))
        self.arq.close()

    def salvarTabuleiro(self, eixoX, eixoY, valor):
        self.arq = open("arquivoTabuleiro.txt", "w")
        self.arq.write(str(eixoX) + "-" + str(eixoY) + "-" + str(valor) + "\n")
        self.arq.close()

    def carregarJogadas(self):
        arq = open("arquivoJogadas.txt", "r")
        for linha in arq:
            self.nJogadas = int(linha)
        arq.close()

    def carregarTabuleiro(self):
        arq = open("arquivoTabuleiro.txt", "r")
        for linha in arq:
            valor = linha.split("-")
            self.matriz[int(valor[0])][int(valor[1])] = "B"
        arq.close()


    def jogada(self):

        jogadaEixoX = int(input("Digite a posicao do eixo X:"))
        jogadaEixoY = int(input("Digite a posicao do eixo Y:"))

        if self.matriz[jogadaEixoX][jogadaEixoY] == "B":
            self.matriz[jogadaEixoX][jogadaEixoY] = "X"
            self.salvarTabuleiro(jogadaEixoX, jogadaEixoY, "X")
            print("Barco Afundado!")
            self.nJogadas -= 1
            self.nBarcos -= 1
            self.salvarJogadas()

        elif self.matriz[jogadaEixoX][jogadaEixoY] == "A":
            print("Tiro na água!")
            self.nJogadas -= 1
            self.salvarJogadas()
        else:
            print("Barco já afundado!")


    def limparLogs(self):
        self.arq = open("arquivoJogadas.txt", "w")
        self.arq.close()
        self.arq = open("arquivoTabuleiro.txt", "w")
        self.arq.close()
