choice = 0
flag = 1
index = 0
name = []
numbers = []
phone_books_index = [0]*30
phone_books_name = []
phone_books_numbers = []

while flag:
    print("--- 메뉴 ---")
    print("1. 전화번호 목록")
    print("2. 전화번호 등록")
    print("3. 전화번호 삭제")
    print("4. 전화번호 수정")
    print("5. 종료")
    choice = int(input(": "))

    if choice is 1: #목록
        for i in range(30):
            if phone_books_index[i] == 1:
                print(f"{i}.{phone_books_name[i], phone_books_numbers[i]}")
    if choice is 2: #등록
        index = -1
        print(f"{phone_books_index}")
        for i in range(30):
            if phone_books_index[i] == 0:
                index = i
                break

        if index < 0:
            print("더 이상 등록할 수 없습니다.")
        phone_books_name.append(index)
        phone_books_name[index] = input("이름 : ")
        phone_books_numbers.append(index)
        phone_books_numbers[index] = input("번호 : ")
        phone_books_index[index] = 1

    if choice is 3: #삭제
        index = int(input("삭제할 번호 (0~29) :"))
        if index < 0 or index >= 30:
            print("잘못된 번호입니다.")
        phone_books_index[index] = 0
        print("삭제가 완료되었습니다.")

    if choice is 4: #수정
        index = int(input("수정할 번호 (0~29) :"))
        if index < 0 or index >= 30:
            print("잘못된 번호입니다.")
        if phone_books_index[index] == 0:
            print("수정할 연락처가 없습니다.")
        phone_books_name.append(index)
        phone_books_name[index] = input("변경할 이름 : ")
        phone_books_numbers.append(index)
        phone_books_numbers[index] = input("변경할 번호 : ")
        phone_books_index[index] = 1

    if choice is 5: #종료
        print("서비스를 종료합니다 .")
        flag = 0