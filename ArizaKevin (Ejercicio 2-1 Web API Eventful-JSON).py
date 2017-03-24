# -*- coding: utf-8 -*-

print "WEB API EVENTFUL."
print ""

import requests
import json

#Escribir el nombre de una ciudad o localidad, junto con el parámetro de busqueda a realizar.

ciudad = raw_input("Escribir nombre de una ciudad/localidad: ")
busqueda = raw_input("Escribir término de búsqueda: ")

#Escribir rango de búsqueda que quieres consultar.

print ""

print "RANGO DE BÚSQUEDA"
print ""
print "Opción 1: Past"
print "Opción 2: Today"
print "Opción 3: Future"
print "Opción 4: This Week"
print "Opción 5: Next Week"

print ""

rango = raw_input("Escribir rango de búsqueda: ")

#Escribir el tipo de la búsqueda a realizar.

print ""

print "TIPO DE BÚSQUEDA"
print ""
print "Opción 1: Relevance"
print "Opción 2: Date"
print "Opción 3: Popularity"

print ""

tipo = raw_input("Escribir orden de búsqueda (Relevance, Date, Popularity): ")

#Escribir el orden del resultado de la búsqueda.

print ""

print "ORDEN DE BÚSQUEDA"
print ""
print "Opción 1: Ascending"
print "Opción 2: Descending"

print ""

orden = raw_input("Escribir tipo de búsqueda (Ascending, Descending): ")

#Escribir el número de página que queremos consultar en la búsqueda.

print ""

pagina = raw_input("Escribir número de página a consultar: ")

with open ("key.txt","r") as archivo:
    clave = archivo.read()

#Generación de URL, para la realización de la consulta de recogida de datos, hacia la API de Eventful.

payload = {"app_key":clave,"keywords":busqueda,"location":ciudad,"t":rango,"sort_order":tipo,"sort_direction":orden,"page_number":pagina}
r = requests.get("http://api.eventful.com/json/events/search?",params=payload)

#Generación de resultados, cons los parámetros de búsqueda escritos.

if r.status_code == 200:
    try:
        print ""
        print "Listado de eventos referente a la busqueda realizada."
        print ""
        eventos = r.text
        terminos = json.loads(eventos)
        for busqueda2 in terminos["events"]["event"]:
            print "Nombre Del Evento:",busqueda2["title"]
            print "Celebración Del Evento:",busqueda2["venue_address"]
            print "Fecha y Horario Del Evento:",busqueda2["start_time"]
            print ""
    except TypeError:
        print "No se han encontrado resultados con los parámetros de búsqueda introducidos."

