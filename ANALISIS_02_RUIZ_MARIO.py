# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 14:25:33 2020

@author: Mario Ruiz
"""
#APERTURA DEL PROGRAMA
import csv

lista_datos = []

#INDICAMOS AL PROGRAMA QUE ABRIREMOS UN ARCHIVO EN MODO LECTURA
with open ("synergy_logistics_database.csv", "r" ) as archivo_csv:
    lector = csv.reader(archivo_csv)
#PRIMER FOR QUE NOS AYUDARA A IR AGREGANDO VALORES A UNA LISTA VACIA
    for linea in lector:
        lista_datos.append(linea)
        
        
#EXPORTACIONES Y SUS RUTAS + ORDENACION DE MENOR A MAYOR
def rutas (direccion):
   #direccion = "Exports"
    contador = 0
    lista_rutas = []
    conteo_rutas =[]
    
    for ruta in lista_datos:
        if ruta [1] == direccion: 
            ruta_actual = [ruta[2], ruta [3]]
            
            if ruta_actual not in lista_rutas:
                for nuevo_movimiento in lista_datos:
                    if ruta_actual == [nuevo_movimiento[2], nuevo_movimiento[3]]:
                        contador += 1
                        
                lista_rutas.append(ruta_actual)
                formato_ideal = [ruta[2], ruta[3], contador]
                conteo_rutas.append(formato_ideal)
                contador = 0 
    conteo_rutas.sort(reverse=True, key = lambda x:x[2])
    return conteo_rutas
         
#INTRODUCCION AL PROGRAMA   
print("BIENVENIDO NUEVAMENTE\n")
print("¿QUE DESEA SABER?\n")
#SELECCION DE LO QUE SE DESEA ANALIZAR
opcion=int(input("ELIGE UNA OPCIÓN:\n 1.- Importaciones \n 2.- Exportaciones \n La opcion que deseo es:  "))
if opcion==1:
    print("\n Haz seleccionado la opcion de conocer todas aquellas rutas de importacion y su cantidad en orden de mayor a menor \n")
    lista_rutas = rutas ("Imports")
  #  print("Importación")
elif opcion == 2:
    print("\n Haz seleccionado la opcion de conocer todas aquellas rutas de exportacion y su cantidad en orden de mayor a menor \n")
    lista_rutas = rutas("Exports")
   # print("Exportación")
else:
    print("No existe esta opción")

print(lista_rutas)

#SUMA DE LOS VALORES

# lista_datos.pop(0)
# valores=[]
# for ruta in lista_datos:
#     valores.append(int(ruta[9]))
#lista_datos.sort(reverse=True, key = lambda x:x[9])

#AQUI PRESENTE ERRORES PARA PLASMAR LO SOLICITADO
#ESTE PROYECTO FUE UN VERDADERO RETO PARA MI COMO INGENIERO INDUSTRIAL, MIS CONOCIMIENTOS EN PROGRAMACION
#EN UN INICIO ERAN NULOS, AHORA QUE TERMINO, ME VOY SATISFECHO Y CONTENTO CON LO POCO O MUCHO QUE LOGRE HACER
#GRACIAS JAVIER POR TODO EL APOYO!! ESPERO EN UN FUTURO VOLVERNOS A ENCONTRAR

#SALUDOS!! - MARIO ALBERTO RUIZ CORTEZ....

#FINAL DEL PROYECTO
