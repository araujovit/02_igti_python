# declaração das variáveis
inicio = 0
fim = 100
# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim):
 if numero % 5 == 0:
 print(numero)


inicio = 0
fim = 500

multdois = ()
multcinco = ()
multsete = ()

a = 0
b = 0
c = 0

for numero in range(inicio, fim):
    if numero % 2 == 0:
        multdois[a] = numero
        a = a + 1
    if numero % 5 == 0:
        multcinco[b] = numero
        b = b + 1
    if numero % 7 == 0: 
        multsete[c] = numero 
        c = c + 1
print(multdois)
print(multcinco)
print(multsete)