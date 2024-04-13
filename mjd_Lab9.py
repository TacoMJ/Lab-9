#Mikael Josh Deang (MJ)
from decoder import decoder
def encoder(password):
    new_password = ''
    for num in password:
        num = int(num)
        num = num + 3
        if num > 9:
            num = num % 10
        num = str(num)
        new_password = new_password + num

    return new_password

def main():
    i = 1
    while i > 0:
        print("Menu")
        print("----------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        menu = input("Please enter an option: ")
        if int(menu) == 1:
            x = input("Please enter your password to encode: ")
            encoded_password = encoder(x)
            print("Your password has been encoded and stored!\n")
        elif int(menu) == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decoder(encoded_password)}\n")
        elif int(menu) == 3:
            break
        else:
            print("That is not a valid option!\n")

if __name__ == "__main__":
    main()
