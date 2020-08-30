from math import *

class DataBase():
    #usuarios (owner/user)
    #funcion para añadir usuario
    #funcion para checar usuario


class Reservation():
    #numero de personas, mesa asignada, hora {dure una hora}, numero de reserva
    
    #funcion para imprimir el espacio disponible
    #funcion para escoger asiento {hora} [maximo 4 personas]
    #funcion para liberar asiento
    

class Owner():
    # restaurante, largo y ancho del local, trablecer espacio {maxima ocupacion, distancia, porcentaje}
    def __init__(self,name,leng,wdt,tbl,perc,dis):
        self.__name =   name
        self.__leng =   leng
        self.__wdt  =   wdt
        self.__tbl  =   tbl
        self.__perc =   perc
        self.__dis  =   dis

        spacejam=[]
        for i in range (length*2):
            line=[]
            for j in range(width*2):
                line.append(0)
            spacejam.append(line)
        
        self.__stablishment=spacejam
    
    @dis.setter
    def distance_setter(self, val):
        self.__dis = val
    
    @perc.setter
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
    
    def make_reservation(persons):
        
    # funcion para reservar asiento
    # funcion para liberar asiento 
    # funcion para ver lugar


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
    #funcion para reservar
    #funcion para consultar reserva
    #funcion para cancelar reserva 





class Stablishment():
    # CAD en .SLD o .PRT 



def space_maker(space,mx_ocup,distance,percent):
    
    tables =  math.floor((mx_ocup*percent)/100))
    area= length * width
    
    if math.ciel(area/tables)<distance :
        #mensaje de error
    else :
        ocupi(math.ciel(area/tables)*100)/area)
    


    return spacejam

class Punto2D:
    def __str__(self):
        return f'Punto: x={self.x}, y={self.y} '

    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value

    def distancia_euclidiana(self,punto2):
        return((self.x-punto2.x)**2+(self.y-punto2.y)**2)**0.5

    def punto_medio(self,punto2):
        return Punto2D((self.x+punto2.x)/2,(self.y+punto2.y)/2)
    
    def __add__(self, p):
        return Punto2D(self.x + p.x, self.y + p.y)
