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
Curves.polinomial(xi, yi, 2)

# Letra c
Curves.exponencial(xi, yi)

# Letra d
# aguardando resposta

# Letra e
xPrev = np.array([2000, 2005, 2014])
yValue = np.array([169.8, 184.2, 202.7])
Curves.previsaoPolinomial(xi, yi, 2, xPrev, yValue)
Curves.previsaoExponencial(xi, yi, xPrev, yValue)