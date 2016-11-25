from matgoview import *
from matgocard import *
"""
A class for making Player and Computer's Hand
"""
class Player:
    def __init__(self, name):
        self.__name=name
        self.__hand=[] # 패
        self.__montharrange=[[], [], [], [], [], [], [], [], [], [], [], []]
        self.__score=0 # 점수
        self.__go=0 # 고
        self.__fuck=0 # 뻑 / 3뻑시 승리
        self.__shake=0 # 흔듦
        self.__was_score=0
        self.__fuck_month=[]
    def get(self, card):
        self.__hand.append(card)
    def set_score(self, score):
        self.__score=score
    def set_was_score(self, score):
        self.__was_score=score
    def put(self, root, field):
        return self.__hand.pop(Reader.cardchoose(self.__hand,root, field, self.__hand)-1)
    def comput(self, num):
        if len(self.__hand)<=num: # 오류 방지용
            return self.__hand.pop(0)
        else:
            return self.__hand.pop(num)
    def sequence_arrange(self): # 정렬
        temp=[[], [], [], [], [], [], [], [], [], [], [], []]
        for k in self.__hand:
            for i in range(12):
                if int(k.month)-1==i:
                    temp[i].append(k)
        temp2=[]
        for k in range(12):
            for i in temp[k]:
                temp2.append(i)
        return temp2
    def hand_set(self, hand):
        self.__hand=hand
    def month_arrange(self): # 총통, 폭탄, 흔들기 확인용
        self.__montharrange=[[], [], [], [], [], [], [], [], [], [], [], []]
        for i in range(len(self.__hand)):
            for k in range(1, 13):
                if self.__hand[i].month==str(k):
                    self.__montharrange[k-1].append(self.__hand[i])
        return self.__montharrange
    @property 
    def go(self):
        self.__go+=1
    @property
    def go_display(self):
        return self.__go
    @property
    def fuck(self):
        self.__fuck+=1
    @property
    def fuck_display(self):
        return self.__fuck
    def fuck_month_add(self, plus):
        self.__fuck_month.append(plus)
    @property
    def fuck_month(self):
        return self.__fuck_month
    @property
    def shake(self):
        self.__shake+=1
    @property
    def shake_display(self):
        return self.__shake
    @property
    def hand(self):
        return self.__hand
    @property
    def score(self):
        return self.__score
    @property
    def was_score(self):
        return self.__was_score
    @property
    def name(self):
        return self.__name

class got(Player):
    def __init__(self, name):
        self.__name=name
        super().__init__(name)
        self.__waitcards=[]
        self.__gwang=[[], []] # 광, 비광
        self.__dan=[[], [], [], []] # 홍단, 청단, 초단, 단
        self.__animal=[[], []] # 고도리, 열끗, 쌍피열끗(열끗 선택시 여기로)
        self.__pee=[[], []] # 쌍피, 피, 쌍피열끗(쌍피 선택시 여기로)
    def check(self, card1):
        if(card1 not in self.__gwang[0] and card1 not in self.__gwang[1] and card1 not in self.__dan[0] and card1 not in self.__dan[1] and card1 not in self.__dan[2] and card1 not in self.__dan[3] and card1 not in self.__animal[0] and card1 not in self.__animal[1] and card1 not in self.__pee[0] and card1 not in self.__pee[1]):
            return False
        else:
            return True
    @property
    def gwang(self): # 리스트로 return됨
        return self.__gwang[0]
    @property
    def beegwang(self):
        return self.__gwang[1]
    # 광 개수 따질 때 if beegwang()!=[] 인 경우와 beegwang()==[]인 경우로 나누어 계산
    @property
    def reddan(self):
        return self.__dan[0]
    @property
    def bluedan(self):
        return self.__dan[1]
    @property
    def chodan(self):
        return self.__dan[2]
    @property
    def dan(self):
        return self.__dan[3]
    @property
    def godori(self):
        return self.__animal[0]
    @property
    def animal(self):
        return self.__animal[1]
    @property
    def doublepee(self):
        return self.__pee[0]
    @property
    def pee(self):
        return self.__pee[1]
    def doublepee_rob(self):
        return self.__pee[0].pop(0) 
    def pee_rob(self):
        return self.__pee[1].pop(0)
    def sort(self, cards, check):
        self.__waitcards=cards
        for i in range(len(self.__waitcards)):
            gcheck=True
            if self.__waitcards[i].special=="광":
                for k in range(i+1, len(self.__waitcards)):
                    if self.__waitcards[k]=="광" or self.__waitcards[k]=="비광":
                        gcheck=False
                if gcheck:
                    if len(self.__gwang[1])==0:
                        if len(self.__gwang[0])==2:
                            print("삼광")
                        if len(self.__gwang[0])==3:
                            print("사광")
                    else:
                        if len(self.__gwang[0])==1:
                            print("비삼광")
                        if len(self.__gwang[0])==2:
                            print("사광")
                        if len(self.__gwang[0])==3:
                            print("오광")
                self.__gwang[0].append(self.__waitcards[i])
            elif self.__waitcards[i].special=="비광":
                for k in range(i+1, len(self.__waitcards)):
                    if self.__waitcards[k]=="광" or self.__waitcards[k]=="비광":
                        gcheck=False
                if gcheck:
                    if len(self.__gwang[0])==2:
                        print("비삼광")
                    if len(self.__gwang[0])==3:
                        print("사광")
                    if len(self.__gwang[0])==4:
                        print("오광")
                self.__gwang[1].append(self.__waitcards[i])
            elif self.__waitcards[i].special=="홍단":
                if len(self.__dan[0])==2:
                    print("홍단")
                self.__dan[0].append(self.__waitcards[i])
            elif self.__waitcards[i].special=="청단":
                if len(self.__dan[1])==2:
                    print("청단")
                self.__dan[1].append(self.__waitcards[i])
            elif self.__waitcards[i].special=="초단":
                if len(self.__dan[2])==2:
                    print("초단")
                self.__dan[2].append(self.__waitcards[i])
            elif self.__waitcards[i].special=="단":
                self.__dan[3].append(self.__waitcards[i])
            elif self.__waitcards[i].special=="고도리":
                if len(self.__animal[0])==2:
                    print("고도리")
                self.__animal[0].append(self.__waitcards[i])
            elif self.__waitcards[i].special=="열끗":
                self.__animal[1].append(self.__waitcards[i])
            elif self.__waitcards[i].special =="쌍피열끗" and check:
                self.__animal[1].append(self.__waitcards[i])
            elif self.__waitcards[i].special=="쌍피":
                self.__pee[0].append(self.__waitcards[i])
            elif self.__waitcards[i].special=="피":
                self.__pee[1].append(self.__waitcards[i])
            elif self.__waitcards[i].special=="쌍피열끗" and not check:
                self.__pee[0].append(self.__waitcards[i])