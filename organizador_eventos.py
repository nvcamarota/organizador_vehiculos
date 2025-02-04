"""
ORGANIZADOR DE EVENTOS
Crear un sistema de vehículos en Python con una superclase Vehículo y tres subclases:
1. Auto: Tiene un método tocar_bocina() que imprime '¡Beep beep! 🚗'.
2. Moto: Tiene un método hacer_wheelie() que imprime '¡Mira este wheelie! 🏍'.
3. Bicicleta: Tiene un método pedalear() que imprime 'Pedaleando con fuerza 🚲'.

Objetivo: Imprementa la herencia correctamente.
• Usa super()__init__() en las subclases para llamar al constructor de Vehículo.
• Crea objetos de cada clase y prueba sus métodos.
"""

class Vehículo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def describir(self):
        return f'Este vehículo es de marca "{self.marca}", modelo "{self.modelo}".'
        
class Auto(Vehículo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def describir(self):
        return super().describir()
    
    def tocar_bocina(self):
        return '¡Beep beep! 🚗\n'
    
class Moto(Vehículo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        
    def describir(self):
        return super().describir()
        
    def hacer_wheelie(self):
        return '¡Mira este wheelie! 🏍\n'
    
class Bicicleta(Vehículo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        
    def describir(self):
        return super().describir()
        
    def pedalear(self):
        return 'Pedaleando con fuerza 🚲\n'
    
auto = Auto('Renault', 'Kangoo')
moto = Moto('Honda', 'NX 500')
bicicleta = Bicicleta('Venzo', 'Flash')

print(auto.describir())
print(auto.tocar_bocina())

print(moto.describir())
print(moto.hacer_wheelie())

print(bicicleta.describir())
print(bicicleta.pedalear())
