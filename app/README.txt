Para el descubrimiento y visualización de servicios web se deberán llevar a cabo los siguientes pasos:

1-. Ejecutar el script localizado en el directorio 'scanner/app/opcat.py' para el descubrimiento de servicios WEB. Por defecto la herramienta escanea direcciones IP aleatorias y terminará cuando se encuentre un servicio abierto en el puerto 80. Para ver 		las diferentes opciones se puede ejecutar el script con la opción -h.

2-. Al descubrir al menos un servicio podrá visualizar la información recolectada haciendo uso del script localizado
en 'scanner/app/web_service.py'.

3-. Para acceder al servicio WEB habilitado como Front-end de la aplicación, deberá acceder a la siguiente URL,
http://<dirección ip>:8888

4-. Si desea modificar el puerto de escucha habilitado por Tornado para acceder al servicio web, deberá modificar la línea
109 del fichero 'scanner/app/web_service.py'

	
Disposición por directorio de proyecto:

+ 'scanner' es el directorio principal del proyecto.
	
+ 'app' es el directorio que almacena el back-end de la aplicación, está escrito en python.
	
+ 'html' es el directorio donde se almacena el front-end de la aplicación.
