#!/usr/bin/python
#!encoding: UTF-8

import pylab as dibujo 

x = [1,2,3,4]
y = [10,20,30,40]
y2= [5,15,25,35]
y3= [7,12,22,33]
y4= [12,25,33,39]

p1 = dibujo.subplot(211)    # Para poner dos funciones en el mismo grafico (el 2 muestra dos filas el 1 una columna y el otro 1 el primer dibujo.
 
dibujo.title('Titulo del dibujo 1')

##  PONER EL FOR CON EL UMBRAL 

dibujo.plot (x,y, marker= 's', linestyle= ':', color= 'g', label= 'Linea 1')           #label es el valor que sale en la leyenda
dibujo.plot (x,y2, marker= '*', linestyle= '--', color= 'r', label= ' Linea 2') 
dibujo.plot (x,y3, marker= 'p', linestyle= '-.', color= 'm', label= ' Linea 3')

                                                # TItulos del dibujo 1
dibujo.xlabel (' Texto para el eje x (dibujo 1)')
dibujo.ylabel (' Texto para el eje y ')

dibujo.legend()   #Pone la leyenda del dibujo 1



p2 = dibujo.subplot (212) # los polots que vengan a continuacion van en el dibujo 2

dibujo.plot (x,y4, marker= 'o', linestyle= '-', color= 'c', label= ' Linea 4')

dibujo.title('Titulo del dibujo 2')
                                               # Titulos del dibujo 2 
dibujo.xlabel (' Texto para el eje x')
dibujo.ylabel (' Texto para el eje y ')

dibujo.legend()   #Pone la leyenda del dibujo 2
dibujo.xlim(0,6)     # Para que la leyenda quede fuera del dibujo, 
dibujo.xticks(x)    # El enunciado de la practica te pide eso, es para que la leyenda quede sin valores de x 

dibujo.show()   # muestra el dibujo 


