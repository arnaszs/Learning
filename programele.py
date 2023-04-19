import os
os.system('cls')


class Bank:
    def __init__(self, savininkas, saskaitos_numeris, balansas, pin_kodas=4303):
        self.saskaitos_numeris = saskaitos_numeris
        self.savininkas = savininkas
        self.__balansas = balansas
        self.__pin_kodas = pin_kodas

        while True:
            print('----- Menu -----')
            print('1: Saskaitos likutis')
            print('2: Nusiimti pinigų')
            print('3: Įsidėti pinigų')
            print('9: Palikti bankomatą nes neturi pinigų LOL')

            pasirinkimas = int(input('Įrašykite savo pasirinkimą: '))

            if pasirinkimas == 1:
                os.system('cls')
                print('Jūsų saskaitoje yra:')
                print(self.__balansas)

            elif pasirinkimas == 2:
                os.system('cls')
                kiek = int(input('Kiek pinigų norite išimti: '))
                self.sumazinti(kiek)

            elif pasirinkimas == 3:
                os.system('cls')
                kiek = int(input('Kiek pinigų norite įdėti: '))
                self.papildyti(kiek)

            elif pasirinkimas == 9:
                os.system('cls')
                print('Viso gero!')
                break

    def sumazinti(self, kiek):
        kodas = int(input('Įrašykite pin kodą: '))
        if kodas == self.__pin_kodas:
            self.__balansas -= kiek
            print(f'{kiek} EU buvo sekmingai nuskaityta iš jūsų sąskaitos, dabartinis likutis {self.__balansas}')
        else:
            raise ValueError('Neteisingas pin kodas')
        return


    def papildyti(self, kiek):
        # Priverstinai įvesti pin kodą
        kodas = int(input('Įrašykite pin kodą: '))
        if kodas == self.__pin_kodas:
            self.__balansas += kiek
            print(f'{kiek} EU buvo sekmingai pridėta į jūsų sąskaitą, dabartinis likutis {self.__balansas}')
        else:
            raise ValueError('Neteisingas pin kodas')
        return


saskaita = Bank('Arnas', 'LT123456789', 3670)