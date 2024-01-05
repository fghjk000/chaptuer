x = 0
y = 0
z = 0
flag =1
x = int(input("변의 길이를 입력하시오 :"))
y = int(input("변의 길이를 입력하시오 :"))
z = int(input("변의 길이를 입력하시오 :"))
while flag:
    if z**2 == x**2 + y**2 or x**2 == y**2 + z**2 or y**2 == z**2 + x**2:
        print("right")
        break
    else:
        print("wrong")
        break