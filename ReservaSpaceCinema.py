# Mostrar b1, b2, b3, b4.... até o b10
# E dai a pessoa vai reservando a cadeira que ela quer (ela pode reservar mais de 1 vez)
# Dai se ela querer reservar uma cadeira ja reserva se vai mostrar um error.
chairs_available = ['| B1 |', ' B2 |', ' B3 |', ' B4 |', ' B5 |', ' B6 |', ' B7 |', ' B8 |', ' B9 |', ' B10 |']
def is_available(cp):
    if chairs_available[cp-1] != ' --- |':
        return 'True'
    elif chairs_available[cp-1] == ' --- |':
        return 'False'
def chairs(chair): 
    if chair == 'none':
        for c in range(0, len(chairs_available)):
            print(chairs_available[c], end='')
    elif chair != 'none':
        for cn in range(0, 10):
            if chair == cn:
                if is_available(cn) == 'True':
                    chairs_available[chair-1] = ' --- |'
                elif is_available(cn) == 'False':
                    print('Esta cadeira não está disponivel!!')
                    return 'break'

while True:
    chairs('none')
    while True:
        char_cinema = int(input('\nQual cadeira você escolhe? B'))
        if char_cinema >= 1 and char_cinema <= 10:
            break
    if chairs(char_cinema) == 'break':
        break
