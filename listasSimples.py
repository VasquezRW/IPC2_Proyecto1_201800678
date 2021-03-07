class nodoNumero:
    def __init__(self, numero=None, y=None, next=None):
        self.numero = numero
        self.next = next
        self.y = y


class Fila:

    def __init__(self, x=None, frecuencia=None):
        self.head = None  
        self.x = x
        self.frecuencia = frecuencia
        self.size = 0

    def insertar(self, numero, y):
        if not self.head:
            self.head = nodoNumero(numero=numero, y=y)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = nodoNumero(numero=numero, y=y)
        self.size += 1

    def insertarPosicion(self, numero, y):
        current = self.head
        while current.next is not self.head:
            if current.y == y:
                current.numero = numero
                break
            else:
                current = current.next

    def comprobarPosicion(self, y):
        current = self.head
        while current.next is not self.head:
            if current.y == y:
                if current.numero is not None:
                    return True
                else:
                    return False
            else:
                current = current.next

    def obtenerBinario(self):
        fila = []
        current = self.head
        for i in range(0, self.size+1):
            if current.numero == 0:
                fila.append(0)
            else:
                fila.append(1)
            current = current.next
        return fila

    def convertirBinario(self):
        current = self.head
        while current is not None:
            if current.numero != 0:
                current.numero = 1
            current = current.next

    def imprimir(self):
        nod = self.head
        while nod is not None:

            print(nod.numero, end="|")
            nod = nod.next


# --------------------------------------------------------------------------

class nodoFila:
    def __init__(self, fila=None, next=None):
        self.fila = fila
        self.next = next


class Matriz:

    def __init__(self):
        self.head = None
        self.size = 0

    def insertar(self, fila):
        if not self.head:
            self.head = nodoFila(fila=fila)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = nodoFila(fila=fila)
        self.size += 1

    def insertarPosicion(self, x, y, numero):
        nodo = self.head
        while nodo.next is not self.head:
            if nodo.fila.x == x:
                nodo.fila.insertarPosicion(numero, y)
                break
            else:
                nodo = nodo.next

    def comprobarPosicion(self, x, y):
        nodo = self.head
        while nodo.next is not self.head:
            if nodo.fila.x == x:
                return nodo.fila.comprobarPosicion(y)
            else:
                nodo = nodo.next

    def eliminarfila(self, x):
        # print("matriz antes de eliminar fila")
        # self.imprimir()
        previous = self.head
        current = previous.next
        if self.head.fila.x == x:
            self.head = self.head.next
        else:
            while current.fila.x != x:
                previous = current
                current = current.next
            previous.next = current.next

        self.size -= 1
        # print("matriz despues de eliminar fila")
        # self.imprimir()
    """

    def eliminarfila(self, x):
        current = self.head
        previous = None
        while current and current.fila.x != x:
            previous = current
            current = current.next
            if previous is None:
                self.head = current.next
            elif current:
                previous.next = current.next
                current.next = None
    """
    def reducirMatriz(self):
            actual = self.head
            while actual is not None:
                siguiente = actual.next
                while siguiente is not None:
                    if actual.fila.obtenerBinario() == siguiente.fila.obtenerBinario():
                        self.sumarFila(actual.fila, siguiente.fila)
                        actual.fila.frecuencia += 1
                        filaAeliminar = int(siguiente.fila.x)
                        siguiente = siguiente.next
                        self.eliminarfila(filaAeliminar)
                    else:
                        siguiente = siguiente.next
                actual = actual.next

    def sumarFila(self, fila1, fila2):
        actualFila1 = fila1.head
        actualFila2 = fila2.head
        while actualFila1 is not None:
            actualFila1.numero += int(actualFila2.numero)
            actualFila1 = actualFila1.next
            actualFila2 = actualFila2.next

    def imprimir(self):
        nodo = self.head
        while nodo is not None:
            print(f" frecuencia: {nodo.fila.frecuencia} | {nodo.fila.imprimir()}")
            nodo = nodo.next

    def convertirMatrizBinaria(self):
        actual = self.head
        while actual is not None:
            actual.fila.convertirBinario()
            actual = actual.next
