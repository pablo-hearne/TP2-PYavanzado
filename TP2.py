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
    return 



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


def Prime_number_generator(n:int) -> list:
    """
    
    
    :param number: Description
    :type number: int
    :return: Description
    :rtype: list[Any]
    """
    if n <= 1:
        print("Por favor ingrese un valor válido (mayor a 1)")
        return []
    return [((i*0.5)+1) for i in range(n)] #nada q ver no

print(Prime_number_generator(4))