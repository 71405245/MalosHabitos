def f_rectangulo(altura, base):
    resultado = altura * base
    return resultado


def f_triangulo(ancho, largo):
    r = 0.5 * ancho * largo
    return r

# Función principal
def Principal():
    #Datos a ingresar para el calculo del area del rectangulo
    x = 4
    y = 6
    rectangulo_area = f_rectangulo(x, y)
    print("El Área del rectángulo es:", rectangulo_area)

    #Datos a ingresar para el calculo del triangulo
    base = 5
    altura = 8
    triangulo_area = f_triangulo(base, altura)
    print("El Área del triángulo es:", triangulo_area)

Principal()
