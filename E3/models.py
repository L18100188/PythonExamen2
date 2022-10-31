from app import db

class Cine(db.Model):
    idCine=db.Column(db.Integer,primary_key=True)
    nombreCine=db.Column(db.String(250))
    direccion=db.Column(db.String(250))
    numSalas=db.Column(db.Integer)
    horario=db.Column(db.String(250))

    def __str__(self) -> str:
        return (f'idCine:{self.idCine},'
                f'nombreCine:{self.nombreCine},'
                f'direccion:{self.direccion},'
                f'numSalas:{self.numSalas},'
                f'horario:{self.horario}'
        )

    def __init__(self,nombreCine,direccion,numSalas,horario):
        self.nombreCine=nombreCine
        self.direccion=direccion
        self.numSalas=numSalas
        self.horario=horario

class SalaCine(db.Model):
    idSala=db.Column(db.Integer,primary_key=True)
    capacidad=db.Column(db.Integer)
    ocupado=db.Column(db.String(250))
    horaProxFuncion=db.Column(db.String(250))

    def __str__(self) -> str:
        return (f'idSala:{self.idSala},'
                f'capacidad:{self.capacidad},'
                f'ocupado:{self.ocupado},'
                f'horaProxFuncion:{self.horaProxFuncion}'
        )

class Producto(db.Model):
    idProducto=db.Column(db.Integer,primary_key=True)
    nombreProducto = db.Column(db.String(250))
    inventario = db.Column(db.Integer)
    precioVenta =  db.Column(db.Float)

    def __str__(self) -> str:
        return (f'idProducto:{self.idProducto},'
                f'nombreProducto:{self.nombreProducto},'
                f'inventario:{self.inventario},'
                f'precioVenta:{self.precioVenta}'
        )

class Pelicula(db.Model):
    idPelicula=db.Column(db.Integer,primary_key=True)
    nombrePelicula = db.Column(db.String(250))
    fechaEstreno = db.Column(db.String(250))
    estudioCinematografico =  db.Column(db.String(250))

    def __str__(self) -> str:
        return (f'idPelicula:{self.idPelicula},'
                f'nombrePelicula:{self.nombrePelicula},'
                f'fechaEstreno:{self.fechaEstreno},'
                f'estudioCinematografico:{self.estudioCinematografico}'
        )

class Boleto(db.Model):
    idBoleto=db.Column(db.Integer,primary_key=True)
    funcion = db.Column(db.String(250))
    fechaFuncion = db.Column(db.String(250))
    precio =  db.Column(db.String(250))

    def __str__(self) -> str:
        return (f'idBoleto:{self.idBoleto},'
                f'Funcion:{self.funcion},'
                f'FechaFuncion:{self.fechaFuncion},'
                f'precio:{self.precio}'
        )