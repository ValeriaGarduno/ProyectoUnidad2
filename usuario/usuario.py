from datetime import datetime
from typing import List
from usuario.utils.rol import Rol

class Usuario:
    id_trabajador: str
    nombre: str
    apellido: str
    fecha_nacimiento: datetime
    fecha_ingreso_trabajador: datetime
    rfc: str
    curp: str
    salario: float
    horario: datetime
    rol: Rol

    def __init__(self, id_trabajador: str, nombre: str, apellido: str, fecha_nacimiento: datetime, fecha_ingreso_trabajador: datetime, rfc: str , curp: str , salario: float , horario: datetime ,rol: Rol):
        self.id_trabajador= id_trabajador
        self.nombre= nombre
        self.apellido= apellido
        self.fecha_nacimiento= fecha_nacimiento
        self.fecha_ingreso_trabajador= fecha_ingreso_trabajador
        self.rfc= rfc
        self.curp= curp
        self.salario= salario
        self.horario= horario
        self.rol= rol