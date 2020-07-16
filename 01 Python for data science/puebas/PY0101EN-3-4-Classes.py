

import matplotlib.pyplot as plt

class circulo(object):
    """docstring for circulo"""

    # constructor
    def __init__(self, radio, color):
        self.radio = radio
        self.color = color

    # metodo para aumentar el radio
    def add_radio(self, r):
        self.radio = self.radio + r
        return (self.radio)

    # metodo para dibujar el objeto
    def dibujarCirculo(self):
        plt.gca().add_patch(plt.Circle((0,0), radius = self.radio, fc = self.color))
        plt.axis('scaled')
        plt.show()

circulo_rojo = circulo(10, 'red')
dir(circulo_rojo)

circulo_rojo.radio
circulo_rojo.color = 'blue'
circulo_rojo.radio = 2

circulo_rojo.dibujarCirculo()




class rectangulo(object):

    """Nuestra clase va a generar un rectangulo a partir de los atributos
    ancho, alto y Color
    """

    def __init__(self, ancho, alto, color):
        self.ancho = ancho
        self.alto = alto
        self.color = color

    def dibujarRectangulo(self):
        plt.gca().add_patch(plt.Rectangle((0,0), width = self.ancho, height = self.alto, fc = self.color ))
        plt.axis('scaled')
        plt.grid()
        plt.show()





rectangulo_rosa = rectangulo(4,9,'pink')
rectangulo_rosa.dibujarRectangulo()

rectangulo_negro = rectangulo(21,18,'black')
rectangulo_negro.dibujarRectangulo()
rectangulo_azul = rectangulo(18,12,'blue')
rectangulo_azul.dibujarRectangulo()
