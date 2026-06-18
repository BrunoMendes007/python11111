class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_barulho(self):
        pass

class Passaro(Animal):
    def fazer_barulho(self):
        return "Au Au!"
   
class Leao(Animal):
    def fazer_barulho(self):
        return "Miau!"

animais = [Passaro("Águia"), Leao("Simba")]

for animal in animais:
    print(f"{animal.nome} faz: {animal.fazer_barulho()}")