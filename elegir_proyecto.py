import random

num = random.randint(1,5)

lista = ["Ajedrez", "Snake", "tic-tac-toe", "convertidor div y criptos", "seguimiento datos"]
contador = 0 
jose = ''
for i in lista:
    contador += 1
    if contador == num:
        jose = i
        break
    else:
        pass
print(jose)
