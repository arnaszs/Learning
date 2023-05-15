
from sqlalchemy.orm import sessionmaker
from modeliai import Order, Customer, Product, Status, OrderProduct, engine
# List'as; get'as; insert'as; update'as; delet'as:
Session = sessionmaker(bind=engine)
session = Session()

def options_list(class_):
    options = session.query(class_).all()
    for i in options:
        print(i, end=' ')


def create_customer():
    f_name = input("Vardas: ")
    l_name = input("Pavardė: ")
    email = input("Email: ")
    customer = Customer(f_name=f_name, l_name=l_name, email=email)
    session.add(customer)
    session.commit()
    print('Sukurta!\n')
    
def create_status():
    print('Egzistuojantys statusai:')
    options_list(Status)
    name = input("\nĮveskite naują statusą: ")
    status = Status(name=name)
    session.add(status)
    session.commit()
    print('Sukurta!\n')
    
   
def create_product():
    print('Esami produktai:')
    options_list(Product)
    name = input("\nPavadinimas: ")
    price = input("Kaina: ")
    product = Product(name=name, price=price)
    session.add(product)
    session.commit()
    print('Sukurta!\n')
    
  
def create_order():
    options_list(Customer)
    customer_id = input("\nKliento Id: ")
    order = Order(customer_id=customer_id, status_id=1)
    session.add(order)
    session.commit()
    last_order_id = session.query(Order).all()[-1].id
    print('Yra sandėlyje:')
    options_list(Product)
          
    product_id = input('\nProdukto Id: ')
    quantity = input('Kiekis: ')
    while True:
        if product_id and quantity:
            order_product = OrderProduct(order_id=last_order_id, product_id=product_id, quantity=quantity)
            session.add(order_product)
            session.commit()
        else:
            print('Sukurta!\n')
            break
    

def get_order():
    last_order_id = session.query(Order).all()[-1].id
    id_ = input(f'Užsakymo id (1-{last_order_id}): ') 
    order = session.query(Order).get(id_)
    order_lines = session.query(OrderProduct).filter_by(order_id=order.id)
    print(f'\nUžsakymas #{id_}, klientas - {order.customer.f_name} {order.customer.l_name}:')
    print('\nProduktas\tQty\tKaina\tSuma')
    total = 0
    for line in order_lines:
        print(f'{line.product.name}\t{line.quantity}\t{line.product.price}\t{line.quantity * line.product.price}')
        total += line.product.price * line.quantity
    print(f'\n\t\tTotal:\t{total}')
    print(f'\t\tStatus:\t{order.status.name}')

# Update status
def change_status():
    last_order_id = session.query(Order).all()[-1].id
    id_ = input(f'Užsakymo id (1-{last_order_id}): ') 
    order = session.query(Order).get(id_)
    options_list(Status)
    status_id = input('\nPaskirti statuso id:')
    order.status_id = status_id
    session.commit()


while True:
    choice = input('1 Pridėti pirkėją \n 2 Pridėti produktą \n 3 Pridėti statusą\
     \n 4 Pridėti užsakymą \n 5 Gauti užsakymą \n 6 Pakeisti statusą | 0 Quit\nPasirinkitę veiksmą: ')
    if choice == '1':
        create_customer()
    elif choice == '2':
        create_product()
    elif choice == '3':
        create_status()
    elif choice == '4':
        create_order()
    elif choice == '5':
        get_order()
    elif choice == '6':
        change_status()
    elif choice == '0':
        break
    else:
        print('Blogas pasirinkimas!')

session.close()
