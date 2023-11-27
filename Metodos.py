import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def plot_root_finding(f, a, b, roots, title):
    x = np.linspace(a - 1, b + 1, 400)
    y = f(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.plot(roots, [f(root) for root in roots], 'ro', label='Roots')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_data_fitting(x, y, fitted_func, title):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'bo', label='Data Points')
    x_fit = np.linspace(min(x) - 1, max(x) + 1, 400)
    y_fit = fitted_func(x_fit)
    plt.plot(x_fit, y_fit, 'r-', label='Fitted Curve')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def metodo_falsa_posicion(f, a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        return "Falsa posición: No se garantiza una raíz en este intervalo."
    roots = []
    for _ in range(max_iter):
        c = b - f(b) * (b - a) / (f(b) - f(a))
        roots.append(c)
        if abs(f(c)) < tol:
            plot_root_finding(f, a, b, roots, "Método de Falsa Posición")
            return f"Raíz encontrada (falsa posición): {c}"
    plot_root_finding(f, a, b, roots, "Método de Falsa Posición")
    return f"Raíz aproximada después de {max_iter} iteraciones: {a}"

def metodo_biseccion(f, a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        return "Bisección: No se garantiza una raíz en este intervalo."

    roots = []
    for _ in range(max_iter):
        c = (a + b) / 2
        roots.append(c)
        if abs(f(c)) < tol:
            plot_root_finding(f, a, b, roots, "Método de Bisección")
            return f"Raíz encontrada (bisección): {c}"
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    plot_root_finding(f, a, b, roots, "Método de Bisección")
    return f"Raíz aproximada después de {max_iter} iteraciones: {c}"

def metodo_newton_raphson(f, df, x0, tol, max_iter):
    x = x0
    for _ in range(max_iter):
        x_next = x - f(x) / df(x)
        if abs(x_next - x) < tol:
            return f"Raíz encontrada (Newton-Raphson): {x_next}"
        x = x_next
    return f"Raíz aproximada después de {max_iter} iteraciones: {x}"

def metodo_secante(f, x0, x1, tol, max_iter):
    for _ in range(max_iter):
        if abs(f(x1)) < tol:
            return f"Raíz encontrada (secante): {x1}"
        x_temp = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
        x0, x1 = x1, x_temp
    return f"Raíz aproximada después de {max_iter} iteraciones: {x1}"

def taylor(f, df, x0, h, n):
    resultado = f(x0)
    for i in range(1, n + 1):
        resultado += (df(x0) ** i) / np.math.factorial(i) * (h ** i)
    return f"Resultado de la serie de Taylor: {resultado}"

def cota_error(f_derivadas, x0, y0, h, n, cota_derivada):
    error = cota_derivada * h**(n + 1) / np.math.factorial(n + 1)
    return f"Cota del error: {error}"

def euler(f, x0, y0, h, n):
    x_vals, y_vals = [x0], [y0]
    x, y = x0, y0
    for i in range(n):
        y += h * f(x, y)
        x += h
        x_vals.append(x)
        y_vals.append(y)
    return f"Resultado de Euler en x = {x}: y = {y}"

def diferenciacion_adelante(f, a, h):
    resultado = (f(a + h) - f(a)) / h
    return f"Derivada por diferenciación adelante: {resultado}"

def diferenciacion_atras(f, a, h):
    resultado = (f(a) - f(a - h)) / h
    return f"Derivada por diferenciación atrás: {resultado}"

def diferenciacion_centrada(f, a, h):
    resultado = (f(a + h) - f(a - h)) / (2 * h)
    return f"Derivada por diferenciación centrada: {resultado}"

def runge_kutta(f, x0, y0, h, n):
    x_vals, y_vals = [x0], [y0]
    x, y = x0, y0
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
        x_vals.append(x)
        y_vals.append(y)
    return f"Resultado de Runge-Kutta en x = {x}: y = {y}"

def minimos_cuadrados(x, y):
    n = len(x)
    x_sum = sum(x)
    y_sum = sum(y)
    xy_sum = sum(x[i] * y[i] for i in range(n))
    xx_sum = sum(x[i] ** 2 for i in range(n))
    m = (n * xy_sum - x_sum * y_sum) / (n * xx_sum - x_sum ** 2)
    b = (y_sum - m * x_sum) / n
    fitted_func = lambda x: m * x + b
    plot_data_fitting(x, y, fitted_func, "Mínimos Cuadrados")
    return f"Ecuación de la línea de mínimos cuadrados: y = {m}x + {b}"

def polinomio_simple(x, y):
    n = len(x)
    A = np.vander(x, n)
    coeficientes = np.linalg.solve(A, y)
    p = np.poly1d(coeficientes[::-1])

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'bo', label='Data Points')
    x_range = np.linspace(min(x), max(x), 400)
    plt.plot(x_range, p(x_range), 'r-', label='Fitted Polynomial')
    plt.title("Polynomial Fit")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    return f"Polinomio resultante: {p}"

def lagrange(x, y, valor):
    total = 0
    n = len(x)
    for i in range(n):
        xi, yi = x[i], y[i]
        pi = 1
        for j in range(n):
            if i != j:
                pi *= (valor - x[j]) / (xi - x[j])
        total += yi * pi
    return f"Resultado de interpolación de Lagrange en {valor}: {total}"

def trapecio_con_formula(f, a, b):
    resultado = (b - a) / 2 * (f(a) + f(b))

    x_range = np.linspace(a, b, 400)
    y_range = [f(x) for x in x_range]

    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_range, label='f(x)')
    plt.fill_between([a, b], [f(a), f(b)], color='grey', alpha=0.5)
    plt.title('Trapecio con Fórmula')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return f"Resultado de la regla del trapecio con fórmula: {resultado}"

