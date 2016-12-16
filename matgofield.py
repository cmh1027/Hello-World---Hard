from matgohand import *
from matgocard import *
from matgoview import *
class fields:
	def __init__(self, ob, put, field, nextcard, bomb):
		self.__object=ob # 플레이어/컴퓨터 객체 / 흔들기, 폭탄 확인용. matgohand.py 참조
		# 낸 카드(put)의 월을 참조하여 self.__object.sequence_arrange()를 이용하여, 
		#해당하는 월의 리스트에 카드가 2개가 있는지 확인.
		# 필드에 카드가 있으면 폭탄, 없으면 흔들기
		# matgohand.py의 self.__object.fuck() self.__object.shake() 활용할 것
		self.__put=put # 낸 카드
		self.__field=field # 현재 필드
		self.__nextcard=nextcard # 덱의 다음 카드
		self.__bomb=bomb # 낸 카드가 폭탄 카드인가? 맞다면 self.__put을 사용하지 말고 self.__nextcard만 사용

	def result(self):
		fobject = self.__object
		fput = self.__put
		ffield = self.__field
		fnextcard=self.__nextcard
		fbomb = self.__bomb 
		fhand = self.__object.hand
		steal = 0
		card = []
		last_field = [[],[],[],[],[],[],[],[],[],[],[],[]]
		bombcheck=True
		no_match=True

		if self.__bomb: # 폭탄을 냈을때
			check=True
			for k in range(12):
				if len(ffield[k])>0:
					if fnextcard.month == ffield[k][0].month: # 덱에서 나온 카드와 같은 월이 필드에 존재한다.
						if len(ffield[k]) == 1: # 덱에서 나온카드와 같은 월이 1개일때 
							ffield[k].append(fnextcard)
							card = card + ffield[k]
							ffield[k]=[]
							last_field = ffield
							count = 0
							check=False
							for i in ffield: # 싹쓸 
								if i == []:
									count += 1
							if count == 12:
								print("싹쓸")
								steal += 1
												
						elif len(ffield[k]) == 2: # 덱에서 나온 카드와 필드에 같은 월이 2개 있을때
							if fobject.name!="Computer":
								print(ffield[k][0],"/",ffield[k][1],"중", end=" ")
							response = Reader.card_choose(fobject,ffield[k][0],ffield[k][1]) # 2개중 무엇을 먹을건지 선택
							ffield[k].append(fnextcard)
							card = card + [ffield[k][response]] + [ffield[k][2]]
							if response==0:
								ffield[k]=[ffield[k][1]]
							else:
								ffield[k]=[ffield[k][0]]
							last_field = ffield
							check=False																
										
						elif len(ffield[k]) == 3: #덱에서 나온 카드와 필드에 같은 월이 3개 있을때
							if fnextcard.month in fobject.fuck_month:
								ffield[k].append(fnextcard)
								card = card + ffield[k]
								ffield[k] = []
								last_field = ffield
								steal += 2
								print("자뻑 먹음")
							else: # 자뻑이 아닌경우 
								ffield[k].append(fnextcard)
								card = card + ffield[k]
								ffield[k] = []
								last_field = ffield
								steal += 1
								print("뻑 먹음")
							count = 0
							for i in ffield: # 싹쓸 
								if i == []:
									count += 1
							if count == 12:
								print("싹쓸")
								steal += 1
							check=False
			if check:
				for k in range(12):
					if ffield[k]==[]:
						ffield[k].append(fnextcard)
						break
				last_field=ffield

		else: # 폭탄말고 다른것을 냈을때 
			bomb = 0
			for i in fhand:
				if i.month == fput.month:
					bomb += 1
			if bomb == 2: # 폭탄 or 흔들기가 됨
				for i in range(12):
					if len(ffield[i])>0:
						if ffield[i][0].month == fput.month: #폭탄 3장 다내고 피 1장
							ffield[i].append(fput)
							temp = []
							for k in range(len(fobject.hand)):
								if fobject.hand[k].month==fput.month:
									ffield[i].append(fobject.hand[k])
									temp.append(k)
							if fobject.name=="Computer":
								ffield[i][2].flip()
								ffield[i][3].flip()
							fobject.comput(temp[1])
							fobject.comput(temp[0])
							steal += 1
							if fobject.name=="Computer":
								fobject.get(Card("폭탄", "13", False,"폭탄"))
								fobject.get(Card("폭탄", "13", False,"폭탄"))
							if fobject.name!="Computer":
								fobject.get(Card("폭탄", "13",True,"폭탄"))
								fobject.get(Card("폭탄", "13",True,"폭탄"))								
							fobject.shake
							bombcheck=False
							temp=True
							for k in range(12):
								if len(ffield[k])>0:
									if ffield[k][0].month==fnextcard.month:
										if len(ffield[k])==1:
											ffield[k].append(fnextcard)
											card=card+ffield[i]+ffield[k]
											ffield[i]=[]
											ffield[k]=[]
											last_field=ffield
											temp=False
											count = 0
											for i in ffield: # 싹쓸 
												if i == []:
													count += 1
												if count == 12:
													print("싹쓸")
													steal += 1
											no_match=False
										elif len(ffield[k])==2:
											if fobject.name!="Computer":
												print(ffield[k][0],"/",ffield[k][1],"중", end=" ")
											response = Reader.card_choose(fobject,ffield[k][0],ffield[k][1])
											ffield[k].append(fnextcard)
											card = card + ffield[i] + [ffield[k][response]] + [ffield[k][2]]
											if response==0:
												ffield[k]=[ffield[k][1]]
											else:
												ffield[k]=[ffield[k][0]]
											ffield[i]=[]
											last_field = ffield
											temp=False
											count = 0
											for i in ffield: # 싹쓸 
												if i == []:
													count += 1
											if count == 12:
												print("싹쓸")
												steal += 1
											no_match=False
										elif len(ffield[k])==3:
											ffield[k].append(fnextcard)
											card=card+ffield[i]+ffield[k]
											if ffield[k][0].month in fobject.fuck_month:
												print("자뻑 먹음")
												steal +=2
											else:
												print("뻑 먹음")
												steal +=1
											ffield[i]=[]
											ffield[k]=[]
											last_field=ffield
											temp=False
											count = 0
											for i in ffield: # 싹쓸 
												if i == []:
													count += 1
											if count == 12:
												print("싹쓸")
												steal += 1
											no_match=False
							if temp:
								for k in range(12):
									if ffield[k]==[]:
										ffield[k].append(fnextcard)
										break
								card=card+ffield[i]
								ffield[i]=[]
								last_field=ffield
								no_match=False
				if bombcheck: # 흔들기 일때
					print("흔들기")
					fobject.shake
			if bombcheck:
				for fmonth1 in range(12):  # 0 ~ 11
					if len(ffield[fmonth1]) > 0: # 빈 리스트 아님
						if fput.month == ffield[fmonth1][0].month: # 같은 월이 있을때  
							if len(ffield[fmonth1]) == 1: # 같은 월이 1개일떄 
								if fnextcard.month==fput.month: # 뻑
									print("뻑")
									ffield[fmonth1].append(fput)
									ffield[fmonth1].append(fnextcard)
									last_field=ffield
									fobject.fuck
									fobject.fuck_month_add(fput.month)
									no_match=False
								else:
									temp=True
									for k in range(12):
										if len(ffield[k])>0:
											if ffield[k][0].month==fnextcard.month:
												if len(ffield[k])==1:
													ffield[fmonth1].append(fput)
													ffield[k].append(fnextcard)
													card=card+ffield[fmonth1]+ffield[k]
													ffield[fmonth1]=[]
													ffield[k]=[]
													temp=False
													last_field=ffield
													count=0
													for i in ffield: # 싹쓸 
														if i == []:
															count += 1
													if count == 12:
														print("싹쓸")
														steal += 1
													no_match=False
												elif len(ffield[k])==2:
													ffield[fmonth1].append(fput)
													if fobject.name!="Computer":
														print(ffield[k][0],"/",ffield[k][1],"중", end=" ")
													response = Reader.card_choose(fobject,ffield[k][0],ffield[k][1])
													ffield[k].append(fnextcard)
													card = card + ffield[fmonth1] + [ffield[k][response]] + [ffield[k][2]]
													if response==0:
														ffield[k]=[ffield[k][1]]
													else:
														ffield[k]=[ffield[k][0]]
													ffield[fmonth1]=[]
													last_field = ffield
													temp=False
													count=0
													for i in ffield: # 싹쓸 
														if i == []:
															count += 1
													if count == 12:
														print("싹쓸")
														steal += 1
													no_match=False
												elif len(ffield[k])==3:
													ffield[fmonth1].append(fput)
													ffield[k].append(fnextcard)
													card=card+ffield[fmonth1]+ffield[k]
													if ffield[k][0].month in fobject.fuck_month:
														print("자뻑 먹음")
														steal +=2
													else:
														print("뻑 먹음")
														steal +=1
													ffield[fmonth1]=[]
													ffield[k]=[]
													last_field=ffield
													temp=False
													count = 0
													for i in ffield: # 싹쓸 
														if i == []:
															count += 1
													if count == 12:
														print("싹쓸")
														steal += 1
													no_match=False
									if temp:
										ffield[fmonth1].append(fput)
										for k in range(12):
											if ffield[k]==[]:
												ffield[k].append(fnextcard)
												break
										card=card+ffield[fmonth1]
										ffield[fmonth1]=[]
										last_field=ffield
										no_match=False
							elif len(ffield[fmonth1]) == 2: # 같은 월이 2개일떄
								if fnextcard.month == fput.month: # 따닥일때
									print("따닥")
									ffield[fmonth1].append(fput)
									ffield[fmonth1].append(fnextcard)
									card = card + ffield[fmonth1]
									ffield[fmonth1]=[]
									last_field = ffield
									steal += 1
									count = 0
									for i in ffield: # 싹쓸 
										if i == []:
											count += 1
									if count == 12:
										print("싹쓸")
										steal += 1
									no_match=False

								else: # 따닥이 아닐때 
									if fobject.name!="Computer":
										print(ffield[fmonth1][0],"/",ffield[fmonth1][1],"중", end=" ")
									response = Reader.card_choose(fobject,ffield[fmonth1][0],ffield[fmonth1][1])
									temp=True
									for k in range(12):
										if len(ffield[k])>0:
											if ffield[k][0].month==fnextcard.month:
												if len(ffield[k])==1:
													ffield[fmonth1].append(fput)
													ffield[k].append(fnextcard)
													card=card+[ffield[fmonth1][response]]+[ffield[fmonth1][2]]+ffield[k]
													if response==0:
														ffield[fmonth1]=[ffield[fmonth1][1]]
													else:
														ffield[fmonth1]=[ffield[fmonth1][0]]
													ffield[k]=[]
													temp=False
													last_field=ffield
													count=0
													for i in ffield: # 싹쓸 
														if i == []:
															count += 1
													if count == 12:
														print("싹쓸")
														steal += 1
													no_match=False
												elif len(ffield[k])==2:
													ffield[fmonth1].append(fput)
													if fobject.name!="Computer":
														print(ffield[k][0],"/",ffield[k][1],"중", end=" ")
													response2 = Reader.card_choose(fobject,ffield[k][0],ffield[k][1])
													ffield[k].append(fnextcard)
													card = card + [ffield[fmonth1][2]] + [ffield[fmonth1][response]] + [ffield[k][response2]] + [ffield[k][2]]
													if response2==0:
														ffield[k]=[ffield[k][1]]
													if response2==1:
														ffield[k]=[ffield[k][0]]
													if response==0:
														ffield[fmonth1]=[ffield[fmonth1][1]]
													if response==1:
														ffield[fmonth1]=[ffield[fmonth1][0]]
													last_field = ffield
													temp=False
													count=0
													for i in ffield: # 싹쓸 
														if i == []:
															count += 1
													if count == 12:
														print("싹쓸")
														steal += 1
													no_match=False
												elif len(ffield[k])==3:
													ffield[fmonth1].append(fput)
													ffield[k].append(fnextcard)
													card=card+[ffield[fmonth1][response]]+[ffield[fmonth1][2]]+ffield[k]
													if response==0:
														ffield[fmonth1]=[ffield[fmonth1][1]]
													else:
														ffield[fmonth1]=[ffield[fmonth1][0]]
													if ffield[k][0].month in fobject.fuck_month:
														print("자뻑 먹음")
														steal +=2
													else:
														print("뻑 먹음")
														steal +=1
													ffield[k]=[]
													last_field=ffield
													temp=False
													count = 0
													for i in ffield: # 싹쓸 
														if i == []:
															count += 1
													if count == 12:
														print("싹쓸")
														steal += 1
													no_match=False
									if temp:
										ffield[fmonth1].append(fput)
										for k in range(12):
											if ffield[k]==[]:
												ffield[k].append(fnextcard)
												break
										card=card+[ffield[fmonth1][response]]+[ffield[fmonth1][2]]
										if response==0:
											ffield[fmonth1]=[ffield[fmonth1][1]]
										else:
											ffield[fmonth1]=[ffield[fmonth1][0]]
										last_field=ffield
										no_match=False

							elif len(ffield[fmonth1]) == 3: # 같은 월이 3개일떄 
								if ffield[fmonth1][0].month in fobject.fuck_month:
									print("자뻑 먹음")
									steal+=2
								else:
									print("뻑 먹음")
									steal+=1
								temp=True
								for k in range(12):
									if len(ffield[k])>0:
										if ffield[k][0].month==fnextcard.month:
											if len(ffield[k])==1:
												ffield[fmonth1].append(fput)
												ffield[k].append(fnextcard)
												card=card+ffield[fmonth1]+ffield[k]
												ffield[fmonth1]=[]
												ffield[k]=[]
												temp=False
												last_field=ffield
												count=0
												for i in ffield: # 싹쓸 
													if i == []:
														count += 1
												if count == 12:
													print("싹쓸")
													steal += 1
												no_match=False
											elif len(ffield[k])==2:
												ffield[fmonth1].append(fput)
												if fobject.name!="Computer":
													print(ffield[k][0],"/",ffield[k][1],"중", end=" ")
												response = Reader.card_choose(fobject,ffield[k][0],ffield[k][1])
												ffield[k].append(fnextcard)
												card = card + ffield[fmonth1] + [ffield[k][response]] + [ffield[k][2]]
												if response==0:
													ffield[k]=[ffield[k][1]]
												else:
													ffield[k]=[ffield[k][0]]
												ffield[fmonth1]=[]
												last_field = ffield
												temp=False
												count=0
												for i in ffield: # 싹쓸 
													if i == []:
														count += 1
												if count == 12:
													print("싹쓸")
													steal += 1
												no_match=False
											elif len(ffield[k])==3:
												ffield[fmonth1].append(fput)
												ffield[k].append(fnextcard)
												card=card+ffield[fmonth1]+ffield[k]
												if ffield[k][0].month in fobject.fuck_month:
													print("자뻑 먹음")
													steal +=2
												else:
													print("뻑 먹음")
													steal +=1
												ffield[fmonth1]=[]
												ffield[k]=[]
												last_field=ffield
												temp=False
												count = 0
												for i in ffield: # 싹쓸 
													if i == []:
														count += 1
												if count == 12:
													print("싹쓸")
													steal += 1
												no_match=False
								if temp:
									ffield[fmonth1].append(fput)
									for k in range(12):
										if ffield[k]==[]:
											ffield[k].append(fnextcard)
											break
									card=card+ffield[fmonth1]
									ffield[fmonth1]=[]
									last_field=ffield
									no_match=False
				if no_match:
					for k in range(12):
						if ffield[k]==[]:
							ffield[k].append(fput)
							break
					temp=True
					for k in range(12):
						if len(ffield[k])>0:
							if ffield[k][0].month==fnextcard.month==fput.month:
								print("쪽")
								steal+=1
								ffield[k].append(fnextcard)
								card=card+ffield[k]
								ffield[k]=[]
								temp=False
								last_field=ffield
								count=0
								for i in ffield: # 싹쓸 
									if i == []:
										count += 1
								if count == 12:
									print("싹쓸")
									steal += 1
							elif ffield[k][0].month==fnextcard.month!=fput.month:
								if len(ffield[k])==1:
									ffield[k].append(fnextcard)
									card=card+ffield[k]
									ffield[k]=[]
									temp=False
									last_field=ffield
									count=0
									for i in ffield: # 싹쓸 
										if i == []:
											count += 1
									if count == 12:
										print("싹쓸")
										steal += 1
								elif len(ffield[k])==2:
									if fobject.name!="Computer":
										print(ffield[k][0],"/",ffield[k][1],"중", end=" ")
									response = Reader.card_choose(fobject,ffield[k][0],ffield[k][1])
									ffield[k].append(fnextcard)
									card = card + [ffield[k][response]] + [ffield[k][2]]
									if response==0:
										ffield[k]=[ffield[k][1]]
									else:
										ffield[k]=[ffield[k][0]]
									last_field = ffield
									temp=False
									count=0
									for i in ffield: # 싹쓸 
										if i == []:
											count += 1
									if count == 12:
										print("싹쓸")
										steal += 1
								elif len(ffield[k])==3:
									ffield[k].append(fnextcard)
									card=card+ffield[k]
									if ffield[k][0].month in fobject.fuck_month:
										print("자뻑 먹음")
										steal +=2
									else:
										print("뻑 먹음")
										steal +=1
									ffield[k]=[]
									last_field=ffield
									temp=False
									count = 0
									for i in ffield: # 싹쓸 
										if i == []:
											count += 1
									if count == 12:
										print("싹쓸")
										steal += 1
					if temp:
						for k in range(12):
							if ffield[k]==[]:
								ffield[k].append(fnextcard)
								break
						last_field=ffield

		return (card,last_field,steal)
   

