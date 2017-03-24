# -*- coding: utf-8 -*-

print "WEB API EVENTFUL."
print ""

import requests
from lxml import etree

ciudad=raw_input("Escribir nombre de una ciudad: ")
busqueda=raw_input("Escribir termino de búsqueda: ")

with open ("key.txt","r") as archivo:
    clave = archivo.read()

payload={'app_key':clave,'keywords':busqueda,'location':ciudad}
r=requests.get("http://api.eventful.com/rest/events/search?",params=payload)

print ""
print "Listado de eventos referente a la búsqueda",busqueda,"en",ciudad
print ""

if r.status_code == 200:
    doc = etree.fromstring (r.text.encode('utf-8'))
    terminos_de_busqueda = doc.findall("events/event/title")
    for busqueda2 in terminos_de_busqueda:
        print busqueda2.text