def trapecio_con_datos(x, y):
    n = len(x)
    area_total = 0
    for i in range(n - 1):
        delta_x = x[i + 1] - x[i]
        area_trapecio = (delta_x / 2) * (y[i] + y[i + 1])
        area_total += area_trapecio

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, '-o', label='Data Points')
    for i in range(n - 1):
        plt.fill_between([x[i], x[i + 1]], [y[i], y[i + 1]], color='grey', alpha=0.5)
    plt.title('Trapecio con Datos')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    return f"Área aproximada usando la regla del trapecio con datos: {area_total}"

def simpson_un_tercio(f, a, b, n):
    if n % 2 != 0:
        return "Simpson 1/3 requiere un número par de subintervalos."
    dx = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        coef = 4 if i % 2 != 0 else 2
        suma += coef * f(a + i * dx)
    resultado = (dx / 3) * suma

    x_range = np.linspace(a, b, 400)
    y_range = [f(x) for x in x_range]
    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_range, label='f(x)')
    x_fill = np.linspace(a, b, n+1)
    plt.fill_between(x_fill, [f(x) for x in x_fill], color='grey', alpha=0.5)
    plt.title('Simpson 1/3')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return f"Resultado de la regla de Simpson 1/3: {resultado}"

def simpson_tres_octavos(f, a, b, n):
    if n % 3 != 0:
        return "Simpson 3/8 requiere que el número de subintervalos sea múltiplo de 3."
    dx = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        coef = 3 if i % 3 != 0 else 2
        suma += coef * f(a + i * dx)
    resultado = (3 * dx / 8) * suma
    
    x_range = np.linspace(a, b, 400)
    y_range = [f(x) for x in x_range]
    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_range, label='f(x)')
    x_fill = np.linspace(a, b, n+1)
    plt.fill_between(x_fill, [f(x) for x in x_fill], color='grey', alpha=0.5)
    plt.title('Simpson 3/8')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return f"Resultado de la regla de Simpson 3/8: {resultado}"