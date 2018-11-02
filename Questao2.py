import Curves
import numpy as np

xi = np.array(range(6, 17))
yi = np.array([
    0.029, 0.052, 0.079, 0.125, 0.181,  \
    0.425, 0.261, 0.738, 1.130, 1.882, 2.812   \
])

# Letra a
Curves.dispersao(xi, yi, xString="Dias", yString="gramas")

# Letra b
Curves.polinomial(xi, yi, 5)

# Letra c
# Aguardando resposta

# Letra d
# A partir da resposta em c, testar para dia = 20