choice = 0
Balance =0
flag = 1
num_1 = 0

while flag:
    print("--- 메뉴 ---")
    print("1. 입금 2. 출금 3. 잔액 조회 4. 종료")
    choice = int(input(": "))

    if choice is 1:
        num_1 = int(input("입금할 금액 :"))
        if num_1 >= 0:
            Balance = Balance + num_1
            print("입금이 완료되었습니다.")
            print(f"현재잔액은{Balance}원입니다.")
        else:
            print("잘못 입력하셨습니다.")
            num_1 = 0
    if choice is 2:
        num_1 = int(input("출금할 금액 :"))
        if num_1 >= 0:
            if Balance > num_1:
                Balance = Balance - num_1
                print("출금이 완료 되었습니다.")
                print(f"현재잔액은{Balance}원입니다.")
            else:
                print("잘못입력 하셨습니다.")
        else:
            print("잘못입력 하셨습니다.")
    if choice is 3:
        print(f"현재잔액은 {Balance}원 입니다.")
    if choice is 4:
        print("서비스를 종료합니다.")
        flag = 0