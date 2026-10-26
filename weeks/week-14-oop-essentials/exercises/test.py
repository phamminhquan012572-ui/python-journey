"""Basic tests for Exercise 03: inheritance."""

from ex03_inheritance import Animal, Dog


def test_animal_stores_name():
    animal = Animal("Milo")
    assert animal.name == "Milo"


def test_dog_inherits_name_from_animal():
    dog = Dog("Milo")
    assert dog.name == "Milo"


def test_dog_speak():
    dog = Dog("Milo")
    assert dog.speak() == "Milo: woof"
