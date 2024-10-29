import os

carros = [("Chevrolet tracker", 120),
          ("Chevrolet Onix" , 90),
          ("Chrevolet spin" , 180),
          ("Hyundai HB20" , 85),
          ("Hyundai Tucson" , 120),
          ("Fiat Uno" , 60),
          ("Fiat Mobi" , 70),
          ("Fiat Pulse" , 130)
          ]
alugados = []




def mostrar_lista_carros(lista_de_carros):
    for i,car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} / dia".format(i,car[0], car[1]))

mostrar_lista_carros(carros)

while True:
    os.system('cls')
    print('==========')
    print('Bem vindo à locadora de carros!.')
    print('==========')
    print('O que deseja fazer? ')
    print('0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro ')
    op = int(input())
    os.system('cls')
    if op == 0:
        pass
    elif op == 1:
        pass
    elif op == 2:
        pass

    print("")
    print("==========")
    print('Digite 0 para CONTINUAR || Digite 1 para SAIR')
    if float(input()) == 1:
        break