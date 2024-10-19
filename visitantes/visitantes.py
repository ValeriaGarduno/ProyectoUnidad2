from datetime import datetime
from guia.guia import Guia
from typing import List

class Visitantes: 
    id_visitante =    str
    nombre = str
    apellido = str
    curp = str
    fecha_registro = datetime
    numero_visitas = int
    fecha_nacimiento = datetime
    guia = List[Guia]
   
    
    def __init__(self,id_visitante: str, nombre: str, apellido: str, curp: str, fecha_registro: datetime, fecha_nacimiento: datetime):
        self.id_visitante = id_visitante
        self.nombre = nombre
        self.apellido = apellido
        self.curp = curp
        self.fecha_registro = fecha_registro     
        self.fecha_nacimiento = fecha_nacimiento 
        self.numero_visitas = 0 # Inicializar  
        self.guia = []
        
    def mostrar_info_visitantes(self):
        info = f"Nombre completo: {self.nombre} {self.apellido}, Curp: {self.curp}, Num. Visitas{self.numero_visitas}, ID: {self.id_visitante}"
        return info