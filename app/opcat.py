#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    #############################
    #                           #
    #   Autor: Equipo Enigma    #
    #                           #
    #############################

"""

try:
    from selenium import webdriver
except Exception as e:
    print("pip install selenium")
    exit(1)

try:
    from ipwhois import IPWhois
except Exception as e:
    print("pip install ipwhois")
    exit(1)

from sys import exit
from ipaddress import IPv4Address
from optparse import OptionParser
from sqlite3 import connect
from socket import socket, AF_INET, SOCK_STREAM, setdefaulttimeout,getfqdn
from random import randint
from dns import resolver, reversename
from os import path

def print_header():
    print("\n\t    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+ MMMMMMMMMMMMMMMMMMMMMMMMM. MMMMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM...MMMMMMMMMMMMMMMMMMMMMMM ...MMMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM ....MMMMMMMMMMMMMMMMMMMMM ....7MMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN .... MMMMMM7.    :DMMMMM.......MMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.......  ................ .......,MMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM..................................MMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:..................................MMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM ...................................MMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM................................... MMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.....  MMMM ............MMMMD ..... MMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM....,MMMMMMMM ........$MMMMMMMM.... MMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM ....MMMMMMMMM .......MMMMMMMM.....MMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.....MMMMMMMM ......NMMMMMMM......MMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM= .... DMN+ .......... NMN.......MMMMM\n\
            MMMMMMMMMMMMMMMMN=..... .7MMMMMMMMMMMMMMMMM...............................MMMMMM\n\
            MMMMMMMMMMMMD.................:MMMMMMMMMMMMM:........................... MMMMMMM\n\
            MMMMMMMMMM ...................... DMMMMMMMMMMM ........................MMMMMMMMM\n\
            MMMMMMMN.............................NMMMMMMMMMM~ ................. ,MMMMMMMMMMM\n\
            MMMMMMO.   ,$$:   .............  . ....MMMMMMMMMMMMM...  ....   .MMMMMMMMMMMMMMM\n\
            MMMMM,.$NNNNNNNNNNO .... NNNNNNNNNNNN....OM?....MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
            MMMM?$NNNN:   .,NNNN8... NNN  ....NNNNN ............:MMMMMMMMMM8,....MMMMMMMMMMM\n\
            MMMMNNNN NNNNNNNN NNNN.. NNN.NNNNNN.ONNN............................. MMMMMMMMMM\n\
            MMMDNN8=NNNN~:DNNNIINN8. NNN.NN..DNN.DNN............................. MMMMMMMMMM\n\
            MMMNND,NNN .....ONN~NNN  NNN.NN . NNN?NN,.............................MMMMMMMMMM\n\
            MMMNN+NND....... NNN=NN. NNN.NN..ZNN:NNN..............................MMMMMMMMMM\n\
            MMMNN=NNN........NNN:NN. NNN.NNNNNNI~NNN..............................MMMMMMMMMM\n\
            MMMNNN.NND......7NN?NNN. NNN     .DNNNN ........,.....................MMMMMMMMMM\n\
            MMMNNN+DNNN=..~NNNM NNM. NNN.NNNNNNND ......$NN$IDNN.. NIN ..NZ7777N..MMMMMMMMMM\n\
            MMM.NNND.NNNNNNNM NNNN . NNN.NN   . .......NM?NNNNN...NONDN....NNN=.  MMMMMMMMMM\n\
            MMMM.DNNND..  ..NNNNN .. NNN.NN ...........N.N.......,NONZN ...NNN=...MMMMMMMMMM\n\
            MMMM~. NNNNNNNNNNNN .... NNNNNN............N+N ......N.N.N:N...NNN=...MMMMMMMMMM\n\
            MMMMM ... ~NNNN=.........       ...........DN NNNNN ONNNNNNN7..NNN=..MMMMMMMMMMM\n\
            MMMMMM .....................................,NNNNNNNNMNNNNNNN .NNN=. MMMMMMMMMMM\n\
            MMMMMMM ......                                  .                   ,MMMMMMMMMMM\n\
            MMMMMMMM.......MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
            MMMMMMMMM.......DMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
            MMMMMMMMMM+........MMMMMMMMMMMMMMMMMMMN?  ...........ZMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
            MMMMMMMMMMMM ......... . :=,..............................MMMMMMMMMMMMMMMMMMMMMM\n\
            MMMMMMMMMMMMMM. ............................................ MMMMMMMMMMMMMMMMMMM\n\
            MMMMMMMMMMMMMMMMD....................  . ,+ONMMMMZ=............,MMMMMMMMMMMMMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMI....  .. $MMMMMMMMMMMMMMMMMMMMMMMM ........7MMMMMMMMMMMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM........MMMMMMMMMMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.......MMMMMMMMMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM ... MMMMMMMMMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMENIGMAMMMMMMMM\n\
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n")


"""
Formatear whois

@whois -> String, Imprimimos data
@return -> result, Whois formateado

