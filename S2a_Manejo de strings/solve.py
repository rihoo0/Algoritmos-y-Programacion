def solve(input_list):
    """
    Calcula la suma de los valores de calibración de una lista de líneas.

    Cada línea puede contener dígitos numéricos y/o dígitos escritos en inglés:
    zero, one, two, three, four, five, six, seven, eight, nine.

    Para cada línea se debe formar un número de dos cifras con:
        - el primer dígito que aparece al recorrer la línea de izquierda a derecha;
        - el último dígito que aparece al recorrer la línea de izquierda a derecha.

    Las palabras pueden solaparse. Por ejemplo:
        - "twone" contiene "two" y "one", por tanto produce 21.
        - "oneight" contiene "one" y "eight", por tanto produce 18.

    Parámetros:
        input_list: lista de cadenas de texto, una por cada línea de entrada.

    Restricciones:
        - No leer datos por teclado dentro de esta función.
        - No imprimir resultados dentro de esta función.
        - Devolver un entero con la suma total.
    """
    num_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0}
    solution = []
    
    for line in input_list:
        
        char_per_line = []
        number = ""

        for char in line:
            number += char

            for key, val in num_dict.items():

                if number.endswith(key):
                    char_per_line.append(val)

            if char.isdigit():
                char_per_line.append(int(char))

        solution.append(int(str(char_per_line[0]) + str(char_per_line[-1])))
        char_per_line = []

    return sum(solution)

