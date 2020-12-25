from instruments import *
from Persons import *

guitar = StringInstrument("guitar", 1.2, 0.5, "wood", 10, 10, 6)
Daniel = Professional("Daniel", 18, 20, 7)
Daniel.play_instrument()
Daniel.take_instrument(guitar)
Daniel.play_instrument()
Daniel.show_info()
guitar.show_info()
