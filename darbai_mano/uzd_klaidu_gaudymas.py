
while True:
    try:
        skaicius = float(input('Įveskite skaičių: '))
        if skaicius < 0:
            raise ValueError('Įvestas skaičius yra neigiamas')
        else:
            print(f'Ačiū, jūs įvedėte: {skaicius}')
            break
    except ValueError as error:
        print('Klaida', error)