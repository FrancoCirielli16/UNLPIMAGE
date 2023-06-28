import pandas as pd
import matplotlib.pyplot as plt
import time
from src.constants.directions import METADATA, EVENTS
from src.manipulators.user import User
from wordcloud import WordCloud


def graf_torta_tipos() -> plt.Figure:
    """
    Esta función genera la figura "pie" con los tipos de imagenes
    

    args:
        No requiere

    Returns:
        plt.Figure
    """
    data = pd.read_csv(METADATA, encoding='UTF-8', delimiter=';')
    lista = data.groupby('Tipo')['Tipo'].count()
    tipos = lista.index.tolist()
    valores = lista.tolist()

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.pie(valores, labels=tipos, autopct='%1.1f%%')
    ax.set_title('Tipo de imagenes')
    return fig

def ranking_tags() -> pd.DataFrame:
    """
    Esta función genera un Data Frame con el ranking de mayores cantidades de tag usadas
    

    args:
        No requiere

    Returns:
        pd.DataFrame: 
    """
        
    data = pd.read_csv(METADATA, encoding='UTF-8', delimiter=';')
    tags = data['Lista de tags'].str.split(';')

    tag_list = []
    for tag_group in tags:
        tag_list.extend([tag.strip()
                        for tag in tag_group for tag in tag.split(',')])

    # Calcular el conteo de cada etiqueta
    tag_counts = pd.Series(tag_list).value_counts()

    # Obtener las 5 etiquetas más usadas
    top_tags = tag_counts.head(5)

    ranking_df = pd.DataFrame(
        {'Tag': top_tags.index, 'Cantidad': top_tags.values})
    ranking_df.index += 1
    
    return(ranking_df)


def graf_torta_generos() -> plt.Figure:
    """
    Esta función genera la figura "pie" con los datos del archivo, agrupando por generos
    

    args:
        No requiere

    Returns:
        plt.Figure: 
    """
    # Cargar datos del archivo CSV
    data = pd.read_csv(EVENTS, encoding='UTF-8', delimiter=';')

    usuarios_generos = User.get_usuarioygenero()

    # Obtener los usuarios únicos
    usuarios_operaciones = [(usuario, operacion) for usuario, operacion in zip(
        data['Usuario'], data['Operacion'])]

    # Obtener todos los géneros presentes en el diccionario
    generos = set(usuarios_generos.values())

    # Inicializar el contador de operaciones por género
    operaciones_por_genero = {genero: 0 for genero in generos}
    for usuario in usuarios_operaciones:
        # Obtener el género del usuario o usar "Otros" como valor predeterminado
        genero = usuarios_generos.get(usuario[0])
        operacion = usuario[1]

        if 'imagen-clasificada' == operacion:
            operaciones_por_genero[genero] += 1

        if 'modificacion-imagen' == operacion:
            operaciones_por_genero[genero] += 1

    # Calcular los porcentajes
    total_operaciones = sum(operaciones_por_genero.values())
    porcentajes = {genero: (count / total_operaciones) *
                   100 for genero, count in operaciones_por_genero.items()}

    # Generar el gráfico de torta

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.pie(porcentajes.values(), labels=porcentajes.keys(), autopct='%1.1f%%')
    ax.set_title('Porcentaje de operaciones según género')

    return fig


def graf_torta_uso_genero() -> plt.Figure:
    """
    Esta función genera la figura "pie" con los datos de uso de la App por genero
    

    args:
        No requiere

    Returns:
        plt.Figure: 
    """
    # Cargar datos del archivo CSV
    data = pd.read_csv(EVENTS, encoding='UTF-8', delimiter=';')

    usuarios_generos = User.get_usuarioygenero()

    # Obtener los usuarios únicos
    usuarios_operaciones = [(usuario, operacion) for usuario, operacion in zip(
        data['Usuario'], data['Operacion'])]

    # Obtener todos los géneros presentes en el diccionario
    generos = set(usuarios_generos.values())

    # Inicializar el contador de operaciones por género
    operaciones_por_genero = {genero: 0 for genero in generos}

    for usuario in usuarios_operaciones:
        # Obtener el género del usuario o usar "Otros" como valor predeterminado
        genero = usuarios_generos.get(usuario[0])
        operacion = usuario[1]

        if 'imagen-clasificada' == operacion:
            operaciones_por_genero[genero] += 1

        if 'modificacion-imagen' == operacion:
            operaciones_por_genero[genero] += 1

        if 'Genero-meme' == operacion:
            operaciones_por_genero[genero] += 1

        if 'Genero-collage' == operacion:
            operaciones_por_genero[genero] += 1

    # Calcular los porcentajes
    total_operaciones = sum(operaciones_por_genero.values())
    porcentajes = {genero: (count / total_operaciones) *
                   100 for genero, count in operaciones_por_genero.items()}

    # Generar el gráfico de torta

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.pie(porcentajes.values(), labels=porcentajes.keys(), autopct='%1.1f%%')
    ax.set_title('Porcentaje de uso según género')

    return fig




