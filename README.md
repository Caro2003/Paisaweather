# Proyecto de Servicios Web y Servicio Meteorológico

Este proyecto implementa dos servicios web utilizando Flask y Docker, uno para obtener datos meteorológicos de OpenWeatherMap y otro visualizar los datos a través de una interfaz web.


## Despliegue

### Requisitos Previos
- Docker: [Instrucciones de instalación](https://docs.docker.com/get-docker/)
- Docker Compose: [Instrucciones de instalación](https://docs.docker.com/compose/install/)
- Python 3.10: [Instrucciones de instalación](https://www.python.org/downloads/release/python-3100/)
- API Key de OpenWeatherMap: Obtén una clave de API de OpenWeatherMap siguiendo sus [instrucciones](https://openweathermap.org/api).

### Dependencias
- blinker==1.7.0
- certifi==2023.7.22
- charset-normalizer==3.3.2
- click==8.1.7
- Flask==3.0.0
- waitress==2.0.0
- idna==3.4
- itsdangerous==2.1.2
- Jinja2==3.1.2
- jsonify==0.5
- MarkupSafe==2.1.3
- python-dotenv==1.0.0
- requests==2.31.0
- urllib3==2.0.7
- Werkzeug==3.0.1

### Pasos de Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/tu-proyecto.git
   cd tu-proyecto
    ```
2. Crea un archivo .env en la raíz del proyecto y define tu API Key de OpenWeatherMap:
   
    ```plaintext
    COMPOSE_PROJECT_NAME=paisaweather
    API_KEY=<tu-api-key>
    ```
3. Levanta los servicios utilizando Docker Compose (necesitarás permisos de administrador):

    ```bash
    docker-compose up -d --build
    ```
4. Accede a la interfaz web en http://localhost:5000