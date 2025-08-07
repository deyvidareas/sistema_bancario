class Cachorro:
  def __init__(self, nome, cor, acordado=True):
    print("Inicializando a classe...")
    self.nome = nome
    self.cor = cor
    self.acordado = acordado

  def __del__(self):
    print("Removendo Instância da Classe!")

  def falar(self):
    print("au au")

  def criar_cachorro(self):
    c = Cachorro("Zeus", "puddle")
    print(c.nome)

c = Cachorro("Chapolin", "amarelo")
c.falar()
c.criar_cachorro()
del c
print("ola mundo")