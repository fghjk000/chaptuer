choice = 0
score = 0
print("1.영어 모드 2.한글모드")
choice = int (input(':'))
if choice is 1:
    score = int(input('What your score? :'))
    if 100 >= score >= 90:
        print(f"A")
    elif 90 > score >= 80:
        print(f"B")
    elif 80 > score >= 70:
        print(f"C")
    elif 70 > score >= 0:
        print(f"F")
    else:
        print("error")

if choice is 2:
    score = int(input('점수를 입력하시오. :'))
    if 100 >= score >= 90:
        print(f"수")
    elif 90 > score >= 80:
        print(f"우")
    elif 80 > score >= 70:
        print(f"미")
    elif 70 > score >= 0:
        print(f"양")
    else:
        print("오류")
