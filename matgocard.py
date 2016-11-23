import random

"""
Card class
"""
# Card class
class Card:  
    __special = ("광","비광","초단","청단","홍단","단","열끗","쌍피","피","고도리","쌍피열끗","폭탄")
    __month = ("1","2","3","4","5","6","7","8","9","10","11","12")

    def __init__(self, special, month, face_up = True, img = None):
        self.__special = special
        self.__month = month
        self.__face_up = face_up
        self.__img = img
    
    @staticmethod
    def fresh_deck():
        cards = []
        for i in Card.__special:
            for k in Card.__month:
                if i == "광" and (k =="1" or k =="3" or k =="8" or k =="11"):
                    cards.append(Card(i,k,False,k+"_"+i+".png"))
                if i == "비광" and (k == "12"):
                    cards.append(Card(i,k,False,k+"_"+i+".png"))            
                if i == "초단" and (k =="4" or k =="5" or k =="7"):
                    cards.append(Card(i,k,False,k+"_"+i+".png"))             
                if i == "청단" and (k =="6" or k =="9" or k =="10"):
                    cards.append(Card(i,k,False,k+"_"+i+".png"))                     
                if i == "홍단" and (k =="1" or k =="2" or k =="3"):
                    cards.append(Card(i,k,False,k+"_"+i+".png"))
                if i == "단" and (k =="12"):
                    cards.append(Card(i,k,False,k+"_"+i+".png"))
                if i == "고도리" and (k == "2" or k =="4" or k =="8"):
                    cards.append(Card(i,k,False,k+"_"+i+".png"))
                if i == "쌍피열끗" and (k == "9"):
                    cards.append(Card(i,k,False,k+"_"+i+".png"))
                if i == "열끗" and (k =="5" or k =="6" or k =="7" or k =="10" or k =="12"):
                    cards.append(Card(i,k,False,k+"_"+i+".png"))              
                if i == "쌍피" and (k =="11" or k =="12"):
                    cards.append(Card(i,k,False,k+"_"+i+".png"))                
                if i == "피" and k != "12":
                    cards.append(Card(i,k,False,k+"_"+i+"1"+".png"))
                    cards.append(Card(i,k,False,k+"_"+i+"2"+".png"))
        random.shuffle(cards)
        return cards

    def flip(self):
      self.__face_up = not self.__face_up

    def __str__(self):
        if self.__face_up:
            if self.__special!="폭탄":
                return self.__month + "." + self.__special
            else:
                return self.__special
        else:
            return "XXX" + "." + "XX"

    @property
    def special(self):
        return self.__special

    @property
    def month(self):
        return self.__month

    @property
    def face_up(self):
        return self.__face_up
    @property
    def img(self):
        return str(self.__img)

"""
Deck class
"""
# Deck class
class Deck:
    def __init__(self):
        self.__deck = Card.fresh_deck()

    def next(self, open=True):
        card = self.__deck.pop()
        if open :
            card.flip()
        return card

    @property
    def check(self):
        return self.__deck[-1]

    @property
    def current(self):
        return self.__deck