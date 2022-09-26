def q1():
    cislo = input("2 x 2 + 3 + 3 x 0 = ")
    c = eval(cislo)
    if c == 7:
        print('Správně :)')
    else:
        print('Špatně :(')

def q2():
    cislo = input("0 + 4 : 2 + 5 x 3 - 10 = ")
    c = eval(cislo)
    if c == 7:
        print(c, 'je správně :)')
    else:
        print(c, 'je špatně :(')

def q3():
    x = input('Zadej hodnotu x: ')
    y = input('Zadej hodnotu y: ')
    x1 = eval(x)
    y1 = eval(y)
    print('Hodnota x = {} a y = {}'.format(x1, y1))

def q4():
    cislo1 = input('Zadej první číslo: ')
    cislo2 = input('Zadej druhé číslo: ')
    cislo3 = input('Zadej třetí číslo: ')
    c1 = eval(cislo1)
    c2 = eval(cislo2)
    c3 = eval(cislo3)
    print('Čísla, která jste zadali:', end=' ')
    print(c1, c2, c3, sep=',')

def q5():
    cislo = input('Zadej desetinné číslo: ')
    c1 = eval(cislo)
    print('Hodnota čísla na 2 desetinná místa: %3.2f' %c1)

def q6():
    prijmeni = input('Zadej prijmeni: ')
    jmeno = input('Zadej jméno: ')
    print('{1}{0}'.format(jmeno, prijmeni))

def vypis():
    print('Tohle je {jaky} formulář a {ano} mě'.format(jaky='zábavný', ano='baví'))

q1()
q2()
q3()
q4()
q5()
q6()
vypis()





