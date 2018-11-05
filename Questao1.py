import Curves
import numpy as np

xi = np.array([
        1872, 1890, 1900, 1920, 1940, 1950, \
        1960, 1970, 1980, 1991, 1996
    ])

yi = np.array([
        9.9, 14.3, 17.4, 30.6, 41.2, \
        51.90, 70.2, 93.1, 119.0, 146.2, 157.1
    ])


# Letra a:
Curves.dispersao(xi, yi, xString="Ano", yString="População (Milhões de Hab.)")

# Letra b:
r1 = Curves.polinomial(xi, yi, 2)

# Letra c
r2 = Curves.exponencial(xi, yi)

# Letra d
v1 = Curves.variancia(r1, xi)
v2 = Curves.variancia(r2, xi)
if v1 > v2:
    print("Grau 2")
    Curves.polinomial(xi, yi, 2)
else:
    print("Exponencial")
    Curves.exponencial(xi, yi)

# Letra e
xPrev = np.array([2000, 2005, 2014])
yValue = np.array([169.8, 184.2, 202.7])
Curves.previsaoPolinomial(xi, yi, 2, xPrev, yValue)
Curves.previsaoExponencial(xi, yi, xPrev, yValue)