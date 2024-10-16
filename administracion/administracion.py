from usuario.usuario import Usuario
from datetime import datetime
from usuario.utils.rol import Rol

class Administracion(Usuario):
    
    def __init__(self,id_trabajador:str,  nombre: str, apellido: str, fecha_nacimiento: datetime, fecha_ingreso_trabajador: datetime, rfc: str, curp: str, salario: float, horario: datetime, rol:Rol.ADMINISTRACION):
        super().__init__(id_trabajador, nombre, apellido, fecha_nacimiento, fecha_ingreso_trabajador, rfc, curp, salario, horario, rol)
    
    def mostrar_info_administracion(self):
        info = f"Nombre completo: {self.nombre}{self.apellido}, Curp: {self.curp}, Salario: {self.salario}, ID: {self.id_trabajador}"
        return info