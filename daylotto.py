import random
from tkinter import *
from tkinter import font
import tkinter as tk
"""
Daylotto Class
"""
# Daylotto Class
class Daylotto:
	"""
	Constructor
	"""
	# Constructor
	def __init__(self, root):
		self.root=root
		self.numlist=[1,2,3,4,5,6,7,8,9]
		self.openlist=[]
		self.chooselist=[]
		random.shuffle(self.numlist)
		self.flag=0
		self.checkflag=True
		self.reward=[]
		self.result=0
		self.font = tk.font.Font(root, size=47, weight='bold')
	def getresult(self):
		return self.result
	"""
	Playing by this method
	"""
	# Playing by this method
	def play(self):
		A=0
		B=0
		C=0
		D=0
		for _ in range(20):
			while True:
				number=random.randrange(5001)
				if 0<=number<100 and D<16: 	
					self.reward.append(10000*number)
					D+=1
					break
				elif 100<=number<200 and C<3:
					self.reward.append(10000*number)
					C+=1
					break
				elif 200<=number<400 and B<2:
					self.reward.append(10000*number)
					B+=1
					break
				elif 400<number and A<1:
					self.reward.append(10000*number)
					A+=1
					break
		def button1():
			if self.flag<=2:
				if 1 not in self.openlist:
					self.openlist.append(1)
					self.chooselist.append(self.numlist[0])
					numlabel=Label(self.root, text=" "+str(self.numlist[0])+" ")
					numlabel['font']=self.font
					numlabel.place(x=80, y=60)
					self.flag+=1
		def button2():
			if self.flag<=2:
				if 2 not in self.openlist:
					self.openlist.append(2)
					self.chooselist.append(self.numlist[1])
					numlabel=Label(self.root, text=" "+str(self.numlist[1])+" ")
					numlabel['font']=self.font
					numlabel.place(x=190, y=60)
					self.flag+=1
		def button3():
			if self.flag<=2:
				if 3 not in self.openlist:
					self.openlist.append(3)
					self.chooselist.append(self.numlist[2])
					numlabel=Label(self.root, text=" "+str(self.numlist[2])+" ")
					numlabel['font']=self.font
					numlabel.place(x=300, y=60)
					self.flag+=1
		def button4():
			if self.flag<=2:
				if 4 not in self.openlist:
					self.openlist.append(4)
					self.chooselist.append(self.numlist[3])
					numlabel=Label(self.root, text=" "+str(self.numlist[3])+" ")
					numlabel['font']=self.font
					numlabel.place(x=80, y=170)
					self.flag+=1
		def button5():
			if self.flag<=2:
				if 5 not in self.openlist:
					self.openlist.append(5)
					self.chooselist.append(self.numlist[4])
					numlabel=Label(self.root, text=" "+str(self.numlist[4])+" ")
					numlabel['font']=self.font
					numlabel.place(x=190, y=170)
					self.flag+=1
		def button6():
			if self.flag<=2:
				if 6 not in self.openlist:
					self.openlist.append(6)
					self.chooselist.append(self.numlist[5])
					numlabel=Label(self.root, text=" "+str(self.numlist[5])+" ")
					numlabel['font']=self.font
					numlabel.place(x=300, y=170)
					self.flag+=1
		def button7():
			if self.flag<=2:
				if 7 not in self.openlist:
					self.openlist.append(7)
					self.chooselist.append(self.numlist[6])
					numlabel=Label(self.root, text=" "+str(self.numlist[6])+" ")
					numlabel['font']=self.font
					numlabel.place(x=80, y=280)
					self.flag+=1
		def button8():
			if self.flag<=2:
				if 8 not in self.openlist:
					self.openlist.append(8)
					self.chooselist.append(self.numlist[7])
					numlabel=Label(self.root, text=" "+str(self.numlist[7])+" ")
					numlabel['font']=self.font
					numlabel.place(x=190, y=280)
					self.flag+=1
		def button9():
			if self.flag<=2:
				if 9 not in self.openlist:
					self.openlist.append(9)
					self.chooselist.append(self.numlist[8])
					numlabel=Label(self.root, text=" "+str(self.numlist[8])+" ")
					numlabel['font']=self.font
					numlabel.place(x=300, y=280)
					self.flag+=1
		def c1():
			if self.flag==3:
				numsum=self.numlist[0]+self.numlist[3]+self.numlist[6]
				self.result = self.reward[numsum-6]
				self.root.destroy()
				self.root.quit()
		def c2():
			if self.flag==3:
				numsum=self.numlist[1]+self.numlist[4]+self.numlist[7]
				self.result = self.reward[numsum-6]
				self.root.destroy()
				self.root.quit()
		def c3():
			if self.flag==3:
				numsum=self.numlist[2]+self.numlist[5]+self.numlist[8]
				self.result = self.reward[numsum-6]
				self.root.destroy()
				self.root.quit()
		def r1():
			if self.flag==3:
				numsum=self.numlist[0]+self.numlist[1]+self.numlist[2]
				self.result = self.reward[numsum-6]
				self.root.destroy()
				self.root.quit()
		def r2():
			if self.flag==3:
				numsum=self.numlist[3]+self.numlist[4]+self.numlist[5]
				self.result = self.reward[numsum-6]
				self.root.destroy()
				self.root.quit()
		def r3():
			if self.flag==3:
				numsum=self.numlist[6]+self.numlist[7]+self.numlist[8]
				self.result = self.reward[numsum-6]
				self.root.destroy()
				self.root.quit()
		def l_d():
			if self.flag==3:
				numsum=self.numlist[0]+self.numlist[4]+self.numlist[8]
				self.result = self.reward[numsum-6]
				self.root.destroy()
				self.root.quit()
		def r_d():
			if self.flag==3:
				numsum=self.numlist[2]+self.numlist[4]+self.numlist[6]
				self.result = self.reward[numsum-6]
				self.root.destroy()
				self.root.quit()
		c1p=PhotoImage(file="./images/column.png")
		c2p=PhotoImage(file="./images/column.png")
		c3p=PhotoImage(file="./images/column.png")
		r1p=PhotoImage(file="./images/row.png")
		r2p=PhotoImage(file="./images/row.png")
		r3p=PhotoImage(file="./images/row.png")
		l_dp=PhotoImage(file="./images/left_diagonal.png")
		r_dp=PhotoImage(file="./images/right_diagonal.png")
		b_c1=Button(self.root, image=c1p, command=c1)
		b_c2=Button(self.root, image=c2p, command=c2)
		b_c3=Button(self.root, image=c3p, command=c3)
		b_r1=Button(self.root, image=r1p, command=r1)
		b_r2=Button(self.root, image=r2p, command=r2)
		b_r3=Button(self.root, image=r3p, command=r3)
		b_ld=Button(self.root, image=l_dp, command=l_d)
		b_rd=Button(self.root, image=r_dp, command=r_d)
		b_ld.place(x=25, y=15)
		b_c1.place(x=102, y=15)
		b_c2.place(x=211, y=15)
		b_c3.place(x=320, y=15)
		b_rd.place(x=400, y=15)
		b_r1.place(x=25, y=82)
		b_r2.place(x=25, y=191)
		b_r3.place(x=25, y=300)
		image=PhotoImage(file="./images/temp.png")
		bt1=Button(self.root,image=image, command=button1)
		bt1.place(x=80, y=60)
		bt2=Button(self.root,image=image, command=button2)
		bt2.place(x=190, y=60)
		bt3=Button(self.root,image=image, command=button3)
		bt3.place(x=300, y=60)
		bt4=Button(self.root,image=image, command=button4)
		bt4.place(x=80, y=170)
		bt5=Button(self.root,image=image, command=button5)
		bt5.place(x=190, y=170)
		bt6=Button(self.root,image=image, command=button6)
		bt6.place(x=300, y=170)
		bt7=Button(self.root,image=image, command=button7)
		bt7.place(x=80, y=280)
		bt8=Button(self.root,image=image, command=button8)
		bt8.place(x=190, y=280)
		bt9=Button(self.root,image=image, command=button9)
		bt9.place(x=300, y=280)
		string1=""
		string2=""
		string3=""
		font = tk.font.Font(self.root, size=13, weight='bold')
		for i in range(7):
			string1+=str(i+6)+" : "+str(self.reward[i])+"\n"
		reward1 = Label(self.root, text=string1)
		reward1.place(x=55, y=390)
		reward1['font']=font
		for i in range(7, 14):
			string2+=str(i+6)+" : "+str(self.reward[i])+"\n"
		reward2 = Label(self.root, text=string2)
		reward2.place(x=175, y=390)
		reward2['font']=font
		for i in range(14, 20):
			string3+=str(i+6)+" : "+str(self.reward[i])+"\n"
		reward3 = Label(self.root, text=string3)
		reward3.place(x=295, y=390)
		reward3['font']=font
		number = random.randrange(1, 10)
		self.openlist.append(number)
		self.chooselist.append(self.numlist[number-1])
		if number==1:
			numlabel=Label(self.root, text=" "+str(self.numlist[0])+" ")
			numlabel.place(x=80, y=60)
			numlabel['font']=self.font
		elif number==2:
			numlabel=Label(self.root, text=" "+str(self.numlist[1])+" ")
			numlabel.place(x=190, y=60)
			numlabel['font']=self.font
		elif number==3:
			numlabel=Label(self.root, text=" "+str(self.numlist[2])+" ")
			numlabel.place(x=300, y=60)
			numlabel['font']=self.font
		elif number==4:
			numlabel=Label(self.root, text=" "+str(self.numlist[3])+" ")
			numlabel.place(x=80, y=170)
			numlabel['font']=self.font
		elif number==5:
			numlabel=Label(self.root, text=" "+str(self.numlist[4])+" ")
			numlabel.place(x=190, y=170)
			numlabel['font']=self.font
		elif number==6:
			numlabel=Label(self.root, text=" "+str(self.numlist[5])+" ")
			numlabel.place(x=300, y=170)
			numlabel['font']=self.font
		elif number==7:
			numlabel=Label(self.root, text=" "+str(self.numlist[6])+" ")
			numlabel.place(x=80, y=280)
			numlabel['font']=self.font
		elif number==8:
			numlabel=Label(self.root, text=" "+str(self.numlist[7])+" ")
			numlabel.place(x=190, y=280)
			numlabel['font']=self.font
		elif number==9:
			numlabel=Label(self.root, text=" "+str(self.numlist[8])+" ")
			numlabel.place(x=300, y=280)
			numlabel['font']=self.font
		self.root.mainloop()


"""
Make Daylotto Object and Play in this method
"""
# Make Daylotto Object and Play in this method
def day_lotto_start(root):
	root.title("일일복권")
	root.geometry("450x540")
	img_field = PhotoImage(file = "./images/d_lottery.png")
	x = Label(root, image = img_field)
	x.place(x = 0, y = 0)
	root.update()
	ready = Daylotto(root)
	ready.play()
	result=ready.getresult()
	return result
	root.mainloop()