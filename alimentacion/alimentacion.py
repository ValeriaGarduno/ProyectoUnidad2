from typing import List
from mantenimiento.mantenimiento import Mantenimiento
from animales.animales import Animales
from datetime import datetime

class Alimentacion(): 
    empleado = List[Mantenimiento]
    id_animal = List[Animales]
    proceso = str
    observaciones = str
    fecha_proceso = datetime
     
    def __init__(self, proceso: str, observaciones: str, fecha_proceso: datetime) -> None:
        self.empleado = []
        self.id_animal = []
        self.proceso = proceso
        self. observaciones = observaciones
        self.fecha_proceso = fecha_proceso