from usuario.usuario import Usuario
from datetime import datetime
from usuario.utils.rol import Rol

class Veterinario(Usuario): 
    def __init__(self, id_trabajador:str, nombre: str, apellido: str, fecha_nacimiento: datetime, fecha_ingreso_trabajador: datetime, rfc: str, curp: str, salario: float, horario: datetime, rol:Rol.VETERINARIO):
        super().__init__(id_trabajador=id_trabajador, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, fecha_ingreso_trabajador=fecha_ingreso_trabajador, rfc=rfc, curp=curp, salario=salario, horario=horario, rol=rol)
        self.rol = Rol
    def mostrar_info_veterinario(self):
        info = f"Nombre completo: {self.nombre}{self.apellido}, Curp: {self.curp}, Salario: {self.salario}, ID: {self.id_trabajador}"
        return info