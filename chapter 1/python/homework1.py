num_1 = 0
num_2 = 0
num_3 = 0
choice = 0
print("---메뉴---")
print("1.덧셈")
print("2.뺄셈")
print("3.곱셈")
print("4.나눗셈 (주의 : 0으로 나눌시 종료됩니다.)")
print("5.나머지 (주의 : 0으로 나눌시 종료됩니다.)")
choice = int(input(':'))
num_1 = int (input('첫번째 숫자를입력하세요. :'))
num_2 = int (input('두번째 숫자를입력하세요. :'))

if choice == 1:
    num_1 = num_1 + num_2
    print(f": {num_1}")
if choice == 2:
    num_1 = num_1 - num_2
    print(f": {num_1}")
if choice == 3:
    num_1 = num_1 * num_2
    print(f": {num_1}")
if choice == 4 and num_2 != 0:
    num_1 = num_1 / num_2
    print(f": {num_1}")
if choice == 5 and num_2 != 0:
    num_1 = num_1 % num_2
    print(f": {num_1}")