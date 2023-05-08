import pickle

class Fridge():
    def __init__(self):
        self.fridge = {}
        
    def add_groceries(self, product, weight):
        if product in self.fridge:
            self.fridge[product] += weight
        else:
            self.fridge[product] = weight
        return self.fridge
    
    def subtract_groceries(self, product, weight):
        if product in self.fridge:
            if self.fridge[product] >= weight:
                self.fridge[product] -= weight
                if self.fridge[product] == 0:
                    del self.fridge[product]
            else:
                print('Error: Not enough of {} in fridge'.format(product))
        else:
            print('Error: {} not found in fridge'.format(product))

    def all_weight(self):
        fridge_weight = sum(self.fridge.values())
        return fridge_weight
    
    def products_in_fridge(self):
        return self.fridge

print('---Menu---')
print('1 - Add groceries')
print('2 - Take out product')
print('3 - Prints the weight of the Fridges products')
print('4 - Shows you whats inside the fridge')
print('5 - Save fridge')
print('0 - Exit')

my_fridge = Fridge()

while True:
    choice = input('Your choice: ')
    if choice == '1':
        product = input('Enter product name: ')
        weight = float(input('Enter weight in kg: '))
        my_fridge.add_groceries(product, weight)
        print(my_fridge.fridge)
    elif choice == '2':
        product = input('Enter product name: ')
        weight = float(input('Enter weight in kg: '))
        my_fridge.subtract_groceries(product, weight)
        print(my_fridge.fridge)
    elif choice == '3':
        print('The total weight of the fridge is:', my_fridge.all_weight())
    elif choice == '4':
        print(my_fridge)
    elif choice == '5':
        with open('fridge.pickle', 'wb') as f:
            pickle.dump(my_fridge, f)
            print('Fridge saved to file')
    elif choice == '0':
        print('GoodBye')
        break
    else:
        print('Invalid choice')

    
        