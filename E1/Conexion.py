import psycopg2 as bd
from psycopg2 import pool
from logger_base import log
class Conexion:
    _DATABASE='examen1'
    _USERNAME='postgres'
    _PASSWORD='admin'
    _DBPORT='5432'
    _HOST='127.0.0.1'
    _MIN_CON=1
    _MAX_CON=5
    _pool=None

    _conexion=None
    _cursor=None

    @classmethod
    def ObtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool=pool.SimpleConnectionPool(cls._MIN_CON,
                cls._MAX_CON,
                host=cls._HOST,
                user=cls._USERNAME,
                password=cls._PASSWORD,
                port=cls._DBPORT,
                database=cls._DATABASE)
                log.debug(f'Creacion del pool {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un errir en el pool {e}')
        else:
            return cls._pool
        
    @classmethod
    def ObtenerConexion(cls):
        conexion=cls.ObtenerPool().getconn()
        log.debug(f'conexion obtenida: {conexion}')
        return conexion
    
    @classmethod
    def LiberarConexion(cls,conexion):
        cls.ObtenerPool().putconn(conexion)
        log.debug(f'Conexion regresada: {conexion}')

    @classmethod 
    def cerrarConexiones(cls):
        cls.ObtenerPool().closeall()

    

if __name__=='__main__':
    conexion1=Conexion.ObtenerConexion()
    conexion2=Conexion.ObtenerConexion()
        

    
