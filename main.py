import BatalhaNaval

a = BatalhaNaval.BatalhaNaval(3)
a.preencherTabuleiro()
while a.numMaximoJogadas > 0:
    a.jogada()
    print("Você ainda possui "+str(a.numMaximoJogadas)+" jogada(s).")

a.limparLogs()
print("Acabou")