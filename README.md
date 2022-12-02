# INFORME DE CALIDAD Y PREDICCIÓN EN XML

En este repositorio se encuentran los archivos necesarios para hacer un xml de la predicción sobre los ingredientes que una pizzería deberá comprar semanalmente en función de los datos de dicho negocio de 2016. Además, también crea un xml con un informe de calidad sobre los datos trabajados.

## Archivos Adjuntados

- data_dictionary.csv: Explicación acerca de los datos que encontraremos en los demás csv.

- order_details.csv: Detalles sobre los pedidos que se han realizado a lo largo del año. En él encontramos el identificador del pedido, el identificador de la pizza pedida y la cantidad pedida. Deberemos limpiar los datos, ya que no están en el formato correcto.

- orders.csv: Detalles sobre los pedidos que se han realizado a lo largo del año. En él encontramos el identificador del pedido, la fecha en la que se realizó y la hora. Deberemos limpiar los datos, ya que no están en el formato correcto.

- pizza_types.csv: Detalles sobre las pizzas disponibles en la pizzaría. En él encontramos el identificador del tipo de pizza, su nombre completo, la categoría en la que está y los ingredientes necesarios para prepararla.

- pizzas.csv: Detalles sobre las pizzas disponibles en la pizzaría. En él encontramos el identificador del tipo de pizza, su tipo, su tamaño y su precio.

- prediccion_ingredientes16.csv: Dataframe creado tras ejecutar el archivo codigo_prediccion.py. Te ofrece una predicción de los ingredientes que la pizzería debería comprar semanalmente en función de los datos de 2016 analizados.

- requirements.txt: En este archivo encontramos las librerías que se necesitan instalar para poder ejecutar los archivos.

- crear_prediccion_xml.py: En este archivo encontramos el código necesario para crear el xml a partir del prediccion_ingredientes16.csv con la predicción de los ingredientes a comprar semanalmente.

- crear_informe_xml.py: Código neceario para hacer un informe de calidad en formato xml sobre los datos encontrados en data_dictionary.csv, order_details.csv, orders.csv, pizza_types.csv y pizzas.csv.

- xml_informe_calidad.xml: Informe de calidad sobre los datos de los csv en formato xml.

- xml_prediccion_ingredientes_xml: Predicción de los ingredientes a comprar en el csv prediccion_ingredientes16.csv en formato xml.

## Modo de Ejecución

1. Instalar el requirements.txt
2. Ejecutar el archivo crear_informe_xml.py para realizar el informe de calidad de los datos de cada uno de los csv en formato xml.
3. Ejecutar el archivo crear_prediccion_xml.py para transformar el archivo prediccion_ingredientes16.csv a formato xml.
