#Mikael Josh Deang (MJ)
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
            print(f"Encoded password: {encoder(x)}\n")
        elif int(menu) == 2:
            y = input("Type in an 8 character password to decode: ")
            print(f"Decoded password: Decoder Function\n")
        elif int(menu) == 3:
            break
        else:
            print("That is not a valid option!\n")

