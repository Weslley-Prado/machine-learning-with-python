class Bicycle:
    """Class representing a bicycle."""

    def __init__(self, brand: str, model: int, color: str, price: float):
        """
        Initializes a new instance of the Bicycle class.

        Args:
            brand (str): The brand of the bicycle.
            model (int): The model of the bicycle.
            color (str): The color of the bicycle.
            price (float): The price of the bicycle.
        """
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        print("Allocating memory for the bicycle.")

    def honk(self) -> None:
        """Emits the sound of the bicycle's horn."""
        print("Beep!")

    def stop(self) -> None:
        """Simulates stopping the bicycle."""
        print("Stopping the bicycle...")
        print("Bicycle stopped!")

    def ride(self) -> None:
        """Simulates the sound of the bicycle riding."""
        print("Vroom")

    def __str__(self) -> str:
        """Returns a string representation of the bicycle."""
        attributes = ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
        return f"{self.__class__.__name__}: {attributes}"

    def __del__(self):
        """Method called when the instance is deleted."""
        print("Bicycle removed!")


# Creating an instance of the Bicycle class
caloi = Bicycle("Caloi", 2022, "red", 600.00)

# Interactions with the bicycle instance
caloi.honk()
caloi.ride()
caloi.stop()

# Print the string representation of the instance
print(caloi)
