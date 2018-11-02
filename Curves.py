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

def quadratic(xi, yi, degree):
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

# Quadratico tem graus como parametro
def quadraticPrevision(xi, yi, degree, xPrev, yPrev):
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


def exponencialPrevision(xi, yi, xPrev, yPrev):
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