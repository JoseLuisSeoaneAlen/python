Class Animal(object):
 def __init__(self):
  vivo = boolean
  boolean = True
  
 def estoy_vivo(self, vivo):
    return self.vivo
  
Class Gato(Animal):
  def __init__(self):
    return super(Gato,self)
  def ronronear(self, onomatopeya):
    onomatopeya="RRRRRR"
    return onomatopeya
  def maullar(self, onomatopeya):
    onomatopeya="MIIIIAAAAAUUU"
    return onomatopeya
  def gruñir(self, onomatopeya):
    onomatopeya="GGGRRRRR"
    return onomatopeya
 
# declaramos un animal
animal = Gato()

sonido=""
print(animal.ronronear(onomateya))
print(animal.maullar(onomatopeya))
print(animal.gruñir(onomatopeya))
