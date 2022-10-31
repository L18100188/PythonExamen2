from persona import Persona
from Conexion import Conexion
from logger_base import log
from cursorDelPool import CursorDelPool  

class PersonaDao:
    _SELECCIONAR=   "SELECT * FROM persona ORDER BY idpersona"
    _INSERTAR =     "INSERT INTO persona(idpersona,nombre,edad,correo) Values(%s,%s,%s,%s)"
    _ACTUALIZAR=    "UPDATE persona SET nombre=%s, edad=%s, correo=%s WHERE idpersona=%s"
    _ELIMINAR =     "DELETE FROM persona WHERE idpersona=%s"

    @classmethod
    def seleccionar(cls):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas=[]
                for r in registros:
                    persona=(Persona(r[0],r[1],r[2],r[3]))
                    personas.append(persona)
                return personas
    @classmethod
    def INSERT(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona._idpersona,persona._nombre,persona._edad,persona._correo)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
        
    @classmethod
    def UPDATE(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona._nombre,persona._edad,persona._correo,persona._idpersona)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
        
    @classmethod
    def DELETE(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona._idpersona,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
if __name__=="__main__":
    #Mostrar
     personas = PersonaDao.seleccionar()
     for p in personas:
       log.debug(p)
    #INSERT
    #persona1 = Persona(idpersona="1",nombre="Emiliano",correo="emilaino@gccl.com",edad=26)
    #personasInsertadas = PersonaDao.INSERT(persona1)
    #log.debug(f"Personas insertadas {personasInsertadas}")
    #UPDATE
    #persona1 = Persona(idpersona="1",nombre="Samuel",edad=50,correo="samuel@gmail.com")
    #personasActualizadas = PersonaDao.UPDATE(persona1)
    #log.debug(f"Personas Actualizadas {personasActualizadas}")
    #DELETE
    #personasEliminadas = PersonaDao.DELETE(persona1)
    #log.debug(f"Personas Eliminadas {personasEliminadas}")
