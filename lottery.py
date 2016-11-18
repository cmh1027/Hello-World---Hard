import random
import tkinter as tk
from matgo import *
from tkinter import *
from tkinter import font
from daylotto import *
import time
"""
Simulator Mainclass
"""
# Simulator Mainclass
class Main:
	"""
	Constructor
	"""
	# Constructor.
	def __init__(self, root):
		self.money=25000000
		self.announce=""
		self.date=1
		self.police_stars=0
		self.bank_debt=0
		self.private_debt=0
		self.root=root
		self.choosehorse=[]
		self.chooseimm=[]
		self.immlotto=[0,0,0,0,0]
		Label(self.root ,text = "").grid(row=1, column=0)
		Label(self.root ,text = "          ").grid(row=2, column=0)
		Label(self.root ,text = "             ").grid(row=0, column=2)
		Label(self.root ,text = "             ").grid(row=0, column=4)
		font = tk.font.Font(self.root, size=13)
		font2 = tk.font.Font(self.root, size=11)
		self.asset = Label(self.root,text = "현재 전재산 : "+str(self.money), relief="solid", padx=5, pady=5)
		self.asset['font']=font2
		self.asset.place(x=1, y=1)
		self.info = Label(self.root,text = " <                 상황판                 >\n짜릿한 주갤러의 인생을 즐겨보세요!"+self.announce)
		self.info.place(x=410, y=0)
		self.today = Label(self.root,text = "도박인생 "+str(self.date)+"일차", relief="solid", padx=5, pady=5)
		self.today['font']=font2
		self.today.place(x=230, y=0)
		self.stocklist=[[],[],[],[],[],[],[],[],[],[]] # [이름, 남은개수, 가격]
		self.stockfluct=[[],[],[],[],[],[],[],[],[],[]]
		self.havestock=[[],[],[],[],[],[],[],[],[],[]] # [이름, 개수]
		self.namelist=["사성", "랏데", "제일", "와이", "근대", "피케", "한하", "도산", "넥손", "키아"]
		self.sortlist=["전자", "물류", "중공", "산업", "종합", "홀딩", "물산", "통신", "군수", "엘씨"]
		for k in range(10):
			while True:
				check=True
				a = random.randrange(10)
				b = random.randrange(10)
				name=self.namelist[a]+self.sortlist[b]
				for i in range(10):
					if name in self.stocklist[i]:
						check=False
						break
				if check:
					self.stocklist[k].append(name)
					self.stocklist[k].append(100)
					self.stocklist[k].append(100000-100*random.randrange(-150, 151))
					break
	"""
	Adding Announcement
	"""
	# Adding Announcement (< 상황판 >)
	def addannounce(self, string, root):
		self.police_stars-=random.randrange(5, 25)
		eat_ran=100*random.randrange(60, 150)
		self.announce="하루 식비로 "+str(eat_ran)+"원이 나갔습니다.\n"
		self.money-=eat_ran
		event=random.randrange(100)
		if self.date%7==0:
			self.announce+="세금으로 30만원이 나갔습니다.\n"
			self.money-=300000
		if event==10:
			lob_ran=10000*random.randrange(30, 1000)
			self.announce+="강도에게 "+str(lob_ran)+"원을 빼앗겼습니다.\n"
			self.money-=lob_ran
		elif event==20:
			lob_ran=100000*random.randrange(20, 300)
			self.announce+="고소를 당해 "+str(lob_ran)+"원을 잃었습니다.\n"
			self.money-=lob_ran
		elif event==30:
			lob_ran = 100000*random.randrange(5, 100)
			self.announce+="사기를 당해 "+str(lob_ran)+"원을 잃었습니다.\n"
			self.money-=lob_ran
		elif event==40:
			lob_ran = 100000*random.randrange(5, 100)
			self.announce+="큰 병에 걸려 병원비로 \n"+str(lob_ran)+"원을 지출했습니다.\n"
			self.money-=lob_ran
		if self.money>0:
			self.announce+=string
			if self.police_stars >= 150:
				self.announce+="잦은 사기로 현상수배범에 올랐습니다.\n"
			if self.bank_debt>0:
				self.announce+="현재 대출빚이 "+str(self.bank_debt)+"원입니다.\n이자로 "+str(int(self.bank_debt*0.05))+"원이 빠져나갑니다.\n"
				self.money-=int(self.bank_debt*0.05)
			if self.private_debt>0:
				self.announce+="현재 사채빚이 "+str(self.private_debt)+"원입니다.\n이자로 "+str(int(self.private_debt*0.2))+"원이 빠져나갑니다.\n"
				self.money-=int(self.private_debt*0.2)
		for i in range(10):
			fluct=100*random.randrange(-175, 151)
			if len(self.stockfluct[i])==10:
				self.stockfluct[i].pop(0)
				self.stockfluct[i].append(fluct)
			else:
				self.stockfluct[i].append(fluct)
			self.stocklist[i][2]+=fluct
			for k in range(10):
				if self.stocklist[i][0] in self.havestock[k]:
					if fluct>=0:
						self.announce+=self.havestock[k][0]+"("+str(self.havestock[k][1])+"주 보유)"+" ↑"+str(fluct)+"\n"
					else:
						self.announce+=self.havestock[k][0]+"("+str(self.havestock[k][1])+"주 보유)"+" ↓"+str(-1*fluct)+"\n"
		for i in range(10):
			if self.stocklist[i][2]<=0:
				for k in range(10):
					if self.stocklist[i][0] in self.havestock[k]:
						self.announce+="보유주식 중 하나가 부도났습니다.\n"
						self.announce+="부도난 회사 : " + self.havestock[k][0]+"\n"
						self.havestock[k]=[]
				self.stocklist[i]=[]
				self.stockfluct[i]=[]
				while True:
					check=True
					name=self.namelist[random.randrange(10)]+self.sortlist[random.randrange(10)]
					for j in range(10):
						if name in self.stocklist[j]:
							check=False
							break
					if check:
						self.stocklist[i].append(name)
						self.stocklist[i].append(100)
						self.stocklist[i].append(100000-100*random.randrange(-150, 151))
		self.update()
		total=0
		for i in range(10):
			if len(self.havestock[i])!=0:
				total+=self.havestock[i][1]*self.stocklist[i][2]

		if self.money<=0:
			if self.money+total>0:
				self.announce+="파산 위기에 주식을 모두 매각했습니다.\n"
				self.money+=total
				for i in range(10):
					if len(self.havestock[i])!=0:
						self.stocklist[i][1]+=self.havestock[i][1]
						self.havestock[i]=[]
				self.update()
			else:
				self.money=0
				gg=Toplevel(root)
				field_pic=PhotoImage(file="./images/gg.png")
				field=Label(gg, image=field_pic)
				field.place(x=0, y=0)
				gg.title("게임 오버")
				gg.geometry("280x186")
				font = tk.font.Font(self.root, size=12)
				msg = Label(gg, text="파산하셨습니다.\n오늘은 한강물이 차갑군요.")
				msg['font']=font
				msg.place(x=45, y=20)
				def quit():
					root.destroy()
					root.quit()
					self.root.destroy()
					self.root.quit()
				Button(gg,text = "확인", command = quit).place(x=120, y=150)	
				gg.mainloop()
		if self.money>0:
			return True
	"""
	updating the main menu screen
	"""
	# updating the main menu screen
	def update(self):
		font = tk.font.Font(self.root, size=13)
		font2 = tk.font.Font(self.root, size=11)
		self.asset.destroy()
		self.asset = Label(self.root,text = "현재 전재산 : "+str(self.money), relief="solid", padx=5, pady=5)
		self.asset['font']=font2
		self.asset.place(x=1, y=1)
		self.info.destroy()
		self.info = Label(self.root,text = "<                 상황판                 >\n"+self.announce)
		self.info.place(x=410, y=0)
		self.today.destroy
		self.today = Label(self.root,text = "도박인생 "+str(self.date)+"일차", relief="solid", padx=5, pady=5)
		self.today['font']=font2
		self.today.place(x=230, y=0)

	"""
	checking whether player is arrested or not
	"""
	# checking whether player is arrested or not
	def arrested(self):
		r=random.randrange(1000)
		if r<self.police_stars:
			arrestroot = Toplevel(self.root)
			field_pic=PhotoImage(file = "./images/arrest.png")
			field=Label(arrestroot, image=field_pic)
			field.place(x=0, y=0)
			arrestroot.title("체포되었습니다")
			arrestroot.geometry("320x202")
			font = tk.font.Font(self.root, size=12)
			msg = Label(arrestroot, text="경찰에 체포되셨습니다.\n인생을 돌아보십시오.")
			msg['font']=font
			msg.place(x=70, y=100)
			def quit():
				self.root.destroy()
				self.root.quit()
				return False
			Button(arrestroot,text = "확인", command = quit).place(x=137, y=150)
			arrestroot.mainloop()
		else:
			return True

	"""
	Mainscreen, Start the game by this method
	"""
	# Mainscreen, Start the game by this method
	def mainscreen(self):
		"""
		daylotto. 일일복권
		"""
		# daylotto. 일일복권
		def d_lotto():
			window=Toplevel(self.root)
			result = day_lotto_start(window)
			resultroot = Toplevel(self.root)
			resultroot.title("결과")
			resultroot.geometry("160x160")
			field_pic=PhotoImage(file = "./images/gold.png")
			field=Label(resultroot, image=field_pic).place(x=0, y=0)
			font2 = tk.font.Font(self.root, size=11)
			def quit():
				self.date+=1
				self.money-=1000000
				string="일일복권으로 "+str(result)+"원을 얻었습니다.\n복권가격으로 100만원을 사용했습니다."
				self.money+=result
				check = self.addannounce(string, resultroot)
				if check:
					self.update()
					resultroot.destroy()
					resultroot.quit()
			if int(result)>=0:
				get=Label(resultroot, text=str(result)+"원을\n따냈습니다.\n")
				get['font']=font2
				get.place(x=35, y=30)
			else:
				get=Label(resultroot, text=str(result*(-1))+"원을\n잃었습니다.\n")
				get['font']=font2
				get.place(x=35, y=30)
			font = tk.font.Font(self.root, size=13)
			quitbutton=Button(resultroot,text = "확인", command = quit)
			quitbutton['font']=font
			quitbutton.place(x=60, y=115)
			resultroot.mainloop()
		"""
		immediate lotto. 즉석복권
		"""
		# immediate lotto. 즉석복권
		def i_lotto():
			self.chooseimm=[]
			self.immlotto=[0, 0, 0, 0, 0]
			while len(self.chooseimm)!=100:
				number = random.randrange(1, 8145061)
				if number not in self.chooseimm:
					self.chooseimm.append(number)
			for i in self.chooseimm:
				if 3821291<=i<3821296:
					self.immlotto[0]+=1
				elif 5182932<=i<5183181:
					self.immlotto[1]+=1
				elif 582<=i<3582:
					self.immlotto[2]+=1
				elif 688428<=i<884231:
					self.immlotto[3]+=1
				elif 1042912<=i<1342912:
					self.immlotto[4]+=1
			immroot = Toplevel(self.root)
			immroot.title("즉석복권")
			immroot.geometry("320x195")
			field_pic=PhotoImage(file = "./images/imm_lottery.png")
			field=Label(immroot, image=field_pic)
			field.place(x=0, y=0)
			font = tk.font.Font(root, size=13, weight='bold')
			font2 = tk.font.Font(root, size=11)
			msg=Label(immroot, text="즉석복권 100개를 사서 긁었습니다.")
			msg['font']=font
			msg.place(x=25, y=3)
			k=0
			if self.immlotto[0]>0:
				one=Label(immroot, text="1등이 "+str(self.immlotto[0])+"번 당첨되었습니다.")
				one['font']=font2
				one.place(x=70, y=40)
				k+=1
			if self.immlotto[1]>0:
				two=Label(immroot, text="2등이 "+str(self.immlotto[1])+"번 당첨되었습니다.")
				two['font']=font2
				two.place(x=70, y=40+23*k)
				k+=1
			if self.immlotto[2]>0:
				three=Label(immroot, text="3등이 "+str(self.immlotto[2])+"번 당첨되었습니다.")
				three['font']=font2
				three.place(x=70, y=40+23*k)
				k+=1
			if self.immlotto[3]>0:
				four=Label(immroot, text="4등이 "+str(self.immlotto[3])+"번 당첨되었습니다.")
				four['font']=font2
				four.place(x=70, y=40+23*k)
				k+=1
			if self.immlotto[4]>0:
				five=Label(immroot, text="5등이 "+str(self.immlotto[4])+"번 당첨되었습니다.")
				five['font']=font2
				five.place(x=70, y=40+23*k)
			def quit():
				self.date+=1
				self.money-=1000000
				addmoney=3000000000*self.immlotto[0]+300000000*self.immlotto[1]+5000000*self.immlotto[2]+100000*self.immlotto[3]+10000*self.immlotto[4]
				string="즉석복권에 100만원을 사용했습니다.\n"+"1등이 "+str(self.immlotto[0])+"번\n"+"2등이 "+str(self.immlotto[1])+"번\n"+"3등이 "+str(self.immlotto[2])+"번\n"
				string+="4등이 "+str(self.immlotto[3])+"번\n"+"5등이 "+str(self.immlotto[4])+"번\n당첨되었습니다.\n"+str(addmoney)+"원을 얻었습니다.\n"
				self.money+=addmoney
				check = self.addannounce(string, immroot)
				if check:
					self.update()
					immroot.destroy()
					immroot.quit()				
			quitbutton=Button(immroot,text = "확인", command = quit)
			quitbutton.place(x=147, y=160)
			immroot.mainloop()

		"""
		lotto. 로또복권
		"""
		# lotto. 로또복권
		def l_lotto():
			chooselotto=[]
			lotto=[]
			chosen=0
			for _ in range(7):
				while True:
					number=random.randrange(1, 46)
					if number not in lotto:
						lotto.append(number)
						break
			lottoroot = Toplevel(self.root)
			lottoroot.title("로또복권")
			lottoroot.geometry("410x324")
			field_pic=PhotoImage(file = "./images/lotto.png")
			field=Label(lottoroot, image=field_pic)
			field.place(x=0, y=0)
			font = tk.font.Font(root, size=16, weight='bold')
			msg=Label(lottoroot, text="7개의 번호를 고르세요")
			msg['font']=font
			msg.place(x=100, y=15)
			font = tk.font.Font(root, size=13)
			"""
			checking the numbers chosen
			"""
			# checking the numbers chosen
			def determine():
				resultroot=Toplevel(lottoroot)
				resultroot.title("결과")
				resultroot.geometry("360x120")
				font_1 = tk.font.Font(root, size=12, weight='bold')
				font_2 = tk.font.Font(root, size=24, weight='bold')
				for i in range(7):
					if 1<=chooselotto[i]<=9:
						chooselotto[i]="0"+str(chooselotto[i])
					else:
						chooselotto[i]=str(chooselotto[i])
				cho = Label(resultroot, text="고른 숫자 : "+chooselotto[0]+" "+chooselotto[1]+" "+\
				chooselotto[2]+" "+chooselotto[3]+" "+chooselotto[4]+" "+chooselotto[5]+" ["+chooselotto[6]+"] ")
				cho['font']=font_1
				cho.place(x=55, y=90)
				for i in range(7):
					if 1<=lotto[i]<=9:
						lotto[i]="0"+str(lotto[i])
					else:
						lotto[i]=str(lotto[i])
				string=lotto[0]+" "+lotto[1]+" "+lotto[2]+" "+lotto[3]+" "+lotto[4]+" "+lotto[5]+" ["+lotto[6]+"] "
				lt = Label(resultroot, text=string)
				lt['font']=font_2
				lt.place(x=11, y=30)
				def quit():
					resultroot.destroy()
					resultroot.quit()
					count=0
					bonus=False
					for i in range(6):
						if chooselotto[i] in lotto:
							count+=1
					if chooselotto[6] in lotto:
						bonus=True
					if count==6:
						string="1등에 당첨되셨습니다. \n상금은 50억원입니다.\n"
						self.money+=5000000000
					elif count==5 and bonus:
						string="2등에 당첨되셨습니다. \n상금은 1억원입니다.\n\n"
						self.money+=100000000
					elif count==5 and not bonus:
						string="3등에 당첨되셨습니다. \n상금은 2000만원입니다.\n"
						self.money+=20000000
					elif count==4:
						string="4등에 당첨되셨습니다. \n상금은 500만원입니다.\n"
						self.money+=5000000
					elif count==3:
						string="5등에 당첨되셨습니다. \n상금은 100만원입니다.\n"
						self.money+=1000000
					elif count==2:
						string="6등에 당첨되셨습니다. \n상금은 25만원입니다.\n"
						self.money+=250000
					else:
						string="꽝이 걸렸습니다.\n"
					self.money-=250000
					check=self.addannounce("로또복권을 25만원에 구입했습니다.\n"+string, lottoroot)
					if check:
						self.update()
						lottoroot.destroy()
						lottoroot.quit()
				quitbt=Button(resultroot, text="확인", command=quit)
				quitbt.place(x=320, y=5)
				resultroot.mainloop()
			def n1():
				if 1 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(1)
					b1['font']=font
					b1.place(x=35, y=70)
				if len(chooselotto)==7:
					determine()
			def n2():
				if 2 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(2)
					b1['font']=font
					b1.place(x=75, y=70)
				if len(chooselotto)==7:
					determine()
			def n3():
				if 3 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(3)
					b1['font']=font
					b1.place(x=115, y=70)
				if len(chooselotto)==7:
					determine()
			def n4():
				if 4 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(4)
					b1['font']=font
					b1.place(x=155, y=70)
				if len(chooselotto)==7:
					determine()
			def n5():
				if 5 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(5)
					b1['font']=font
					b1.place(x=195, y=70)
				if len(chooselotto)==7:
					determine()
			def n6():
				if 6 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(6)
					b1['font']=font
					b1.place(x=235, y=70)
				if len(chooselotto)==7:
					determine()
			def n7():
				if 7 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(7)
					b1['font']=font
					b1.place(x=275, y=70)
				if len(chooselotto)==7:
					determine()
			def n8():
				if 8 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(8)
					b1['font']=font
					b1.place(x=315, y=70)
				if len(chooselotto)==7:
					determine()
			def n9():
				if 9 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(9)
					b1['font']=font
					b1.place(x=355, y=70)
				if len(chooselotto)==7:
					determine()
			def n10():
				if 10 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(10)
					b1['font']=font
					b1.place(x=35, y=115)
				if len(chooselotto)==7:
					determine()
			def n11():
				if 11 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(11)
					b1['font']=font
					b1.place(x=75, y=115)
				if len(chooselotto)==7:
					determine()
			def n12():
				if 12 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(12)
					b1['font']=font
					b1.place(x=115, y=115)
				if len(chooselotto)==7:
					determine()
			def n13():
				if 13 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(13)
					b1['font']=font
					b1.place(x=155, y=115)
				if len(chooselotto)==7:
					determine()
			def n14():
				if 14 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(14)
					b1['font']=font
					b1.place(x=195, y=115)
				if len(chooselotto)==7:
					determine()
			def n15():
				if 15 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(15)
					b1['font']=font
					b1.place(x=235, y=115)
				if len(chooselotto)==7:
					determine()
			def n16():
				if 16 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(16)
					b1['font']=font
					b1.place(x=275, y=115)
				if len(chooselotto)==7:
					determine()
			def n17():
				if 17 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(17)
					b1['font']=font
					b1.place(x=315, y=115)
				if len(chooselotto)==7:
					determine()
			def n18():
				if 18 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(18)
					b1['font']=font
					b1.place(x=355, y=115)
				if len(chooselotto)==7:
					determine()
			def n19():
				if 19 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(19)
					b1['font']=font
					b1.place(x=35, y=160)
				if len(chooselotto)==7:
					determine()
			def n20():
				if 20 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(20)
					b1['font']=font
					b1.place(x=75, y=160)
				if len(chooselotto)==7:
					determine()
			def n21():
				if 21 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(21)
					b1['font']=font
					b1.place(x=115, y=160)
				if len(chooselotto)==7:
					determine()
			def n22():
				if 22 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(22)
					b1['font']=font
					b1.place(x=155, y=160)
				if len(chooselotto)==7:
					determine()
			def n23():
				if 23 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(23)
					b1['font']=font
					b1.place(x=195, y=160)
				if len(chooselotto)==7:
					determine()
			def n24():
				if 24 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(24)
					b1['font']=font
					b1.place(x=235, y=160)
				if len(chooselotto)==7:
					determine()
			def n25():
				if 25 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(25)
					b1['font']=font
					b1.place(x=275, y=160)
				if len(chooselotto)==7:
					determine()
			def n26():
				if 26 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(26)
					b1['font']=font
					b1.place(x=315, y=160)
				if len(chooselotto)==7:
					determine()
			def n27():
				if 27 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(27)
					b1['font']=font
					b1.place(x=355, y=160)
				if len(chooselotto)==7:
					determine()
			def n28():
				if 28 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(28)
					b1['font']=font
					b1.place(x=35, y=205)
				if len(chooselotto)==7:
					determine()
			def n29():
				if 29 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(29)
					b1['font']=font
					b1.place(x=75, y=205)
				if len(chooselotto)==7:
					determine()
			def n30():
				if 30 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(30)
					b1['font']=font
					b1.place(x=115, y=205)
				if len(chooselotto)==7:
					determine()
			def n31():
				if 31 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(31)
					b1['font']=font
					b1.place(x=155, y=205)
				if len(chooselotto)==7:
					determine()
			def n32():
				if 32 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(32)
					b1['font']=font
					b1.place(x=195, y=205)
				if len(chooselotto)==7:
					determine()
			def n33():
				if 33 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(33)
					b1['font']=font
					b1.place(x=235, y=205)
				if len(chooselotto)==7:
					determine()
			def n34():
				if 34 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(34)
					b1['font']=font
					b1.place(x=275, y=205)
				if len(chooselotto)==7:
					determine()
			def n35():
				if 35 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(35)
					b1['font']=font
					b1.place(x=315, y=205)
				if len(chooselotto)==7:
					determine()
			def n36():
				if 36 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(36)
					b1['font']=font
					b1.place(x=355, y=205)
				if len(chooselotto)==7:
					determine()
			def n37():
				if 37 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(37)
					b1['font']=font
					b1.place(x=35, y=250)
				if len(chooselotto)==7:
					determine()
			def n38():
				if 38 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(38)
					b1['font']=font
					b1.place(x=75, y=250)
				if len(chooselotto)==7:
					determine()
			def n39():
				if 39 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(39)
					b1['font']=font
					b1.place(x=115, y=250)
				if len(chooselotto)==7:
					determine()
			def n40():
				if 40 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(40)
					b1['font']=font
					b1.place(x=155, y=250)
				if len(chooselotto)==7:
					determine()
			def n41():
				if 41 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(41)
					b1['font']=font
					b1.place(x=195, y=250)
				if len(chooselotto)==7:
					determine()
			def n42():
				if 42 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(42)
					b1['font']=font
					b1.place(x=235, y=250)
				if len(chooselotto)==7:
					determine()
			def n43():
				if 43 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(43)
					b1['font']=font
					b1.place(x=275, y=250)
				if len(chooselotto)==7:
					determine()
			def n44():
				if 44 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(44)
					b1['font']=font
					b1.place(x=315, y=250)
				if len(chooselotto)==7:
					determine()
			def n45():
				if 45 not in chooselotto:
					b1=Label(lottoroot, text="    ")
					chooselotto.append(45)
					b1['font']=font
					b1.place(x=355, y=250)
				if len(chooselotto)==7:
					determine()
			b1 = Button(lottoroot, text="01", command=n1)
			b1.place(x=35, y=70)
			b1['font']=font
			b2 = Button(lottoroot, text="02", command=n2)
			b2.place(x=75, y=70)
			b2['font']=font
			b3 = Button(lottoroot, text="03", command=n3)
			b3.place(x=115, y=70)
			b3['font']=font
			b4 = Button(lottoroot, text="04", command=n4)
			b4.place(x=155, y=70)
			b4['font']=font
			b5 = Button(lottoroot, text="05", command=n5)
			b5.place(x=195, y=70)
			b5['font']=font
			b6 = Button(lottoroot, text="06", command=n6)
			b6.place(x=235, y=70)
			b6['font']=font
			b7 = Button(lottoroot, text="07", command=n7)
			b7.place(x=275, y=70)
			b7['font']=font
			b8 = Button(lottoroot, text="08", command=n8)
			b8.place(x=315, y=70)
			b8['font']=font
			b9 = Button(lottoroot, text="09", command=n9)
			b9.place(x=355, y=70)
			b9['font']=font
			###################
			b10 = Button(lottoroot, text="10", command=n10)
			b10.place(x=35, y=115)
			b10['font']=font
			b11 = Button(lottoroot, text="11", command=n11)
			b11.place(x=75, y=115)
			b11['font']=font
			b12 = Button(lottoroot, text="12", command=n12)
			b12.place(x=115, y=115)
			b12['font']=font
			b13 = Button(lottoroot, text="13", command=n13)
			b13.place(x=155, y=115)
			b13['font']=font
			b14 = Button(lottoroot, text="14", command=n14)
			b14.place(x=195, y=115)
			b14['font']=font
			b15 = Button(lottoroot, text="15", command=n15)
			b15.place(x=235, y=115)
			b15['font']=font
			b16 = Button(lottoroot, text="16", command=n16)
			b16.place(x=275, y=115)
			b16['font']=font
			b17 = Button(lottoroot, text="17", command=n17)
			b17.place(x=315, y=115)
			b17['font']=font
			b18 = Button(lottoroot, text="18", command=n18)
			b18.place(x=355, y=115)
			b18['font']=font
			###################
			b19 = Button(lottoroot, text="19", command=n19)
			b19.place(x=35, y=160)
			b19['font']=font
			b20 = Button(lottoroot, text="20", command=n20)
			b20.place(x=75, y=160)
			b20['font']=font
			b21 = Button(lottoroot, text="21", command=n21)
			b21.place(x=115, y=160)
			b21['font']=font
			b22 = Button(lottoroot, text="22", command=n22)
			b22.place(x=155, y=160)
			b22['font']=font
			b23 = Button(lottoroot, text="23", command=n23)
			b23.place(x=195, y=160)
			b23['font']=font
			b24 = Button(lottoroot, text="24", command=n24)
			b24.place(x=235, y=160)
			b24['font']=font
			b25 = Button(lottoroot, text="25", command=n25)
			b25.place(x=275, y=160)
			b25['font']=font
			b26 = Button(lottoroot, text="26", command=n26)
			b26.place(x=315, y=160)
			b26['font']=font
			b27 = Button(lottoroot, text="27", command=n27)
			b27.place(x=355, y=160)
			b27['font']=font
			###################
			b28 = Button(lottoroot, text="28", command=n28)
			b28.place(x=35, y=205)
			b28['font']=font
			b29 = Button(lottoroot, text="29", command=n29)
			b29.place(x=75, y=205)
			b29['font']=font
			b30 = Button(lottoroot, text="30", command=n30)
			b30.place(x=115, y=205)
			b30['font']=font
			b31 = Button(lottoroot, text="31", command=n31)
			b31.place(x=155, y=205)
			b31['font']=font
			b32 = Button(lottoroot, text="32", command=n32)
			b32.place(x=195, y=205)
			b32['font']=font
			b33 = Button(lottoroot, text="33", command=n33)
			b33.place(x=235, y=205)
			b33['font']=font
			b34 = Button(lottoroot, text="34", command=n34)
			b34.place(x=275, y=205)
			b34['font']=font
			b35 = Button(lottoroot, text="35", command=n35)
			b35.place(x=315, y=205)
			b35['font']=font
			b36 = Button(lottoroot, text="36", command=n36)
			b36.place(x=355, y=205)
			b36['font']=font
			###################
			b37 = Button(lottoroot, text="37", command=n37)
			b37.place(x=35, y=250)
			b37['font']=font
			b38 = Button(lottoroot, text="38", command=n38)
			b38.place(x=75, y=250)
			b38['font']=font
			b39 = Button(lottoroot, text="39", command=n39)
			b39.place(x=115, y=250)
			b39['font']=font
			b40 = Button(lottoroot, text="40", command=n40)
			b40.place(x=155, y=250)
			b40['font']=font
			b41 = Button(lottoroot, text="41", command=n41)
			b41.place(x=195, y=250)
			b41['font']=font
			b42 = Button(lottoroot, text="42", command=n42)
			b42.place(x=235, y=250)
			b42['font']=font
			b43 = Button(lottoroot, text="43", command=n43)
			b43.place(x=275, y=250)
			b43['font']=font
			b44 = Button(lottoroot, text="44", command=n44)
			b44.place(x=315, y=250)
			b44['font']=font
			b45 = Button(lottoroot, text="45", command=n45)
			b45.place(x=355, y=250)
			b45['font']=font	
			lottoroot.mainloop()

		"""
		Matgo (맞고)
		"""
		# Matgo (맞고)
		def matgo():
			result=matgostart(self.root, self.money)
			resultroot = Toplevel(self.root)
			resultroot.title("결과")
			resultroot.geometry("290x171")
			field_pic=PhotoImage(file = "./images/hwato.png")
			field=Label(resultroot, image=field_pic).place(x=0, y=0)
			def quit():
				self.date+=1
				self.money+=int(result)
				if int(result)>=0:
					check = self.addannounce(str(result)+"원을 맞고로 얻었습니다.\n", resultroot)
				else:
					check = self.addannounce(str(result*(-1))+"원을 맞고로 잃었습니다.\n", resultroot)
				if check:
					self.update()
					resultroot.destroy()
					resultroot.quit()
			if int(result)>=0:
				Label(resultroot, text=str(result)+"원을 얻었습니다.").place(x=80, y=100)
			else:
				Label(resultroot, text=str(result*(-1))+"원을 잃었습니다.").place(x=80, y=100)
			quitbutton=Button(resultroot,text = "확인", command = quit)
			quitbutton.place(x=130, y=130)
			resultroot.mainloop()
		"""
		Horse racing (경마)
		"""
		# Horse racing (경마)		
		def horse():
			self.choosehorse=[]
			horse=[1,2,3,4,5,6,7,8]
			winhorse=horse.pop(random.randrange(8))
			sechorse=horse.pop(random.randrange(7))
			horseloot = Toplevel(self.root)
			horseloot.title("경마")
			horseloot.geometry("400x234")
			field_pic=PhotoImage(file = "./images/horse.png")
			field=Label(horseloot, image=field_pic)
			field.place(x=0, y=0)
			font = tk.font.Font(root, size=15, weight='bold')
			msg=Label(horseloot, text="1등, 2등 할 말을 예상하세요")
			msg['font']=font
			msg.place(x=70, y=3)
			def choose1():
				b1=Label(horseloot, text="★")
				b1.place(x=8, y=40)
				if 1 not in self.choosehorse:
					self.choosehorse.append(1)
				if len(self.choosehorse)==2:
					determine(self.choosehorse)
			def choose2():
				b2=Label(horseloot, text="★")
				b2.place(x=108, y=40)
				if 2 not in self.choosehorse:
					self.choosehorse.append(2)
				if len(self.choosehorse)==2:
					determine(self.choosehorse)
			def choose3():
				b3=Label(horseloot, text="★")
				b3.place(x=208, y=40)
				if 3 not in self.choosehorse:
					self.choosehorse.append(3)
				if len(self.choosehorse)==2:
					determine(self.choosehorse)
			def choose4():
				b4=Label(horseloot, text="★")
				b4.place(x=308, y=40)
				if 4 not in self.choosehorse:
					self.choosehorse.append(4)
				if len(self.choosehorse)==2:
					determine(self.choosehorse)
			def choose5():
				b5=Label(horseloot, text="★")
				b5.place(x=8, y=130)
				if 5 not in self.choosehorse:
					self.choosehorse.append(5)
				if len(self.choosehorse)==2:
					determine(self.choosehorse)
			def choose6():
				b6=Label(horseloot, text="★")
				b6.place(x=108, y=130)
				if 6 not in self.choosehorse:
					self.choosehorse.append(6)
				if len(self.choosehorse)==2:
					determine(self.choosehorse)
			def choose7():
				b7=Label(horseloot, text="★")
				b7.place(x=208, y=130)
				if 7 not in self.choosehorse:
					self.choosehorse.append(7)
				if len(self.choosehorse)==2:
					determine(self.choosehorse)
			def choose8():
				b8=Label(horseloot, text="★")
				b8.place(x=308, y=130)
				if 8 not in self.choosehorse:
					self.choosehorse.append(8)
				if len(self.choosehorse)==2:
					determine(self.choosehorse)
			def determine(choose):
				self.date+=1
				if choose[0]==winhorse and choose[1]==sechorse or choose[0]==sechorse and choose[1]==winhorse:
					addmoney=500000*random.randrange(10, 250)
					self.money+=addmoney
					string="1등은 "+str(winhorse)+"번 말\n 2등은 "+str(sechorse)+"번 말이 차지했습니다. \n"+str(addmoney)+"원을 따냈습니다.\n"
					check = self.addannounce(string, horseloot)
					if check:
						self.update()
						horseloot.destroy()
						horseloot.quit()
				else:
					self.money-=500000
					string="1등은 "+str(winhorse)+"번 말\n 2등은 "+str(sechorse)+"번 말이 차지했습니다. \n500000원을 잃었습니다.\n"
					check = self.addannounce(string, horseloot)
					if check:
						self.update()
						horseloot.destroy()
						horseloot.quit()				
				
			horse1=PhotoImage(file = "./images/horse1.png")
			horse2=PhotoImage(file = "./images/horse2.png")
			horse3=PhotoImage(file = "./images/horse3.png")
			horse4=PhotoImage(file = "./images/horse4.png")
			horse5=PhotoImage(file = "./images/horse5.png")
			horse6=PhotoImage(file = "./images/horse6.png")
			horse7=PhotoImage(file = "./images/horse7.png")
			horse8=PhotoImage(file = "./images/horse8.png")
			b1=Button(horseloot, image = horse1, command = choose1)
			b1.place(x=8, y=40)
			b2=Button(horseloot, image = horse2, command = choose2)
			b2.place(x=108, y=40)
			b3=Button(horseloot, image = horse3, command = choose3)
			b3.place(x=208, y=40)
			b4=Button(horseloot, image = horse4, command = choose4)
			b4.place(x=308, y=40)
			b5=Button(horseloot, image = horse5, command = choose5)
			b5.place(x=8, y=130)
			b6=Button(horseloot, image = horse6, command = choose6)
			b6.place(x=108, y=130)
			b7=Button(horseloot, image = horse7, command = choose7)
			b7.place(x=208, y=130)
			b8=Button(horseloot, image = horse8, command = choose8)
			b8.place(x=308, y=130)
			horseloot.mainloop()
		"""
		stock(주식)
		"""
		# stock(주식)
		def stock():
			# self.stocklist=[[],[],[],[],[],[],[],[],[],[]] # [이름, 남은개수, 가격]
			# self.stockfluct=[[],[],[],[],[],[],[],[],[],[]]
			# self.havestock=[[],[],[],[],[],[],[],[],[],[]] # [이름, 개수]
			stockroot = Toplevel(self.root)
			stockroot.title("주식")
			stockroot.geometry("600x347")
			field_pic=PhotoImage(file = "./images/stock.png")
			field=Label(stockroot, image=field_pic)
			field.place(x=0, y=0)
			font = tk.font.Font(root, size=15, weight='bold')
			font2 = tk.font.Font(root, size=14, weight='bold')
			def buy1():
				get=be1.get()
				if get.isdigit() and self.stocklist[0][1]>=int(get) and int(get)*self.stocklist[0][2] < self.money:
					self.date+=1
					self.money -= int(get)*self.stocklist[0][2]
					if len(self.havestock[0])==0:
						self.havestock[0].append(self.stocklist[0][0])
						self.havestock[0].append(int(get))
					else:
						self.havestock[0][1]+=int(get)
					self.stocklist[0][1] -= int(get)
					string = self.stocklist[0][0]+" 주식을 "+get+"주 구입했습니다.\n"
					string += str(int(get)*self.stocklist[0][2])+"원을 주식에 지출했습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=be1.get()
			def sell1():
				get=se1.get()
				if get.isdigit() and len(self.havestock[0])!=0 and self.havestock[0][1]>=int(get): 
					self.date+=1
					self.money += int(get)*self.stocklist[0][2]
					self.stocklist[0][1] += int(get)
					self.havestock[0][1] -= int(get)
					string = self.stocklist[0][0]+" 주식을 "+get+"주 판매했습니다.\n"
					string += str(int(get)*self.stocklist[0][2])+"원을 얻었습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=se1.get()
			def buy2():
				get=be2.get()
				if get.isdigit() and self.stocklist[1][1]>=int(get) and int(get)*self.stocklist[1][2] < self.money:
					self.date+=1
					self.money -= int(get)*self.stocklist[1][2]
					if len(self.havestock[1])==0:
						self.havestock[1].append(self.stocklist[1][0])
						self.havestock[1].append(int(get))
					else:
						self.havestock[1][1]+=int(get)
					self.stocklist[1][1] -= int(get)
					string = self.stocklist[1][0]+" 주식을 "+get+"주 구입했습니다.\n"
					string += str(int(get)*self.stocklist[1][2])+"원을 주식에 지출했습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=be2.get()
			def sell2():
				get=se2.get()
				if get.isdigit() and len(self.havestock[1])!=0 and self.havestock[1][1]>=int(get): 
					self.date+=1
					self.money += int(get)*self.stocklist[1][2]
					self.stocklist[1][1] += int(get)
					self.havestock[1][1] -= int(get)
					string = self.stocklist[1][0]+" 주식을 "+get+"주 판매했습니다.\n"
					string += str(int(get)*self.stocklist[1][2])+"원을 얻었습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=se2.get()
			def buy3():
				get=be3.get()
				if get.isdigit() and self.stocklist[2][1]>=int(get) and int(get)*self.stocklist[2][2] < self.money:
					self.date+=1
					self.money -= int(get)*self.stocklist[2][2]
					if len(self.havestock[2])==0:
						self.havestock[2].append(self.stocklist[2][0])
						self.havestock[2].append(int(get))
					else:
						self.havestock[2][1]+=int(get)
					self.stocklist[2][1] -= int(get)
					string = self.stocklist[2][0]+" 주식을 "+get+"주 구입했습니다.\n"
					string += str(int(get)*self.stocklist[2][2])+"원을 주식에 지출했습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=be3.get()
			def sell3():
				get=se3.get()
				if get.isdigit() and len(self.havestock[2])!=0 and self.havestock[2][1]>=int(get): 
					self.date+=1
					self.money += int(get)*self.stocklist[2][2]
					self.stocklist[2][1] += int(get)
					self.havestock[2][1] -= int(get)
					string = self.stocklist[2][0]+" 주식을 "+get+"주 판매했습니다.\n"
					string += str(int(get)*self.stocklist[2][2])+"원을 얻었습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=se3.get()
			def buy4():
				get=be4.get()
				if get.isdigit() and self.stocklist[3][1]>=int(get) and int(get)*self.stocklist[3][2] < self.money:
					self.date+=1
					self.money -= int(get)*self.stocklist[3][2]
					if len(self.havestock[3])==0:
						self.havestock[3].append(self.stocklist[3][0])
						self.havestock[3].append(int(get))
					else:
						self.havestock[3][1]+=int(get)
					self.stocklist[3][1] -= int(get)
					string = self.stocklist[3][0]+" 주식을 "+get+"주 구입했습니다.\n"
					string += str(int(get)*self.stocklist[3][2])+"원을 주식에 지출했습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=be4.get()
			def sell4():
				get=se4.get()
				if get.isdigit() and len(self.havestock[3])!=0 and self.havestock[3][1]>=int(get): 
					self.date+=1
					self.money += int(get)*self.stocklist[3][2]
					self.stocklist[3][1] += int(get)
					self.havestock[3][1] -= int(get)
					string = self.stocklist[3][0]+" 주식을 "+get+"주 판매했습니다.\n"
					string += str(int(get)*self.stocklist[3][2])+"원을 얻었습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=se4.get()
			def buy5():
				get=be5.get()
				if get.isdigit() and self.stocklist[4][1]>=int(get) and int(get)*self.stocklist[4][2] < self.money:
					self.date+=1
					self.money -= int(get)*self.stocklist[4][2]
					if len(self.havestock[4])==0:
						self.havestock[4].append(self.stocklist[4][0])
						self.havestock[4].append(int(get))
					else:
						self.havestock[4][1]+=int(get)
					self.stocklist[4][1] -= int(get)
					string = self.stocklist[4][0]+" 주식을 "+get+"주 구입했습니다.\n"
					string += str(int(get)*self.stocklist[4][2])+"원을 주식에 지출했습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=be5.get()
			def sell5():
				get=se5.get()
				if get.isdigit() and len(self.havestock[4])!=0 and self.havestock[4][1]>=int(get): 
					self.date+=1
					self.money += int(get)*self.stocklist[4][2]
					self.stocklist[4][1] += int(get)
					self.havestock[4][1] -= int(get)
					string = self.stocklist[4][0]+" 주식을 "+get+"주 판매했습니다.\n"
					string += str(int(get)*self.stocklist[4][2])+"원을 얻었습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=se5.get()
			def buy6():
				get=be6.get()
				if get.isdigit() and self.stocklist[5][1]>=int(get) and int(get)*self.stocklist[5][2] < self.money:
					self.date+=1
					self.money -= int(get)*self.stocklist[5][2]
					if len(self.havestock[5])==0:
						self.havestock[5].append(self.stocklist[5][0])
						self.havestock[5].append(int(get))
					else:
						self.havestock[5][1]+=int(get)
					self.stocklist[5][1] -= int(get)
					string = self.stocklist[5][0]+" 주식을 "+get+"주 구입했습니다.\n"
					string += str(int(get)*self.stocklist[5][2])+"원을 주식에 지출했습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=be6.get()
			def sell6():
				get=se6.get()
				if get.isdigit() and len(self.havestock[5])!=0 and self.havestock[5][1]>=int(get): 
					self.date+=1
					self.money += int(get)*self.stocklist[5][2]
					self.stocklist[5][1] += int(get)
					self.havestock[5][1] -= int(get)
					string = self.stocklist[5][0]+" 주식을 "+get+"주 판매했습니다.\n"
					string += str(int(get)*self.stocklist[5][2])+"원을 얻었습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=se6.get()
			def buy7():
				get=be7.get()
				if get.isdigit() and self.stocklist[6][1]>=int(get) and int(get)*self.stocklist[6][2] < self.money:
					self.date+=1
					self.money -= int(get)*self.stocklist[6][2]
					if len(self.havestock[6])==0:
						self.havestock[6].append(self.stocklist[6][0])
						self.havestock[6].append(int(get))
					else:
						self.havestock[6][1]+=int(get)
					self.stocklist[6][1] -= int(get)
					string = self.stocklist[6][0]+" 주식을 "+get+"주 구입했습니다.\n"
					string += str(int(get)*self.stocklist[6][2])+"원을 주식에 지출했습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=be7.get()
			def sell7():
				get=se7.get()
				if get.isdigit() and len(self.havestock[6])!=0 and self.havestock[6][1]>=int(get): 
					self.date+=1
					self.money += int(get)*self.stocklist[6][2]
					self.stocklist[6][1] += int(get)
					self.havestock[6][1] -= int(get)
					string = self.stocklist[6][0]+" 주식을 "+get+"주 판매했습니다.\n"
					string += str(int(get)*self.stocklist[6][2])+"원을 얻었습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=se7.get()
			def buy8():
				get=be8.get()
				if get.isdigit() and self.stocklist[7][1]>=int(get) and int(get)*self.stocklist[7][2] < self.money:
					self.date+=1
					self.money -= int(get)*self.stocklist[7][2]
					if len(self.havestock[7])==0:
						self.havestock[7].append(self.stocklist[7][0])
						self.havestock[7].append(int(get))
					else:
						self.havestock[7][1]+=int(get)
					self.stocklist[7][1] -= int(get)
					string = self.stocklist[7][0]+" 주식을 "+get+"주 구입했습니다.\n"
					string += str(int(get)*self.stocklist[7][2])+"원을 주식에 지출했습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=be8.get()
			def sell8():
				get=se8.get()
				if get.isdigit() and len(self.havestock[7])!=0 and self.havestock[7][1]>=int(get): 
					self.date+=1
					self.money += int(get)*self.stocklist[7][2]
					self.stocklist[7][1] += int(get)
					self.havestock[7][1] -= int(get)
					string = self.stocklist[7][0]+" 주식을 "+get+"주 판매했습니다.\n"
					string += str(int(get)*self.stocklist[7][2])+"원을 얻었습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=se8.get()
			def buy9():
				get=be9.get()
				if get.isdigit() and self.stocklist[8][1]>=int(get) and int(get)*self.stocklist[8][2] < self.money:
					self.date+=1
					self.money -= int(get)*self.stocklist[8][2]
					if len(self.havestock[8])==0:
						self.havestock[8].append(self.stocklist[8][0])
						self.havestock[8].append(int(get))
					else:
						self.havestock[8][1]+=int(get)
					self.stocklist[8][1] -= int(get)
					string = self.stocklist[8][0]+" 주식을 "+get+"주 구입했습니다.\n"
					string += str(int(get)*self.stocklist[8][2])+"원을 주식에 지출했습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=be9.get()
			def sell9():
				get=se9.get()
				if get.isdigit() and len(self.havestock[8])!=0 and self.havestock[8][1]>=int(get): 
					self.date+=1
					self.money += int(get)*self.stocklist[8][2]
					self.stocklist[8][1] += int(get)
					self.havestock[8][1] -= int(get)
					string = self.stocklist[8][0]+" 주식을 "+get+"주 판매했습니다.\n"
					string += str(int(get)*self.stocklist[8][2])+"원을 얻었습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=se9.get()
			def buy10():
				get=be10.get()
				if get.isdigit() and self.stocklist[9][1]>=int(get) and int(get)*self.stocklist[9][2] < self.money:
					self.date+=1
					elf.money -= int(get)*self.stocklist[9][2]
					if len(self.havestock[9])==0:
						self.havestock[9].append(self.stocklist[9][0])
						self.havestock[9].append(int(get))
					else:
						self.havestock[9][1]+=int(get)
					self.stocklist[9][1] -= int(get)
					string = self.stocklist[9][0]+" 주식을 "+get+"주 구입했습니다.\n"
					string += str(int(get)*self.stocklist[9][2])+"원을 주식에 지출했습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=be10.get()
			def sell10():
				get=se10.get()
				if get.isdigit() and len(self.havestock[9])!=0 and self.havestock[9][1]>=int(get): 
					self.date+=1
					self.money += int(get)*self.stocklist[9][2]
					self.stocklist[9][1] += int(get)
					self.havestock[9][1] -= int(get)
					string = self.stocklist[9][0]+" 주식을 "+get+"주 판매했습니다.\n"
					string += str(int(get)*self.stocklist[9][2])+"원을 얻었습니다.\n"
					check = self.addannounce(string, stockroot)
					if check:
						self.update()
						stockroot.destroy()
						stockroot.quit()
				else:
					get=se10.get()
			def r1():
				recentroot = Toplevel(stockroot)
				recentroot.title("최근동향")
				recentroot.geometry("100x250")
				Label(recentroot, text=self.stocklist[0][0]+" 최근동향").place(x=7, y=5)
				string=""
				def quit():
					recentroot.destroy()
					recentroot.quit()
				for i in range(len(self.stockfluct[0])):
					if self.stockfluct[0][i]>0:
						string+="↑ "+str(self.stockfluct[0][i])+"\n"
					else:
						string+="↓ "+str(self.stockfluct[0][i]*(-1))+"\n"
				Label(recentroot, text=string).place(x=30, y=30)
				quitbutton=Button(recentroot, text="확인", command=quit)
				quitbutton.place(x=43, y=220)
				recentroot.mainloop()
			def r2():
				recentroot = Toplevel(stockroot)
				recentroot.title("최근동향")
				recentroot.geometry("100x250")
				Label(recentroot, text=self.stocklist[1][0]+" 최근동향").place(x=7, y=5)
				string=""
				def quit():
					recentroot.destroy()
					recentroot.quit()
				for i in range(len(self.stockfluct[1])):
					if self.stockfluct[1][i]>0:
						string+="↑ "+str(self.stockfluct[1][i])+"\n"
					else:
						string+="↓ "+str(self.stockfluct[1][i]*(-1))+"\n"
				Label(recentroot, text=string).place(x=30, y=30)
				quitbutton=Button(recentroot, text="확인", command=quit)
				quitbutton.place(x=43, y=220)
				recentroot.mainloop()
			def r3():
				recentroot = Toplevel(stockroot)
				recentroot.title("최근동향")
				recentroot.geometry("100x250")
				Label(recentroot, text=self.stocklist[2][0]+" 최근동향").place(x=7, y=5)
				string=""
				def quit():
					recentroot.destroy()
					recentroot.quit()
				for i in range(len(self.stockfluct[2])):
					if self.stockfluct[2][i]>0:
						string+="↑ "+str(self.stockfluct[2][i])+"\n"
					else:
						string+="↓ "+str(self.stockfluct[2][i]*(-1))+"\n"
				Label(recentroot, text=string).place(x=30, y=30)
				quitbutton=Button(recentroot, text="확인", command=quit)
				quitbutton.place(x=43, y=220)
				recentroot.mainloop()
			def r4():
				recentroot = Toplevel(stockroot)
				recentroot.title("최근동향")
				recentroot.geometry("100x250")
				Label(recentroot, text=self.stocklist[3][0]+" 최근동향").place(x=7, y=5)
				string=""
				def quit():
					recentroot.destroy()
					recentroot.quit()
				for i in range(len(self.stockfluct[3])):
					if self.stockfluct[3][i]>0:
						string+="↑ "+str(self.stockfluct[3][i])+"\n"
					else:
						string+="↓ "+str(self.stockfluct[3][i]*(-1))+"\n"
				Label(recentroot, text=string).place(x=30, y=30)
				quitbutton=Button(recentroot, text="확인", command=quit)
				quitbutton.place(x=43, y=220)
				recentroot.mainloop()
			def r5():
				recentroot = Toplevel(stockroot)
				recentroot.title("최근동향")
				recentroot.geometry("100x250")
				Label(recentroot, text=self.stocklist[4][0]+" 최근동향").place(x=7, y=5)
				string=""
				def quit():
					recentroot.destroy()
					recentroot.quit()
				for i in range(len(self.stockfluct[4])):
					if self.stockfluct[4][i]>0:
						string+="↑ "+str(self.stockfluct[4][i])+"\n"
					else:
						string+="↓ "+str(self.stockfluct[4][i]*(-1))+"\n"
				Label(recentroot, text=string).place(x=30, y=30)
				quitbutton=Button(recentroot, text="확인", command=quit)
				quitbutton.place(x=43, y=220)
				recentroot.mainloop()
			def r6():
				recentroot = Toplevel(stockroot)
				recentroot.title("최근동향")
				recentroot.geometry("100x250")
				Label(recentroot, text=self.stocklist[5][0]+" 최근동향").place(x=7, y=5)
				string=""
				def quit():
					recentroot.destroy()
					recentroot.quit()
				for i in range(len(self.stockfluct[5])):
					if self.stockfluct[5][i]>0:
						string+="↑ "+str(self.stockfluct[5][i])+"\n"
					else:
						string+="↓ "+str(self.stockfluct[5][i]*(-1))+"\n"
				Label(recentroot, text=string).place(x=30, y=30)
				quitbutton=Button(recentroot, text="확인", command=quit)
				quitbutton.place(x=43, y=220)
				recentroot.mainloop()
			def r7():
				recentroot = Toplevel(stockroot)
				recentroot.title("최근동향")
				recentroot.geometry("100x250")
				Label(recentroot, text=self.stocklist[6][0]+" 최근동향").place(x=7, y=5)
				string=""
				def quit():
					recentroot.destroy()
					recentroot.quit()
				for i in range(len(self.stockfluct[6])):
					if self.stockfluct[6][i]>0:
						string+="↑ "+str(self.stockfluct[6][i])+"\n"
					else:
						string+="↓ "+str(self.stockfluct[6][i]*(-1))+"\n"
				Label(recentroot, text=string).place(x=30, y=30)
				quitbutton=Button(recentroot, text="확인", command=quit)
				quitbutton.place(x=43, y=220)
				recentroot.mainloop()
			def r8():
				recentroot = Toplevel(stockroot)
				recentroot.title("최근동향")
				recentroot.geometry("100x250")
				Label(recentroot, text=self.stocklist[7][0]+" 최근동향").place(x=7, y=5)
				string=""
				def quit():
					recentroot.destroy()
					recentroot.quit()
				for i in range(len(self.stockfluct[7])):
					if self.stockfluct[7][i]>0:
						string+="↑ "+str(self.stockfluct[7][i])+"\n"
					else:
						string+="↓ "+str(self.stockfluct[7][i]*(-1))+"\n"
				Label(recentroot, text=string).place(x=30, y=30)
				quitbutton=Button(recentroot, text="확인", command=quit)
				quitbutton.place(x=43, y=220)
				recentroot.mainloop()
			def r9():
				recentroot = Toplevel(stockroot)
				recentroot.title("최근동향")
				recentroot.geometry("100x250")
				Label(recentroot, text=self.stocklist[8][0]+" 최근동향").place(x=7, y=5)
				string=""
				def quit():
					recentroot.destroy()
					recentroot.quit()
				for i in range(len(self.stockfluct[8])):
					if self.stockfluct[8][i]>0:
						string+="↑ "+str(self.stockfluct[8][i])+"\n"
					else:
						string+="↓ "+str(self.stockfluct[8][i]*(-1))+"\n"
				Label(recentroot, text=string).place(x=30, y=30)
				quitbutton=Button(recentroot, text="확인", command=quit)
				quitbutton.place(x=43, y=220)
				recentroot.mainloop()
			def r10():
				recentroot = Toplevel(stockroot)
				recentroot.title("최근동향")
				recentroot.geometry("100x250")
				Label(recentroot, text=self.stocklist[9][0]+" 최근동향").place(x=7, y=5)
				string=""
				def quit():
					recentroot.destroy()
					recentroot.quit()
				for i in range(len(self.stockfluct[9])):
					if self.stockfluct[9][i]>0:
						string+="↑ "+str(self.stockfluct[9][i])+"\n"
					else:
						string+="↓ "+str(self.stockfluct[9][i]*(-1))+"\n"
				Label(recentroot, text=string).place(x=30, y=30)
				quitbutton=Button(recentroot, text="확인", command=quit)
				quitbutton.place(x=43, y=220)
				recentroot.mainloop()
			Label(stockroot, text=self.stocklist[0][0]).place(x=45, y=10)
			Label(stockroot, text="\\"+str(self.stocklist[0][2])+" / "+str(self.stocklist[0][1])+"주 남음").place(x=10, y=30)
			Label(stockroot, text="사기").place(x=15, y=57)
			Label(stockroot, text="팔기").place(x=15, y=87)
			be1 = Entry(stockroot,  width=5)
			be1.place(x=50, y=57)
			se1 = Entry(stockroot,  width=5)
			se1.place(x=50, y=87)
			b1 = Button(stockroot, text="확인", command=buy1)
			b1.place(x=95, y=55)
			s1 = Button(stockroot, text="확인", command=sell1)
			s1.place(x=95, y=85)
			Label(stockroot, text=self.stocklist[1][0]).place(x=195, y=10)
			Label(stockroot, text="\\"+str(self.stocklist[1][2])+" / "+str(self.stocklist[1][1])+"주 남음").place(x=160, y=30)
			Label(stockroot, text="사기").place(x=165, y=57)
			Label(stockroot, text="팔기").place(x=165, y=87)
			be2 = Entry(stockroot,  width=5)
			be2.place(x=200, y=57)
			se2 = Entry(stockroot,  width=5)
			se2.place(x=200, y=87)
			b2 = Button(stockroot, text="확인", command=buy2)
			b2.place(x=245, y=55)
			s2 = Button(stockroot, text="확인", command=sell2)
			s2.place(x=245, y=85)
			Label(stockroot, text=self.stocklist[2][0]).place(x=345, y=10)
			Label(stockroot, text="\\"+str(self.stocklist[2][2])+" / "+str(self.stocklist[2][1])+"주 남음").place(x=310, y=30)
			Label(stockroot, text="사기").place(x=315, y=57)
			Label(stockroot, text="팔기").place(x=315, y=87)
			be3 = Entry(stockroot,  width=5)
			be3.place(x=350, y=57)
			se3 = Entry(stockroot,  width=5)
			se3.place(x=350, y=87)
			b3 = Button(stockroot, text="확인", command=buy3)
			b3.place(x=395, y=55)
			s3 = Button(stockroot, text="확인", command=sell3)
			s3.place(x=395, y=85)
			Label(stockroot, text=self.stocklist[3][0]).place(x=495, y=10)
			Label(stockroot, text="\\"+str(self.stocklist[3][2])+" / "+str(self.stocklist[3][1])+"주 남음").place(x=460, y=30)
			Label(stockroot, text="사기").place(x=465, y=57)
			Label(stockroot, text="팔기").place(x=465, y=87)
			be4 = Entry(stockroot,  width=5)
			be4.place(x=500, y=57)
			se4 = Entry(stockroot,  width=5)
			se4.place(x=500, y=87)
			b4 = Button(stockroot, text="확인", command=buy4)
			b4.place(x=545, y=55)
			s4 = Button(stockroot, text="확인", command=sell4)
			s4.place(x=545, y=85)
			Label(stockroot, text=self.stocklist[4][0]).place(x=45, y=120)
			Label(stockroot, text="\\"+str(self.stocklist[4][2])+" / "+str(self.stocklist[4][1])+"주 남음").place(x=10, y=140)
			Label(stockroot, text="사기").place(x=15, y=167)
			Label(stockroot, text="팔기").place(x=15, y=197)
			be5 = Entry(stockroot,  width=5)
			be5.place(x=50, y=167)
			se5 = Entry(stockroot,  width=5)
			se5.place(x=50, y=197)
			b5 = Button(stockroot, text="확인", command=buy5)
			b5.place(x=95, y=165)
			s5 = Button(stockroot, text="확인", command=sell5)
			s5.place(x=95, y=195)
			Label(stockroot, text=self.stocklist[5][0]).place(x=195, y=120)
			Label(stockroot, text="\\"+str(self.stocklist[5][2])+" / "+str(self.stocklist[5][1])+"주 남음").place(x=160, y=140)
			Label(stockroot, text="사기").place(x=165, y=167)
			Label(stockroot, text="팔기").place(x=165, y=197)
			be6 = Entry(stockroot,  width=5)
			be6.place(x=200, y=167)
			se6 = Entry(stockroot,  width=5)
			se6.place(x=200, y=197)
			b6 = Button(stockroot, text="확인", command=buy6)
			b6.place(x=245, y=165)
			s6 = Button(stockroot, text="확인", command=sell6)
			s6.place(x=245, y=195)
			Label(stockroot, text=self.stocklist[6][0]).place(x=345, y=120)
			Label(stockroot, text="\\"+str(self.stocklist[6][2])+" / "+str(self.stocklist[6][1])+"주 남음").place(x=310, y=140)
			Label(stockroot, text="사기").place(x=315, y=167)
			Label(stockroot, text="팔기").place(x=315, y=197)
			be7 = Entry(stockroot,  width=5)
			be7.place(x=350, y=167)
			se7 = Entry(stockroot,  width=5)
			se7.place(x=350, y=197)
			b7 = Button(stockroot, text="확인", command=buy7)
			b7.place(x=395, y=165)
			s7 = Button(stockroot, text="확인", command=sell7)
			s7.place(x=395, y=195)
			Label(stockroot, text=self.stocklist[7][0]).place(x=495, y=120)
			Label(stockroot, text="\\"+str(self.stocklist[7][2])+" / "+str(self.stocklist[7][1])+"주 남음").place(x=460, y=140)
			Label(stockroot, text="사기").place(x=465, y=167)
			Label(stockroot, text="팔기").place(x=465, y=197)
			be8 = Entry(stockroot,  width=5)
			be8.place(x=500, y=167)
			se8 = Entry(stockroot,  width=5)
			se8.place(x=500, y=197)
			b8 = Button(stockroot, text="확인", command=buy8)
			b8.place(x=545, y=165)
			s8 = Button(stockroot, text="확인", command=sell8)
			s8.place(x=545, y=195)
			Label(stockroot, text=self.stocklist[8][0]).place(x=45, y=230)
			Label(stockroot, text="\\"+str(self.stocklist[8][2])+" / "+str(self.stocklist[8][1])+"주 남음").place(x=10, y=250)
			Label(stockroot, text="사기").place(x=15, y=277)
			Label(stockroot, text="팔기").place(x=15, y=307)
			be9 = Entry(stockroot,  width=5)
			be9.place(x=50, y=277)
			se9 = Entry(stockroot,  width=5)
			se9.place(x=50, y=307)
			b9 = Button(stockroot, text="확인", command=buy9)
			b9.place(x=95, y=275)
			s9 = Button(stockroot, text="확인", command=sell9)
			s9.place(x=95, y=305)
			Label(stockroot, text=self.stocklist[9][0]).place(x=195, y=230)
			Label(stockroot, text="\\"+str(self.stocklist[9][2])+" / "+str(self.stocklist[9][1])+"주 남음").place(x=160, y=250)
			Label(stockroot, text="사기").place(x=165, y=277)
			Label(stockroot, text="팔기").place(x=165, y=307)
			be10 = Entry(stockroot,  width=5)
			be10.place(x=200, y=277)
			se10 = Entry(stockroot,  width=5)
			se10.place(x=200, y=307)
			b10 = Button(stockroot, text="확인", command=buy10)
			b10.place(x=245, y=275)
			s10 = Button(stockroot, text="확인", command=sell10)
			s10.place(x=245, y=305)
			Label(stockroot, text="최근동향").place(x=415, y=240)
			r1 = Button(stockroot, text=self.stocklist[0][0], command=r1)
			r1.place(x=295, y=265)
			r2 = Button(stockroot, text=self.stocklist[1][0], command=r2)
			r2.place(x=355, y=265)
			r3 = Button(stockroot, text=self.stocklist[2][0], command=r3)
			r3.place(x=415, y=265)
			r4 = Button(stockroot, text=self.stocklist[3][0], command=r4)
			r4.place(x=475, y=265)
			r5 = Button(stockroot, text=self.stocklist[4][0], command=r5)
			r5.place(x=535, y=265)
			r6 = Button(stockroot, text=self.stocklist[5][0], command=r6)
			r6.place(x=295, y=305)
			r7 = Button(stockroot, text=self.stocklist[6][0], command=r7)
			r7.place(x=355, y=305)
			r8 = Button(stockroot, text=self.stocklist[7][0], command=r8)
			r8.place(x=415, y=305)
			r9 = Button(stockroot, text=self.stocklist[8][0], command=r9)
			r9.place(x=475, y=305)
			r10 = Button(stockroot, text=self.stocklist[9][0], command=r10)
			r10.place(x=535, y=305)
			stockroot.mainloop()
		"""
		loan(대출)
		"""
		# loan(대출)

"""
main method
"""
# main method
def main(root):
	def play():
		for child in root.winfo_children():
			child.destroy()
		root.geometry("648x286")
		Main(root).mainscreen()
	def quit():
		root.destroy()
		root.quit()
	font = tk.font.Font(root, size=23, weight='bold')
	play = Button(root, text ="시작하기", command = play)
	play.place(x=250, y=150)
	play['font']=font 
	quit = Button(root, text ="종료", command = quit)
	quit.place(x=280, y=250)
	quit['font']=font
	root.mainloop()

"""
GUI
"""
# GUI 
root = Tk()
root.title("주갤러 인생 시뮬레이터")
root.geometry("648x406")
img_field = PhotoImage(file = "./images/start.png")
Label(root, image = img_field).place(x = 0, y = 0)
root.update()
main(root)
root.mainloop()