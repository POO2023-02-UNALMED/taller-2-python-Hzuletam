class Asiento:
  
  def __init__(self,color,precio,registro):
    self.color = color
    self.precio = precio
    self.registro = registro
    
  def cambiarColor(self,color):
    coloresValidos = ['rojo', 'verde', ' amarillo', 'negro','blanco']
    if color in coloresValidos:
      self.color = color


class Motor:
  
  def __init__(self,numeroCilindros,tipo,registro):
    self.numeroCilindros = numeroCilindros
    self.tipo = tipo
    self.registro = registro
    
  def cambiarRegistro(self, registro):
    if registro.isnumeric():  
      self.registro = registro
      
  def asignarTipo(self,tipo):
    tiposValidos = ['gasolina','electrico']
    if tipo in tiposValidos:
      self.tipo = tipo


class Auto:
  
  cantidadCreados = 0
  
  def __init__(self,modelo, precio, asientos,marca,motor,registro,cantidadCreados):
    self.modelo = modelo
    self.precio = precio
    self.asientos = [x for x in asientos if type(x) == type(Asiento())]
    self.marca = marca
    self.motor = motor
    self.registro = registro
    
  def cantidadAsientos(self):
    return len(self.asientos)
    
  def verificarIntegridad(self):
    if self.motor.registro == self.registro and all(self.registro == asiento.registro for asiento in self.asientos]
    