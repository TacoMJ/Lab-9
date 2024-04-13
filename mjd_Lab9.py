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
        print("----")
        print("1. Encoder")
        print("2. Decoder")
        print("3. Exit Program")
        menu = input("Choose an option: ")
        if int(menu) == 1:
            x = input("Type in an 8 character password to encode: ")
            encoded_password = encoder(x)
            print(f"Encoded password: {encoder(x)}\n")
        elif int(menu) == 2:
            print(f"Decoded password: {decoder(encoded_password)}\n")
        elif int(menu) == 3:
            break
        else:
            print("That is not a valid option!\n")

if __name__ == "__main__":
    main()
