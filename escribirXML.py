import subprocess
import xml.etree.ElementTree as ET


def escribirArchivoXML(datos, ruta):
    try:
        elementoMatrices = ET.Element("matrices")
        matrizz = datos.head
        for i in range(0, datos.size):
            filaa = matrizz.matriz.head
            elementoMatriz = ET.SubElement(elementoMatrices, "matriz", nombre=matrizz.nombre, n=str(matrizz.n),
                                           m=str(matrizz.m), g=str(matrizz.matriz.size))
            # i = 1
            while filaa is not None:
                dato = filaa.fila.head
                while dato is not None:
                    ET.SubElement(elementoMatriz, "dato", x=str(filaa.fila.x), y=str(dato.y)).text = str(dato.numero)
                    dato = dato.next
                filaa = filaa.next
                # i += 1
            filaa = matrizz.matriz.head
            while filaa is not None:
                ET.SubElement(elementoMatriz, "frecuencia", g=str(filaa.fila.x)).text = str(filaa.fila.frecuencia)
                filaa = filaa.next
            matrizz = matrizz.next


        arbol = ET.ElementTree(elementoMatrices)


        arbol.write(ruta, encoding='UTF-8', xml_declaration=True)

        # archivo = open(ruta, 'wb')
        # archivo.write(ET.tostring(elementoMatrices, encoding='utf-8').decode('utf-8'))

        #b_xml = ET.tostring(elementoMatrices, encoding='utf-8')
        #with open(ruta, 'wb') as f:
        #    f.write(b_xml)

        subprocess.Popen([ruta], shell=True)
    except:
        print("algo ocurrio")

