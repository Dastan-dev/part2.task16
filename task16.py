a = float(input('enter your weight:'))
b=int(input('enter year:'))
result = a*0.165
for x in range(0,b+1):
    y=x*0.165+result
    print(y)
