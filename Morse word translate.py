morse={
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":"."
}
text=input("Enter a text:").upper()
for letter in text:
    if letter in morse:
        print(morse[letter],end=" ")