def graf_lineal() -> plt.figure:
    """
    Esta función genera la figura "plot" con los datos de actualización 


    args:
        No requiere

    Returns:
        plt.figure
    """
    
    def sumar_repetidos(lista):
        diccionario = {}
        for elemento in lista:
            if elemento in diccionario:
                diccionario[elemento] += 1
            else:
                diccionario[elemento] = 1
        return diccionario
    data = pd.read_csv(EVENTS, encoding='UTF-8', delimiter=';')
    data = data[data['Operacion'] == 'modificacion-imagen']
    datos_agrupados = data.sort_values("Fecha y hora")
    datos_agrupados = data.groupby("Fecha y hora")["Fecha y hora"].apply(pd.Series)
    tiempo = datos_agrupados.to_list()
    tiempo = [time.localtime(x).tm_yday for x in tiempo]
    tiempo.sort()
    tiempo = sumar_repetidos(tiempo)
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(tiempo.keys(), tiempo.values())
    ax.set_xlabel("Dia del año")
    ax.set_ylabel("CANTIDAD ACT.")
    ax.set_title("Gráfico Actualizaciones App")
    return fig

def graf_dias () -> plt.figure:
    """

    Esta función genera la figura "bar" con los datos de los dias donde los usuarios 
    realizaron alguna actividad en la aplicación

    args:
        No requiere

    Returns:
        plt.figure
    """
    data = pd.read_csv(METADATA, encoding='UTF-8', delimiter=';')
    datos = data["Ultima actualizacion"]
    datos = [time.localtime(x).tm_wday for x in datos]
    dias = [0, 0, 0, 0, 0, 0, 0]
    nombres = ["Lunes", "Martes", "Miercoles",
               "Jueves", "Viernes", "Sabado", "Domingo"]
    for x in datos:
        dias[x] += 1
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.bar(nombres, dias)
    return fig



def max_max () ->tuple:
    """
    Esta función calcula los maximos en cuando a ancho y alto de las imagenes del 
    archivo
    

    args:
        No requiere

    Returns:
        tuple:
    """
    data = pd.read_csv(METADATA, encoding='UTF-8', delimiter=';')
    col = data["Resolucion"].str.split(",")
    valores = col.tolist()
    listancho = [x[0] for x in valores]
    listalto = [x[1] for x in valores]
    return (max(listancho), max(listalto))

def graf_disp () -> plt.figure:
    """
    Esta función genera la figura "scatter" con la informacion de las resoluciones 
    utilizadas por los usuarios 
    

    args:
        No requiere

    Returns:
        plt.figure:
    """
    data = pd.read_csv(METADATA, encoding="UTF-8", delimiter=";")
    lista = data.groupby("Resolucion")["Resolucion"].all()
    valores = lista.index.tolist()
    valores1 = [int(x.split(",")[0]) for x in valores]
    valores2 = [int(x.split(",")[1]) for x in valores]
    valores1.sort()
    valores2.sort()
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(valores1, valores2)
    ax.set_xlabel("Ancho")
    ax.set_ylabel("Alto")
    return fig


def usuarios_imagenes_act() -> pd.DataFrame:
    """
    Esta función calcula el ranking de promedios de tamaños 


    args:
        No requiere

    Returns:
        pd.DataFrame
    """

    data = pd.read_csv(METADATA, delimiter=';')

    usuarios = data.groupby('Perfil que actualizo')[
        'Tamaño'].agg(['sum', 'mean', 'count'])

    ranking_df = pd.DataFrame(usuarios).reset_index()
    ranking_df['Promedio'] = ranking_df['mean']
    ranking_df.drop(columns=['mean'], inplace=True)
    ranking_df.columns = ['Usuario', 'Suma',
                          'Cantidad de Imágenes', 'Tamaño promedio(MB)']
    ranking_df = ranking_df[['Usuario', 'Suma', 'Cantidad de Imágenes', 'Tamaño promedio(MB)']].sort_values(by=['Tamaño promedio(MB)'], ascending=False)
    ranking_df = ranking_df.reset_index()
    ranking_df.index += 1
    ranking_df = ranking_df[['Usuario', 'Suma', 'Cantidad de Imágenes', 'Tamaño promedio(MB)']]
    return ranking_df

