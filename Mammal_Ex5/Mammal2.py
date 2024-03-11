class Mammal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def move(self):
        print(f"{self.name} is moving.")


class Cat(Mammal):
    def __init__(self, name, age, gender, breed):
        super().__init__(name, age, gender)
        self.breed = breed

    def meow(self):
        print("Meow!")


class Dog(Mammal):
    def __init__(self, name, age, gender, breed):
        super().__init__(name, age, gender)
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")


class Lion(Mammal):
    def __init__(self, name, age, gender, pride):
        super().__init__(name, age, gender)
        self.pride = pride

    def roar(self):
        print("Roarrrrr!")


class Tiger(Mammal):
    def __init__(self, name, age, gender, stripes):
        super().__init__(name, age, gender)
        self.stripes = stripes

    def growl(self):
        print("Grrrrrr!")


# Example usage
if __name__ == "__main__":
    cat = Cat("Whiskers", 3, "Male", "Siamese")
    cat.eat()
    cat.sleep()
    cat.move()
    cat.meow()

    dog = Dog("Buddy", 5, "Female", "Golden Retriever")
    dog.eat()
    dog.sleep()
    dog.move()
    dog.bark()

    lion = Lion("Simba", 8, "Male", "Savannah")
    lion.eat()
    lion.sleep()
    lion.move()
    lion.roar()

    tiger = Tiger("Stripe", 6, "Female", "Bengal")
    tiger.eat()
    tiger.sleep()
    tiger.move()
    tiger.growl()
