first = float(input("Enter first num =>"))
sec = float(input("Enter Second num =>"))
opr = str(input("Enter opr (+, -, *, /) => "))

if opr == "+":
    total = first + sec
elif opr == "-":
    total = first - sec
elif opr == "*":
    total = first * sec
elif opr == "/":
    total = first / sec
else:
    total = str("Please Enter a Valid Opr") 

print (total) 
