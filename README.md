<h1>¿Qué hace OPCAT?</h1>

<p>OPCAT es una aplicación escrita en Python 3 útil para el descubrimiento de servicios web. Dispone de dos scripts, 'app/opcat.py' para descubrir activos y 'app/web_services.py' que habilita un servicio web en el puerto TCP 8888 para la navegación de los resultados obtenidos.</p>
<p>Para ejecutar el descubrimiento de servicios, OPCAT genera direcciones IPv4 públicas aleatorias, una vez encuentra un servicio con el puerto TCP 80 habilitado obtiene el banner del servicio, el DNS, el Whois y el nombre de dominio asociado a la dirección IPv4, también realiza una captura fotográfica de la página web de inicio. Toda esta información una vez ha sido captura es almacenada en una base de datos SQLite en el directorio 'app/db/'.</p>


<h1>Pasos a realizar</h1>

<p>Para el descubrimiento y visualización de servicios web se deberán llevar a cabo los siguientes pasos:</p>
<ol>
	<li>Ejecutar el script localizado en el directorio 'scanner/app/opcat.py' para el descubrimiento de servicios WEB. Por defecto la herramienta escanéa direcciones IP aleatorias y terminará por defecto una vez se encuentre un servicio abierto en el puerto 80. Es posible asignar un número de servicios a descubrir indicando un valor número entero con la opción "-i", además para ver las diferentes opciones se puede ejecutar el script con la opción -h.</li>

	<li>Al descubrir al menos un servicio podrá visualizar la información recolectada haciendo uso del script localizado en 'scanner/app/web_service.py', se hace uso del framework Tornado.</li>

	<li>Para acceder al servicio WEB habilitado como Front-end de la aplicación deberá acceder a la siguiente URL, http://localhost:8888</li>

	<li>Si desea modificar el puerto de escucha habilitado por Tornado para acceder al servicio web, deberá modificar la línea 'application.listen(8888)' del fichero 'scanner/app/web_service.py'</li>
</ol>
	
<h1>Disposición por directorio de proyecto</h1>
<blockquote>
	<p>+ 'opcat' es el directorio principal del proyecto.</p>
	
	<p>+ 'app' es el directorio que almacena el back-end de la aplicación, está escrito en python 3.</p>
	
	<p>+ 'html' es el directorio donde se almacena el front-end de la aplicación, se utiliza el framework Tornado.</p>
</blockquote>
