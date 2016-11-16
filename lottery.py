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