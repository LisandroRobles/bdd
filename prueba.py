#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlobject import *
import csv

# declaro la conexion asi -> "mysql://user:password@host/database"
__connection__ = connectionForURI("mysql://guest:guest@localhost/ormtest")
__connection__.query("SET default_storage_engine = MyISAM")
# __connection__.debug = True


class Estacionamiento(SQLObject):
    nombre = StringCol(length=120, varchar=True)
    calle = StringCol(length = 120, varchar=True)
    altura = StringCol(length = 120, varchar =True)
    horario = StringCol(length = 120, varchar=True)

class Piso(SQLObject):
    numero = StringCol(length = 120, varchar = True)
    estacionamiento = ForeignKey('Estacionamiento',default = None)

if __name__ == '__main__':
    # borro la tabla si ya existia
    Estacionamiento.dropTable(ifExists=True)
    Piso.dropTable(ifExists = True)

    # creo la tabla
    Estacionamiento.createTable()
    Piso.createTable()

    #Leo el archivo estacionamientos.csv
    data = csv.DictReader(open('estacionamientos.csv'), delimiter=',', quotechar='"')

    #Para cada fila del archivo leido
    for row1 in data:
       Estacionamiento(nombre = row1["nombre"],calle = row1["calle"],altura = row1["altura"],horario = row1["horario"]) 

    #Leo pisos.csv
    data = csv.DictReader(open('pisos.csv'),delimiter = ',',quotechar='"')

    #Para cada fila del archivo leido
    for row2 in data:
        Piso(numero = row2["numero"],estacionamiento = Estacionamiento.selectBy(nombre = row2["estacionamiento"]).getOne())










