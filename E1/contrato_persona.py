from logger_base import log
class Contrato_Persona():
    def __init__(self,idpersona,idcontrato) -> None:
        self._idpersona = idpersona
        self._idcontrato=idcontrato
        pass
    
    def __str__(self) -> str:
        return f"idPersona: {self._idpersona}\nidContrato: {self._idcontrato}"