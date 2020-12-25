class Instrument:
    def __init__(self, name, height, width, material, loudness, weight):
        self.name = name
        self.height = height
        self.width = width
        self.material = material
        self.loudness = loudness
        self.weight = int(weight)
        self.owner = ''

    def make_sound(self):
        print("Basic instrumental sound - to doooooo to doooooo")

    def add_info(self):
        if self.loudness < 10:
            print(self.name + " will play quietly")
        elif self.loudness > 20:
            print(self.name + " will play loudly")
        else:
            print(self.name + " will play medium volume")

    def show_info(self):
        print('Instrument`s name:' + self.name)
        print('Instrument`s height:' + str(self.height))
        print('Instrument`s width:' + str(self.width))
        print('Instrument`s material:' + self.material)
        print('Instrument`s loudness:' + str(self.loudness))
        print('Instrument`s weight:' + str(self.weight))
        print('Instrument`s owner:' + self.owner)


class StringInstrument(Instrument):
    def __init__(self, name, height, width, material, loudness, weight, strings):
        Instrument.__init__(self,name, height, width, material, loudness, weight)
        self.strings = int(strings)

    def make_sound(self):
        print("very beautiful string sounds - trun trun")

    def add_info(self):
        Instrument.add_info(self)
        if self.strings < 5:
            print(self.name + " has " + str(self.strings) + " strings, it will be easy to play")
        elif self.strings > 10:
            print(self.name + " has " + str(self.strings) + " strings, how to play it???")
        else:
            print(self.name + " has " + str(self.strings) + " strings, it would be fine")

    def show_info(self):
        Instrument.show_info(self)
        print('Instrument`s strings:' + str(self.strings))


class DrumInstrument(Instrument):
    def __init__(self, name, height, width, material, loudness, drums, weight):
        Instrument.__init__(self,name, height, width, material, loudness, weight)
        self.drums = int(drums)

    def make_sound(self):
        print("very beautiful drum sounds - bom bom")

    def add_info(self):
        Instrument.add_info(self)
        if self.drums < 5:
            print(self.name + " has " + str(self.drums) + " drums, it will be easy to play")
        elif self.drums > 10:
            print(self.name + " has " + str(self.drums) + " drums, how to play it???")
        else:
            print(self.name + " has " + str(self.drums) + " drums, it would be fine")

    def show_info(self):
        Instrument.show_info(self)
        print('Instrument`s drums:' + str(self.drums))


class KeyInstrument(Instrument):
    def __init__(self, name, height, width, material, loudness, keys, weight):
        Instrument.__init__(self, name, height, width, material, loudness, weight)
        self.keys = int(keys)

    def make_sound(self):
        print("very beautiful key sounds - tik tok")

    def add_info(self):
        Instrument.add_info(self)
        if self.keys < 10:
            print(self.name + " has " + str(self.keys) + " keys, even a child can play")
        elif self.keys > 30:
            print(self.name + " has " + str(self.keys) + " keys, am I Mozart???")
        else:
            print(self.name + " has " + str(self.keys) + " keys, it's going to be fun")

    def show_info(self):
        Instrument.show_info(self)
        print('Instrument`s keys:' + str(self.keys))