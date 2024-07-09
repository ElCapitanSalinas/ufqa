# UFQA - Una Familia Que Ayuda Crowdfunding plattform

###### Bienvenido lector, en este documento explicaremos la anatomía de la página web de UFQA\


## Version

La versión actual es v1.0


## Sistema utilizado

Para el desarrollo de la página web se utilizó Django, el deploy se realizó utilizando gunicorn para django y nginx para entregar los archivos estáticos.

## Estructura

Todas las funciones de la página se manejan desde el archivo views.py, dentro de la carpeta ufqaweb.

- Cada función está asignada desde el archivo urls.py, dentro de la misma carpeta.
- Los archivos estáticos (JavaScript, Imagenes y CSS) están dentro de la carpeta static, en ufqaweb.
- Los archivos HTML están en la carpeta templates.

## Dependencias

  We used this libraries:
  
  - Django (Web framework)
  - Pillow (Image management)
  - Gunicorn (Deploy Framework)
  - Unidecode (Re-naming the images and avoiding special characters)
  - Numpy (Numeric calculations software)

## How to install

  - Verifique todas las **Dependencias**
  - Realiza las migraciones del proyecto, con el siguiente comando:
  
    ```
    py manage.py makemigrations
    ```
  - Una vez hechas las migraciones puedes comenzar el servidor de desarrollo:
  
    ```
    py manage.py runserver
    ```
  - En caso de requerir acceso remoto puedes usar el siguiente comando: (For this example the port 8000 TCP must be opened in your firewall and router)
    
      ```
      py manage.py runserver 0.0.0.0:8000
      ```

## How to deploy

  Para reiniciar el servidor tienes que usar el siguiente comando, recuerda que tienes que estar en el entorno

  - Comando del entorno:
    ```
    cd /home/
    source /ufqa-lib/bin/activate
    ```
  - Tienes que parar el entorno de gunicorn

    ```
    pkill gunicorn
    ```
  
  - Tienes que ingresar a la carpeta ufqa
    ```
    cd ufqa/
    ```
  - Tienes que iniciar de nuevo el entorno con:

    ``gunicorn -c conf/gunicorn_config.py ufqa.wsgi service``


  Listo!!
  


  - Done! The project is remotely joinable from the url 127.0.0.1:8000 if its local. For remote you must check the [Django documentation](https://docs.djangoproject.com/en/4.0/)
