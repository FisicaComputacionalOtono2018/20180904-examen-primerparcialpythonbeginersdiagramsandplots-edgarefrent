#EdgarEfren Tomay Tiburcio
#4 de septiembre de 2018
#Grafica de la funcion f(x)=-x²+3x y su punto de inflexion

from matplotlib import pyplot
#Funcion
def f1(x):
  return -(x**2)+3*x

#valores del eje x que toma la grafica
x= range(-3, 6)

#graficar funcion
pyplot.plot(x, [f1(i)for i in x])

#establecer el color de los ejes
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

#limitamos los valores from matplotlib import pyplot

#Funcion
def f1(x):
  return -(x**2)+3*x

#valores del eje x que toma la grafica
x= range(-3, 6)

#graficar funcion
pyplot.plot(x, [f1(i)for i in x])

#la funcion cambia de pendiente en el punto  verde (1.5, 2.25)
pyplot.plot((1.5), (2.25),'go',)

#establecer el color de los ejes
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

#limitamos los valores de los ejes
pyplot.xlim(-10, 10)
pyplot.ylim(-10, 10)

#guardamos grafica como imagen png
pyplot.savefig("ejercicio2.png")

#mostrar grafica
pyplot.show
