from json import load
from datetime import datetime
# Import modules here!

SERVICES_FILENAME = "./services.json"
TRANSACTIONS_FILENAME = "./transactions.txt"


def print_welcome_message():
    print("""
                         .--~~,__
            :-....,-------`~~'._.'
            `-,,,  ,_      ;'~U'
            _,-' ,'`-__; '--.
            (_/'~~      ''''(;
 WELCOME TO LUXURY DOG SERVICES!
    """)


def load_services(filename):
    with open(filename, 'r') as file:
        json_services = load(file)
    return json_services['services']


def print_services(services):
    print("These are the services we offer:")
    for key, value in services.items():
        price = value.get('price')
        number_of_dots = 20 - len(key) - len(str(price))
        print("\t{}{}${:.2f}".format(
            key, '.' * number_of_dots, price))
    print('Which service would you like to order today?\n')


def get_service(keys):
    while True:
        choice = input('>>> ').lower().strip()
        if choice in keys:
            return choice
        print(choice, "is an invalid option!")


def save_transaction(filename, service):
    line = f"\n{datetime.now()}, {service['name']}, {service['price']}"
    with open(filename, 'a') as file:
        file.write(line)


def dog_spa():
    print_welcome_message()
    services = load_services(SERVICES_FILENAME)
    print_services(services)
    service_name = get_service(services.keys())
    print(service_name.title(), 'such a good choice!')
    print('Your total is: ${:.2f}'.format(services[service_name]['price']))
    save_transaction(TRANSACTIONS_FILENAME, services[service_name])
    print("Thank you have a nice day!")


if __name__ == '__main__':
    dog_spa()
