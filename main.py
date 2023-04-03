import math
decisao = int(input('digite um valor para o tipo da função, 1 ou 2: '))

if decisao < 1 or decisao > 2 : 
    print('Grau inválido')
elif decisao == 1:
    print('A equação é do primeiro grau.')
    a = float(input('digite o valor de a: '))
    b = float(input('digite o valor de b: '))
    if a == 0:
        print('Valor de a inválido')
    elif a !=0:
        x = -b/a
        print(f"{a}x + {b} = 0")
        print(f'x = {x:.2f}')
elif decisao == 2: 
    print('A equação é do segundo grau.')
    a = float(input('digite o valor de a: '))
    b = float(input('digite o valor de b: '))
    c = float(input('digite o valor de c: '))
    if a == 0: 
        print('valor invalido')
    elif a !=0: 

        print(f'{a}x² + {b}x + {c} = 0')
        if (b*b) -4*a*c < 0:
            print('A equação não possui raízes reais')
        elif (b*b) -4*a*c ==0:
            print('A equação possui apenas uma raiz real')
            x= -b + math.sqrt(((b*b)-4*a*c)/2*a)
            print(f'x = {x:.2f}')
        elif (b*b) -4*a*c > 0:
            print('A equação possui duas raízes reais')
            x1= -b - math.sqrt(((b*b)-4*a*c)/2*a)
            x2= -b + math.sqrt(((b*b)-4*a*c)/2*a)
            print(f'raíz 1 = {x1:.2f}, raíz 2 = {x2:.2f}')
        
