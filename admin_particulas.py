from particula import Particula

class Admin_particulas:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, part:Particula):
        self.__particulas.append(part)

    def agregar_inicio(self, part:Particula):
        self.__particulas.insert(0, part)
    
    def consultar(self):
        for part in self.__particulas:
            print(part)


l01 = Particula(id=2, origen_x=1, origen_y=5, destino_x=9, destino_y=9, velocidad=12, red=120, green=34, blue=255)
l02 = Particula(4, 25, 12, 32, 14, 34, 2505, 255, 255)
particula = Admin_particulas()
particula.agregar_final(l01)
particula.agregar_inicio(l02)
particula.consultar()
        