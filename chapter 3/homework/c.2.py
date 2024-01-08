MAX_SIZE = 30
score_book = []
def diplay(action):
    if action == "menu":
        print("----- 메뉴 -----")
        print("1. 성적 입력")
        print("2. 종료")
        try:
            c = int(input(": "))
        except ValueError:
            print("정수만 입력할 수 있습니다.")
        return c
def score_add():
    if len(score_book) == MAX_SIZE:
        print("더이상 저장할 수 없습니다.")

    score = int(input("점수 :"))
    print(score)
    if score <= 100 and score >= 0:
        score_book.append(score)
        print("등록이 완료되었습니다.")
    elif not score <= 100 and score >= 0:
        print("잘못 입력 하셨습니다.")
    return 0
def grade():
    score_book.sort(reverse=True)
    print(f"{score_book[0:4]}: A")
    print(f"{score_book[5:14]}: B")
    print(f"{score_book[15:24]}: C")
    print(f"{score_book[25:29]}: F")
    return 0

while True:

    choice = diplay("menu")
    if choice == 1:
        score_add()

    if choice == 2:
        print("입력한 점수의 등급")
        break
    elif not choice > 0 and choice < 3:
        print("잘못입력하셨습니다.")
        continue

grade()