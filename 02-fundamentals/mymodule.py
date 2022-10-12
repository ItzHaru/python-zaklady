EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

def energie(hmotnost, SPEED_OF_LIGHT):
    '''
    Výpočet energie tělesa
    '''
    return hmotnost * SPEED_OF_LIGHT**2

def silaZ(hmotnost, EARTH_GRAVITY):
    '''
    Výpočet síly přitažlivosti Země na těleso
    '''
    return hmotnost * EARTH_GRAVITY

def silaM(hmotnost, MOON_GRAVITY):
    '''
    Výpočet síly přitažlivosti Měsíce na těleso
    '''
    return hmotnost * MOON_GRAVITY

def draha(SPEED_OF_SOUND, cas):
    '''
    Výpočet dráhy nadzvukové stíhačky
    '''
    return SPEED_OF_SOUND * cas


