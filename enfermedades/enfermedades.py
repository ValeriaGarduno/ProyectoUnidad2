class Enfermedades:
    enfermedad: str
    def __init__(self,  enfermedad: str):
        self.enfermedad= enfermedad
    def mostrar_enfermedad(self):
        info_enfermedad = f"\n  Enfermedad: {self.enfermedad}"
        return info_enfermedad