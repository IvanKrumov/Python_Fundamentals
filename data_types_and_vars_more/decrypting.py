key = int(input())
symbols = int(input())
decrypted_message = ''

for _ in range(symbols):
    char = input()
    decrypted_symbol = ord(char) + key
    decrypted_message += chr(decrypted_symbol)

print(decrypted_message)
