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
    def purr(self):
        print("Purrr...")


class Dog(Mammal):
    def bark(self):
        print("Woof! Woof!")


class Lion(Mammal):
    def roar(self):
        print("Roarrrrr!")


class Tiger(Mammal):
    def growl(self):
        print("Grrrrrr!")


# Example usage
if __name__ == "__main__":
    cat = Cat("Whiskers", 3, "Male")
    cat.eat()
    cat.sleep()
    cat.move()
    cat.purr()

    dog = Dog("Buddy", 5, "Female")
    dog.eat()
    dog.sleep()
    dog.move()
    dog.bark()

    lion = Lion("Simba", 8, "Male")
    lion.eat()
    lion.sleep()
    lion.move()
    lion.roar()

    tiger = Tiger("Stripe", 6, "Female")
    tiger.eat()
    tiger.sleep()
    tiger.move()
    tiger.growl()