def ranking_memes() -> pd.DataFrame:
    """
    Esta función calcula el ranking con los usuarios que generaron más memes

    

    args:
        No requiere

    Returns:
        pd.DataFrame: 
    """
    data = pd.read_csv(EVENTS, delimiter=';')

    # Filtrar los registros de generación de memes
    memes_data = data[data['Operacion'] == 'Genero-meme']

    ranking_memes = memes_data['Ruta imagen'].value_counts().head(5)

    # Crear un DataFrame con los datos del ranking
    ranking_df = pd.DataFrame(ranking_memes).reset_index()
    ranking_df.columns = ['Imágenes', 'Cantidad']
    ranking_df.index += 1
    # Mostrar el ranking como una tabla en Streamli
    return ranking_df

def ranking_collage() -> pd.DataFrame:
    """

    Esta función calcula el ranking con los usuarios que generaron más collages


    args:
        No requiere

    Returns:
        pd.DataFrame: 
    """
    data = pd.read_csv(EVENTS, delimiter=';')

    # Filtrar los registros de generación de memes
    collage_data = data[data['Operacion'] == 'Genero-collage']

    ranking_collage = collage_data['Ruta imagen'].value_counts().head(5)

    # Crear un DataFrame con los datos del ranking
    ranking_df = pd.DataFrame(ranking_collage).reset_index()
    ranking_df.columns = ['Imágenes', 'Cantidad']
    ranking_df.index += 1
    # Mostrar el ranking como una tabla en Streamli
    return ranking_df


def grafico_operaciones() -> plt:
    """
    Esta función genera una figura "bar" con las cantidades de operaciones realizadas


    args:
        No requiere

    Returns:
        plt
    """
    data = pd.read_csv(EVENTS, delimiter=';')

    operaciones = data['Operacion'].value_counts()

    plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura
    plt.bar(operaciones.index, operaciones.values)
    plt.xlabel('Operación')
    plt.ylabel('Cantidad')
    plt.title('Cantidades de cada operación realizada')
    plt.xticks(rotation=15)
    return plt


import pandas as pd
import matplotlib.pyplot as plt

def grafico_operaciones_por_nick() -> plt:
    """
    Esta función genera una figura "plot" que contiene la cantidad de operaciones
    por nick

    args:
        No requiere

    Returns:
        plt:
    """
    data = pd.read_csv(EVENTS, delimiter=';')

    operaciones_por_nick = data.groupby(['Usuario', 'Operacion']).size().unstack()

    ax = operaciones_por_nick.plot(kind='barh', stacked=True)
    plt.ylabel('Nick')
    plt.title('Cantidades de operaciones por nick')
    plt.legend(title='Operación', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks([])
    plt.yticks(rotation=75)

    for rect in ax.containers:
        ax.bar_label(rect)

    plt.tight_layout(pad=1.5)
    return plt

def nube_de_palabras() -> plt:
    """
    Esta función genera un nube de palabras con los tags más utilizados en la app

    args:
        No requiere

    Returns:
        plt: 
    """

    data = pd.read_csv(METADATA, delimiter=';')
    # Obtener la columna de las tags y eliminar los valores nulos
    tags = data['Lista de tags'].dropna()

    # Unir las palabras en un solo texto
    texto = " ".join(tags)

    # Crear el objeto WordCloud
    wordcloud = WordCloud(width=800, height=400,
                          background_color='white').generate(texto)

    # Mostrar la nube de palabras
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    return plt

def nube_de_palabras_collages() -> plt:
    """
    Esta función genera una nube de palabras con los titulos de los collages creados
    

    args:
        No requiere

    Returns:
        plt: 
    """
    data = pd.read_csv(EVENTS, delimiter=';')

    collage_data = data[data['Operacion'] == 'Genero-collage']
    # Obtener la columna de las tags y eliminar los valores nulos
    textos = collage_data['Texto'].dropna()

    # Unir todas las palabras en un solo texto
    texto = " ".join(textos)
    # Crear el objeto WordCloud
    wordcloud = WordCloud(width=800, height=400,
                          background_color='white').generate(texto)

    # Mostrar la nube de palabras
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    return plt

def nube_de_palabras_memes() -> plt:
    """
    Esta función genera una nube de palabras con los textos utilizados para los memes
    
    agrs:
        No requiere


    Returns:
        plt: 
    """

    data = pd.read_csv(METADATA, delimiter=';')

    meme_data = data[data['Operacion'] == 'Genero-meme']
    # Obtener la columna de las tags y eliminar los valores nulos
    tags = meme_data['Texto'].dropna()

    # Obtener las tags repetidas
    tags_repetidas = tags.value_counts(
    )[tags.value_counts() > 1].index.tolist()

    # Unir las palabras en un solo texto
    texto = " ".join(tags_repetidas)

    # Crear el objeto WordCloud
    wordcloud = WordCloud(width=800, height=400,
                          background_color='white').generate(texto)

    # Mostrar la nube de palabras
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    return plt