class Bicicleta:
    """Classe que representa uma bicicleta."""

    def __init__(self, marca: str, modelo: int, cor: str, valor: float):
        """
        Inicializa uma nova instância da classe Bicicleta.

        Args:
            marca (str): Marca da bicicleta.
            modelo (int): Modelo da bicicleta.
            cor (str): Cor da bicicleta.
            valor (float): Valor da bicicleta.
        """
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.valor = valor

    def buzinar(self) -> None:
        """Emite o som da buzina da bicicleta."""
        print("Biuu!")

    def parar(self) -> None:
        """Simula a parada da bicicleta."""
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self) -> None:
        """Simula o som da bicicleta correndo."""
        print("Vrumm")

    def __str__(self) -> str:
        """Retorna uma representação em string da bicicleta."""
        atributos = ', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())
        return f"{self.__class__.__name__}: {atributos}"

# Criar uma instância da classe Bicicleta
caloi = Bicicleta("Caloi", 2022, "vermelha", 600.00)

# Interações com a instância da bicicleta
caloi.buzinar()
caloi.correr()
caloi.parar()

# Imprimir a representação da instância
print(caloi)
