# Classe Bicicleta

Este repositório contém uma implementação simples da classe `Bicicleta` em Python. Esta classe demonstra os conceitos fundamentais de Programação Orientada a Objetos (POO), incluindo classes, objetos e métodos.

## Conceitos Básicos

### Classe

Uma **classe** é uma estrutura que define um novo tipo de objeto. Ela serve como um molde (ou blueprint) para criar objetos. Em Python, uma classe é definida usando a palavra-chave `class`, seguida pelo nome da classe.

### Objeto

Um **objeto** é uma instância de uma classe. Quando você cria um objeto, você está criando uma nova instância da classe que pode ter seus próprios dados e comportamentos.

### Método

Um **método** é uma função definida dentro de uma classe. Os métodos descrevem os comportamentos dos objetos que são instâncias dessa classe. Eles podem acessar e modificar os dados dos objetos.

## Implementação da Classe Bicicleta

A classe `Bicicleta` representa uma bicicleta e inclui os seguintes atributos e métodos:

### Atributos

- **marca**: A marca da bicicleta (tipo `str`).
- **modelo**: O modelo da bicicleta (tipo `int`).
- **cor**: A cor da bicicleta (tipo `str`).
- **valor**: O valor da bicicleta (tipo `float`).

### Métodos

- **`__init__`**: O inicializador da classe que configura os atributos da bicicleta.
- **buzinar()**: Emite o som da buzina da bicicleta.
- **parar()**: Simula a parada da bicicleta.
- **correr()**: Simula o som da bicicleta correndo.
- **`__str__`**: Retorna uma representação em string da bicicleta, facilitando a visualização dos atributos.

## Exemplo de Uso

Aqui está um exemplo de como usar a classe `Bicicleta`:

```python
# Criar uma instância da classe Bicicleta
caloi = Bicicleta("Caloi", 2022, "vermelha", 600.00)

# Interações com a instância da bicicleta
caloi.buzinar()  # Emite o som da buzina
caloi.correr()   # Simula o som da bicicleta correndo
caloi.parar()    # Simula a parada da bicicleta

# Imprimir a representação da instância
print(caloi)     # Exibe os atributos da bicicleta
