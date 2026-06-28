text=input("Enter message: ")
shift = 3

encrypted = ""

for char in text:
    if char.isalpha():
        new=chr(ord(char)+shift)
        encrypted +=new
    else:
        encrypted += char

print("Encrypted=",encrypted)    