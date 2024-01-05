# 다음 코드를 복사하여 윤석열나이 계산 프로그램을 만드세요.
# 부족한 부분을 채워 프로그램이 동작되도록 만들면 됩니다.

import datetime
your_year = 0
your_month = 0
your_day = 0
age =0

now = datetime.datetime.now()
now_year = 2024
now_month = 1
now_day = 5

print (f"now_year{now_year}")

your_year = int (input("너의 생년 :" ))
your_month = int (input("너의 월 :" ))
your_day = int (input("너의 일 :" ))

if now_month >= your_month and now_day >= your_day:
  age = now_year - your_year #연나이
  age -= 1
else:
  age = now_year - your_year
  age -= 2    #만나이
print(f"나이 : {age}")
