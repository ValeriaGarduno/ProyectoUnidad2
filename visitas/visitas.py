from typing import List
from visitantes.visitantes import Visitantes
from datetime import datetime
from guia.guia import Guia

class Visitas: 
    guia_cargo = List[Guia]
    visitantes = List[Visitantes]
    costo_visita = float
    fecha_visita = datetime
    cantidad_ninos = int
    cantidad_adultos = int
    
    def __init__(self, costo_visita: float, fecha_visita: datetime, cantidad_ninos: int, cantidad_adultos: int):
        self.guia_cargo = []
        self.costo_visita = costo_visita
        self.fecha_visita = fecha_visita
        self.cantidad_adultos = cantidad_adultos
        self.cantidad_ninos = cantidad_ninos
        self.visitantes = []

    def info_visitas(self):
            no_visitantes= self.cantidad_adultos + self.cantidad_ninos
            info_visitas = f"\n   Niños: {self.cantidad_ninos}, Adultos: {self.cantidad_adultos}, Total de Visitantes: {no_visitantes}, Costo: {self.costo_visita}"
            return info_visitas