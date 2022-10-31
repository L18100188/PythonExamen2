from contrato_persona import Contrato_Persona
from Conexion import Conexion
from logger_base import log
from cursorDelPool import CursorDelPool

class contrato_personaDAO:
    _SELECCIONAR=   "SELECT * FROM contrato_persona"
    _INSERTAR =     "INSERT INTO contrato_persona(idpersona,idcontrato) Values(%s,%s)"

    @classmethod
    def seleccionar(cls):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                contratosypersonas=[]
                for r in registros:
                    contratosypersona=(Contrato_Persona(r[0],r[1]))
                    contratosypersonas.append(contratosypersona)
                return  contratosypersonas
    @classmethod
    def INSERT(cls,contratosypersonas):
        with CursorDelPool() as cursor:
            valores = (contratosypersonas._idpersona,contratosypersonas._idcontrato)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount

if __name__=="__main__":
    #Mostrar
    #con = contrato_personaDAO.seleccionar()
    #for c in con:
       #log.debug(f"Lista de contratos y personas\n{c}")
    #INSERT
    Con1 = Contrato_Persona(idpersona="1",idcontrato="100")
    insertado = contrato_personaDAO.INSERT(Con1)
    log.debug(f"Ciudades insertadas {insertado}")