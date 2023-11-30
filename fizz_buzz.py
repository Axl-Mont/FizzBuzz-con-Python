def get_input():
    """
    Solicita al usuario ingresar un rango de números y valida la entrada.

    Returns:
        tuple or False: Un tuple con los números de inicio y fin
        si la entrada es válida, False en caso contrario.
    """
    inicio = input('\nIngresa el número donde quieres iniciar: ')
    fin = input('Ingresa el número donde quieres finalizar: ')

    if validated(inicio, fin):
        return int(inicio), int(fin)
    else:
        return False

def validated(init, end):
    """
    Valida que los parámetros de inicio y fin sean números y que el inicio no sea mayor que el fin.

    Args:
        init (str): El número de inicio ingresado por el usuario.
        end (str): El número de fin ingresado por el usuario.

    Returns:
        bool: True si la validación es exitosa, False en caso contrario.
    """
    try:
        init_int = int(init)
        end_int = int(end)

        if init_int > end_int:
            print('\nEl parámetro de inicio no puede ser mayor al final')
            return False
    except ValueError:
        print('\nEl inicio y el final deben ser valores numéricos')
        return False

    return True

def fizz_buzz(init, end):
    """
    Genera una lista de números o las cadenas "Fizz", "Buzz" o "FizzBuzz",
    si el numero es divisible por:
    3 = Fizz,
    5 = buzz,
    3 y por 5 = FizzBuzz

    Args:
        init (int): El número de inicio del rango.
        end (int): El número de fin del rango.

    Returns:
        list: Una lista que contiene números o las cadenas "Fizz", "Buzz" o "FizzBuzz".
    """
    numbers_list = ["FizzBuzz" if item % 2 == 0 and item % 3 == 0 else
                    "Fizz" if item % 3 == 0 else
                    "Buzz" if item % 5 == 0 else
                    item
                    for item in range(init, end + 1)
                    ]
    return numbers_list

def percentage_str(list_str):
    """
    Calcula y muestra el porcentaje de aparición de las cadenas
    "Fizz", "Buzz" y "FizzBuzz" en la lista.

    Args:
        list_str (list): Lista de números y cadenas generada por fizz_buzz.
    """
    fiz_buzz_count = ('Fizz', 'Buzz', 'FizzBuzz')

    for i in fiz_buzz_count:
        count = list_str.count(i)
        result = (count / len(list_str)) * 100
        print(f"\nEl porcentaje de aparición de {i} es: {result:.2f}%")

def percentage_int(list_int):
    """
    Calcula y muestra el porcentaje de aparición de números en la lista.

    Args:
        list_int (list): Lista de números y cadenas generada por fizz_buzz.
    """
    type_number = int
    count = 0
    for i in list_int:
        if isinstance(i, type_number):
            count += 1
    result = (count / len(list_int)) * 100
    print(f"\nEl porcentaje de aparición de números es: {result:.2f}%")

def print_results(list_final):
    """
    Imprime los resultados finales, incluyendo la lista de números y los porcentajes de aparición.

    Args:
        list_final (list): Lista de números y cadenas generada por fizz_buzz.
    """
    print("\nResultados:")
    for i in list_final:
        print(i)
    print(f'\nEl total de números en el rango es: {len(list_final)}')
    percentage_str(list_final)
    percentage_int(list_final)

def main():
    """
    Función principal que maneja la interacción con el usuario y controla la ejecución del programa.
    """
    print('\nBienvenido a Fizz-Buzz')
    count = 0

    while count < 3:
        user_input = get_input()

        if user_input:
            inicio, fin = user_input
            n_list = fizz_buzz(inicio, fin)
            print_results(n_list)
            break

        else:
            print('\n Intenta nuevamente')
            count += 1

    if count == 3:
        print('\nDemasiados intentos fallidos. Saliendo del programa.')

if __name__ == "__main__":
    main()
