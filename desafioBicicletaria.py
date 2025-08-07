class Bicicleta:

  def __init__(self, cor, modelo, ano, valor):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano 
    self.valor = valor

  def buzinar(self):
    print("Prim Prim...")

  def parar(self):
    print("Parando..")
    print("Parou.")

  def correr(self):
    print("Vrummmmmmm..")

# def __str__(self):
#  return f"Bicicleta: Cor = {self.cor}, Modelo = {self.modelo}, Ano = {self.ano}, Valor = {self.valor}"
    
  def __str__(self):
    return f"{self.__class__.__name__}: {[', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())]}"

  def trocar_marcha(self, nro_marcha):
    print("Trocando marcha...")
    
    def _trocar_marcha():
      if nro_marcha > self:
        print("Marcha trocada...")
      else:
        print("Não foi possível trocar marcha!")

b1 = Bicicleta("vermelha", "caloi", 2001, 500)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor,b1.modelo,b1.ano,b1.valor) 

b2 = Bicicleta("verde", "monark", 2000, 189)
b2.buzinar() # É o mesmo que Bicicleta.buzinar(b2)

print(b2)