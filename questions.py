#Asks a question and converts the answer to a string and returns it. If the answer is not a string it will throw an error and repeat itself.
def str_input(question):
    while True:
        try:
            x = str(input(question))
            return x
        except:
            print("Not an option. Try again!")
#Asks a question and converts the answer to a string and returns it. If the answer is not a integer it will throw an error and repeat itself.
def int_input(question):
    while True:
        try:
            x = int(input(question))
            return x
        except:
            print("Not a valid number. Try again!")
