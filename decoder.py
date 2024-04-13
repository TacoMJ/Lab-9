#William Ezequelle
def decoder(password):
    decoding = ""
    for i in password:
        temp_decoding = int(i)
        temp_decoding -= 3
        temp_decoding %= 10
        temp_decoding = str(temp_decoding)
        decoding += temp_decoding
    return decoding