cont = 0

while cont < 100:
    cont += 1
    if cont % 3 == 0 and cont % 5 == 0:
        print(f'FizzBuzz')
    elif cont % 3 == 0:
        print(f'Fizz')
    elif cont % 5 == 0:
        print(f'Buzz')
    else:
        print(f'{cont}')
