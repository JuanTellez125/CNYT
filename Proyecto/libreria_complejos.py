import math 

# 1. suma de numeros complejos
def suma(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

# 2. producto de numeros complejos 
def producto(c1, c2):
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imag = c1[0] * c2[1] + c1[1] * c2[0]
    return (real, imag)

# 3. resta de numeros complejos
def resta(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])

# 4. division de numeros complejos
def division(c1, c2):
    denom = c2[0]**2 + c2[1]**2
    if denom == 0:
        raise ValueError("Division by zero is not allowed.")
    real = (c1[0] * c2[0] + c1[1] * c2[1]) / denom
    imag = (c1[1] * c2[0] - c1[0] * c2[1]) / denom
    return (real, imag)

# 5. modulo de un numero complejo
def modulo(c):
    return math.sqrt(c[0]**2 + c[1]**2)

# 6. conjugado de un numero complejo
def conjugado(c):
    return (c[0], -c[1])

# 7. conversion de forma polar a cartesiano, en los dos sentidos
def polar_a_cartesiano(r, theta):
    real = r * math.cos(theta)
    imag = r * math.sin(theta)
    return (real, imag)

def cartesiano_a_polar(c):
    r = modulo(c)
    theta = math.atan2(c[1], c[0])
    return (r, theta)

# 8. Retornar la fase de un numero complejo
def fase(c):
    return math.atan2(c[1], c[0])