"""
def whoisFormatter(whois):
    result=''
    for x in whois:
        if(x is not 'nets'):
            result+='{0}: {1}<br/>'.format(x,whois[x])
        else:
            result+='{0}:<br/>'.format(x)
            for y in whois[x][0]:
                result += '&nbsp;&nbsp;&nbsp;&nbsp;{0}: {1}<br/>'.format(y,str(whois[x][0][y]).replace('<br/>',''))
    return result


"""
Crea conexión a base de datos

@return -> Connection mysql
"""
def sqlite_open_connection():
       
    try:
        db_path = path.join(path.dirname(__file__), "db/opcat.db")
        db_path = path.join(db_path) 
        connection = connect(db_path)
    except Exception as e:
        print(e)
        print("It has been an error establishing the connection with the database.")
        return None

    return connection


"""
Elimina tablas de la base de datos
@cursor -> Cursor de la conexión a base de datos

@return -> Connection mysql
"""
def sqlite_delete_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS ip")
    cursor.execute("DROP TABLE IF EXISTS banner")
    cursor.execute("DROP TABLE IF EXISTS dns")
    cursor.execute("DROP TABLE IF EXISTS whois")
    cursor.execute("DROP TABLE IF EXISTS domainName")


"""
Crea las tablas en la base de datos
"""
def sqlite_create_table():

    connection = sqlite_open_connection()
    if( connection != None ):
        try:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS ip(iid INTEGER, ip VARCHAR(15), PRIMARY KEY (iid) )")
            cursor.execute("CREATE TABLE IF NOT EXISTS banner(bid INTEGER, iid INTEGER, port INTEGER(5), data VARCHAR(10000), screenshot LONGBLOB, PRIMARY KEY (bid), FOREIGN KEY (iid) REFERENCES ip(iid))")
            cursor.execute("CREATE TABLE IF NOT EXISTS dns(did INTEGER, iid INTEGER, data VARCHAR(10000), PRIMARY KEY (did), FOREIGN KEY (iid) REFERENCES ip(iid))")
            cursor.execute("CREATE TABLE IF NOT EXISTS whois(wid INTEGER, iid INTEGER, data VARCHAR(10000), PRIMARY KEY (wid), FOREIGN KEY (iid) REFERENCES ip(iid))")
            cursor.execute("CREATE TABLE IF NOT EXISTS domainName(dmid INTEGER, iid INTEGER, data VARCHAR(10000),PRIMARY KEY (dmid),FOREIGN KEY (iid) REFERENCES ip(iid))")
        except Exception as e:
            print(e)
            print("[Error] It has been an error creating the tables.")
        finally:
            cursor.close()
            connection.close()

"""
Inserta información de protocolos en base de datos

@ip     -> String, dirección IPv4
@port   -> Int, puerto TCP
@banner -> String, Banner del servicio
@dns    -> String, Información DNS
@whois  -> String, Información whois
@domainName -> String, Nombre de dominio
@screenshot -> Bytes, Imagen

@return -> Boolean, Estado de la inserción
"""
def sqlite_insert_data( ip, port, banner, dns, whois, domainName, screenshot ):
    # Obtenemos la conexión a BBDD
    connection = sqlite_open_connection()
    
    if connection != None:
        try:
            with connection:
                cursor = connection.cursor()
                
                sql = "INSERT INTO ip(ip) VALUES (?)"
                cursor.execute( sql, ( str(ip), ) )
                iid = cursor.lastrowid

                sql = "INSERT INTO banner(iid, port, data, screenshot) VALUES (?, ?, ?, ?)"
                cursor.execute( sql, ( int(iid), int(port), str(banner), screenshot, ) )

                sql = "INSERT INTO dns(iid, data) VALUES (?, ?)"
                cursor.execute( sql, (int(iid), str(dns),) )

                sql = "INSERT INTO whois(iid, data) VALUES (?, ?)"
                cursor.execute( sql, (int(iid), str(whois),) )

                sql = "INSERT INTO domainName(iid, data) VALUES (?, ?)"
                cursor.execute( sql, (int(iid),str(domainName), ) )
                
            # Realizamos commit para guardar los cambios    
            connection.commit()
        except Exception as e:
            print(e)
            print("It has been an error during the insertion.")
        finally:
            # Cerramos conexion
            cursor.close()
            connection.close()


"""
Registramos en base de datos

@host -> IPv4Address, Dirección IPv4
@port -> Port, Número de puerto
@data -> Data, 
"""
def generateInformationDB(host, port, banner, screenshot):
    
    #Obtenemos el Nombre de Dominio y realizamos un Whois para obtener más información
    domainName = getfqdn(host) 
    whois      = whoisFormatter( IPWhois(host).lookup() )
    aux        = domainName.split('.')
    dnsQuery   = '{0}.{1}'.format(aux[-2],aux[-1])

    addr = reversename.from_address(host)
    dns = "<h5>Nombre reverso</h5>"
    dns += str(addr) + "<br/>"  

    try:

        ptrText = "<br/><h5>PTR</h5>"
        for ptr in resolver.query( addr, "PTR" ):
            ptrText += str(ptr)+"</br/>"

        dns += ptrText

    except Exception as e:
        pass

    try:

        nsText = "<br/><h5>Servidores de nombre</h5>"
        for server in resolver.query(dnsQuery, 'NS'):
            nsText += str(server).rstrip('.')+'<br/>'

        dns += nsText

    except Exception as e:
        pass

    
    sqlite_insert_data( host, port, banner, dns, whois, domainName, screenshot )

    return True


"""

