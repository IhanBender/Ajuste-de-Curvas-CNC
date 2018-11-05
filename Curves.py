import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg 

def dispersao(xi, yi, xString='x', yString='y'):
    if len(xi) != len(yi):
        raise NameError('Listas de valores com tamanhos diferentes') 
    size = len(xi)

    #grafico
    plt.xlabel(xString)
    plt.ylabel(yString)
    plt.plot(xi, yi, 'bo', label="Diagrama de Dispersão")
    plt.show()

def polinomial(xi, yi, degree):
    if len(xi) != len(yi):
        raise NameError('Listas de valores com tamanhos diferentes') 

    #preenche a matriz de acordo com o grau desejado
    matrix = []
    for i in range (degree + 1):
        matrix.append(xi ** (degree - i))

    V = np.array(matrix).transpose()  
    a = ((np.linalg.inv((V.transpose()).dot(V))).dot(V.transpose())).dot(yi) 

    xx = np.linspace(xi[0], xi[len(xi)-1])  
    plt.plot(xi,yi,'ro',xx,np.polyval(a,xx),'b-')  
    plt.grid()
    plt.show()

    results = []
    for value in xi:
        results.append(np.polyval(a,value))

    return results


def exponencial(xi, yi):
    if len(xi) != len(yi):
        raise NameError('Listas de valores com tamanhos diferentes')

    V = np.array([np.ones(len(xi)),xi]).transpose()  
    a = np.linalg.lstsq(V,np.log(yi))[0]  
    a[0] = np.exp(a[0])  

    xx = np.linspace(xi[0], xi[len(xi)-1])  
    plt.plot(xi,yi,'ro',xx, a[0] * np.exp(a[1]*xx),'b-')  
    plt.grid()
    plt.show()

    results = []
    for value in xi:
        results.append(a[0] * np.exp(a[1]*value))

    return results

# Quadratico tem graus como parametro
def previsaoPolinomial(xi, yi, degree, xPrev, yPrev):
    if len(xi) != len(yi):
        raise NameError('Listas de valores com tamanhos diferentes') 

    #preenche a matriz de acordo com o grau desejado
    matrix = []
    for i in range (degree + 1):
        matrix.append(xi ** (degree - i))

    V = np.array(matrix).transpose()  
    a = ((np.linalg.inv((V.transpose()).dot(V))).dot(V.transpose())).dot(yi) 

    # alcance dos valores de x
    xx = np.linspace(xi[0], xPrev[len(xPrev) - 1])  
    plt.plot(                                \
        xi,yi,'ro',                          \
        xx,np.polyval(a,xx),'b-',            \
        xPrev,np.polyval(a,xPrev), 'bo',     \
        xPrev,yPrev, 'go'                    \
    )  
    plt.grid()
    plt.show()

def previsaoPolinomialCega(xi, yi, degree, xPrev):
    if len(xi) != len(yi):
        raise NameError('Listas de valores com tamanhos diferentes') 

    #preenche a matriz de acordo com o grau desejado
    matrix = []
    for i in range (degree + 1):
        matrix.append(xi ** (degree - i))

    V = np.array(matrix).transpose()  
    a = ((np.linalg.inv((V.transpose()).dot(V))).dot(V.transpose())).dot(yi) 

    # alcance dos valores de x
    xx = np.linspace(xi[0], xPrev[len(xPrev) - 1])  
    plt.plot(                                \
        xi,yi,'ro',                          \
        xx,np.polyval(a,xx),'b-',            \
        xPrev,np.polyval(a,xPrev), 'bo',     \
    )  
    plt.grid()
    plt.show()


def previsaoExponencial(xi, yi, xPrev, yPrev):
    if len(xi) != len(yi):
        raise NameError('Listas de valores com tamanhos diferentes')

    V = np.array([np.ones(len(xi)),xi]).transpose()  
    a = np.linalg.lstsq(V,np.log(yi))[0]  
    a[0] = np.exp(a[0])  

    xx = np.linspace(xi[0], xPrev[len(xPrev) - 1])
    plt.plot(
        xi,yi,'ro',xx, a[0] * np.exp(a[1]*xx),'b-',     \
        xPrev,a[0] * np.exp(a[1]*xPrev),'bo',           \
        xPrev,yPrev, 'go'                               \
    )  
    plt.grid()
    plt.show()


def variancia(list1, list2):
    if len(list1) != len(list2):
        raise NameError('Listas com tamanhos diferentes')

    v = 0
    for i in range (len(list1)):
        v = v + ((list1[i] - list2[i]) ** 2)

    return v
