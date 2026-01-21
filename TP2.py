"""
                        ~ Trabajo práctico 2 ~
"""


"""
Ejercicio 1: Calculadora de Descuentos

Crea una función que calcule el precio final de un producto después de aplicar un descuento.

Requisitos:
    -La función debe recibir el precio original y el porcentaje de descuento.
    -Debe retornar el precio final después del descuento.
    -Incluye un docstring que describa la función, sus parámetros y el valor de retorno.

"""

def Discount_calculator(price:float,discount:int) -> float:
    """
    This fucntion calulates the final price of an element given the percentege of discount
    
    :param price(int): the original price of the service/goods
    :param discount(int): the amount of discount going to be applied to the original price

    :return: returns the final price with the discount applied
    """
    return (price-price*(discount/100))


"""
Ejercicio 2: Conversión de Temperaturas

Crea una función que convierta temperaturas de Celsius a Fahrenheit o viceversa.

Requisitos:
    -La función debe recibir la temperatura, la unidad de origen y la unidad de destino.
    -Debe retornar la temperatura convertida.
    -Incluye ejemplos de uso en el docstring.
"""

def Temperature_converter(degrees:float,origin:str,destiny:str) -> float:
    """
    This function transforms the temperature unit from farenheit to celsius and viceversa

    :param degrees: The amount of degrees
    :type degrees: float
    :param origin: The unit of origin (celsius or farenheit)
    :type origin: str
    :param destiny: The unit needed (celsius or farenheit)
    :type destiny: str
    :return: The amount of degrees already transformed

    :examples
      Temperature_converter(32,"farenheit","celsius") = 0

    """
    origin.capitalize()
    destiny.capitalize()
    if origin == destiny:
        print("La unidad de destino debe ser distinta a la de origen")
    elif origin == "CELSIUS":
        return (degrees*(9/5)) + 32
    elif origin == "FARENHEIT":
        return ((degrees - 32)*(5/9))
    else:
        print("La función no está preparado para recibir unidades distintas a 'CELSIUS' o 'FARENHEIT'")
    return degrees



"""
Ejercicio 3: Verificación de Palíndromos

Escribe una función que determine si una palabra o frase es un palíndromo.

Requisitos:
    -La función debe recibir una cadena de texto.
    -Debe retornar True si es un palíndromo y False en caso contrario.
"""

def Is_palindrome(word:str) ->bool:
    """
    Determines if it's a palindrome or not

    :param word: The word to check if it's a palindrome or not
    :type word: str
    :return: Boolean value answering to the question
    :rtype: bool
    """
    word = word.upper()
    if word != word[::-1]:
        return False
    return True


# print(Is_palindrome("oso"))

"""
Ejercicio 4: Análisis de Texto
Crea una función que cuente la cantidad de palabras y caracteres en un texto.
Requisitos:
    -La función debe recibir una cadena de texto.
    -Debe retornar un diccionario con la cantidad de palabras y caracteres.
    -Documenta claramente la estructura del diccionario en el docstring.
"""

def Textual_analysis(text:str) -> dict:
    """
    Calculates the amount of words and characters present on a given text.
    Returns a dictionary containing said information.\n
    :param: text: The text given by the user
    :type text: str
    :return: A dictionary containing the information solicited \nExample of dictionary: \nwords_and_characters = {'Amount of words' : 3 , 'Total characters' : 20}\n
    
    :rtype: dict[Any, Any]
    
    
    
    """
    words_and_characters = {}
    words_and_characters["Amount of words"] = len(text.split(" "))
    words_and_characters["Total characters"] = len(text)
    return words_and_characters



"""
Ejercicio 5: Generador de Números Primos

Escribe una función que genere una lista de números primos hasta un número dado.

Requisitos:
    -La función debe recibir un número entero positivo.
    -Debe retornar una lista con todos los números primos hasta ese número.
    -Incluye en el docstring una explicación sobre qué es un número primo.
"""
import math

def is_prime(n):
    """Check if a number is prime using trial division up to the square root.
    A prime number is such that it's only divisable by 1 and itself
    :param n: the number to check if it's prime
    :type n: int
    :return: Boolean value (True if prime, False if it's not)
    
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def Prime_number_generator_user(n:int) -> list[int]:
    """
    Prime number generator, gives back a list with all the prime numberes up until the number given.
    :param number: The amount of prime numbers needed in the list
    :type number: int
    :return: The list containing all the prime numbers up until the number solicited
    :rtype: list[int]
    """
    return [i for i in range(n) if is_prime(i)]


# print(Prime_number_generator_user(10))


"""
Ejercicio 6: Gestión de Inventario

Crea una función que actualice el inventario de una tienda.

Requisitos:
    -La función debe recibir un diccionario representando el inventario y una lista de productos vendidos.
    -Debe actualizar las cantidades en el inventario y retornar el inventario actualizado.
    -Incluye en el docstring un ejemplo de entrada y salida.
"""
present_products = {"Pipetas pulgas":5 ,"Paradiarreas":7, "Pet90": 10,"Correas":20 }
sold_products = list(present_products.keys())



def Inventory(present_products:dict[str,int],sold_products:list[str]) -> dict[str,int]:
    """
    Actualizes the amount of a product present in the inventory

    :param present_products: The products present in the inventory
    :type present_products: dict
    :param sold_products: The products that have been sold and need antualization
    :type sold_products: list
    :return: The actualized dictionary, hence the actualized inventory
    :rtype: dict[str, int]:

    Examples:
    >>> present_products = {"Pipetas pulgas":5 ,"Paradiarreas":7, "Pet90": 10,"Correas":20 }
    >>> sold_products = list(present_products.keys())
    >>> Inventory(present_products,sold_products)
    {'Pipetas pulgas': 4, 'Paradiarreas': 6, 'Pet90': 9, 'Correas': 19}
    """
    for product in sold_products:
        present_products[product] -= 1
    return present_products


# print(present_products)
# print(Inventory(present_products,sold_products))


"""
Ejercicio 7: Validación de Contraseñas
Escriba un programa de Python para convertir una lista de string en 
una nueva lista con listas de caracteres utilizando map.
Requisitos:
input : ["hola","adios"]
output: [["h","o","l","a"] , ["a","d","i","o","s"]]
"""

input = ["hola","adios"]
output_example = [["h","o","l","a"] , ["a","d","i","o","s"]]

def Password_validator(input:list[str]) -> list[list[str]]:
    """
    A simple function that transform a list of strings into a list of list containing each character    
    :param input: The list containing the strings 
    :type input: list[str]
    :return: The list of lists containing each character from the aforementioned strings
    :rtype: list[list[str]]
    """
    # output = []
    # for word in input:
    #     temporary_list = list(map(str,word))
    #     output.append(temporary_list)
    return [list(map(str,word)) for word in input]



# print(Password_validator(input))


"""
Ejercicio 8: Cálculo de Estadísticas
Crea una función que calcule la media, mediana y moda de una lista de números.
Requisitos:
La función debe recibir una lista de números.
Debe retornar un diccionario con la media, mediana y moda.
Incluye en el docstring una explicación de cada estadística y un ejemplo de uso.
"""