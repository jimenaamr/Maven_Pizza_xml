import pandas as pd
import xml.etree.cElementTree as ET

df_diccionario_datos = pd.read_csv('data_dictionary.csv',sep = ",", encoding = "LATIN_1")

tipos_diccionario = df_diccionario_datos.dtypes
nans_diccionario = df_diccionario_datos.isna().sum()
nulls_diccionario = df_diccionario_datos.isnull().sum()


df_detalle_pedidos = pd.read_csv('order_details.csv',sep = ";", encoding = "LATIN_1")

tipos_detalle_pedidos = df_detalle_pedidos.dtypes
nans_detalle_pedidos = df_detalle_pedidos.isna().sum()
nulls_detalle_pedidos = df_detalle_pedidos.isnull().sum()


df_pedidos = pd.read_csv('orders.csv',sep = ";", encoding = "LATIN_1")

tipos_pedidos = df_pedidos.dtypes
nans_pedidos = df_pedidos.isna().sum()
nulls_pedidos = df_pedidos.isnull().sum()


df_tipos_pizza = pd.read_csv('pizza_types.csv', sep = ",", encoding = "LATIN_1")

tipos_tipos_pizza = df_tipos_pizza.dtypes
nans_tipos_pizza = df_tipos_pizza.isna().sum()
nulls_tipos_pizza = df_tipos_pizza.isnull().sum()


df_pizza = pd.read_csv('pizzas.csv', sep = ",", encoding = "LATIN_1")

tipos_pizza = df_pizza.dtypes
nans_pizza = df_pizza.isna().sum()
nulls_pizza = df_pizza.isnull().sum()

lista_tit_diccionario = list(df_diccionario_datos.columns)
lista_tit_detalle_pedidos = list(df_detalle_pedidos.columns)
lista_tit_pedidos = list(df_pedidos.columns)
lista_tit_tipos_pizza = list(df_tipos_pizza.columns)
lista_tit_pizza = list(df_pizza.columns)

root = ET.Element("root")
doc = ET.SubElement(root, "doc")
nodo1 = ET.SubElement(doc, "nodo1", name="nodo")

