""""Arreglo de numeros creado por el rango para manipular la informacion"""
numbert_list = []
"""Funcion que aplica la logica Fizz Buzz"""
def fizz_buzz(init_a,end_b):
    """
    Esta función toma dos números, 'init_a' y 'end_b', se utilizan como un rango
    
    Args:
        a (int): inicio del rango.
        b (int): fin del rango.
    """
    for i in range(init_a, end_b + 1):
        if i % 3 == 0 and i % 5 == 0:
            numbert_list.append('FizzBuzz')
        elif i % 3 == 0:
            numbert_list.append('Fizz')
        elif i % 5 == 0:
            numbert_list.append('Buzz')
        else:
            numbert_list.append(i)

def percentage(num, name):
    """
    Esta función toma un números, 'num' y un nombre'name',
    
    Args:
        a (int): numero para calcular el porcentaje.
        b (string): nombre que se utiliza para imprimir el resultado.
    """
    result=(num/len(numbert_list))*100
    print(f"\nEl porcentaje de aparición de {name} es: {result:.2f}%")
    
def number_count():
    """Esta funcion cuenta cuantos elementos son numeros en el arreglo

    Returns:
        int: count
    """
    type_number = int
    count = 0 
    for i in numbert_list:
        if isinstance(i, type_number):
            count += +1 
    return count

def data_print():
    """"" Esta fucion imprime el arreglo y los porcentajes de apariciones"""
    for i in numbert_list:
        print(i)
    print(f'\nEl total de numeros en el rango es de: {len(numbert_list)}')
    percentage(numbert_list.count('FizzBuzz'),'FizzBuz')
    percentage(numbert_list.count('Fizz'),'Fizz')
    percentage(numbert_list.count('Buzz'),'Buz')
    percentage(number_count(),'Numeros')
   

def main():
    """"Funcio que inicia la ejecuccion del programa"""
    print(' Bienvenido a Fizz-Buzz')
    inicio = int(input('Ingresa el número donde quieres Ininiciar: '))
    fin = int(input('Ingresea el número donde quieras Finalizar: '))
    fizz_buzz(inicio,fin)
    data_print()

main()
