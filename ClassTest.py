class Enemy:
    life = 3

    def attack(self):
        print("ouch!")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")


# Making an object.
# Objects are a way to access the stuff inside a class
# An object is a copy of the class (instans?)

enemy1 = Enemy()

enemy1.attack()
enemy1.checkLife()
enemy1.attack()
enemy1.checkLife()
