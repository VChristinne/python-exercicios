from math import sin, cos, tan, radians

angulo = float(input("Digite um ângulo: "))
sin = sin((radians(angulo)))
cos = cos((radians(angulo)))
tan = tan((radians(angulo)))

print(f"O comprimento do seno é {sin :.2f}")
print(f"O comprimento do cosseno é {cos :.2f}")
print(f"O comprimento da tangente é {tan :.2f}")