
## Project Structure

```
├── manage.py # Arquivo central de Django para interagir com o projecto
├── Procfile # el archivo de configuracion de HEROKU
├── project # el paquete de python donde vive el proyecto de django
│ ├── asgi.py # es el modulo para ejecucion del ASGI (Asynchronous Server Gateway Interface)
│ ├── __init__.py # modulo de inicializacion del paquete
│ ├── settings.py # modulo donde se definen las configuraciones de DJANGO
│ ├── urls.py # modulos donde se definer los path y la relacion con las views [URL conf]
│ └── wsgi.py # modulo para la ejecucion del WSGI (Web Server Gateway Interface)
├── README.md # documentacion en markdown
├── requirements.txt # o arquivo mostra as bibliotecas que o projeto precisa para funcionar 



```
