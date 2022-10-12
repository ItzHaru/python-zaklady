import mymodule as physics

EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

print("Energie tělesa o hmotnosti 15kg je " + str(physics.energie(15, SPEED_OF_LIGHT)) + "J")
print("Síla přitažlivosti Země na těleso o hmotnosti 20kg je " + str(round(physics.silaZ(20, EARTH_GRAVITY))) + "N")
print("Síla přitažlivosti Měsíce na těleso o hmotnosti 35kg je " + str(physics.silaM(35, MOON_GRAVITY)) + "N")
print("Délka dráhy nadzvukové stíhačky, kterou urazila za 5 sekund je " + str(physics.draha(5, SPEED_OF_SOUND)) + "m")

