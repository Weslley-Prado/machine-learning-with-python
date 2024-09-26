class Bicicleta:
    # Inicializador
    def __init__(self, marca, modelo, cor, valor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
    
    def buzinar(self):
        print("Biuu!")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Vrumm")

caloi = Bicicleta("Calor", 2022, "vermelha", 600)
caloi.buzinar()
caloi.correr()
caloi.parar()