"""
def takeScreenshot(host, port):

    # Realizamos una captura del servicio web
    setdefaulttimeout(200)        

    try:
        browser = webdriver.Firefox(timeout=200)
        browser.implicitly_wait(200) # Segundos
        browser.set_page_load_timeout(200)
        browser.get('http://{0}'.format(host))
        screenshot = browser.get_screenshot_as_png()
        state = True
        browser.quit()
    
    except selenium.common.exception.WebDriverException as e:
        print("ERROR: Do you have Firefox installed?")
        exit(1)

    except Exception as e:
        state = False
        print("[Error] takeScreenShot: {0}".format(e))
        browser.quit()
  

    if state:
        return screenshot
    else:
        return None


"""
Determinamos si la dirección IP generada aleatoriamente es una página web        
@host -> String, Dirección IPv4. 
@port -> Int, Número de puerto.

@return -> Boolean, estado de la operación.
"""
def isOpenPort( host, port, timeout ):
    
    setdefaulttimeout(timeout)
    template = "{0:16}{1:3}{2:40}"
    #Intentamos establecer una conexión a un puerto, en caso positivo realizamos las funciones pertinentes
    try:
        # Definimos conexión
        #   AF_INET: Representa conjunto (host, port)
        #   SOCK_STREAM: Establece protocolo de la conexión TCP
        connection = socket(AF_INET, SOCK_STREAM)
        # Establecemos par de dirección IP y puerto
        connection.connect((host, port))
        # Obtenemos el banner y lo parseamos
        connection.send(b'HEAD / HTTP/1.0\r\n\r\n')
        banner = connection.recv(1024)
        # Imprimimos mensaje Puerto abierto junto a la dirección IPv4
        print(template.format(host, '->', 'Open Port'))
        # Adaptamos salto de línea a HTML
        aux = str(banner).replace('\\r\\n','<br/>')
        # Obtenemos banner eliminando carácteres especiales del principio
        # y del final
        banner = aux[2:len(aux)-3]
        # Cerramos la conexión
        connection.close()
        
        #Intenamos realizar la captura de la página web, 
        #si se realiza con éxito generamos el fichero de información.
        screenshot = takeScreenshot(host, str(port))


        if generateInformationDB( host, port, banner, screenshot ) :
            return True

    except Exception as e:
        print(template.format(host, '->', 'Closed Port: ('+str(e)+')'))
        connection.close()
        return False


"""
Generamos una dirección IP aleatoria.

@return -> IPv4Address, Dirección ipv4 válida.
"""
def ipFactory():
    ip = IPv4Address('{0}.{1}.{2}.{3}'.format(randint(0,255),randint(0,255),randint(0,255),randint(0,255)))

    if(ip.is_multicast or ip.is_private or ip.is_unspecified or ip.is_reserved or ip.is_loopback or ip.is_link_local):
        return ipFactory()

    return ip


"""
Función principal, 

Establece a partir de dos parametros de entarada el número de puerto
y el número de iteraciones. Obtiene una dirección IPv4 válida y comprueba
si el puerto está abierto.

@Port -> Número de puerto
@Iterations-> Número de iteraciones

"""
if __name__ == "__main__":
    try:
        sqlite_create_table()
        # Imprimimos sintaxis para inserción de valores
        parser = OptionParser("Usage: %prog [-i] <iterations [default:1]> [-a] <IP address [default:random]> [-t] <timeout [default:2]>")
        parser.add_option("-t", dest="timeout", default="2", type="float", help="Specify the timeout (seconds).")
        parser.add_option("-a", dest="ip", default="0.0.0.0", type="string", help="Specify the IP for scan.")
        parser.add_option("-i", dest="iterations", default="1", type="string", help="Specify the number of iterations.")
        (options, args) = parser.parse_args()
        # Asignamos parámaetros de entrada
        numberOfIteration = int(options.iterations)
        ip = str(options.ip)
        timeout = options.timeout
        port = 80

        # Imprimir imagen de header
        print_header()

        # Imprimimos mensaje de escaneo activo
        print( 'Scanning...' )

        if(ip == "0.0.0.0"):
            # Contador para comprobar el número de iteración actual
            count = 0
            # Realizamos búsqueda de 'N' servidores con número de puerto abierto
            while(count < numberOfIteration):
                # Comprobamos si el puerto está abierto
                if( isOpenPort( str( ipFactory() ), port, timeout ) ):
                    count += 1
        else:
            if(numberOfIteration != '1'):
                print('\n[+] The following IP address will be scanned: {0}, the -i parameter will not be used.\n'.format(ip))
            isOpenPort( ip, port, timeout )
        
    except KeyboardInterrupt as e:
        print("[+] Bye!")

