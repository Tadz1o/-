a = int(input("ВВедите число "))

sum = 0
while a != 0:
    last = a % 10
    sum += last
    a//=10
print(sum)


