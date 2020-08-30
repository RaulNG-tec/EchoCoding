from math import *

class DataBase():
    #usuarios (owner/user)
    #funcion para añadir usuario
    #funcion para checar usuario

class Owner(): 
    # restaurante, largo y ancho del local, establecer espacio {maxima ocupacion, distancia, porcentaje}
    def __init__(self,name,leng,wdt,tbl,perc,dis,officehrs):
        self.__name     =   name
        self.__leng     =   leng
        self.__wdt      =   wdt
        self.__tbl      =   tbl
        self.__perc     =   perc
        self.__dis      =   dis
        self.__officehrs =  officehrs

        schedule={}
        spacejam=[]
        for i in range (leng*2):
            line=[]
            for j in range(wdt*2):
                line.append(0)
            spacejam.append(line)
        for x in range()
        self.__stablishment=spacejam
    
    @safe_distance.setter
    def distance_setter(self, val):
        self.__dis = val
    
    @occupancy_percent.setter
    def occupancy_percent(self, val):
        self.__perc = val
    
    @property
    def lenght(self):
        return self.__leng
    
    @property
    def width(self):
        return self.__wdt
    
    @property
    def maximum_tables(self):
        return self.__tbl
    
    # funcion para cambiar ocupacion 
    @property
    def maximum_occupancy(self):
        return self.__perc
    
    # funcion para cambiar distancia 
    @property
    def safe_distance(self):
        return self.__dis
    
    @property
    def stablishment(self):
        return self.__stablishment

    def printTables(leng, wdt):
        

class User():

    def __init__(self,name,phone):
        self.__name=name
        self.__phone=phone
    
    @name.setter
    def name(self, tag):
        self.__name = tag

    @property
    def name(self):
        return self.__name

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def phone(self):
        return self.__phone
    
    def do_reservation(self, persons):
        

    def cancel_reservation(self):
        self.__reservation=NULL
    
    # funcion para reservar asiento
    def make_reservation(self, persons):
        self.__reservation=
    # funcion para liberar asiento 
    def delete_reservation(self):
        
    
    # funcion para ver lugar
    def display_stablishment(self):

def space_maker(space,mx_ocup,distance,percent, length, width):
    
    tables =  math.floor((mx_ocup*percent)/100))
    area= length * width
    
    if math.ciel(area/tables)<distance :
        #mensaje de error
    else :
        ocupied_p=(math.ciel(area/tables)*100)/area)
        array_approx = (length*2)*(width*2)
        squares= math.ciel(array_approx/(occupied_p/100)) 




    return spacejam


