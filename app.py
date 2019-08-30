from json import load
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


def dog_spa():
    print_welcome_message()


if __name__ == '__main__':
    dog_spa()
