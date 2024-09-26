# Bicycle Class

This repository contains a simple implementation of the `Bicycle` class in Python. This class demonstrates fundamental Object-Oriented Programming (OOP) concepts, including classes, objects, and methods.

## Basic Concepts

### Class

A **class** is a structure that defines a new type of object. It serves as a mold (or blueprint) for creating objects. In Python, a class is defined using the keyword `class`, followed by the class name.

### Object

An **object** is an instance of a class. When you create an object, you are creating a new instance of the class that can have its own data and behaviors.

### Method

A **method** is a function defined within a class. Methods describe the behaviors of objects that are instances of that class. They can access and modify the data of the objects.

## Bicycle Class Implementation

The `Bicycle` class represents a bicycle and includes the following attributes and methods:

### Attributes

- **brand**: The brand of the bicycle (type `str`).
- **model**: The model of the bicycle (type `int`).
- **color**: The color of the bicycle (type `str`).
- **price**: The price of the bicycle (type `float`).

### Methods

- **`__init__`**: The initializer of the class that sets up the bicycle's attributes.
- **honk()**: Emits the sound of the bicycle's horn.
- **stop()**: Simulates stopping the bicycle.
- **ride()**: Simulates the sound of the bicycle riding.
- **`__str__`**: Returns a string representation of the bicycle, making it easier to visualize the attributes.

## Usage Example

Here is an example of how to use the `Bicycle` class:

```python
# Create an instance of the Bicycle class
caloi = Bicycle("Caloi", 2022, "red", 600.00)

# Interactions with the bicycle instance
caloi.honk()  # Emits the sound of the horn
caloi.ride()  # Simulates the sound of the bicycle riding
caloi.stop()  # Simulates stopping the bicycle

# Print the string representation of the instance
print(caloi)  # Displays the bicycle's attributes

# Understanding `__init__` and `__del__` Methods in Python

In Python, `__init__` and `__del__` are special methods (also known as dunder methods) that are automatically called when an object is created or deleted. They allow you to manage the initialization and cleanup of your class instances effectively.

## `__init__` Method

### What is `__init__`?

The `__init__` method is a constructor in Python. It is automatically invoked when a new instance of a class is created. Its primary purpose is to initialize the attributes of the new object.


