import lectorXML
from ListaCircular import *
import escribirXML

datos = linked_list_circular()
datos2 = linked_list_circular()
ruta = ""

if __name__ == '__main__':
    op = None
    while op != 6:
        print("----------------------------------")
        print("Bienvenido a Practica 1")
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar grafica")
        print("6. Salida")
        print("----------------------------------")
        op = int(input())

        if op == 1:
            print("----------------------------------")
            # ruta = input("Ingrese la ruta\n")
            ruta = "C:\\Users\\Storias\\Desktop\\1ER SEMESTRE 2021\\IPC2\\Proyecto1\\entrada1.xml"
            datos = lectorXML.leer_Archivo(ruta)
            datos.imprimir()

            # C:\Users\Storias\Desktop\1ER SEMESTRE 2021\IPC2\Proyecto1\entrada1.xml
            # C:\Users\Storias\Desktop\1ER SEMESTRE 2021\IPC2\Proyecto1\salida2.xml
            print("----------------------------------")
        elif op == 2:
            print("----------------------------------")
            datos2 = lectorXML.leer_Archivo(ruta)
            datos2.crearMatricesReducidas()
            datos2.imprimirMatrizReducida()
            print("----------------------------------")
        elif op == 3:
            print("----------------------------------")
            #ruta2 = input("Ingrese la ruta\n")
            ruta2 = "C:\\Users\\Storias\\Desktop\\1ER SEMESTRE 2021\\IPC2\\Proyecto1\\salida2.xml"
            escribirXML.escribirArchivoXML(datos2, ruta2)
            print("----------------------------------")
        elif op == 4:
            print("----------------------------------")

            print("----------------------------------")
        elif op == 5:
            print("----------------------------------")
            print("Wilmer Estuardo Vasquez Raxon")
            print("201800678")
            print("Introduccion a la programacion y computacion 2 seccion \"E\" ")
            print("Ingenieria en Ciencias y Sistemas")
            print("4to Semestre")
            print("----------------------------------")
        elif op == 6:
            print("----------------------------------")
        else:
            print("nose :v")
