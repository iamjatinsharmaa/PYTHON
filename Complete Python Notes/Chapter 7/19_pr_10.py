a=int(input("Enter The Number: "))
a_range=range(0,11)
reverserange=reversed(a_range)
for i in reverserange:
    print(f"{i}*{a}={i*a}")