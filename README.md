# Proyecto Final - PaisaWeather

Este proyecto implementa dos servicios web utilizando Flask y Docker, uno para obtener datos meteorológicos de OpenWeatherMap y otro visualizar los datos a través de una interfaz web.

## Como Funciona?

### Estructura del Proyecto:
El proyecto consta de dos servicios principales: weather y web.
weather obtiene datos meteorológicos de OpenWeatherMap y expone estos datos a través de una API en el puerto 5000.
web proporciona una interfaz web en el puerto 8080 para visualizar los datos meteorológicos.
### weather (Servicio de Datos Meteorológicos):
Dockerfile: Usa una imagen de Python 3.10, instala las dependencias desde requirements.txt y ejecuta weather_service.py.
Puerto: Expone el puerto 5000 para que otros servicios puedan acceder a la API de datos meteorológicos.
API Key: Utiliza la variable de entorno API_KEY para autenticarse con la API de OpenWeatherMap.
Funcionamiento: Proporciona un endpoint /weather que devuelve datos meteorológicos en formato JSON para la ubicación especificada (en este caso, "Medellin").
### web (Servicio Web y Mapa):
Dockerfile: Usa una imagen de Python 3.10, instala las dependencias desde requirements.txt y copia los archivos estáticos y las plantillas HTML. Ejecuta web_service.py.
Puerto: Expone el puerto 8080 para la interfaz web.
Dependencias: Utiliza Flask para la aplicación web.
Funcionamiento:
'/': Renderiza la plantilla HTML principal (index.html) para la interfaz web.
'/weather': Realiza una solicitud al servicio weather para obtener datos meteorológicos y los devuelve en formato JSON.
### Docker Compose:
Se utiliza docker-compose.yml para definir la configuración de los servicios, las redes y las variables de entorno.
Los servicios están en la misma red (paisaweather), lo que les permite comunicarse entre sí utilizando los alias de red (weather y web).


## Despliegue

### Requisitos Previos
Necesario tener instalado:
- Docker: [Instrucciones de instalación](https://docs.docker.com/get-docker/)
- Docker Compose: [Instrucciones de instalación](https://docs.docker.com/compose/install/)
- API Key de OpenWeatherMap: Obtén una clave de API de OpenWeatherMap siguiendo sus [instrucciones](https://openweathermap.org/api).
- Habilitar los puertos 5000 y 8080 en el firewall de tu sistema operativo.


### Pasos de Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/caro2003/paisaweather.git
   cd paisaweather
    ```
2. En el archivo .env en la raíz del proyecto y define tu API Key de OpenWeatherMap:
   
    ```plaintext
    COMPOSE_PROJECT_NAME=paisaweather
    API_KEY=<tu-api-key>
    ```
3. Levanta los servicios utilizando Docker Compose (necesitarás permisos de administrador):

    ```bash
    docker-compose up -d --build
    ```
4. Accede a la interfaz web en http://localhost:8080