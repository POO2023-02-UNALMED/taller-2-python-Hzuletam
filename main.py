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
    if isnumeric(registro):  
      self.registro = registro
      
  def asignarTipo(self,tipo):
    tiposValidos = ['gasolina','electrico']
    if tipo in tiposValidos:
      self.tipo = tipo


class Auto:
  
  cantidadCreados = 0
  
  def __init__(self,modelo, precio, asientos,marca,motor,registro):
    self.modelo = modelo
    self.precio = precio
    self.asientos = [x for x in asientos if type(x) == type(Asiento('negro',200,415))]
    self.marca = marca
    self.motor = motor
    self.registro = registro
    self.cantidadCreados+=1
    
  def cantidadAsientos(self):
    return len(self.asientos)
    
  def verificarIntegridad(self):
    if self.motor.registro == self.registro and all(self.registro == asiento.registro for asiento in self.asientos):
      return print('Auto original')
    else:
      return print('Las piezas no son originales')
    
