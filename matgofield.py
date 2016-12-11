from matgohand import *
from matgocard import *
from matgoview import *
"""
If a player or computer put a card, then calculate and return the field after one puts
"""
# If a player or computer put a card, then calculate and return the field after one puts
class fields:
	def __init__(self, ob, put, field, nextcard, bomb):
		self.__object=ob 
		self.__put=put
		self.__field=field
		self.__nextcard=nextcard
		self.__bomb=bomb

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
		response=0
		respons2=0

		if self.__bomb:
			check=True
			for k in range(12):
				if len(ffield[k])>0:
					if fnextcard.month == ffield[k][0].month:
						if len(ffield[k]) == 1:
							ffield[k].append(fnextcard)
							card = card + ffield[k]
							ffield[k]=[]
							last_field = ffield
							count = 0
							check=False
							for i in ffield:
								if i == []:
									count += 1
							if count == 12:
								print("싹쓸")
								steal += 1
												
						elif len(ffield[k]) == 2:
							if fobject.name!="Computer":
								response = Reader.card_choose(fobject,ffield[k][0],ffield[k][1]) 
							ffield[k].append(fnextcard)
							card = card + [ffield[k][response]] + [ffield[k][2]]
							if response==0:
								ffield[k]=[ffield[k][1]]
							else:
								ffield[k]=[ffield[k][0]]
							last_field = ffield
							check=False																
										
						elif len(ffield[k]) == 3:
							if fnextcard.month in fobject.fuck_month:
								ffield[k].append(fnextcard)
								card = card + ffield[k]
								ffield[k] = []
								last_field = ffield
								steal += 2
								print("자뻑 먹음")
							else:
								ffield[k].append(fnextcard)
								card = card + ffield[k]
								ffield[k] = []
								last_field = ffield
								steal += 1
								print("뻑 먹음")
							count = 0
							for i in ffield: 
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

		else:
			bomb = 0
			for i in fhand:
				if i.month == fput.month:
					bomb += 1
			if bomb == 2:
				for i in range(12):
					if len(ffield[i])>0:
						if ffield[i][0].month == fput.month:
							print("폭탄")
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
											for i in ffield: 
												if i == []:
													count += 1
												if count == 12:
													print("싹쓸")
													steal += 1
											no_match=False
										elif len(ffield[k])==2:
											if fobject.name!="Computer":
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
											for i in ffield: #
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
											for i in ffield:
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
				if bombcheck:
					print("흔들기")
					fobject.shake
			if bombcheck:
				for fmonth1 in range(12): 
					if len(ffield[fmonth1]) > 0:
						if fput.month == ffield[fmonth1][0].month:
							if len(ffield[fmonth1]) == 1: 
								if fnextcard.month==fput.month: 
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
													for i in ffield: 
														if i == []:
															count += 1
													if count == 12:
														print("싹쓸")
														steal += 1
													no_match=False
												elif len(ffield[k])==2:
													ffield[fmonth1].append(fput)
													if fobject.name!="Computer":
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
													for i in ffield:  
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
													for i in ffield:
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
							elif len(ffield[fmonth1]) == 2:
								if fnextcard.month == fput.month: 
									print("따닥")
									ffield[fmonth1].append(fput)
									ffield[fmonth1].append(fnextcard)
									card = card + ffield[fmonth1]
									ffield[fmonth1]=[]
									last_field = ffield
									steal += 1
									count = 0
									for i in ffield: 
										if i == []:
											count += 1
									if count == 12:
										print("싹쓸")
										steal += 1
									no_match=False

								else:
									if fobject.name!="Computer":
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
													for i in ffield:
														if i == []:
															count += 1
													if count == 12:
														print("싹쓸")
														steal += 1
													no_match=False
												elif len(ffield[k])==2:
													ffield[fmonth1].append(fput)
													if fobject.name!="Computer":
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
													for i in ffield: 
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
													for i in ffield: 
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

							elif len(ffield[fmonth1]) == 3:
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
												for i in ffield:
													if i == []:
														count += 1
												if count == 12:
													print("싹쓸")
													steal += 1
												no_match=False
											elif len(ffield[k])==2:
												ffield[fmonth1].append(fput)
												if fobject.name!="Computer":
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
												for i in ffield:
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
												for i in ffield: 
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
								for i in ffield:
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
									for i in ffield:
										if i == []:
											count += 1
									if count == 12:
										print("싹쓸")
										steal += 1
								elif len(ffield[k])==2:
									if fobject.name!="Computer":
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
									for i in ffield:
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
									for i in ffield:
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