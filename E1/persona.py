from logger_base import log
class Persona():
    def __init__(self,idpersona,nombre,edad,correo) -> None:
        self._idpersona = idpersona
        self._nombre = nombre
        self._edad = edad
        self._correo = correo
        pass
    
    def __str__(self) -> str:
        return f"idPersona: {self._idpersona}\nNombre: {self._nombre}\nEdad: {self._edad}\nCorreo: {self._correo}"