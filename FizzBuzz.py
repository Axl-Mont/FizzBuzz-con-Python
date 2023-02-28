def fizzbuzz():
    for i in range(100):
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            print(f'FizzBuzz')
        elif i % 3 == 0:
            print(f'Fizz')
        elif i % 5 == 0:
            print(f'Buzz')
        else:
            print(f'{i}')


fizzbuzz()
