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

    numbers_list = []
    for i in range(init, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            numbers_list.append('FizzBuzz')
        elif i % 3 == 0:
            numbers_list.append('Fizz')
        elif i % 5 == 0:
            numbers_list.append('Buzz')
        else:
            numbers_list.append(i)
    return numbers_list

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
    
    Args:
    None

    Returns:
    None: La función imprime los resultados en la consola.
    """
    print(' Bienvenido a Fizz-Buzz')
    inicio = int(input('\nIngresa el número donde quieres Ininiciar: '))
    fin = int(input('Ingresea el número donde quieras Finalizar: '))
    n_list = fizz_buzz(inicio,fin)
    print("\nResultados:")
    for result in n_list:
        print(result)
    print(f'El total de numeros en el rango es:{len(n_list)}')
    percentage_str(n_list,"Fizz")
    percentage_str(n_list,"Buzz")
    percentage_str(n_list,"FizzBuzz")
    percentage_int(n_list)

main()
