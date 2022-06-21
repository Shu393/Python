def calc(number1,operation="/",number2=5):
    if operation == "/":
        return number1//number2
    if operation == "*":
        return number1*number2
    if operation == "**":
        return number1**number2
ans=0
ans = calc(3)

print(ans)