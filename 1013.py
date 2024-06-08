A, B, C = map(float, input().split())
area_triangle = (A * C) / 2

pi = 3.14159
area_circle = pi * C**2

area_trapezium = ((A + B) * C) / 2

area_square = B**2

area_rectangle = A * B

print(f"TRIANGULO: {area_triangle:.3f}")
print(f"CIRCULO: {area_circle:.3f}")
print(f"TRAPEZIO: {area_trapezium:.3f}")
print(f"QUADRADO: {area_square:.3f}")
print(f"RETANGULO: {area_rectangle:.3f}")