# 1.일단 낸 카드의 월이 패에 2장 더 있는지 본다
# 2. 있으면 필드를 보고 흔들기인지 폭탄인지 확인한다
# 3. 없으면 필드에 낸다. 
# 3-a. 필드에 같은 월이 한장
# 3-a-a 덱 뒤집어서 같은월이면 뻑
# 3-b. 필드에 같은 월이 두장 : 먹을카드 선택
# 3-b-a. 덱 뒤집어서 같은월이면 따닥
# 3-c. 필드에 같은 월이 세장 : 네장 모두 리스트에 넣고 peerob+1 (뻑 먹기)
# 3-d 필드에 같은 월이 0장
# 3-d-a 덱 뒤집어서 같은월이면 쪽




	# 한개도 못 먹었을 경우 / 2개 먹었을 경우 / 4개 먹었을 경우 
	#(필드에 2개가 깔려있을 경우 무엇을 먹을지 선택하도록 해야함. 
	#필요에 따라 matgoview에 추가할것.)
	# 뻑, 따닥, 쪽, 폭탄, 싹쓸, 흔들기
	# 폭탄이라면 객체의 손에 폭탄카드 2개를 부여해야 함.
	# (먹은 카드(리스트), 처리한 다음 필드, 
	#상대에게서 가져와야 할 피의 개수) -------> 튜플로 리턴