class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"


class Mammal(Animal):
    def __init__(self, fur_color, **kw):
        self.fur_color = fur_color
        super().__init__(**kw)


class Bird(Animal):
    def __init__(self, beak_color, **kw):
        self.beak_color = beak_color
        super().__init__(**kw)


class Cat(Mammal):
    pass


class Platypus(Mammal, Bird):
    def __init__(self, beak_color, fur_color, num_legs):
        super().__init__(fur_color=fur_color, beak_color=beak_color, num_legs=num_legs)


cat = Cat(num_legs=4, fur_color="Black")
print(cat)

platypus = Platypus(num_legs=2, fur_color="Red", beak_color="Orange")
print(platypus)
