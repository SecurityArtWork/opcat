#!/usr/bin/env python


from sys import exit
try:
    from tornado.escape import json_encode
    from tornado.ioloop import IOLoop
    from tornado.web import RequestHandler, Application
except Exception as e:
    print("pip install tornado")
    exit(1)
from sqlite3 import connect
#import json
from os import path
from base64 import b64encode
from re import search

"""
Retorna los resultados obtenidos tras ejecutar una consulta en 
base de datos.
"""
def _execute(query):
    # Definimos variables
    result = None

    try:
        # Establecemos ruta hacia el fichero de base datos
        db_path = path.join(path.dirname(__file__), "db/opcat.db")
        # Establecemos conexión con el fichero de base de datos
        connection = connect(db_path)
        # Instanciamos el cursor
        cursorobj = connection.cursor()
        # Ejecutamos la sentencia SQL
        cursorobj.execute(query)
        # Obtenemos los resultados de la base de datos
        result = cursorobj.fetchall()
        # Aplicamos los cambios oportunos
        connection.commit()
    except Exception:
        print("Error al conectar con la base de datos.")
    finally:
        # Cerramos la conexión a la base de datos
        connection.close()

    return result

"""
Renderiza el listado de activos en la plantilla oportuna.
"""
class MainHandler(RequestHandler):
    def get(self):
        # Componemos sentencia SQL
        query = 'SELECT iid, ip FROM ip'
        # Ejecutamos la sentencia SQL
        rows = _execute(query)
        
        # Si la ejecución fue satisfactoria se renderizan los resultados
        # en la plantilla 
        if rows:
            self.render("../html/index.html", listOfAssets=rows)
        else:
            self.render("../html/notResult.html")

"""
Retorna en formato JSON información referente a un activo seleccionado.
"""
class SelectAsset(RequestHandler):
    def post(self):
        # Capturamos parámetro de identificador
        parameter = self.get_argument("parameter", strip=True).split("_")
        
        # Buscamos la subcadena referente al número
        iid = search("[0-9]+", parameter[1]).group(0)

        # Componemos la sentencia SQL
        sql = 'SELECT ip, port, banner.data as banner, banner.screenshot as screenshot, dns.data as dns,' \
              'whois.data as whois, domainName.data as domainName ' \
              'FROM ip, banner, dns, whois, domainName ' \
              'WHERE ip.iid=' + iid + ' AND ip.iid = banner.iid AND ip.iid = dns.iid AND ip.iid = whois.iid AND ip.iid = domainName.iid'
        # Ejecutamos la sentencia SQL
        rows = _execute(sql)

        # Procedemos si se han obtenido resultados
        if rows:
            # Definimos diccionario
            data = {}
            # Iteramos sobre los resultados devueltos
            for row in rows:
                # Componemos diccionario con los resultados obtenidos
                data["ip"]         = row[0]
                data["port"]       = row[1]
                data["banner"]     = row[2]
                data["screenshot"] = str(b64encode(row[3]))
                data["dns"]        = row[4]
                data["whois"]      = row[5]
                data["domainName"] = row[6]
                # Escribimos la respuesta, tendrá formato JSON
                self.write(data)

# Establecemos ruta que apunten a los ficheros estáticos
settings = {
    "static_path": path.join(path.dirname(__file__), "../html/static"),
}

# Establecemos manejador de las peticiones que vienen de la aplicación web
application = Application([
        (r'/', MainHandler),
        (r'/asset', SelectAsset),
    ], **settings)

"""
Código de ejecución principal de la aplicación
"""
if __name__ == "__main__":
    # Establecemos puerto de escucha
    application.listen(8888)
    IOLoop.instance().start()


