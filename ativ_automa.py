def AFD(estado_atual, entrada):
    transicoes = {
        (0, 'a'): 1,
        (0, 'b'): 2,
        (1, 'b'): 1,    
    }
    if (estado_atual, entrada) in transicoes:
        return transicoes[(estado_atual, entrada)]
    else:
        return None

with open("entrada.txt", "r") as entrada_file:
    entrada = entrada_file.read().strip()

estado_inicial = 0
estado_atual = estado_inicial
for i in entrada:
    estado_atual = AFD(estado_atual, i)
    if estado_atual is None:
        with open("saida.txt", "w") as saida_file:
            saida_file.write("A entrada não é válida.")
            print("A entrada não é válida.")
        break
else:
    with open("saida.txt", "w") as saida_file:
        saida_file.write("A entrada é válida.")
        print("A entrada é válida.")

print("resultado gravado no arquivo 'saida.txt'")
