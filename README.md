# UNLPIMAGE

Este proyecto es una aplicacion de escritorio que permite realizar operaciones basicas sobre imagenes. Fue desarrollado en el marco de la materia "Seminario de Lenguajes" de la Universidad Nacional de La Plata.

## Instalacion

> **Nota:** El proyecto fue desarrollado en python 3.11
>
> En caso de no tener instalado python 3.11, referirse a la [documentacion oficial](https://www.python.org/downloads/) para instalarlo

Para instalar el proyecto se debe clonar el repositorio

```bash
# <url> es la url de este repositorio
git clone <url>
```

Para instalar las dependencias se recomienda utilizar un entorno virtual de python

```bash
# crear el entorno virtual
python -m venv .venv

# activar el entorno virtual, ejemplo con bash
source .venv/bin/activate

# instalar las dependencias
pip install -r requirements.txt
```

## Uso

Para ejecutar el proyecto se debe ejecutar el archivo unlpimage.py

```bash
python unlpimage.py
```

## Funcionalidades

- [X] Perfiles de usuario
- [X] Customizar interfaz
- [x] Etiquetar imagenes
- [x] Generar collage
- [x] Generar meme
- [x] Estadisticas

## Etiquetar Imagen

La funcionalidad de Etiquetar Imagen permite asignar etiquetas y descripciones a las imágenes para una mejor organización y clasificación. Cada imagen etiquetada se registra en un archivo CSV dedicado que almacena la metadata correspondiente, incluyendo las etiquetas y descripciones proporcionadas por los usuarios. Cualquier usuario tiene la capacidad de actualizar la metadata de las imágenes, lo que permite un manejo colaborativo y flexible de la información asociada a cada imagen.

El proyecto utiliza rutas relativas para gestionar las ubicaciones de los archivos y carpetas relacionados con cada usuario. Esto garantiza la portabilidad y la correcta organización de los datos, independientemente del sistema operativo utilizado.

## Generar Collage

La función de generar collage te permite crear composiciones visuales a partir de varias imágenes. Utilizando un archivo JSON, puedes definir la ubicación y el tamaño de los recuadros en los que se colocarán las imágenes dentro del collage. Estos recuadros son flexibles y pueden ser ajustados según tus necesidades.

Una vez que se ha generado el collage, se guarda automáticamente en una carpeta específica creada para cada usuario. También se puede acceder al collage generado desde la interfaz de usuario para visualizarlo o aplicarle operaciones adicionales.

## Generar Meme

La función de generar meme te permite crear imágenes con texto superpuesto, siguiendo los estilos típicos de los memes. Utilizando un archivo JSON, puedes especificar los datos de los cuadros de texto donde se colocará el texto deseado. Puedes personalizar el tamaño, la posición y el estilo del texto en cada cuadro.

Una vez que se ha generado el meme, se guarda automáticamente en la carpeta correspondiente al usuario. Puedes acceder a tus memes generados desde la interfaz de usuario para verlos, compartirlos o aplicarles modificaciones adicionales.

Cabe destacar que tanto el generador de collages como el generador de memes crean y almacenan las imágenes generadas en carpetas específicas para cada usuario. Estas carpetas se crean automáticamente cuando se registra un nuevo usuario en la aplicación y contienen el avatar del usuario, los collages y los memes generados. Todo esto se gestiona utilizando rutas relativas para garantizar un almacenamiento organizado y accesible.

## Estadísticas

La aplicación también ofrece una funcionalidad de generación de estadísticas utilizando la biblioteca Streamlit junto con la manipulación de datos utilizando Pandas. Estas estadísticas se generan a partir de los registros de eventos almacenados en archivos CSV, proporcionando información sobre el uso y los patrones de interacción de los usuarios. Los gráficos y visualizaciones resultantes permiten analizar de manera eficiente la actividad dentro de la aplicación y extraer información útil para la toma de decisiones.

## Consideraciones

A continuación, se presentan algunas consideraciones importantes sobre el proyecto.

## 1. Ajuste de tamaño en Linux

La aplicación funciona correctamente en Windows. Sin embargo, si experimentas algún problema de visualización en Linux, puedes realizar el siguiente ajuste:

- Accede a la carpeta `constante`.
- Abre el archivo `style.py` en un editor de texto.
- Busca la constante `SIZE_DEFAULT` y modifica su valor según tus necesidades.
- Guarda los cambios y reinicia la aplicación.

Este ajuste te permitirá cambiar el tamaño predeterminado de la interfaz para adaptarlo a tu sistema operativo Linux.

## 2. Creación automática de archivos CSV

Cada vez que inicies la aplicación y no se encuentren los csv correspondientes se generarán automáticamente por defecto. Estos archivos pueden contener datos relevantes para el funcionamiento de la aplicación o resultados de procesamientos anteriores.

## 3. Imágenes de prueba incluidas

El proyecto incluye carpetas con imágenes predefinidas que están destinadas a ser utilizadas para pruebas y demostraciones. Estas imágenes se encuentran en carpetas específicas dentro del proyecto y pueden ser reemplazadas o actualizadas según tus necesidades.

Si deseas utilizar tus propias imágenes, puedes reemplazar las imágenes existentes en las carpetas correspondientes o agregar nuevas imágenes siguiendo la estructura de carpetas existente.

## 4. Redimensionador de imágenes y tiempo de procesamiento

En la aplicación, se incluye un redimensionador de imágenes desarrollado por nosotros. Este redimensionador acepta cualquier ruta de archivo, siempre y cuando sea una imagen válida. Sin embargo, ten en cuenta que si la imagen es demasiado grande, el proceso de redimensionamiento puede llevar un segundo para completarse.

Es importante considerar este tiempo de procesamiento al trabajar con imágenes de gran tamaño, ya que puede afectar la velocidad de respuesta de la aplicación.

## 5. Clases importantes y manejo de datos

La aplicación utiliza dos clases fundamentales, `Settings.py` y `User.py`, que trabajan de manera estática para el funcionamiento y manejo de datos. Estas clases son responsables de diversos aspectos, incluyendo el manejo de registros en el archivo `logs.csv`.

Si necesitas personalizar o ampliar la funcionalidad relacionada con estas clases, te recomendamos revisar la documentación del proyecto para obtener información detallada sobre su implementación y uso.

> Nota: Asegúrate de seguir las instrucciones de instalación y configuración proporcionadas en la documentación del proyecto para garantizar un correcto funcionamiento y aprovechar al máximo las características de la aplicación.

## 6. Estadisticas

Estas estadisticas se accede desde el boton estadistica en la app y se guarda una foto de cada grafico en el directrio grupo12(Por problemas para guardarlas en una carpeta unica).
Para generar las estadísticas, es necesario tener instaladas las bibliotecas Pandas , Streamlit, Matplotlib y WordCloud. En caso de que no estén instaladas, se recomienda utilizar el administrador de paquetes de Python, pip, para instalarlas previamente:

```bash
    pip install pandas streamlit matplotlib WordCloud
```

Luego, se puede ejecutar el siguiente comando para abrir las estadísticas:

```bash
        streamlit run "python -m streamlit run ./src/screens/Pandas/Strlit/Inicio.py"
```

### Observacion 

El comando streamlit puede fallar ejecutandose en linux y en otra version de python que no sea 3.10 en adelante, si llegara a fallar puede ejecutarase usando el comando anteriormente mostrado desde la consola 
