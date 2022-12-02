import xml.etree.cElementTree as ET
import pandas as pd

pre_ing = pd.read_csv('prediccion_ingredientes16.csv')
lista_ingredientes = list(pre_ing['Ingrediente'])
lista_cantidades = list(pre_ing['Cantidad a comprar'])
lista_datos = []

longitud = len(lista_ingredientes)
contador = 0

while len(lista_datos) < longitud:
    lista = []
    lista.append(lista_ingredientes[contador])
    lista.append(lista_cantidades[contador])
    lista_datos.append(lista)
    contador += 1


root = ET.Element("root")
doc = ET.SubElement(root, "doc")
nodo1 = ET.SubElement(doc, "nodo1", name="nodo")
nodo1.text = 'Ingrediente, Cantidad a comprar'

for i in range(len(lista_datos)):

    ET.SubElement(doc, "nodo2").text = lista_datos[i][0] + ', ' + str(lista_datos[i][1])
    ET.indent(root)
    arbol = ET.ElementTree(root)
    arbol.write("xml_prediccion_ingredientes.xml")