nodo1.text = 'El tipo de datos de cada columna en el data_dictionary.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_diccionario[0] + ', ' + lista_tit_diccionario[1] + ', ' + lista_tit_diccionario[2]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(tipos_diccionario[0]) + ', ' + str(tipos_diccionario[1]) + ', ' + str(tipos_diccionario[2])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El número de NaN de cada columna en el data_dictionary.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_diccionario[0] + ', ' + lista_tit_diccionario[1] + ', ' + lista_tit_diccionario[2]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(nans_diccionario[0]) + ', ' + str(nans_diccionario[1]) + ', ' + str(nans_diccionario[2])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El número de Null de cada columna en el data_dictionary.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_diccionario[0] + ', ' + lista_tit_diccionario[1] + ', ' + lista_tit_diccionario[2]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(nulls_diccionario[0]) + ', ' + str(nulls_diccionario[1]) + ', ' + str(nulls_diccionario[2])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El tipo de datos de cada columna en el order_details.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_detalle_pedidos[0] + ', ' + lista_tit_detalle_pedidos[1] + ', ' + lista_tit_detalle_pedidos[2] + ', ' + lista_tit_detalle_pedidos[3]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(tipos_detalle_pedidos[0]) + ', ' + str(tipos_detalle_pedidos[1]) + ', ' + str(tipos_detalle_pedidos[2]) + ', ' + str(tipos_detalle_pedidos[3])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El número de NaN de cada columna en el order_details.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_detalle_pedidos[0] + ', ' + lista_tit_detalle_pedidos[1] + ', ' + lista_tit_detalle_pedidos[2] + ', ' + lista_tit_detalle_pedidos[3]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(nans_detalle_pedidos[0]) + ', ' + str(nans_detalle_pedidos[1]) + ', ' + str(nans_detalle_pedidos[2]) + ', ' + str(nans_detalle_pedidos[3])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El número de Null de cada columna en el order_details.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_detalle_pedidos[0] + ', ' + lista_tit_detalle_pedidos[1] + ', ' + lista_tit_detalle_pedidos[2] + ', ' + lista_tit_detalle_pedidos[3]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(nulls_detalle_pedidos[0]) + ', ' + str(nulls_detalle_pedidos[1]) + ', ' + str(nulls_detalle_pedidos[2]) + ', ' + str(nulls_detalle_pedidos[3])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El tipo de datos de cada columna en el orders.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_pedidos[0] + ', ' + lista_tit_pedidos[1] + ', ' + lista_tit_pedidos[2]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(tipos_pedidos[0]) + ', ' + str(tipos_pedidos[1]) + ', ' + str(tipos_pedidos[2])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El número de NaN de cada columna en el orders.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_pedidos[0] + ', ' + lista_tit_pedidos[1] + ', ' + lista_tit_pedidos[2]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(nans_pedidos[0]) + ', ' + str(nans_pedidos[1]) + ', ' + str(nans_pedidos[2])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El número de Null de cada columna en el orders.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_pedidos[0] + ', ' + lista_tit_pedidos[1] + ', ' + lista_tit_pedidos[2]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(nulls_pedidos[0]) + ', ' + str(nulls_pedidos[1]) + ', ' + str(nulls_pedidos[2])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El tipo de datos de cada columna en el pizza_types.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_tipos_pizza[0] + ', ' + lista_tit_tipos_pizza[1] + ', ' + lista_tit_tipos_pizza[2] + ', ' + lista_tit_tipos_pizza[3]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(tipos_tipos_pizza[0]) + ', ' + str(tipos_tipos_pizza[1]) + ', ' + str(tipos_tipos_pizza[2]) + ', ' + str(tipos_tipos_pizza[3])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El número de NaN de cada columna en el pizza_types.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_tipos_pizza[0] + ', ' + lista_tit_tipos_pizza[1] + ', ' + lista_tit_tipos_pizza[2] + ', ' + lista_tit_tipos_pizza[3]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(nans_tipos_pizza[0]) + ', ' + str(nans_tipos_pizza[1]) + ', ' + str(nans_tipos_pizza[2]) + ', ' + str(nans_tipos_pizza[3])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El número de Null de cada columna en el pizza_types.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_tipos_pizza[0] + ', ' + lista_tit_tipos_pizza[1] + ', ' + lista_tit_tipos_pizza[2] + ', ' + lista_tit_tipos_pizza[3]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(nulls_tipos_pizza[0]) + ', ' + str(nulls_tipos_pizza[1]) + ', ' + str(nulls_tipos_pizza[2]) + ', ' + str(nulls_tipos_pizza[3])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El tipo de datos de cada columna en el pizzas.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_pizza[0] + ', ' + lista_tit_tipos_pizza[1] + ', ' + lista_tit_tipos_pizza[2] + ', ' + lista_tit_tipos_pizza[3]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(tipos_pizza[0]) + ', ' + str(tipos_pizza[1]) + ', ' + str(tipos_pizza[2]) + ', ' + str(tipos_pizza[3])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El número de NaN de cada columna en el pizzas.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_pizza[0] + ', ' + lista_tit_tipos_pizza[1] + ', ' + lista_tit_tipos_pizza[2] + ', ' + lista_tit_tipos_pizza[3]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(nans_pizza[0]) + ', ' + str(nans_pizza[1]) + ', ' + str(nans_pizza[2]) + ', ' + str(nans_pizza[3])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.SubElement(doc, "nodo2", atributo="algo").text = 'El número de Null de cada columna en el pizzas.csv es:'
ET.SubElement(doc, "nodo2", atributo="algo").text = lista_tit_pizza[0] + ', ' + lista_tit_tipos_pizza[1] + ', ' + lista_tit_tipos_pizza[2] + ', ' + lista_tit_tipos_pizza[3]
ET.SubElement(doc, "nodo2", atributo="algo").text = str(nulls_pizza[0]) + ', ' + str(nulls_pizza[1]) + ', ' + str(nulls_pizza[2]) + ', ' + str(nulls_pizza[3])
ET.SubElement(doc, "nodo2", atributo="algo").text = '\n'

ET.indent(root)
arbol = ET.ElementTree(root)
arbol.write("xml_informe_calidad.xml")
