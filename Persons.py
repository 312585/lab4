class Person:
    name = ''
    age = 0
    power = 0
    instrument = None

    def __init__(self, name, age, power):
        self.age = age
        self.power = power
        self.name = name

    def take_instrument(self, instrument):
        self.instrument = instrument
        self.instrument.owner = self.name

    def play(self):
        self.instrument.add_info()
        self.instrument.make_sound()

    def play_instrument(self):
        if self.instrument is None:
            print("How should " + self.name + " play without any instrument???")
        else:
            if self.power > self.instrument.weight:
                self.play()
            else:
                print("Instrument is too heavy, " + self.name + " cant even play on this")

    def show_info(self):
        print('Person`s name:' + self.name)
        print('Person`s age:' + str(self.age))
        print('Person`s power:' + str(self.power))
        if self.instrument is not None:
            print('Person`s instrument:' + str(self.instrument.name))


class Professional(Person):
    def __init__(self, name, age, power, experience):
        Person.__init__(self, name, age, power)
        self.experience = experience

    def play(self):
        if self.experience < 5:
            print("Oh " + self.name + "has " + str(self.experience) + " years of experience, it wold be easy for "
                                                                      "him/her")
        else:
            print("Oh " + self.name + "has " + str(
                self.experience) + " years of experience, he/she can play even with closed eyes")
        self.instrument.add_info()
        self.instrument.make_sound()

    def show_info(self):
        Person.show_info(self)
        print('Professional`s experience:' + str(self.experience))


class Beginner(Person):
    def __init__(self, name, age, power, wish):
        Person.__init__(self, name, age, power)
        self.wish = wish

    def play(self):
        if self.wish < 5:
            print("Oh " + self.name + " don't want to play very much, so he/she will not")
        else:
            print("Oh " + self.name + " wants to play so much, lets listen")
            self.instrument.add_info()
            self.instrument.make_sound()

    def show_info(self):
        Person.show_info(self)
        print('Beginner`s wish:' + str(self.wish))
