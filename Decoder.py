def displayMenu():
    print('''
Menu
-------------
1. Encode
2. Decode
3. Quit
              
''')
<<<<<<< HEAD
        self.captureInput()
    def captureInput(self):
        options = [1, 2, 3]
        while True:
            menuOptionSelected = input("Please enter an option: ")
            try:
                int(menuOptionSelected)
                break
            except:
                continue
        self.executeOption(int(menuOptionSelected))
    def executeOption(self, option):
        match option:
            case 1:
                self.getPassword()
                self.encodedPassword = self.encode(self.password)
                self.displayMenu()
=======
    captureInput()


def captureInput():
    options = [1, 2, 3]
    while True:
        menuOptionSelected = input("Please enter an option: ")
        try:
            int(menuOptionSelected)
            break
        except:
            continue
    executeOption(int(menuOptionSelected))


def executeOption(option):
    if option == 1:
        getPassword()
        global encodedPassword
        encodedPassword = encode(password)
        displayMenu()
    elif option == 2:
        decode()
        displayMenu()
>>>>>>> 76ad663 (bugged code works now.)


def getPassword():
    while True:
        try:
            global password
            password = int(input("Please enter your password to encode: "))
            break
        except: 
            print("Invalid input")


def encode(password):
    stringPassword = str(password)
    lengthPassword = len(stringPassword)
    newString = ""
    for i in range(lengthPassword): 
        newString += str(int(stringPassword[i]) + 3)
    return int(newString)

<<<<<<< HEAD
instance = Main()
=======

def decode():
    global encodedPassword
    lengthPassword = len(str(encodedPassword))
    stringPassword = str(encodedPassword)
    newString = ""
    for i in range(lengthPassword):
        newString += str(int(stringPassword[i]) - 3)
    print(f"The encoded password is {encodedPassword}, and the original password is {int(newString)}")


if __name__ == '__main__':
    displayMenu()

>>>>>>> 76ad663 (bugged code works now.)
