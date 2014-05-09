#! /usr/bin/python
#!encoding: UTF-8

import pylab as pract13
import timeit
import time
import modulo
l=[]

def error(nro_intervalos,nro_test,umbral):
  fallos=0
  for i in range (nro_test):
    s=modulo.error(nro_intervalos)
    error=abs(s-modulo.pi)
    if error>=umbral:
      fallos=fallos+1
  return ((fallos/nro_test)*100)
  
print "Introduzca numero de intervalos:"
n = int(raw_input());
print "Introduzca el numero de aproximaciones:"
aproximaciones = int(raw_input());
print "Introduzca 5 umbrales de error:"
umbral =[]
for i in range(5):
   print "Introduzca el umbral", i, ":"
   umbral.append(float(raw_input()));
print"Introduzca el nombre fichero resultados"
nombre_fichero = raw_input();

if (n>0):
  try:
    fichero = open (nombre_fichero, "a")
  except:
    fichero = open (nombre_fichero, "w")
  fichero.write("num de intervalos: %d\n"%(aproximaciones))
  for i in range (5):
    start = time.time()
    error(n, aproximaciones, umbral[i])
    finish=time.time() - start
    print "El tiempo que tarda en realizarse es: %14.13f" %finish
    l=l+[finish]
    f.write('El tiempo es:')
    f.write(str(l[0]) + '\n')
  f.close()
else:
  print "El valor de los intervalos debe ser mayor que 0"  
prct13.subplot(2,1,1)

prct13.plot (x,y1, marker= 'o', linestyle= '_', color= 'r', label= '10')           #label es el valor que sale en la leyen
prct13.plot (x,y2, marker= '*', linestyle= '_', color= 'b', label= '50') 
prct13.plot (x,y3, marker= 's', linestyle= '-.', color= 'g', label= '100')
prct13.plot (x,y4, marker= '+', linestyle= '-.', color= 'g', label= '500')
prct13.plot (x,y5, marker= 'p', linestyle= '-.', color= 'm', label= '1000')

# TItulos del dibujo 1
prct13.xlabel (' Texto para el eje x (dibujo 1)')
prct13.ylabel (' Texto para el eje y ')

prct13.legend()   #Pone la leyenda del dibujo 1
prct13.xlim(0,6)
prct13.xticks(x)


prct13.show()




