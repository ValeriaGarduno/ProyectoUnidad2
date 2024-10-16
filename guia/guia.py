from usuario.usuario import Usuario
from datetime import datetime
from usuario.utils.rol import Rol
##nombre, apellidos, fecha de nacimineto, fecha ingreso como trabajo, rfc, curp, salario, horario, rol

class Guia(Usuario): 
    def __init__(self,id_trabajador:str, nombre: str, apellido: str, fecha_nacimiento: datetime, fecha_ingreso_trabajador: datetime, rfc: str, curp: str, salario: float, horario: datetime, rol:Rol.GUIA):
        super().__init__(id_trabajador ,nombre, apellido, fecha_nacimiento, fecha_ingreso_trabajador, rfc, curp, salario, horario, rol)
        self.rol = Rol
    def mostrar_info_guia(self):
        info = f"Nombre completo: {self.nombre} {self.apellido}, Curp: {self.curp}, Salario: {self.salario}, ID: {self.id_trabajador} "
        return info