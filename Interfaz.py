from Metodos import *

def parse_function(function_str):
    x = sp.symbols('x')
    f_expr = sp.sympify(function_str)
    df_expr = sp.diff(f_expr, x)
    f = sp.lambdify(x, f_expr, modules=['numpy'])
    df = sp.lambdify(x, df_expr, modules=['numpy'])
    return f, df

def parse_function1(function_str):
    x, y = sp.symbols('x y')
    f_expr = sp.sympify(function_str)
    f = sp.lambdify((x,y), f_expr, modules=['numpy'])
    return f

# Console interface
def console_interface():
    print("Bienvenido a la Calculadora de Análisis Numérico")

    function_input = input("Ingrese su función, por ejemplo 'x**2 - 4': ")
    f, df = parse_function(function_input)
    f1 = parse_function1(function_input)

    print("\nSeleccione el método numérico a utilizar:")
    print("1: Falsa Posición")
    print("2: Bisección")
    print("3: Newton Raphson")
    print("4: Secante")
    print("5: Taylor")
    print("6: Cota Error")
    print("7: Euler")
    print("8: Runge Kutta")
    print("9: Diferenciación Adelante")
    print("10: Diferenciación Atrás")
    print("11: Diferenciación Centrada")
    print("12: Trapecio con Fórmula")
    print("13: Trapecio con Datos")
    print("14: Simpson 1/3")
    print("15: Simpson 3/8")
    print("16: Mínimos Cuadrados")
    print("17: Polinomio Simple")
    print("18: Lagrange")
    method_choice = input("Método: ")

    try:
        if method_choice == '1':
            # Falsa Posición
            a = float(input("Ingrese el valor inicial a: "))
            b = float(input("Ingrese el valor inicial b: "))
            tol = float(input("Ingrese la tolerancia tol: "))
            max_iter = int(input("Ingrese el número máximo de iteraciones max_iter: "))
            result = metodo_falsa_posicion(f, a, b, tol, max_iter)
        elif method_choice == '2':
            # Bisección
            a = float(input("Ingrese el valor inicial a: "))
            b = float(input("Ingrese el valor inicial b: "))
            tol = float(input("Ingrese la tolerancia tol: "))
            max_iter = int(input("Ingrese el número máximo de iteraciones max_iter: "))
            result = metodo_biseccion(f, a, b, tol, max_iter)
        elif method_choice == '3':
            # Newton Raphson
            x0 = float(input("Ingrese el valor inicial x0: "))
            tol = float(input("Ingrese la tolerancia tol: "))
            max_iter = int(input("Ingrese el número máximo de iteraciones max_iter: "))
            result = metodo_newton_raphson(f, df, x0, tol, max_iter)
        elif method_choice == '4':
            # Secante
            x0 = float(input("Ingrese el valor inicial x0: "))
            x1 = float(input("Ingrese el valor inicial x1: "))
            tol = float(input("Ingrese la tolerancia tol: "))
            max_iter = int(input("Ingrese el número máximo de iteraciones max_iter: "))
            result = metodo_secante(f, x0, x1, tol, max_iter)
        elif method_choice == '5':
            # Taylor
            x0 = float(input("Ingrese el punto x0: "))
            h = float(input("Ingrese el paso h: "))
            n = int(input("Ingrese el número de términos n: "))
            result = taylor(f, df, x0, h, n)
        elif method_choice == '6':
            # Cota Error
            x0 = float(input("Ingrese el punto x0: "))
            y0 = float(input("Ingrese el punto y0: "))
            h = float(input("Ingrese el paso h: "))
            n = int(input("Ingrese el número de términos n: "))
            cota_derivada = float(input("Ingrese la cota de la derivada: "))
            result = cota_error(df, x0, y0, h, n, cota_derivada)
        elif method_choice == '7':
            # Euler
            x0 = float(input("Ingrese el punto inicial x0: "))
            y0 = float(input("Ingrese el valor inicial y0: "))
            h = float(input("Ingrese el tamaño del paso h: "))
            n = int(input("Ingrese el número de pasos n: "))
            result = euler(f1, x0, y0, h, n)
        elif method_choice == '8':
            # Runge Kutta
            x0 = float(input("Ingrese el punto inicial x0: "))
            y0 = float(input("Ingrese el valor inicial y0: "))
            h = float(input("Ingrese el tamaño del paso h: "))
            n = int(input("Ingrese el número de pasos n: "))
            result = runge_kutta(f1, x0, y0, h, n)
        elif method_choice == '9':
            # Diferenciación Adelante
            a = float(input("Ingrese el punto a: "))
            h = float(input("Ingrese el paso h: "))
            result = diferenciacion_adelante(f, a, h)
        elif method_choice == '10':
            # Diferenciación Atrás
            a = float(input("Ingrese el punto a: "))
            h = float(input("Ingrese el paso h: "))
            result = diferenciacion_atras(f, a, h)
        elif method_choice == '11':
            # Diferenciación Centrada
            a = float(input("Ingrese el punto a: "))
            h = float(input("Ingrese el paso h: "))
            result = diferenciacion_centrada(f, a, h)
        elif method_choice == '12':
            # Trapecio con Fórmula
            a = float(input("Ingrese el límite inferior a: "))
            b = float(input("Ingrese el límite superior b: "))
            result = trapecio_con_formula(f, a, b)
        elif method_choice == '13':
            # Trapecio con Datos
            x = [float(i) for i in input("Ingrese los valores de x separados por espacios: ").split()]
            y = [float(i) for i in input("Ingrese los valores de y separados por espacios: ").split()]
            result = trapecio_con_datos(x, y)
        elif method_choice == '14':
            # Simpson 1/3
            a = float(input("Ingrese el límite inferior a: "))
            b = float(input("Ingrese el límite superior b: "))
            n = int(input("Ingrese el número de subintervalos n (debe ser par): "))
            result = simpson_un_tercio(f, a, b, n)
        elif method_choice == '15':
            # Simpson 3/8
            a = float(input("Ingrese el límite inferior a: "))
            b = float(input("Ingrese el límite superior b: "))
            n = int(input("Ingrese el número de subintervalos n (múltiplo de 3): "))
            result = simpson_tres_octavos(f, a, b, n)
        elif method_choice == '16':
            # Mínimos Cuadrados
            x = [float(i) for i in input("Ingrese los valores de x separados por espacios: ").split()]
            y = [float(i) for i in input("Ingrese los valores de y separados por espacios: ").split()]
            result = minimos_cuadrados(x, y)
        elif method_choice == '17':
            # Polinomio Simple
            x = [float(i) for i in input("Ingrese los valores de x separados por espacios: ").split()]
            y = [float(i) for i in input("Ingrese los valores de y separados por espacios: ").split()]
            result = polinomio_simple(x, y)
        elif method_choice == '18':
            # Lagrange
            x = [float(i) for i in input("Ingrese los valores de x separados por espacios: ").split()]
            y = [float(i) for i in input("Ingrese los valores de y separados por espacios: ").split()]
            valor = float(input("Ingrese el valor a interpolar: "))
            result = lagrange(x, y, valor)
        else:
            print("Método no reconocido.")
            return
        
        print(result)
        
    except ValueError as e:
        print(f"Entrada no válida: {e}")
    except Exception as e:
        print(f"Se produjo un error durante el cálculo: {e}")

if __name__ == "__main__":
    console_interface()