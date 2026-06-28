year=int(input("Enter a yr:"))
if year %400 ==0:
    print("Leap Year")
elif year % 100==0:
    print("Not leap year by")
elif year % 4 ==0:
    print("Leap Year by 4")
else:
    print("Not leap year")