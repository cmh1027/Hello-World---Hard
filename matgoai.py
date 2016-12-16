import random
from matgocard import *
from matgohand import *
class AI:
	def __init__(self, ai):
		self.__ai=ai
	def cardchoose(self, aiobject, playerobject, field, deck):
		self.__deck=deck
		self.__aiobject=aiobject
		self.__playerobject=playerobject
		self.__field=field
		if True:
			for k in range(12):
				if len(field[k])==2:
					for i in range(len(aiobject.hand)):
						if deck.check.month==aiobject.hand[i].month==field[k][0].month:
							return i
			next=[]
			for k in range(12):
				if len(field[k])>0:
					if field[k][0].month==deck.check.month:
						next.append(deck.check)
						next.append(field[k])
			if next!=[]:
				if self.deck_and(next, "고도리", "초단") and len(aiobject.godori)==2 and len(aiobject.chodan)==2: # 8점 // 아무거나 내도 됨(뻑제외)
					for k in range(len(aiobject.hand)):
						if aiobject.hand[k].month!=next[0].month:
							return k
				if self.deck_and(next, "고도리", "피") and len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4 and \
				len(aiobject.pee)+2*len(aiobject.doublepee)>=9: # 7점 // 아무거나
					for k in range(len(aiobject.hand)):
						if aiobject.hand[k].month!=next[0].month:
							return k
				if self.deck_and(next, "고도리", "피") and len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)<4 and \
				len(aiobject.pee)+2*len(aiobject.doublepee)>=9: # 6점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
						if self.cardchoose_condition2("열끗", "청단")[0]:
							return self.cardchoose_condition2("열끗", "청단")[1]
						if self.cardchoose_condition2("열끗", "초단")[0]:
							return self.cardchoose_condition2("열끗", "초단")[1]
						if self.cardchoose_condition2("열끗", "단")[0]:
							return self.cardchoose_condition2("열끗", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "홍단")[0]:
							return self.cardchoose_condition2("피", "홍단")[1]
						if self.cardchoose_condition2("피", "청단")[0]:
							return self.cardchoose_condition2("피", "청단")[1]
						if self.cardchoose_condition2("피", "초단")[0]:
							return self.cardchoose_condition2("피", "초단")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "열끗")[0]:
							return self.cardchoose_condition2("피", "열끗")[1]
						if self.cardchoose_condition2("피", "고도리")[0]:
							return self.cardchoose_condition2("피", "고도리")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]						
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]
						if self.cardchoose_bicondition("피")[0]:
							return self.cardchoose_bicondition("피")
					if len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
						if self.cardchoose_condition("열끗")[0]:
							return self.cardchoose_condition("열끗")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
						if self.cardchoose_condition("단")[0]:
							return self.cardchoose_condition("단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]				
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition("피")[0]:
							return self.cardchoose_condition("피")[1]
				if self.deck_and(next, "고도리", "피") and len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4 and \
				len(aiobject.pee)+2*len(aiobject.doublepee)<9: # 6점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
						if self.cardchoose_condition2("열끗", "청단")[0]:
							return self.cardchoose_condition2("열끗", "청단")[1]
						if self.cardchoose_condition2("열끗", "초단")[0]:
							return self.cardchoose_condition2("열끗", "초단")[1]
						if self.cardchoose_condition2("열끗", "단")[0]:
							return self.cardchoose_condition2("열끗", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "홍단")[0]:
							return self.cardchoose_condition2("피", "홍단")[1]
						if self.cardchoose_condition2("피", "청단")[0]:
							return self.cardchoose_condition2("피", "청단")[1]
						if self.cardchoose_condition2("피", "초단")[0]:
							return self.cardchoose_condition2("피", "초단")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "열끗")[0]:
							return self.cardchoose_condition2("피", "열끗")[1]
						if self.cardchoose_condition2("피", "고도리")[0]:
							return self.cardchoose_condition2("피", "고도리")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]						
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]
						if self.cardchoose_bicondition("피")[0]:
							return self.cardchoose_bicondition("피")
					if len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
						if self.cardchoose_condition("열끗")[0]:
							return self.cardchoose_condition("열끗")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
						if self.cardchoose_condition("단")[0]:
							return self.cardchoose_condition("단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]				
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition("피")[0]:
							return self.cardchoose_condition("피")[1]
				if self.deck_and(next, "고도리", "피") and len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)<4 and \
				len(aiobject.pee)+2*len(aiobject.doublepee)<9: # 5점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
						if self.cardchoose_condition2("열끗", "청단")[0]:
							return self.cardchoose_condition2("열끗", "청단")[1]
						if self.cardchoose_condition2("열끗", "초단")[0]:
							return self.cardchoose_condition2("열끗", "초단")[1]
						if self.cardchoose_condition2("열끗", "단")[0]:
							return self.cardchoose_condition2("열끗", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "홍단")[0]:
							return self.cardchoose_condition2("피", "홍단")[1]
						if self.cardchoose_condition2("피", "청단")[0]:
							return self.cardchoose_condition2("피", "청단")[1]
						if self.cardchoose_condition2("피", "초단")[0]:
							return self.cardchoose_condition2("피", "초단")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "열끗")[0]:
							return self.cardchoose_condition2("피", "열끗")[1]
						if self.cardchoose_condition2("피", "고도리")[0]:
							return self.cardchoose_condition2("피", "고도리")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]						
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]
						if self.cardchoose_bicondition("피")[0]:
							return self.cardchoose_bicondition("피")[1]
				if self.deck_and(next, "초단", "열끗") and len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 5점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
						if self.cardchoose_condition2("열끗", "청단")[0]:
							return self.cardchoose_condition2("열끗", "청단")[1]
						if self.cardchoose_condition2("열끗", "초단")[0]:
							return self.cardchoose_condition2("열끗", "초단")[1]
						if self.cardchoose_condition2("열끗", "단")[0]:
							return self.cardchoose_condition2("열끗", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "홍단")[0]:
							return self.cardchoose_condition2("피", "홍단")[1]
						if self.cardchoose_condition2("피", "청단")[0]:
							return self.cardchoose_condition2("피", "청단")[1]
						if self.cardchoose_condition2("피", "초단")[0]:
							return self.cardchoose_condition2("피", "초단")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "열끗")[0]:
							return self.cardchoose_condition2("피", "열끗")[1]
						if self.cardchoose_condition2("피", "고도리")[0]:
							return self.cardchoose_condition2("피", "고도리")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]						
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]
						if self.cardchoose_bicondition("피")[0]:
							return self.cardchoose_bicondition("피")[1]
				if self.deck_and(next, "초단", "열끗") and len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 4점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
				if self.deck_and(next, "초단", "열끗") and len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)<4 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 4점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
				if self.deck_and(next, "초단", "열끗") and len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)<4 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 3점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
				if self.deck_and(next, "청단", "열끗") and len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 5점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
						if self.cardchoose_condition2("열끗", "청단")[0]:
							return self.cardchoose_condition2("열끗", "청단")[1]
						if self.cardchoose_condition2("열끗", "초단")[0]:
							return self.cardchoose_condition2("열끗", "초단")[1]
						if self.cardchoose_condition2("열끗", "단")[0]:
							return self.cardchoose_condition2("열끗", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "홍단")[0]:
							return self.cardchoose_condition2("피", "홍단")[1]
						if self.cardchoose_condition2("피", "청단")[0]:
							return self.cardchoose_condition2("피", "청단")[1]
						if self.cardchoose_condition2("피", "초단")[0]:
							return self.cardchoose_condition2("피", "초단")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "열끗")[0]:
							return self.cardchoose_condition2("피", "열끗")[1]
						if self.cardchoose_condition2("피", "고도리")[0]:
							return self.cardchoose_condition2("피", "고도리")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]
						if self.cardchoose_bicondition("피")[0]:
							return self.cardchoose_bicondition("피")[1]
				if self.deck_and(next, "청단", "열끗") and len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 4점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
				if self.deck_and(next, "청단", "열끗") and len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)<4 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 4점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
				if self.deck_and(next, "청단", "열끗") and len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)<4 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 3점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
				if self.deck_and(next, "홍단", "피") and len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 5점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
						if self.cardchoose_condition2("열끗", "청단")[0]:
							return self.cardchoose_condition2("열끗", "청단")[1]
						if self.cardchoose_condition2("열끗", "초단")[0]:
							return self.cardchoose_condition2("열끗", "초단")[1]
						if self.cardchoose_condition2("열끗", "단")[0]:
							return self.cardchoose_condition2("열끗", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "홍단")[0]:
							return self.cardchoose_condition2("피", "홍단")[1]
						if self.cardchoose_condition2("피", "청단")[0]:
							return self.cardchoose_condition2("피", "청단")[1]
						if self.cardchoose_condition2("피", "초단")[0]:
							return self.cardchoose_condition2("피", "초단")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "열끗")[0]:
							return self.cardchoose_condition2("피", "열끗")[1]
						if self.cardchoose_condition2("피", "고도리")[0]:
							return self.cardchoose_condition2("피", "고도리")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]
						if self.cardchoose_bicondition("피")[0]:
							return self.cardchoose_bicondition("피")[1]
				if self.deck_and(next, "홍단", "피") and len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 4점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
				if self.deck_and(next, "홍단", "피") and len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)<9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 4점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
				if self.deck_and(next, "홍단", "피") and len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)<9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 3점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
				if self.deck_and(next, "초단", "피") and len(aiobject.chodan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 5점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
						if self.cardchoose_condition2("열끗", "청단")[0]:
							return self.cardchoose_condition2("열끗", "청단")[1]
						if self.cardchoose_condition2("열끗", "초단")[0]:
							return self.cardchoose_condition2("열끗", "초단")[1]
						if self.cardchoose_condition2("열끗", "단")[0]:
							return self.cardchoose_condition2("열끗", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "홍단")[0]:
							return self.cardchoose_condition2("피", "홍단")[1]
						if self.cardchoose_condition2("피", "청단")[0]:
							return self.cardchoose_condition2("피", "청단")[1]
						if self.cardchoose_condition2("피", "초단")[0]:
							return self.cardchoose_condition2("피", "초단")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "열끗")[0]:
							return self.cardchoose_condition2("피", "열끗")[1]
						if self.cardchoose_condition2("피", "고도리")[0]:
							return self.cardchoose_condition2("피", "고도리")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]
						if self.cardchoose_bicondition("피")[0]:
							return self.cardchoose_bicondition("피")[1]
				if self.deck_and(next, "초단", "피") and len(aiobject.chodan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 4점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
				if self.deck_and(next, "초단", "피") and len(aiobject.chodan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)<9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 4점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
				if self.deck_and(next, "초단", "피") and len(aiobject.chodan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)<9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 3점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
				if self.deck_and(next, "청단", "피") and len(aiobject.bluedan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 5점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
						if self.cardchoose_condition2("열끗", "청단")[0]:
							return self.cardchoose_condition2("열끗", "청단")[1]
						if self.cardchoose_condition2("열끗", "초단")[0]:
							return self.cardchoose_condition2("열끗", "초단")[1]
						if self.cardchoose_condition2("열끗", "단")[0]:
							return self.cardchoose_condition2("열끗", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "홍단")[0]:
							return self.cardchoose_condition2("피", "홍단")[1]
						if self.cardchoose_condition2("피", "청단")[0]:
							return self.cardchoose_condition2("피", "청단")[1]
						if self.cardchoose_condition2("피", "초단")[0]:
							return self.cardchoose_condition2("피", "초단")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.animal)+len(aiobject.godori)>=4 and \
					len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "열끗")[0]:
							return self.cardchoose_condition2("피", "열끗")[1]
						if self.cardchoose_condition2("피", "고도리")[0]:
							return self.cardchoose_condition2("피", "고도리")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]
						if self.cardchoose_bicondition("피")[0]:
							return self.cardchoose_bicondition("피")[1]
				if self.deck_and(next, "청단", "피") and len(aiobject.bluedan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 4점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
				if self.deck_and(next, "청단", "피") and len(aiobject.bluedan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)<9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 4점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
					if len(aiobject.reddan)==2:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
						if self.cardchoose_condition2("쌍피", "열끗")[0]:
							return self.cardchoose_condition2("쌍피", "열끗")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("쌍피", "단")[0]:
							return self.cardchoose_condition2("쌍피", "단")[1]
					if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("피", "쌍피")[0]:
							return self.cardchoose_condition2("피", "쌍피")[1]
				if self.deck_and(next, "청단", "피") and len(aiobject.bluedan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)<9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 3점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
				if self.deck_and(next, "열끗", "쌍피") and len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
				len(aiobject.animal)+len(aiobject.godori)>=4:
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
				if self.deck_and(next, "열끗", "쌍피") and len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
				len(aiobject.animal)+len(aiobject.godori)<4: # 2점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
				if self.deck_and(next, "열끗", "쌍피") and len(aiobject.pee)+2*len(aiobject.doublepee)==8 and \
				len(aiobject.animal)+len(aiobject.godori)>=4: # 2점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
				if self.deck_and(next, "열끗", "쌍피") and len(aiobject.pee)+2*len(aiobject.doublepee)>8 and \
				len(aiobject.animal)+len(aiobject.godori)>=4: # 2점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
				if self.deck_and(next, "열끗", "쌍피") and len(aiobject.pee)+2*len(aiobject.doublepee)==8 and \
				len(aiobject.animal)+len(aiobject.godori)<4: # 1점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
				if self.deck_and(next, "열끗", "쌍피") and len(aiobject.pee)+2*len(aiobject.doublepee)<8 and \
				len(aiobject.animal)+len(aiobject.godori)>=4: # 1점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
				if self.deck_and(next, "열끗", "피") and len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
				len(aiobject.animal)+len(aiobject.godori)>=4: # 2점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
				if self.deck_and(next, "열끗", "피") and len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
				len(aiobject.animal)+len(aiobject.godori)<4: # 1점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
				if self.deck_and(next, "열끗", "피") and len(aiobject.pee)+2*len(aiobject.doublepee)<9 and \
				len(aiobject.animal)+len(aiobject.godori)>=4: # 1점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
				if self.deck_and(next, "쌍피", "피") and len(aiobject.pee)+2*len(aiobject.doublepee)>=9: # 3점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
				if self.deck_and(next, "쌍피", "피") and len(aiobject.pee)+2*len(aiobject.doublepee)>=8: # 2점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
				if self.deck_and(next, "쌍피", "피") and len(aiobject.pee)+2*len(aiobject.doublepee)>=7: # 1점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
				if self.deck_and(next, "열끗", "단") and len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 2점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
				if self.deck_and(next, "열끗", "단") and len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 1점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
				if self.deck_and(next, "열끗", "단") and len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)<4 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 1점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
				if self.deck_and(next, "단", "쌍피") and len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 3점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("홍단")[0]:
							return self.cardchoose_condition("홍단")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("청단")[0]:
							return self.cardchoose_condition("청단")[1]
					if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition("초단")[0]:
							return self.cardchoose_condition("초단")[1]
					if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("홍단", "고도리")[0]:
							return self.cardchoose_condition2("홍단", "고도리")[1]
					if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("청단", "열끗")[0]:
							return self.cardchoose_condition2("청단", "열끗")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "고도리")[0]:
							return self.cardchoose_condition2("초단", "고도리")[1]
					if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition2("초단", "열끗")[0]:
							return self.cardchoose_condition2("초단", "열끗")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("홍단", "피")[0]:
							return self.cardchoose_condition2("홍단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("청단", "피")[0]:
							return self.cardchoose_condition2("청단", "피")[1]
					if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("초단", "피")[0]:
							return self.cardchoose_condition2("초단", "피")[1]
				if self.deck_and(next, "단", "쌍피") and len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 2점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
				if self.deck_and(next, "단", "쌍피") and len(aiobject.pee)+2*len(aiobject.doublepee)==8 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 1점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1] 
				if self.deck_and(next, "단", "쌍피") and len(aiobject.pee)+2*len(aiobject.doublepee)<8 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 1점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
				if self.deck_and(next, "단", "쌍피") and len(aiobject.pee)+2*len(aiobject.doublepee)>=8 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4: # 2점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
					if len(aiobject.godori)==2:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
				if self.deck_and(next, "단", "쌍피") and len(aiobject.pee)+2*len(aiobject.doublepee)>=8 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)<4: # 1점
					if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
					if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
						if self.cardchoose_condition2("고도리", "피")[0]:
							return self.cardchoose_condition2("고도리", "피")[1]
					if len(aiobject.godori)==2 and \
					len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
						if self.cardchoose_condition2("고도리", "홍단")[0]:
							return self.cardchoose_condition2("고도리", "홍단")[1]
						if self.cardchoose_condition2("고도리", "초단")[0]:
							return self.cardchoose_condition2("고도리", "초단")[1]
			if aiobject.score>=1:
				if len(aiobject.godori)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
					if self.cardchoose_condition("고도리")[0]:
						return self.cardchoose_condition("고도리")[1]
				if len(aiobject.godori)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
					if self.cardchoose_condition2("고도리", "피")[0]:
						return self.cardchoose_condition2("고도리", "피")[1]
				if len(aiobject.godori)==2 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
					if self.cardchoose_condition2("고도리", "홍단")[0]:
						return self.cardchoose_condition2("고도리", "홍단")[1]
					if self.cardchoose_condition2("고도리", "초단")[0]:
						return self.cardchoose_condition2("고도리", "초단")[1]
			if aiobject.score>=2:
				if len(aiobject.godori)==2:
					if self.cardchoose_condition("고도리")[0]:
						return self.cardchoose_condition("고도리")[1]
			if aiobject.score>=3:
				if len(aiobject.reddan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
					if self.cardchoose_condition("홍단")[0]:
						return self.cardchoose_condition("홍단")[1]
				if len(aiobject.bluedan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
					if self.cardchoose_condition("청단")[0]:
						return self.cardchoose_condition("청단")[1]
				if len(aiobject.chodan)==2 and len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
					if self.cardchoose_condition("초단")[0]:
						return self.cardchoose_condition("초단")[1]
				if len(aiobject.reddan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
					if self.cardchoose_condition2("홍단", "고도리")[0]:
						return self.cardchoose_condition2("홍단", "고도리")[1]
				if len(aiobject.bluedan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
					if self.cardchoose_condition2("청단", "열끗")[0]:
						return self.cardchoose_condition2("청단", "열끗")[1]
				if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
					if self.cardchoose_condition2("초단", "고도리")[0]:
						return self.cardchoose_condition2("초단", "고도리")[1]
				if len(aiobject.chodan)==2 and len(aiobject.godori)+len(aiobject.animal)>=4:
					if self.cardchoose_condition2("초단", "열끗")[0]:
						return self.cardchoose_condition2("초단", "열끗")[1]
				if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
					if self.cardchoose_condition2("홍단", "피")[0]:
						return self.cardchoose_condition2("홍단", "피")[1]
				if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
					if self.cardchoose_condition2("청단", "피")[0]:
						return self.cardchoose_condition2("청단", "피")[1]
				if len(aiobject.reddan)==2 and len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
					if self.cardchoose_condition2("초단", "피")[0]:
						return self.cardchoose_condition2("초단", "피")[1]
			if aiobject.score>=4:
				if len(aiobject.reddan)==2:
					if self.cardchoose_condition("홍단")[0]:
						return self.cardchoose_condition("홍단")[1]
				if len(aiobject.bluedan)==2:
					if self.cardchoose_condition("청단")[0]:
						return self.cardchoose_condition("청단")[1]
				if len(aiobject.chodan)==2:
					if self.cardchoose_condition("초단")[0]:
						return self.cardchoose_condition("초단")[1]
				if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and len(aiobject.animal)+len(aiobject.godori)>=4:
					if self.cardchoose_condition2("쌍피", "열끗")[0]:
						return self.cardchoose_condition2("쌍피", "열끗")[1]
				if len(aiobject.pee)+2*len(aiobject.doublepee)>=9 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
					if self.cardchoose_condition2("쌍피", "단")[0]:
						return self.cardchoose_condition2("쌍피", "단")[1]
				if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
					if self.cardchoose_condition2("피", "쌍피")[0]:
						return self.cardchoose_condition2("피", "쌍피")[1]
			if aiobject.score>=5:
				if len(aiobject.animal)+len(aiobject.godori)>=4 and \
				len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
					if self.cardchoose_condition2("고도리", "홍단")[0]:
						return self.cardchoose_condition2("고도리", "홍단")[1]
					if self.cardchoose_condition2("고도리", "초단")[0]:
						return self.cardchoose_condition2("고도리", "초단")[1]
					if self.cardchoose_condition2("열끗", "청단")[0]:
						return self.cardchoose_condition2("열끗", "청단")[1]
					if self.cardchoose_condition2("열끗", "초단")[0]:
						return self.cardchoose_condition2("열끗", "초단")[1]
					if self.cardchoose_condition2("열끗", "단")[0]:
						return self.cardchoose_condition2("열끗", "단")[1]
				if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
				len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
					if self.cardchoose_condition2("쌍피", "단")[0]:
						return self.cardchoose_condition2("쌍피", "단")[1]
				if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4 and \
				len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
					if self.cardchoose_condition2("피", "홍단")[0]:
						return self.cardchoose_condition2("피", "홍단")[1]
					if self.cardchoose_condition2("피", "청단")[0]:
						return self.cardchoose_condition2("피", "청단")[1]
					if self.cardchoose_condition2("피", "초단")[0]:
						return self.cardchoose_condition2("피", "초단")[1]
				if len(aiobject.animal)+len(aiobject.godori)>=4 and \
				len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
					if self.cardchoose_condition2("쌍피", "열끗")[0]:
						return self.cardchoose_condition2("쌍피", "열끗")[1]
				if len(aiobject.animal)+len(aiobject.godori)>=4 and \
				len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
					if self.cardchoose_condition2("피", "열끗")[0]:
						return self.cardchoose_condition2("피", "열끗")[1]
					if self.cardchoose_condition2("피", "고도리")[0]:
						return self.cardchoose_condition2("피", "고도리")[1]
				if len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
					if self.cardchoose_condition2("피", "쌍피")[0]:
						return self.cardchoose_condition2("피", "쌍피")[1]						
				if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
					if self.cardchoose_condition("쌍피")[0]:
						return self.cardchoose_condition("쌍피")[1]
					if self.cardchoose_bicondition("피")[0]:
						return self.cardchoose_bicondition("피")[1]
			if aiobject.score>=6:
				if len(aiobject.animal)+len(aiobject.godori)>=4:
					if self.cardchoose_condition("고도리")[0]:
						return self.cardchoose_condition("고도리")[1]
					if self.cardchoose_condition("열끗")[0]:
						return self.cardchoose_condition("열끗")[1]
				if len(aiobject.reddan)+len(aiobject.bluedan)+len(aiobject.chodan)+len(aiobject.dan)>=4:
					if self.cardchoose_condition("홍단")[0]:
						return self.cardchoose_condition("홍단")[1]
					if self.cardchoose_condition("청단")[0]:
						return self.cardchoose_condition("청단")[1]
					if self.cardchoose_condition("초단")[0]:
						return self.cardchoose_condition("초단")[1]
					if self.cardchoose_condition("단")[0]:
						return self.cardchoose_condition("단")[1]
				if len(aiobject.pee)+2*len(aiobject.doublepee)>=8:
					if self.cardchoose_condition("쌍피")[0]:
						return self.cardchoose_condition("쌍피")[1]				
				if len(aiobject.pee)+2*len(aiobject.doublepee)>=9:
					if self.cardchoose_condition("피")[0]:
						return self.cardchoose_condition("피")[1]
			for k in range(len(playerobject.hand)): # 플레이어 패 봉쇄
				for i in range(len(aiobject.hand)):
					for j in range(12):
						if len(field[j])==1:
							if playerobject.hand[k].month==aiobject.hand[i].month==field[j][0].month!=deck.check.month:
								return i
			if random.randrange(2)==0: # 변덕스러운 쪽
				for k in range(len(aiobject.hand)):
					if aiobject.hand[k].month==deck.check.month:
						check=True
						for i in range(12):
							if len(field[i])==1:
								if field[i][0].month==deck.check.month:
									check=False
						if check:
							return k
			if len(playerobject.gwang)<3:
				if self.cardchoose_condition("광")[0]:
					return self.cardchoose_condition("광")[1]
				if self.cardchoose_condition("비광")[0]:
					return self.cardchoose_condition("비광")[1]
			if len(playerobject.gwang)>=3:
				if self.cardchoose_field("광")[0]:
					return self.cardchoose_field("광")[1]
				if self.cardchoose_field("비광")[0]:
					return self.cardchoose_field("비광")[1]
			if len(playerobject.godori)>=2:
				if self.cardchoose_field("고도리")[0]:
					return self.cardchoose_field("고도리")[1]
			if len(playerobject.reddan)>=2:
				if self.cardchoose_field("홍단")[0]:
					return self.cardchoose_field("홍단")[1]
			if len(playerobject.bluedan)>=2:
				if self.cardchoose_field("청단")[0]:
					return self.cardchoose_field("청단")[1]
			if len(playerobject.chodan)>=2:
				if self.cardchoose_field("초단")[0]:
					return self.cardchoose_field("초단")[1]
			if len(playerobject.godori)==0:
				if self.cardchoose_condition("고도리")[0]:
					return self.cardchoose_condition("고도리")[1]
			if len(playerobject.reddan)==0:
				if self.cardchoose_condition("홍단")[0]:
					return self.cardchoose_condition("홍단")[1]
			if len(playerobject.bluedan)==0:
				if self.cardchoose_condition("청단")[0]:
					return self.cardchoose_condition("청단")[1]
			if len(playerobject.chodan)==0:
				if self.cardchoose_condition("초단")[0]:
					return self.cardchoose_condition("초단")[1]
			if self.cardchoose_condition("뻑")[0] and (len(playerobject.doublepee)>0 or len(playerobject.pee)>0) and \
			playerobject.score>=2:
				return self.cardchoose_condition("뻑")[1]
			for k in range(len(aiobject.hand)):
				if aiobject.hand[k].special=="폭탄":
					for j in range(12):
						if len(field[j])==3 and field[j][0].month==deck.check.month and \
						(len(playerobject.doublepee)>0 or len(playerobject.pee)>0):
							return k
			playerpee=0
			playeranimal=0
			playerdan=0
			for k in range(len(playerobject.hand)):
				if playerobject.hand[k].special=="고도리" or playerobject.hand[k].special=="열끗":
					playeranimal+=1
				if playerobject.hand[k].special=="홍단" or playerobject.hand[k].special=="초단" or \
				playerobject.hand[k].special=="청단" or playerobject.hand[k].special=="단":
					playerdan+=1
				if playerobject.hand[k].special=="쌍피" or playerobject.hand[k].special=="피":
					playerpee+=1
			pee_left=24-len(aiobject.pee)-len(aiobject.doublepee)-len(playerobject.pee)-len(playerobject.doublepee)-playerpee
			animal_left=8-len(aiobject.animal)-len(aiobject.godori)-len(playerobject.animal)-len(playerobject.godori)-playeranimal
			dan_left=10-len(aiobject.reddan)-len(aiobject.bluedan)-len(aiobject.chodan)-len(aiobject.dan)-\
			len(playerobject.reddan)-len(playerobject.bluedan)-len(playerobject.chodan)-len(playerobject.dan)-playerdan
			pee_score=10-len(aiobject.pee)-2*len(aiobject.doublepee)
			animal_score=5-len(aiobject.animal)-len(aiobject.godori)
			dan_score=5-len(aiobject.reddan)-len(aiobject.bluedan)-len(aiobject.chodan)-len(aiobject.dan)
			if pee_score<animal_score and pee_score<dan_score:
				if self.cardchoose_condition("쌍피")[0]:
					return self.cardchoose_condition("쌍피")[1]
				if self.cardchoose_condition("피")[0]:
					return self.cardchoose_condition("피")[1]
			if animal_score<pee_score and animal_score<dan_score:
				if self.cardchoose_condition("고도리")[0]:
					return self.cardchoose_condition("고도리")[1]
				if self.cardchoose_condition("열끗")[0]:
					return self.cardchoose_condition("열끗")[1]
			if dan_score<pee_score and dan_score<animal_score:
				if self.cardchoose_colordan()[0]:
					return self.cardchoose_colordan()[1]
				if self.cardchoose_condition("단")[0]:
					return self.cardchoose_condition("단")[1]
			if pee_score==dan_score and pee_score<animal_score:
				if pee_left > dan_left:
					if self.cardchoose_condition("쌍피")[0]:
						return self.cardchoose_condition("쌍피")[1]
					if self.cardchoose_condition("피")[0]:
						return self.cardchoose_condition("피")[1]
				if pee_left < dan_left:
					if self.cardchoose_colordan()[0]:
						return self.cardchoose_colordan()[1]
					if self.cardchoose_condition("단")[0]:
						return self.cardchoose_condition("단")[1]
				else:
					if random.randrange(2)==0:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]
						if self.cardchoose_condition("피")[0]:
							return self.cardchoose_condition("피")[1]
					else:
						if self.cardchoose_colordan()[0]:
							return self.cardchoose_colordan()[1]
						if self.cardchoose_condition("단")[0]:
							return self.cardchoose_condition("단")[1]
			if pee_score==animal_score and pee_score<dan_score:
				if pee_left > animal_left:
					if self.cardchoose_condition("쌍피")[0]:
						return self.cardchoose_condition("쌍피")[1]
					if self.cardchoose_condition("피")[0]:
						return self.cardchoose_condition("피")[1]
				if pee_left < animal_left:
					if self.cardchoose_condition("고도리")[0]:
						return self.cardchoose_condition("고도리")[1]
					if self.cardchoose_condition("열끗")[0]:
						return self.cardchoose_condition("열끗")[1]
				else:
					if random.randrange(2)==0:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]
						if self.cardchoose_condition("피")[0]:
							return self.cardchoose_condition("피")[1]
					else:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
						if self.cardchoose_condition("열끗")[0]:
							return self.cardchoose_condition("열끗")[1]
			if animal_score==dan_score and animal_score<pee_score:
				if animal_left > dan_left:
					if self.cardchoose_condition("고도리")[0]:
						return self.cardchoose_condition("고도리")[1]
					if self.cardchoose_condition("열끗")[0]:
						return self.cardchoose_condition("열끗")[1]
				if animal_left < dan_left:
					if self.cardchoose_colordan()[0]:
						return self.cardchoose_colordan()[1]
					if self.cardchoose_condition("단")[0]:
						return self.cardchoose_condition("단")[1]
				else:
					if random.randrange(2)==0:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
						if self.cardchoose_condition("열끗")[0]:
							return self.cardchoose_condition("열끗")[1]
					else:
						if self.cardchoose_colordan()[0]:
							return self.cardchoose_colordan()[1]
						if self.cardchoose_condition("단")[0]:
							return self.cardchoose_condition("단")[1]
			if animal_score==dan_score==pee_score:
				if animal_left > dan_left and animal_left > pee_left:
					if self.cardchoose_condition("고도리")[0]:
						return self.cardchoose_condition("고도리")[1]
					if self.cardchoose_condition("열끗")[0]:
						return self.cardchoose_condition("열끗")[1]	
				if dan_left > animal_left and dan_left > pee_left:
					if self.cardchoose_colordan()[0]:
						return self.cardchoose_colordan()[1]
					if self.cardchoose_condition("단")[0]:
						return self.cardchoose_condition("단")[1]
				if pee_left > animal_left and pee_left > dan_left:
					if self.cardchoose_condition("쌍피")[0]:
						return self.cardchoose_condition("쌍피")[1]
					if self.cardchoose_condition("피")[0]:
						return self.cardchoose_condition("피")[1]
				if animal_left == dan_left and animal_left > pee_left:
					if random.randrange(2)==0:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
						if self.cardchoose_condition("열끗")[0]:
							return self.cardchoose_condition("열끗")[1]
					else:
						if self.cardchoose_colordan()[0]:
							return self.cardchoose_colordan()[1]
						if self.cardchoose_condition("단")[0]:
							return self.cardchoose_condition("단")[1]
				if animal_left == pee_left and animal_left > dan_left:
					if random.randrange(2)==0:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
						if self.cardchoose_condition("열끗")[0]:
							return self.cardchoose_condition("열끗")[1]
					else:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]
						if self.cardchoose_condition("피")[0]:
							return self.cardchoose_condition("피")[1]
				if pee_left == dan_left and pee_left > animal_left:
					if random.randrange(2)==0:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]
						if self.cardchoose_condition("피")[0]:
							return self.cardchoose_condition("피")[1]
					else:
						if self.cardchoose_colordan()[0]:
							return self.cardchoose_colordan()[1]
						if self.cardchoose_condition("단")[0]:
							return self.cardchoose_condition("단")[1]
				else:
					k=random.randrange(3)
					if k==0:
						if self.cardchoose_condition("고도리")[0]:
							return self.cardchoose_condition("고도리")[1]
						if self.cardchoose_condition("열끗")[0]:
							return self.cardchoose_condition("열끗")[1]
					if k==1:
						if self.cardchoose_condition("쌍피")[0]:
							return self.cardchoose_condition("쌍피")[1]
						if self.cardchoose_condition("피")[0]:
							return self.cardchoose_condition("피")[1]
					else:
						if self.cardchoose_colordan()[0]:
							return self.cardchoose_colordan()[1]
						if self.cardchoose_condition("단")[0]:
							return self.cardchoose_condition("단")[1]
			for k in range(len(aiobject.hand)): # 100프로 쪽
				if aiobject.hand[k].month == deck.check.month:
					return k
			else:
				if self.cardchoose_exist("폭탄")[0]:
					return self.cardchoose_exist("폭탄")[1]
				if pee_score > animal_score and pee_score > dan_score:
					if self.cardchoose_exist("피")[0]:
						return self.cardchoose_exist("피")[1]
					if self.cardchoose_exist("쌍피")[0]:
						return self.cardchoose_exist("쌍피")[1]
				if dan_score > animal_score and dan_score > pee_score:
					if self.cardchoose_exist("홍단")[0] and len(aiobject.reddan) > 0 and len(playerobject.reddan) > 0:
						return self.cardchoose_exist("홍단")[1]
					if self.cardchoose_exist("청단")[0] and len(aiobject.bluedan) > 0 and len(playerobject.bluedan) > 0:
						return self.cardchoose_exist("청단")[1]
					if self.cardchoose_exist("초단")[0] and len(aiobject.chodan) > 0 and len(playerobject.chodan) > 0:
						return self.cardchoose_exist("초단")[1]
					if self.cardchoose_exist("단")[0]:
						return self.cardchoose_exist("단")[1]
				if animal_score > dan_score and animal_score > pee_score:
					if self.cardchoose_exist("고도리")[0] and len(aiobject.godori) > 0 and len(playerobject.godori) > 0:
						return self.cardchoose_exist("고도리")[1]
					if self.cardchoose_exist("열끗")[0]:
						return self.cardchoose_exist("열끗")[1]
				if pee_score == animal_score and pee_score > dan_score:
					if pee_left > animal_left:
						if self.cardchoose_exist("고도리")[0] and len(aiobject.godori) > 0 and len(playerobject.godori) > 0:
							return self.cardchoose_exist("고도리")[1]
						if self.cardchoose_exist("열끗")[0]:
							return self.cardchoose_exist("열끗")[1]
					if pee_left < animal_left:
						if self.cardchoose_exist("피")[0]:
							return self.cardchoose_exist("피")[1]
						if self.cardchoose_exist("쌍피")[0]:
							return self.cardchoose_exist("쌍피")[1]
					else:
						if random.randrange(2)==0:
							if self.cardchoose_exist("고도리")[0] and len(aiobject.godori) > 0 and len(playerobject.godori) > 0:
								return self.cardchoose_exist("고도리")[1]
							if self.cardchoose_exist("열끗")[0]:
								return self.cardchoose_exist("열끗")[1]
						else:
							if self.cardchoose_exist("피")[0]:
								return self.cardchoose_exist("피")[1]
							if self.cardchoose_exist("쌍피")[0]:
								return self.cardchoose_exist("쌍피")[1]
				if pee_score == dan_score and pee_score > animal_score:
					if pee_left > dan_left:
						if self.cardchoose_exist("홍단")[0] and len(aiobject.reddan) > 0 and len(playerobject.reddan) > 0:
							return self.cardchoose_exist("홍단")[1]
						if self.cardchoose_exist("청단")[0] and len(aiobject.bluedan) > 0 and len(playerobject.bluedan) > 0:
							return self.cardchoose_exist("청단")[1]
						if self.cardchoose_exist("초단")[0] and len(aiobject.chodan) > 0 and len(playerobject.chodan) > 0:
							return self.cardchoose_exist("초단")[1]
						if self.cardchoose_exist("단")[0]:
							return self.cardchoose_exist("단")[1]
					if pee_left < dan_left:
						if self.cardchoose_exist("피")[0]:
							return self.cardchoose_exist("피")[1]
						if self.cardchoose_exist("쌍피")[0]:
							return self.cardchoose_exist("쌍피")[1]
					else:
						if random.randrange(2)==0:
							if self.cardchoose_exist("홍단")[0] and len(aiobject.reddan) > 0 and len(playerobject.reddan) > 0:
								return self.cardchoose_exist("홍단")[1]
							if self.cardchoose_exist("청단")[0] and len(aiobject.bluedan) > 0 and len(playerobject.bluedan) > 0:
								return self.cardchoose_exist("청단")[1]
							if self.cardchoose_exist("초단")[0] and len(aiobject.chodan) > 0 and len(playerobject.chodan) > 0:
								return self.cardchoose_exist("초단")[1]
							if self.cardchoose_exist("단")[0]:
								return self.cardchoose_exist("단")[1]
						else:
							if self.cardchoose_exist("피")[0]:
								return self.cardchoose_exist("피")[1]
							if self.cardchoose_exist("쌍피")[0]:
								return self.cardchoose_exist("쌍피")[1]
				if animal_score==dan_score and animal_score>pee_score:
					if animal_left>dan_left:
						if self.cardchoose_exist("고도리")[0] and len(aiobject.godori) > 0 and len(playerobject.godori) > 0:
							return self.cardchoose_exist("고도리")[1]
						if self.cardchoose_exist("열끗")[0]:
							return self.cardchoose_exist("열끗")[1]
					if animal_left<dan_left:
						if self.cardchoose_exist("홍단")[0] and len(aiobject.reddan) > 0 and len(playerobject.reddan) > 0:
							return self.cardchoose_exist("홍단")[1]
						if self.cardchoose_exist("청단")[0] and len(aiobject.bluedan) > 0 and len(playerobject.bluedan) > 0:
							return self.cardchoose_exist("청단")[1]
						if self.cardchoose_exist("초단")[0] and len(aiobject.chodan) > 0 and len(playerobject.chodan) > 0:
							return self.cardchoose_exist("초단")[1]
						if self.cardchoose_exist("단")[0]:
							return self.cardchoose_exist("단")[1]
					else:
						if random.randrange(2)==0:
							if self.cardchoose_exist("고도리")[0] and len(aiobject.godori) > 0 and len(playerobject.godori) > 0:
								return self.cardchoose_exist("고도리")[1]
							if self.cardchoose_exist("열끗")[0]:
								return self.cardchoose_exist("열끗")[1]
						else:
							if self.cardchoose_exist("홍단")[0] and len(aiobject.reddan) > 0 and len(playerobject.reddan) > 0:
								return self.cardchoose_exist("홍단")[1]
							if self.cardchoose_exist("청단")[0] and len(aiobject.bluedan) > 0 and len(playerobject.bluedan) > 0:
								return self.cardchoose_exist("청단")[1]
							if self.cardchoose_exist("초단")[0] and len(aiobject.chodan) > 0 and len(playerobject.chodan) > 0:
								return self.cardchoose_exist("초단")[1]
							if self.cardchoose_exist("단")[0]:
								return self.cardchoose_exist("단")[1]
				if animal_score==dan_score and animal_score==pee_score and dan_score==pee_score:
					k=random.randrange(3)
					if k==0:
						if self.cardchoose_exist("고도리")[0] and len(aiobject.godori) > 0 and len(playerobject.godori) > 0:
							return self.cardchoose_exist("고도리")[1]
						if self.cardchoose_exist("열끗")[0]:
							return self.cardchoose_exist("열끗")[1]
					if k==1:
						if self.cardchoose_exist("홍단")[0] and len(aiobject.reddan) > 0 and len(playerobject.reddan) > 0:
							return self.cardchoose_exist("홍단")[1]
						if self.cardchoose_exist("청단")[0] and len(aiobject.bluedan) > 0 and len(playerobject.bluedan) > 0:
							return self.cardchoose_exist("청단")[1]
						if self.cardchoose_exist("초단")[0] and len(aiobject.chodan) > 0 and len(playerobject.chodan) > 0:
							return self.cardchoose_exist("초단")[1]
						if self.cardchoose_exist("단")[0]:
							return self.cardchoose_exist("단")[1]
					else:
						if self.cardchoose_exist("피")[0]:
							return self.cardchoose_exist("피")[1]
						if self.cardchoose_exist("쌍피")[0]:
							return self.cardchoose_exist("쌍피")[1]
				if self.cardchoose_exist("쌍피열끗")[0]:
					return self.cardchoose_exist("쌍피열끗")[1]
				if self.cardchoose_exist_colordan()[0]:
					return self.cardchoose_exist_colordan()[0]
				if self.cardchoose_exist("고도리")[0]:
					return self.cardchoose_exist("고도리")[1]
				if self.cardchoose_exist("비광")[0]:
					return self.cardchoose_exist("비광")[1]
				if self.cardchoose_exist("광")[0]:
					return self.cardchoose_exist("광")[1]
				else:
					return random.randrange(len(aiobject.hand))

	def determine(self, aiobject, playerobject, field, deck): # 쌍피열끗 판단
		pee_left=24-len(aiobject.pee)-len(aiobject.doublepee)-len(playerobject.pee)-len(playerobject.doublepee)
		animal_left=8-len(aiobject.animal)-len(aiobject.godori)-len(playerobject.animal)-len(playerobject.godori)
		pee_score=10-len(aiobject.pee)-2*len(aiobject.doublepee)
		animal_score=5-len(aiobject.animal)-len(aiobject.godori)
		if self.__ai=="easy":
			return False # 쌍피
		if self.__ai=="normal":
			if 2*len(aiobject.doublepee)+len(aiobject.pee)>=8:
				return False
			else:
				return True
		if self.__ai=="hard" or self.__ai=="hell":
			if pee_score > 0 and animal_score > 0:
				if pee_left > animal_left:
					if pee_score <= animal_score:
						return False
					else:
						if random.randrange(2)==0:
							return True
						else:
							return False
				if pee_left < animal_left:
					if pee_score >= animal_score:
						return True
					else:
						if random.randrange(2)==0:
							return True
						else:
							return False
				else:
					if pee_score < animal_score:
						return False
					if pee_score > animal_score:
						return True
					else:
						if random.randrange(2)==0:
							return True
						else:
							return False
			if pee_score >= 0 and animal_score < 0:
				return True
			if pee_score < 0 and animal_score >= 0:
				return False
			else:
				if pee_left >= animal_left:
					return False
				else:
					return True
		else: # impossible
			player_hand_pee=0
			player_hand_animal=0
			for k in range(len(playerobject.hand)):
				if playerobject.hand[k].special=="쌍피" or playerobject.hand[k].special=="피":
					player_hand_pee+=1
				if playerobject.hand[k].special=="고도리" or playerobject.hand[k].special=="열끗":
					player_hand_animal+=1
			pee_left-=player_hand_pee
			animal_left-=player_hand_animal
			if pee_score > 0 and animal_score > 0:
				if pee_left > animal_left:
					if pee_score <= animal_score:
						return False
					else:
						if random.randrange(2)==0:
							return True
						else:
							return False
				if pee_left < animal_left:
					if pee_score >= animal_score:
						return True
					else:
						if random.randrange(2)==0:
							return True
						else:
							return False
				else:
					if pee_score < animal_score:
						return False
					if pee_score > animal_score:
						return True
					else:
						if random.randrange(2)==0:
							return True
						else:
							return False
			if pee_score >= 0 and animal_score < 0:
				return True
			if pee_score < 0 and animal_score >= 0:
				return False
			else:
				if pee_left >= animal_left:
					return False
				else:
					return True

	def go_stop(self, aiobject, playerobject, field, deck): # 고할지 스톱할지 판단
		if self.__ai=="easy":
			return False # stop
		if self.__ai=="normal":
			if playerobject.score==0 and random.randrange(6)==0:
				return False
			else:
				if playerobject.score==0:
					return True
				if playerobject.score==1 and random.randrange(4)==0:
					return False
				else:
					if playerobject.score==1:
						return True
					else:
						return False
		if self.__ai=="hard":
			if playerobject.score==0 and random.randrange(10)==0:
				return False
			else:
				if playerobject.score==0:
					return True
				if playerobject.score==1 and random.randrange(8)==0:
					return False
				else:
					if playerobject.score==1:
						return True
					if playerobject.score==2 and random.randrange(6)==0:
						return False
					else:
						if playerobject.score==2 and len(self.__playerobject.godori)<=1:
							return True
						if playerobject.score==3 and random.randrange(3)==0:
							return False
						else:
							if playerobject.score==3 and len(playerobject.gwang)+len(playerobject.beegwang)<=1 and \
							len(playerobject.reddan)<=1 and len(playerobject.bluedan)<=1 and len(playerobject.chodan)<=1 and \
							len(playerobject.godori)<=1 and 0<=random.randrange(8)<=5:
								return True
							if playerobject.score==3:
								return False
							if 4<=playerobject.score<=6:
								length=0
								for k in range(12):
									length+=len(field[k])
								if length==0:
									return True
								else:
									if 0<=random.randrange(10)<=7:
										return False
									else:
										return True
							else:
								return False

		if self.__ai=="hell":
			if playerobject.score==0 and random.randrange(10)==0:
				return False
			else:
				if playerobject.score==0:
					return True
				if playerobject.score==1 and random.randrange(8)==0:
					return False
				else:
					if playerobject.score==1:
						return True
					if playerobject.score==2 and random.randrange(6)==0:
						return False
					else:
						if playerobject.score==2 and len(self.__playerobject.godori)<=1:
							return True
						if playerobject.score==3 and random.randrange(3)==0:
							return False
						else:
							check=True
							for k in range(12):
								if len(field[k])>=1:
									if field[k][0].month==deck.check.month:
										check=False
							if playerobject.score==3 and len(playerobject.gwang)+len(playerobject.beegwang)<=1 and \
							len(playerobject.reddan)<=1 and len(playerobject.bluedan)<=1 and len(playerobject.chodan)<=1 and \
							len(playerobject.godori)<=1 and 0<=random.randrange(8)<=5 and check:
								return True
							if playerobject.score==3:
								return False
							if 4<=playerobject.score<=6:
								length=0
								for k in range(12):
									length+=len(field[k])
								if length==0: # 필드가 비어 있음
									return True
								else:
									return False
							else:
								return False
		else:
			if playerobject.score==0 and random.randrange(10)==0:
				return False
			else:
				if playerobject.score==0:
					return True
				if playerobject.score==1 and random.randrange(8)==0:
					return False
				else:
					if playerobject.score==1:
						return True
					if playerobject.score==2 and random.randrange(6)==0:
						return False
					else:
						if playerobject.score==2 and len(self.__playerobject.godori)<=1:
							return True
						if playerobject.score==3 and random.randrange(3)==0:
							return False
						else:
							check=True
							for k in range(12):
								if len(field[k])>=1:
									if field[k][0].month==deck.check.month:
										check=False
							if playerobject.score==3 and len(playerobject.gwang)+len(playerobject.beegwang)<=1 and \
							len(playerobject.reddan)<=1 and len(playerobject.bluedan)<=1 and len(playerobject.chodan)<=1 and \
							len(playerobject.godori)<=1 and 0<=random.randrange(8)<=5 and check:
								return True
							if playerobject.score==3:
								return False
							if 4<=playerobject.score<=6:
								length=0
								for k in range(12):
									length+=len(field[k])
								check1=True
								for k in range(12):
									if len(field[k])>=1:
										if field[k][0].month==deck.check.month: # 다음 나올 카드의 월과 맞는 카드가 필드에 있는가?
											check1=False
								check2=True
								for k in range(12):
									for i in range(len(playerobject.hand)):
										if len(field[k])>=1:
											if field[k][0].month==playerobject.hand[i].month: # 플레이어 패에 있는 월 중 필드와 맞는게 있는가?
												check2=False
								check3=True
								for k in range(len(playerobject.hand)):
									if deck.check.month==playerobject.hand[k].month: # 다음 나올 카드의 월과 맞는 카드가 플레이어 패에 있는가?
										check3=False
								if length==0: # 필드가 비어 있음
									if check3:
										return True
									else:
										return False
								else: # 필드가 안 비어 있음
									if check1 and check2 and check3:
										return True
									else:
										return False
							else:
								return False

	def cardchoose_condition(self, con): # 패 혹은 필드에 있는가?
		if con!="뻑":
			if con!="열끗" or con!="쌍피":
				for k in range(len(self.__aiobject.hand)):
					for j in range(12):
						if len(self.__field[j])!=0:
							for i in range(len(self.__field[j])):
								if self.__ai!="hell" and self.__ai!="impossible":
									if (self.__field[j][0].month == self.__aiobject.hand[k].month) and \
									(self.__field[j][i].special==con or self.__aiobject.hand[k].special==con) :
										return [True, k]
								else:
									if (self.__field[j][0].month == self.__aiobject.hand[k].month) and \
									(self.__field[j][i].special==con or self.__aiobject.hand[k].special==con) and self.__aiobject.hand[k].month!=self.__deck.check.month:
										return [True, k]
			else:
				for k in range(len(self.__aiobject.hand)):
					for j in range(12):
						if len(self.__field[j])!=0:
							for i in range(len(self.__field[j])):
								if (self.__field[j][0].month == self.__aiobject.hand[k].month) and \
								((self.__field[j][i].special=="쌍피열끗" or self.__aiobject.hand[k].special=="쌍피열끗") or \
								(self.__field[j][i].special==con or self.__aiobject.hand[k].special==con)) :
									return [True, k]

		else:
			for k in range(len(self.__aiobject.hand)):
				for j in range(12):
					if len(self.__field[j])==3:
						if self.__field[j][0].month == self.__aiobject.hand[k].month:
							return [True, k]
		return [False, 0]

	def cardchoose_condition2(self, con1, con2): # 패 혹은 필드에 con1과 con2이 있는가?
		if con1!="쌍피" and con1!="열끗" and con2!="쌍피" and con2!="열끗":
			for k in range(len(self.__aiobject.hand)):
				for j in range(12):
					if len(self.__field[j])!=0:
						for i in range(len(self.__field[j])):
							if self.__ai!="hell" and self.__ai!="impossible":
								if (self.__field[j][0].month == self.__aiobject.hand[k].month) and \
								((self.__field[j][i].special==con1 and self.__aiobject.hand[k].special==con2) or (self.__field[j][i].special==con2 and self.__aiobject.hand[k].special==con1)):
									return [True, k]
							else:
								if (self.__field[j][0].month == self.__aiobject.hand[k].month) and self.__aiobject.hand[k].month!=self.__deck.check.month and \
								((self.__field[j][i].special==con1 and self.__aiobject.hand[k].special==con2) or (self.__field[j][i].special==con2 and self.__aiobject.hand[k].special==con1)):
									return [True, k]
		else:
			if (con1=="쌍피" or con1=="열끗") and con2!="쌍피" and con2!="열끗":
				for k in range(len(self.__aiobject.hand)):
					for j in range(12):
						if len(self.__field[j])!=0:
							for i in range(len(self.__field[j])):
								if self.__ai!="hell" and self.__ai!="impossible":
									if (self.__field[j][0].month == self.__aiobject.hand[k].month) and \
									((self.__field[j][i].special=="쌍피열끗" or self.__field[j][i].special==con1) and self.__aiobject.hand[k].special==con2):			
										return [True, k]
								else:
									if (self.__field[j][0].month == self.__aiobject.hand[k].month) and self.__aiobject.hand[k].month!=self.__deck.check.month and \
									((self.__field[j][i].special=="쌍피열끗" or self.__field[j][i].special==con1) and self.__aiobject.hand[k].special==con2):
										return [True, k]
			if con1!="쌍피" and con1!="열끗" and (con2=="쌍피" or con2=="열끗"):
				for k in range(len(self.__aiobject.hand)):
					for j in range(12):
						if len(self.__field[j])!=0:
							for i in range(len(self.__field[j])):
								if self.__ai!="hell" and self.__ai!="impossible":
									if (self.__field[j][0].month == self.__aiobject.hand[k].month) and \
									(self.__field[j][i].special==con1) and (self.__aiobject.hand[k].special==con2 or self.__aiobject.hand[k].special=="쌍피열끗"):		
										return [True, k]
								else:
									if (self.__field[j][0].month == self.__aiobject.hand[k].month) and self.__aiobject.hand[k].month!=self.__deck.check.month and \
									(self.__field[j][i].special==con1) and (self.__aiobject.hand[k].special==con2 or self.__aiobject.hand[k].special=="쌍피열끗"):
										return [True, k]
			else:
				for k in range(len(self.__aiobject.hand)):
					for j in range(12):
						if len(self.__field[j])!=0:
							for i in range(len(self.__field[j])):
								if self.__ai!="hell" and self.__ai!="impossible":
									if (self.__field[j][0].month == self.__aiobject.hand[k].month) and \
									(self.__field[j][i].special==con1 or self.__field[j][i].special=="쌍피열끗") and (self.__aiobject.hand[k].special==con2 or self.__aiobject.hand[k].special=="쌍피열끗"):			
										return [True, k]
								else:
									if (self.__field[j][0].month == self.__aiobject.hand[k].month) and self.__aiobject.hand[k].month!=self.__deck.check.month and \
									(self.__field[j][i].special==con1 or self.__field[j][i].special=="쌍피열끗") and (self.__aiobject.hand[k].special==con2 or self.__aiobject.hand[k].special=="쌍피열끗"):
										return [True, k]
		return [False, 0]

	def cardchoose_bicondition(self, con): # 패랑 필드에 둘다 있는가?
		for k in range(len(self.__aiobject.hand)):
			for j in range(12):
				if len(self.__field[j])!=0:
					for i in range(len(self.__field[j])):
						if self.__ai!="hell" and self.__ai!="impossible":
							if (self.__field[j][0].month == self.__aiobject.hand[k].month) and \
							(self.__field[j][i].special==con and self.__aiobject.hand[k].special==con):
								return [True, k]
						else:
							if (self.__field[j][0].month == self.__aiobject.hand[k].month) and self.__aiobject.hand[k].month!=self.__deck.check.month and \
							(self.__field[j][i].special==con and self.__aiobject.hand[k].special==con) :
								return [True, k]
		return [False, 0]


	def cardchoose_exist(self, con): # 패에 있는가? (필드에 같은 월이 있는지는 보지 않음)
		if self.__ai!="impossible":
			if con!="쌍피" and con!="열끗":
				for k in range(len(self.__aiobject.hand)):
					if self.__aiobject.hand[k].special==con:
						return [True, k]
			else:
				for k in range(len(self.__aiobject.hand)):
					if self.__aiobject.hand[k].special==con or self.__aiobject.hand[k].special=="쌍피열끗":
						return [True, k]
		else:
			if con!="쌍피" and con!="열끗":
				for k in range(len(self.__aiobject.hand)):
					check=True
					for j in range(len(self.__playerobject.hand)):
						if self.__aiobject.hand[k].month==self.__playerobject.hand[j].month:
							check=False
					if self.__aiobject.hand[k].special==con and check:
						return [True, k]
			else:
				for k in range(len(self.__aiobject.hand)):
					check=True
					for j in range(len(self.__playerobject.hand)):
						if self.__aiobject.hand[k].month==self.__playerobject.hand[j].month:
							check=False
					if (self.__aiobject.hand[k].special==con or self.__aiobject.hand[k].special=="쌍피열끗") and check:
						return [True, k]						
		return [False, 0]

	def cardchoose_field(self, con): # 필드에 있는가?
		if con!="쌍피" and con!="열끗":
			for k in range(len(self.__aiobject.hand)):
				for j in range(12):
					if len(self.__field[j])!=0:
						for i in range(len(self.__field[j])):
							if self.__ai!="hell" and self.__ai!="impossible":						
								if (self.__field[j][0].month == self.__aiobject.hand[k].month) and (self.__field[j][i].special==con):
									return [True, k]
							else:
								if (self.__field[j][0].month == self.__aiobject.hand[k].month) and (self.__field[j][i].special==con) and \
								self.__aiobject.hand[k].month!=self.__deck.check.month:
									return [True, k]
		else:
			for k in range(len(self.__aiobject.hand)):
				for j in range(12):
					if len(self.__field[j])!=0:
						for i in range(len(self.__field[j])):
							if self.__ai!="hell" and self.__ai!="impossible":						
								if (self.__field[j][0].month == self.__aiobject.hand[k].month) and (self.__field[j][i].special==con or \
								self.__field[j][i].special=="쌍피열끗"):
									return [True, k]
							else:
								if (self.__field[j][0].month == self.__aiobject.hand[k].month) and (self.__field[j][i].special==con or \
								self.__field[j][i].special=="쌍피열끗") and self.__aiobject.hand[k].month!=self.__deck.check.month:
									return [True, k]			
		return [False, 0]

	def cardchoose_hand(self, con): # 패에 있는가?
		if con!="쌍피" and con!="열끗":
			for k in range(len(self.__aiobject.hand)):
				for j in range(12):
					if len(self.__field[j])!=0:
						for i in range(len(self.__field[j])):
							if self.__ai!="hell" and self.__ai!="impossible":
								if (self.__field[j][0].month == self.__aiobject.hand[k].month) and (self.__aiobject.hand[k].special==con) :
									return [True, k]
							else:
								if (self.__field[j][0].month == self.__aiobject.hand[k].month) and (self.__aiobject.hand[k].special==con) and \
								self.__aiobject.hand[k].month!=self.__deck.check.month:
									return [True, k]
		else:
			for k in range(len(self.__aiobject.hand)):
				for j in range(12):
					if len(self.__field[j])!=0:
						for i in range(len(self.__field[j])):
							if self.__ai!="hell" and self.__ai!="impossible":
								if (self.__field[j][0].month == self.__aiobject.hand[k].month) and (self.__aiobject.hand[k].special==con or \
								self.__aiobject.hand[k].special=="쌍피열끗") :
									return [True, k]
							else:
								if (self.__field[j][0].month == self.__aiobject.hand[k].month) and (self.__aiobject.hand[k].special==con or \
								self.__aiobject.hand[k].special=="쌍피열끗") and self.__aiobject.hand[k].month!=self.__deck.check.month:
									return [True, k]
		return [False, 0]

	def cardchoose_exist_colordan(self):
		danlist=["홍단", "청단", "초단"]
		random.shuffle(danlist)
		if self.cardchoose_exist(danlist[0])[0]:
			return [True, self.cardchoose_exist(danlist[0])[1]]
		if self.cardchoose_exist(danlist[1])[0]:
			return [True, self.cardchoose_exist(danlist[1])[1]]
		if self.cardchoose_exist(danlist[2])[0]:
			return [True, self.cardchoose_exist(danlist[2])[1]]
		return [False, 0]

	def cardchoose_colordan(self):
		danlist=["홍단", "청단", "초단"]
		random.shuffle(danlist)
		if self.cardchoose_condition(danlist[0])[0]:
			return [True, self.cardchoose_condition(danlist[0])[1]]
		if self.cardchoose_condition(danlist[1])[0]:
			return [True, self.cardchoose_condition(danlist[1])[1]]
		if self.cardchoose_condition(danlist[2])[0]:
			return [True, self.cardchoose_condition(danlist[2])[1]]
		return [False, 0]

	def deck_and(self, lis, con1, con2):
		for k in range(len(lis[1])):
			if lis[1][k].special==con1 and lis[0].special==con2:
				return True
			if lis[1][k].special==con2 and lis[0].special==con1:
				return True
		else:
			return False