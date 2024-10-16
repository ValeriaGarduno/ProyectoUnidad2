from enfermedades.enfermedades import Enfermedades
from datetime import datetime
from random import randint
from typing import List 

class Animales:
    id= str
    tipo = str
    fecha_de_nacimiento: datetime
    fecha_llegada: datetime
    peso = float
    vacunas = bool
    enfermedades = List[Enfermedades]
    frecuencia_alimentacion = str
     
    def __init__(self, id: str, tipo: str, fecha_de_nacimiento: datetime, fecha_llegada: datetime, peso: float, vacunas: bool, frecuencia_alimentacion: str ):
        self.id= id
        self.tipo = tipo
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.fecha_llegada = fecha_llegada
        self.peso = peso 
        self.vacunas = vacunas
        self.frecuencia_alimentacion = frecuencia_alimentacion
        self.enfermedades= []

    def mostrar_info_animales(self):
        info = f"\n - ID: {self.id}, Peso: {self.peso}, tipo: {self.tipo}, Fecha de nacimiento: {self.fecha_de_nacimiento}, Fecha de llegda: {self.fecha_llegada}, Vacunas: {self.vacunas}, Frequencia de Alimentacion: {self.frecuencia_alimentacion}"
        if self.enfermedades:
            info += "\n   Enfermedades:"
            for enfermedad in self.enfermedades:
                info += f"\n  {enfermedad.mostrar_enfermedad()}"
        else:
            info += "\n   No tiene enfermedades registradas."
        return info