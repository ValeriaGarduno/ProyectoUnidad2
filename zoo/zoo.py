from typing import List
from usuario.usuario import Usuario
from guia.guia import Guia
from visitantes.visitantes import Visitantes
from visitas.visitas import Visitas
from usuario.utils.rol import Rol
from mantenimiento.mantenimiento import Mantenimiento
from administracion.administracion import Administracion
from animales.animales import Animales
from alimentacion.alimentacion import Alimentacion
from veterinario.veterinario import Veterinario 
from random import randint
from datetime import datetime
from enfermedades.enfermedades import Enfermedades
import itertools

class Zoo:
    lista_usuarios: List[Usuario] = []
    lista_guia: List[Guia] = []
    lista_visitantes: List[Visitantes] = []
    lista_visitas: List[Visitas] = []
    lista_animales: List[Animales] = []
    lista_veterinarios: List[Veterinario] = []
    lista_enfermedades: List[Enfermedades] = []
    lista_mantenimiento: List[Mantenimiento] = []
    lista_administracion: List[Administracion] = []
    lista_alimentacion: List[Alimentacion] = []

    #INICIO SESION
    def validar_inicio_sesion(self, director: str, contrasena: str):
            if director == director:
                if contrasena == contrasena:
                    return 

    #REGISTROS EN LISTAS AL CORRER
    animalprueba = Animales(id="A122perro", tipo="perro", fecha_de_nacimiento=datetime(2004, 4, 3), fecha_llegada=datetime(2007, 3, 4), peso=33.5, vacunas=True, frecuencia_alimentacion="3 veces al dia")
    lista_animales.append(animalprueba)
    visitante_prueba = Visitantes(id_visitante= "12", nombre= "valeria", apellido= "garduno", curp= "123erfd", fecha_registro= datetime(2005, 9, 10), fecha_nacimiento= datetime(3, 4 ,5))
    lista_visitantes.append(visitante_prueba)
    visitante_prueba1 = Visitantes(id_visitante= "123", nombre= "roberto", apellido= "garduno", curp= "123erfd", fecha_registro= datetime(2005, 9, 10), fecha_nacimiento= datetime(3, 4 ,5))
    lista_visitantes.append(visitante_prueba1)
    visitante_prueba2 = Visitantes(id_visitante= "654", nombre= "alejandra", apellido= "garduno", curp= "123erfd", fecha_registro= datetime(2005, 9, 10), fecha_nacimiento= datetime(3, 4 ,5))
    lista_visitantes.append(visitante_prueba2)
    visitante_prueba3 = Visitantes(id_visitante= "246", nombre= "francisco", apellido= "garduno", curp= "123erfd", fecha_registro= datetime(2005, 9, 10), fecha_nacimiento= datetime(3, 4 ,5))
    lista_visitantes.append(visitante_prueba3)
    visitante_prueba4 = Visitantes(id_visitante= "135", nombre= "barbie", apellido= "garduno", curp= "123erfd", fecha_registro= datetime(2005, 9, 10), fecha_nacimiento= datetime(3, 4 ,5))
    lista_visitantes.append(visitante_prueba4)
    guia_prueba = Guia(id_trabajador="guia1", nombre="Juan", apellido="Perez", fecha_nacimiento=datetime(2006, 2, 1), fecha_ingreso_trabajador=(2009, 4, 2), rfc="23cdf", curp="ffdfgdgvs", salario="1234", horario="12:00 - 1:00", rol=Rol.GUIA)
    lista_guia.append(guia_prueba)
    mantenimientp_prueba = Mantenimiento(id_trabajador="guia1", nombre="Juan", apellido="Perez", fecha_nacimiento=datetime(2006, 2, 1), fecha_ingreso_trabajador=(2009, 4, 2), rfc="23cdf", curp="ffdfgdgvs", salario="1234", horario="12:00 - 1:00", rol=Rol.MANTENIMIENTO)
    lista_mantenimiento.append(mantenimientp_prueba)

    #ANIMALES
    def registrar_enfermedades(self, animal: Animales, enfermedades: Enfermedades):
        animal.enfermedades.append(enfermedades)
        print("Enfermedad registrada correctamente   ")

    def eliminar_animales(self, id: str):  
        for animales in self.lista_animales:
            if animales.id == id:
                self.lista_animales.remove(animales)
                print("Animal eliminado")
                return
        print(f"\n No se encontró el estudiante con numero de control: {id}") 
        
    def modificar_animales(self, id: str, nueva_enfermedad = None, nuevo_tipo: str = None, nuevo_peso: float = None, nuevas_vacunas: bool = None, nuevo_nacimiento: datetime = None, nuevo_llegada: datetime = None, nuevo_alimentacion: str = None):
        for animales in self.lista_animales:
            if animales.id == id:
                if nuevo_tipo is not None:
                    animales.tipo = nuevo_tipo
                if nuevo_peso is not None:
                    animales.peso = nuevo_peso
                if nuevas_vacunas is not None:
                    animales.vacunas = nuevas_vacunas
                if nuevo_llegada is not None:
                    animales.fecha_llegada = nuevo_llegada
                if nuevo_nacimiento is not None:
                    animales.fecha_de_nacimiento = nuevo_nacimiento    
                if nuevo_alimentacion is not None:
                    animales.frecuencia_alimentacion = nuevo_alimentacion 
                if nueva_enfermedad != None:
                    animales.enfermedades = nueva_enfermedad    
                print(f"Animal con ID {id} modificado correctamente.")
                return

    def checar_id(self, id: str):
        for animales in self.lista_animales:
            if animales.id == id:
                print("Animal encontrado")
                return animales
        print(f"\n No se encontró animal con ID: {id}") 
    
    def generar_id_animal(self, tipo: str)-> str:
        ano_actual = datetime.now().day
        longitud_mas_uno = len(self.lista_animales) + 1
        id = f"A-{longitud_mas_uno}{tipo[:2].upper()}{ano_actual}{randint(500, 5000)}"
        return id
    
    def listar_animales(self):
        print("\n** ANIMALES **")
        for animales in self.lista_animales:
            print(animales.mostrar_info_animales())
    
    def registrar_animales(self, animales: Animales):
        self.lista_animales.append(animales)

    #ENFERMEDADES
    def listar_enfermedades(self):
        for enfermedades in self.lista_enfermedades:
            print(enfermedades.mostrar_enfermedad())
            
    #VISITAS
    def registrar_visitas(self, visitas: Visitas):
        self.lista_visitas.append(visitas)

    def mostrar_visitas(self):
        print("VISITA")
        for visitas in self.lista_visitas:
            print(visitas.info_visitas())

    #VISITANTE
    def id_visitante(self, nombre: str):
        ano_actual = datetime.now().day
        longitud_mas_uno = len(self.lista_visitantes) + 1 
        id_visitante = f"V{longitud_mas_uno}{ano_actual}{nombre[:2].upper()}"
        return id_visitante         
    
    def registrar_visitante(self, visitante: Visitantes):
      self.lista_visitantes.append(visitante) 
       
    def obtener_visitante_por_id(self, id_visitante: str):
        for visitante in self.lista_visitantes:
            if visitante.id_visitante == id_visitante:
                return visitante
        return None
    
    def listar_visitante(self):
        for visitante in self.lista_visitantes:
            print(visitante.mostrar_info_visitantes())
    
    def modificar_visitante(self, id_visitante: str, nuevo_nombre: str = None, nuevo_apellido: str = None,  nuevo_nacimiento: datetime= None, nuevo_ingreso: datetime= None, nuevo_visitas: str=None ,nuevo_curp: str= None ):
        for visitante in self.lista_visitantes:
            if visitante.id_visitante == id_visitante:
                if nuevo_nombre is not None:
                    visitante.nombre = nuevo_nombre
                if nuevo_apellido is not None:
                    visitante.apellido = nuevo_apellido
                if nuevo_curp is not None:
                    visitante.curp = nuevo_curp
                if nuevo_nacimiento is not None:
                    visitante.fecha_nacimiento = nuevo_nacimiento             
                if nuevo_visitas is not None:
                    visitante.numero_visitas = nuevo_visitas
                if nuevo_ingreso is not None:
                    visitante.fecha_registro = nuevo_ingreso               
                print(f"Visitante con ID {id} modificado correctamente.")
                return

    #TRABAJADORES
    def generar_id_trabajador(self, nombre:str, rol: Rol ):   
        ano_actual= datetime.now().day
        longitud_mas_uno = len(self.lista_veterinarios) + 1 
        id_trabajador = f"{longitud_mas_uno}{nombre[:2].upper()}{ano_actual}{rol.value}"
        return id_trabajador
    
    
    ##VETERINARIO
    def registrar_veterinario(self, veterinario: Veterinario):
        self.lista_veterinarios.append(veterinario)
        print(f"Veterinario {veterinario.nombre} {veterinario.apellido} registrado.")
    
    def listar_veterinaros(self):
        for veterinario in self.lista_veterinarios:
            print(veterinario.mostrar_info_veterinario())
            
    def eliminar_veterinarios(self, id_trabajador: str):
        for veterinario in self.lista_veterinarios:
            if veterinario.id_trabajador == id_trabajador:
                self.lista_veterinarios.remove(veterinario)
                print ("Veterinario eliminado")

    def checar_id_vet(self, id_trabajador: str):
        for veterinario in self.lista_veterinarios:
            if veterinario.id_trabajador == id_trabajador:
                    print("Veterinario encontrado")
                    return
            print(f"\n No se encontró veterinario con ID: {id_trabajador}")
            return

    def modificar_vet(self, id_trabajador: str, nuevo_nombre: str = None, nuevo_apellido: str = None,  nuevo_nacimiento: datetime= None, nuevo_ingreso_trabajador: datetime= None, nuevo_rfc: str=None ,nuevo_curp: str= None ,nuevo_salario: float= None ,nuevo_horario: datetime= None ):
        for veterinarios in self.lista_veterinarios:
            if veterinarios.id_trabajador == id_trabajador:
                if nuevo_nombre is not None:
                    veterinarios.nombre = nuevo_nombre
                if nuevo_apellido is not None:
                    veterinarios.apellido = nuevo_apellido
                if nuevo_horario is not None:
                    veterinarios.horario = nuevo_horario
                if nuevo_curp is not None:
                    veterinarios.curp = nuevo_curp
                if nuevo_nacimiento is not None:
                    veterinarios.fecha_nacimiento = nuevo_nacimiento    
                if nuevo_rfc is not None:
                    veterinarios.rfc = nuevo_rfc           
                if nuevo_salario is not None:
                    veterinarios.salario = nuevo_salario 
                if nuevo_ingreso_trabajador is not None:
                    veterinarios.fecha_ingreso_trabajador = nuevo_ingreso_trabajador               
                print(f"Trabajador con ID {id} modificado correctamente.")
                return

    ##GUIA
    def registrar_guia(self, guia: Guia):
        self.lista_guia.append(guia)
        print(f"Guia {guia.nombre} {guia.apellido} registrado")
    
    def listar_guia(self):
        for guia in self.lista_guia:
            print(guia.mostrar_info_guia())
    
    def eliminar_guia(self, id_trabajador: str):
        for guia in self.lista_guia:
            if guia.id_trabajador == id_trabajador:
                self.lista_guia.remove(guia)
                print ("Guia eliminado")
    def checar_id_guia(self, id_trabajador: str):
        for guia in self.lista_guia:
            if guia.id_trabajador == id_trabajador:
                print("Guia encontrado")
                return
        print(f"\n No se encontró guia con ID: {id_trabajador}")
        return

    def modificar_guia(self, id_trabajador: str, nuevo_nombre: str = None, nuevo_apellido: str = None,  nuevo_nacimiento: datetime= None, nuevo_ingreso_trabajador: datetime= None, nuevo_rfc: str=None ,nuevo_curp: str= None ,nuevo_salario: float= None ,nuevo_horario: datetime= None ):
        for guias in self.lista_guia:
            if guias.id_trabajador == id_trabajador:
                if nuevo_nombre is not None:
                    guias.nombre = nuevo_nombre
                if nuevo_apellido is not None:
                    guias.apellido = nuevo_apellido
                if nuevo_horario is not None:
                    guias.horario = nuevo_horario
                if nuevo_curp is not None:
                    guias.curp = nuevo_curp
                if nuevo_nacimiento is not None:
                    guias.fecha_nacimiento = nuevo_nacimiento    
                if nuevo_rfc is not None:
                    guias.rfc = nuevo_rfc           
                if nuevo_salario is not None:
                    guias.salario = nuevo_salario 
                if nuevo_ingreso_trabajador is not None:
                    guias.fecha_ingreso_trabajador = nuevo_ingreso_trabajador               
                print(f"Trabajador con ID {id} modificado correctamente.")
                return

    
    ##MANTENIMIENTO    
    def registrar_mantenimiento(self, mantenimiento: Mantenimiento):
        self.lista_mantenimiento.append(mantenimiento)
        print(f"Trabajador de mantenimiento {mantenimiento.nombre} {mantenimiento.apellido} registrado.")
        
    def listar_mantenimiento(self):
        for mantenimiento in self.lista_mantenimiento:
            print(mantenimiento.mostrar_info_mantenimiento())
    
    def mantenimiento_animales(self, id_trabajador: Mantenimiento, id: Animales):
        pass
            
    def eliminar_mantenimiento(self, id_trabajador: str):
        for mantenimiento in self.lista_mantenimiento:
            if mantenimiento.id_trabajador == id_trabajador:
                self.lista_mantenimiento.remove(mantenimiento)
                print ("Personal de mantenimiento eliminado")
    
    def checar_id_matenimiento(self, id_trabajador:str):
        for mantenimiento in self.lista_mantenimiento:
            if mantenimiento.id_trabajador == id_trabajador:
                print("Trabajador encontrado")
                return
            print("No se encontro a un trabajador de mantenimiento con este ID")

    def modificar_mantenimiento(self, id_trabajador: str, nuevo_nombre: str = None, nuevo_apellido: str = None,  nuevo_nacimiento: datetime= None, nuevo_ingreso_trabajador: datetime= None, nuevo_rfc: str=None ,nuevo_curp: str= None ,nuevo_salario: float= None ,nuevo_horario: datetime= None ):
        for mantenimiento in self.lista_mantenimiento:
            if mantenimiento.id_trabajador == id_trabajador:
                if nuevo_nombre is not None:
                    mantenimiento.nombre = nuevo_nombre
                if nuevo_apellido is not None:
                    mantenimiento.apellido = nuevo_apellido
                if nuevo_horario is not None:
                    mantenimiento.horario = nuevo_horario
                if nuevo_curp is not None:
                    mantenimiento.curp = nuevo_curp
                if nuevo_nacimiento is not None:
                    mantenimiento.fecha_nacimiento = nuevo_nacimiento    
                if nuevo_rfc is not None:
                    mantenimiento.rfc = nuevo_rfc           
                if nuevo_salario is not None:
                    mantenimiento.salario = nuevo_salario 
                if nuevo_ingreso_trabajador is not None:
                    mantenimiento.fecha_ingreso_trabajador = nuevo_ingreso_trabajador               
                print(f"Trabajador con ID {id} modificado correctamente.")
                return
            
    #ALIMENTACION
            
    def listar_comida(self):
        print("\n***MANTENIMIENTO / COMIDAS***")
        for alimentacion in self.lista_alimentacion:
            print(alimentacion.mostrar_info_alimentacion())
    
    def registrar_comida(self, alimentacion: Alimentacion):
        self.lista_alimentacion.append(alimentacion)

    
     ##ADMINISTRACION
    def registrar_administracion(self, administracion: Administracion):
        self.lista_administracion.append(administracion)
        print(f"Trabajador de administracion {administracion.nombre} {administracion.apellido} registrado.")
        
    def listar_administracion(self):
        for administracion in self.lista_administracion:
            print(administracion.mostrar_info_administracion())
            
    def eliminar_administracion(self, id_trabajador: str):
        for administracion in self.lista_administracion:
            if administracion.id_trabajador == id_trabajador:
                self.lista_administracion.remove(administracion)
                print ("Administrador eliminado")

    def checar_id_admin(self, id_trabajador: str):
        for administracion in self.lista_administracion:
            if administracion.id_trabajador == id_trabajador:
                    print("administracion encontrado")
                    return
            print(f"\n No se encontró administracion con ID: {id_trabajador}")
            return

    def modificar_admin(self, id_trabajador: str, nuevo_nombre: str = None, nuevo_apellido: str = None,  nuevo_nacimiento: datetime= None, nuevo_ingreso_trabajador: datetime= None, nuevo_rfc: str=None ,nuevo_curp: str= None ,nuevo_salario: float= None ,nuevo_horario: datetime= None ):
        for administracion in self.lista_administracion:
            if administracion.id_trabajador == id_trabajador:
                if nuevo_nombre is not None:
                    administracion.nombre = nuevo_nombre
                if nuevo_apellido is not None:
                    administracion.apellido = nuevo_apellido
                if nuevo_horario is not None:
                    administracion.horario = nuevo_horario
                if nuevo_curp is not None:
                    administracion.curp = nuevo_curp
                if nuevo_nacimiento is not None:
                    administracion.fecha_nacimiento = nuevo_nacimiento    
                if nuevo_rfc is not None:
                    administracion.rfc = nuevo_rfc           
                if nuevo_salario is not None:
                    administracion.salario = nuevo_salario 
                if nuevo_ingreso_trabajador is not None:
                    administracion.fecha_ingreso_trabajador = nuevo_ingreso_trabajador               
                print(f"Trabajador con ID {id} modificado correctamente.")
                return