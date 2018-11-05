import Curves
import numpy as np

xi = np.array(range(6, 17))
yi = np.array([
    0.029, 0.052, 0.079, 0.125, 0.181,  \
    0.425, 0.261, 0.738, 1.130, 1.882, 2.812   \
])
xPrev = np.array([20])

results = []

# Letra a
Curves.dispersao(xi, yi, xString="Dias", yString="gramas")

# Letra b
for i in range(6):
    results.append(Curves.polinomial(xi, yi, i))

# Letra c
index = 0
menor = results[0]
for i in range(6):
    if results[i] < menor:
        index = i

if index != -1:
    print("Grau: " + str(index))
    Curves.polinomial(xi, yi, index)
else:
    raise NameError("Algo de errado aconteceu")    


# Letra d
Curves.previsaoPolinomialCega(xi, yi, index, xPrev)