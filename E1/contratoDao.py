from contrato import Contrato
from Conexion import Conexion
from logger_base import log
from cursorDelPool import CursorDelPool  

class contratoDao:
    _SELECCIONAR=   "SELECT * FROM contrato ORDER BY idcontrato"
    _INSERTAR =     "INSERT INTO contrato(idcontrato,nocontrato,costo,fechainicio,fechafin) Values(%s,%s,%s,%s,%s)"
    _ACTUALIZAR=    "UPDATE contrato SET nocontrato=%s, costo=%s, fechainicio=%s ,fechafin=%s WHERE idcontrato=%s"
    _ELIMINAR =     "DELETE FROM contrato WHERE idcontrato=%s"

    @classmethod
    def seleccionar(cls):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                contratos=[]
                for r in registros:
                    contrato=(Contrato(r[0],r[1],r[2],r[3],r[4]))
                    contratos.append(contrato)
                return contratos
    @classmethod
    def INSERT(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato._idcontrato,contrato._nocontrato,contrato._costo,contrato._fechainicio,contrato._fechafin)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
        
    @classmethod
    def UPDATE(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato._nocontrato,contrato._costo,contrato._fechainicio,contrato._fechafin,contrato._idcontrato)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
        
    @classmethod
    def DELETE(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato._idcontrato,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
if __name__=="__main__":
    #Mostrar
     contratos = contratoDao.seleccionar()
     for c in contratos:
       log.debug(c)
    #INSERT
    #contrato1 = Contrato(idcontrato="1",nocontrato="100",costo=250000,fechainicio="05/10/22",fechafin="05/05/24")
    #contratoinsertado = contratoDao.INSERT(contrato1)
    #log.debug(f"Contrato insertado {contratoinsertado}")
    #UPDATE
    #contrato1 = Contrato(idcontrato="1",nocontrato="100",costo=400000,fechainicio="05/10/24",fechafin="05/05/27")
    #contratoactualizado = contratoDao.UPDATE(contrato1)
    #log.debug(f"Contrato actualizado {contratoactualizado}")
    #DELETE
    #contratoeliminado = contratoDao.DELETE(contrato1)
    #log.debug(f"Personas Eliminadas {contratoeliminado}")
