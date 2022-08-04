opcao = 5

while opcao!=0 :

    opcao = int(input('qual operação você deseja realizar? \n digite:'
          '\n 1 para soma'
          '\n 2 para subtração'
          '\n 3 para multiplicação '
          '\n 4 para divisão'
          '\n 0 para sair \n'))

    if opcao == 1 :
        print('você está realizando uma soma \n')
        n1 = int(input('digite um número: \n'))
        n2 = int(input('digite outro número: \n'))
        n1 = n1 + n2
        print('o resultado é: \n ', n1)

    if opcao == 2 :
        print('você está realizando uma subtração \n')
        n1 = int(input('digite um número: \n'))
        n2 = int(input('digite outro número: \n'))
        n1 = n1 - n2
        print('o resultado é: \n ', n1)

    if opcao == 3 :
        print('você está realizando uma multiplicação \n')
        n1 = int(input('digite um número: \n'))
        n2 = int(input('digite outro número: \n'))
        n1 = n1 * n2
        print('o resultado é: \n ', n1)

    if opcao == 4 :
        print('você está realizando uma divisão \n')
        n1 = int(input('digite um número: \n'))
        n2 = int(input('digite outro número: \n'))
        if n2 == 0 :
            print('nenhum número pode ser dividido por 0 ! \n')
        else :
            n1 = n1 / n2
            print('o resultado é: \n ', n1)