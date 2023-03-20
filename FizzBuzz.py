def fizzbuzz(rangoA,rangoB):
    for i in range(rangoA, rangoB + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f'FizzBuzz')
        elif i % 3 == 0:
            print(f'Fizz')
        elif i % 5 == 0:
            print(f'Buzz')
        else:
            print(f'{i}')

def inicio ():
    print(' Bienvenido a Fizz Buzz FizzBuzz')
    inicio = int(input('Ingresa el número donde quieres Ininiciar : '))
    fin = int(input('Ingresea el número donde quieras Finalizar: '))
    fizzbuzz(inicio,fin)

inicio()
input()