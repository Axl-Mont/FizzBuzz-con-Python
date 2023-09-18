""""
    El usuario proporciona un rango de inicio y fin para el juego Fizz-Buzz.
    Luego se muestra una lista de resultados del juego, seguida de los
    porcentajes de aparición de "Fizz," "Buzz," "FizzBuzz," y números enteros.

    Args:
    None

    Returns:
    None: Se ejecuta la funcion main para iniciar
"""
def fizz_buzz(init,end):
    """
    Genera una lista de números y reemplaza múltiplos de 3 con 'Fizz', múltiplos de 5 con 'Buzz'
    y múltiplos de ambos 3 y 5 con 'FizzBuzz' dentro de un rango dado.

    Args:
        init (int): El primer número del rango (incluido).
        end (int): El último número del rango (incluido).

    Returns:
        list: Una lista que contiene el resultado de recorrer los números en el rango [init, end]
    """
    init_int = int(init)
    end_int = int(end)

    numbers_list = []
    for i in range(init_int, end_int + 1):
        if i % 3 == 0 and i % 5 == 0:
            numbers_list.append('FizzBuzz')
        elif i % 3 == 0:
            numbers_list.append('Fizz')
        elif i % 5 == 0:
            numbers_list.append('Buzz')
        else:
            numbers_list.append(i)
    return numbers_list

def validated(init, fnd):
    """
    Valida dos valores para asegurarse de que sean numéricos y que
    el valor de inicio no sea mayor que el valor final.

    Parameters:
    init (str): El valor de inicio que se debe validar y convertir a entero.
    fnd (str): El valor final que se debe validar y convertir a entero.

    Returns:
    bool: True si los valores son válidos y el valor de inicio no es mayor que el
          valor final; False en caso contrario.
    """
    try:
        init_int = int(init)
        end_int = int(fnd)

        if init_int > end_int:
            print('\nEl parámetro de Inicio no puede ser mayor al Final')
            return False
    except ValueError:
        print('\nEl inicio y el final deben ser valores numéricos')
        return False

    return True

def percentage_str(list_n, name):
    """
        Calcula y muestra el porcentaje de aparición de 'name' en 'list_n'.
    """
    count = list_n.count(name)
    result=(count/len(list_n))*100
    print(f"\nEl porcentaje de aparición de {name} es: {result:.2f}%")

def percentage_int(n_count):
    """
    Calcula y muestra el porcentaje de números enteros en una lista.

    Args:
    n_count (list): Una lista de elementos en la que se buscan números enteros.

    Returns:
    None: La función imprime el resultado en la consola.
    """
    type_number = int
    count = 0
    for i in n_count:
        if isinstance(i, type_number):
            count += 1
    result =(count/len(n_count))*100
    print(f"\nEl porcentaje de aparición de Numeros es: {result:.2f}%")

def main():
    """
    Realiza el juego Fizz-Buzz y calcula el porcentaje de resultados.

    Esta función inicia el juego Fizz-Buzz, solicitando al usuario que ingrese
    un rango de inicio y fin. Luego muestra una lista de resultados del juego
    junto con el porcentaje de aparición de 'Fizz', 'Buzz', 'FizzBuzz' y números enteros.

    Args:
        None

    Returns:
        None: La función imprime los resultados en la consola y no devuelve valores.
    """
    print('\nBienvenido a Fizz-Buzz')
    inicio = input('\nIngresa el número donde quieres Ininiciar: ')
    fin = input('Ingresea el número donde quieras Finalizar: ')
    if validated(inicio,fin):
        n_list = fizz_buzz(inicio,fin)
        print("\nResultados:")
        for result in n_list:
            print(result)
        print(f'El total de numeros en el rango es:{len(n_list)}')
        percentage_str(n_list,"Fizz")
        percentage_str(n_list,"Buzz")
        percentage_str(n_list,"FizzBuzz")
        percentage_int(n_list)
    else:
        print('\n Intenta Nuevamente')
        main()

main()
