from xml.dom import minidom
from ListaCircular import *
from listasSimples import *


def leer_Archivo(ruta):
    mydoc = minidom.parse(ruta)
    items = mydoc.getElementsByTagName('matriz')
    matrices = linked_list_circular()
    for elemento in items:
        matrizCorrecta = True
        nombre = elemento.attributes['nombre'].value
        #print(nombre)
        n = int(elemento.attributes['n'].value)
        m = int(elemento.attributes['m'].value)
        datos = elemento.getElementsByTagName('dato')
        if matrices.comprobar_Nombre(nombre):
            matriz = crear_matriz(n, m)
            for dato in datos:
                x = int(dato.attributes['x'].value)
                y = int(dato.attributes['y'].value)
                if 0 < x <= n and 0 < y <= m:
                    if not matriz.comprobarPosicion(x, y):
                        matriz.insertarPosicion(x, y, int(dato.firstChild.data))
                    else:
                        print("posicion repetida")
                        matrizCorrecta = False
                else:
                    print("Dato con posiciones fuera de rango")
                    matrizCorrecta = False
            if matrizCorrecta:
                # matriz.imprimir()
                matrices.insertar(matriz=matriz, nombre=nombre, n=n, m=m)
            else:
                print(f"Matriz {nombre} no ingresada verifique los datos")
        else:
            print(f"Matriz {nombre} con nombre repetido")
    return matrices
    # matrices.imprimir()


def crear_matriz(n, m):
    matriz = Matriz()
    fin = int(n) + 1
    fin2 = int(m) + 1
    for i in range(1, fin):
        fila = Fila(i, 1)
        for j in range(1, fin2):
            fila.insertar(None, j)
        # fila.imprimir()
        matriz.insertar(fila)
    # matriz.imprimir()
    return matriz
