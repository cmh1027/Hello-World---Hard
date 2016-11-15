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