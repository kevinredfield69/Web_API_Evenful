# -*- coding: utf-8 -*-

print "WEB API EVENTFUL."
print ""

import requests
import json

ciudad=raw_input("Escribir nombre de una ciudad: ")
busqueda=raw_input("Escribir termino de búsqueda: ")

with open ("key.txt","r") as archivo:
    clave = archivo.read()

payload={'app_key':clave,'keywords':busqueda,'location':ciudad}
r=requests.get("http://api.eventful.com/json/events/search?",params=payload)

print ""
print "Listado de eventos referente a la búsqueda",busqueda,"en",ciudad
print ""

if r.status_code == 200:
    eventos = r.text
    terminos = json.loads(eventos)
    for busqueda2 in terminos["events"]["event"]:
        print busqueda2["title"]