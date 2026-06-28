print("1.Rectangle")
print("2.Circle")

choice=input("choice=")

if choice== "1":
 length= int(input("Enter a length:"))
 width=int( input("Enter a breadth"))
 print("Area= ",length * width)

elif choice =="2":
 radius=int(input("Enter a radius="))
 print("Area=",3.14 * radius *radius)
