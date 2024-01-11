# 조인 캐릭서가 서버에 접속

class Sever:
    def __init__(self, channel, name, nick_name, pin):
        self.channel = channel
        self.name = name
        self.nick_name = nick_name
        self.pin = pin

    def join(self):
        print(f"서버 : {self.channel}, 이름:{self.name}, 아이디:{self.nick_name}, 비밀번호:{self.pin}")


class Item:
    def __init__(self, hp, mp, equipment, nommal):
        self.hp = hp
        self.mp = mp
        self.equipment = equipment
        self.nommal = nommal
    def inbentory(self):
        print(f"소비 : {self.hp,self.mp}")
        print(f"장비 : {self.equipment}")
        print(f"기타 : {self.nommal}")
naro_1 = Sever(channel="스카니아", name="나로", nick_name="한섭", pin="0000",)
warrior_1 = Sever(channel="엘리시움", name="전사", nick_name="홍길동", pin="1111")


naro_2 = Item(hp="hp포션*100", mp="mp포션*100", equipment="갑옷", nommal="달팽이껍질")
warrior_2 = Item(hp="하얀포션*100", mp="마나엘릭서", equipment="검", nommal="돼지의리본")

naro_1.join()
naro_2.inbentory()

warrior_1.join()
warrior_2.inbentory()



