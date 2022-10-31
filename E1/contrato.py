from logger_base import log
class Contrato():
    def __init__(self,idcontrato,nocontrato,costo,fechainicio,fechafin) -> None:
        self._idcontrato = idcontrato
        self._nocontrato = nocontrato
        self._costo = costo
        self._fechainicio = fechainicio
        self._fechafin= fechafin
        pass
    
    def __str__(self) -> str:
        return f"idContrato: {self._idcontrato}\nNo.Contrato: {self._nocontrato}\nCosto: {self._costo}\nFechaInicio: {self._fechainicio}\nFechaFin:{self._fechafin}"