import random
import tkinter as tk
from tkinter import *
class Reader:

    @staticmethod
    def go(a):
        push_window = Toplevel(a)
        push_label = Label(push_window,text ="고?")
        push_label.pack()
        def yes():
            global b
            b = True
            push_window.destroy()
            push_window.quit()
        def no():
            global b
            b = False
            push_window.destroy()
            push_window.quit()
        push_yes = Button(push_window,text = "yes",command = yes)
        push_yes.pack()
        push_no = Button(push_window,text = "no",command = no)
        push_no.pack()
        
        push_window.mainloop()
        return b

    @staticmethod
    def push(a):
        push_window = Toplevel(a)
        push_label = Label(push_window,text ="밀기 하시겠습니까?")
        push_label.pack()
        def yes():
            global b
            b = True
            push_window.destroy()
            push_window.quit()
        def no():
            global b
            b = False
            push_window.destroy()
            push_window.quit()
        push_yes = Button(push_window,text = "yes",command = yes)
        push_yes.pack()
        push_no = Button(push_window,text = "no",command = no)
        push_no.pack()
        
        push_window.mainloop()
        return b

    @staticmethod
    def again(a):
        push_label = Label(a,text ="한번더 ?")
        push_label.pack()
        def yes():
            global b
            b = True
            a.destroy()
            a.quit()
        def no():
            global b
            b = False
            a.destroy()
            a.quit()
        push_yes = Button(a,text = "yes",command = yes)
        push_yes.pack()
        push_no = Button(a,text = "no",command = no)
        push_no.pack()
        a.mainloop()
        
        return b

    @staticmethod
    def shake(a):
        push_window = Toplevel(a)
        push_label = Label(push_window,text ="흔들겠습니까?")
        push_label.pack()
        def yes():
            global b
            b = True
            push_window.destroy()
            push_window.quit()
        def no():
            global b
            b = False
            push_window.destroy()
            push_window.quit()
        push_yes = Button(push_window,text = "yes",command = yes)
        push_yes.pack()
        push_no = Button(push_window,text = "no",command = no)
        push_no.pack()
        
        push_window.mainloop()
        return b

    @staticmethod
    def choose(a):
        push_window = Toplevel(a)
        push_label = Label(push_window,text ="쌍피열끗 중 무엇을 얻으시겠습니까?")
        push_label.pack()
        def yes():
            global b
            b = True
            push_window.destroy()
            push_window.quit()
        def no():
            global b
            b= False
            push_window.destroy()
            push_window.quit()
        push_yes = Button(push_window,text = "열끗",command = yes)
        push_yes.pack()
        push_no = Button(push_window,text = "쌍피",command = no)
        push_no.pack()
        push_window.mainloop()
        
        return b

    @staticmethod
    def cardchoose(number,a, field, hand):
        choose_btn = ['','','','','','','','','','']
        def selectnum0():
            global b
            b = 0
            delete()
            a.quit()
        def selectnum1():
            global b
            b = 1
            delete()
            a.quit()
        def selectnum2():
            global b
            b = 2
            delete()
            a.quit()
        def selectnum3():
            global b
            b = 3
            delete()
            a.quit()
        def selectnum4():
            global b
            b = 4
            delete()
            a.quit()
        def selectnum5():
            global b
            b = 5
            delete()
            a.quit()
        def selectnum6():
            global b
            b = 6
            delete()
            a.quit()
        def selectnum7():
            global b
            b = 7
            delete()
            a.quit()
        def selectnum8():
            global b
            b = 8
            delete()
            a.quit()
        def selectnum9():
            global b
            b = 9
            delete()
            a.quit()
        def delete():
            for i in range(len(number)):
                choose_btn[i].grid_forget()
        def check(card, field):
            flag=False
            for i in field:
                for k in i:
                    if k.month==card.month:
                        flag=True
            return flag

        if(len(hand)>=1):
            if(check(hand[0], field)):
                choose_btn[0] = Button(a,text = "!",command = selectnum0)
            else:
                choose_btn[0] = Button(a,text = "?",command = selectnum0)
        if(len(hand)>=2):
            if(check(hand[1], field)):
                choose_btn[1] = Button(a,text = "!",command = selectnum1)
            else:
                choose_btn[1] = Button(a,text = "?",command = selectnum1)
        if(len(hand)>=3):
            if(check(hand[2], field)):
                choose_btn[2] = Button(a,text = "!",command = selectnum2)
            else:
                choose_btn[2] = Button(a,text = "?",command = selectnum2)
        if(len(hand)>=4):
            if(check(hand[3], field)):
                choose_btn[3] = Button(a,text = "!",command = selectnum3)
            else:
                choose_btn[3] = Button(a,text = "?",command = selectnum3)
        if(len(hand)>=5):
            if(check(hand[4], field)):
                choose_btn[4] = Button(a,text = "!",command = selectnum4)
            else:
                choose_btn[4] = Button(a,text = "?",command = selectnum4)
        if(len(hand)>=6):
            if(check(hand[5], field)):
                choose_btn[5] = Button(a,text = "!",command = selectnum5)
            else:
                choose_btn[5] = Button(a,text = "?",command = selectnum5)
        if(len(hand)>=7):
            if(check(hand[6], field)):
                choose_btn[6] = Button(a,text = "!",command = selectnum6)
            else:
                choose_btn[6] = Button(a,text = "?",command = selectnum6)
        if(len(hand)>=8):
            if(check(hand[7], field)):
                choose_btn[7] = Button(a,text = "!",command = selectnum7)
            else:
                choose_btn[7] = Button(a,text = "?",command = selectnum7)
        if(len(hand)>=9):
            if(check(hand[8], field)):
                choose_btn[8] = Button(a,text = "!",command = selectnum8)
            else:
                choose_btn[8] = Button(a,text = "?",command = selectnum8)
        if(len(hand)>=10):
            if(check(hand[9], field)):
                choose_btn[9] = Button(a,text = "!",command = selectnum9)
            else:
                choose_btn[9] = Button(a,text = "?",command = selectnum9)
        for i in range(len(number)):
            choose_btn[i].place(x=3+(i)*40,y=391)
        a.mainloop()
        return int(b+1)
       
    @staticmethod
    def card_choose(obj,a,b):
        if obj.name=="Computer":
            return random.randrange(2)
        else :
            push_window = Toplevel()
            push_label = Label(push_window,text = "어떤것을 가져오시겠습니까?")
            push_label.grid(row =0)
            card1_image = PhotoImage(file = "./img_matgo/"+a.img)
            card1 = Label(push_window,image = card1_image)
            card1.grid(row= 1, column =0)
            card2_image = PhotoImage(file = "./img_matgo/"+b.img)
            card2 = Label(push_window,image = card2_image)
            card2.grid(row = 1, column =1)

            def yes():
                global c
                c = 0
                push_window.destroy()
                push_window.quit()
            def no():
                global c
                c= 1
                push_window.destroy()
                push_window.quit()
            push_yes = Button(push_window,text = "첫번째",command = yes)
            push_yes.grid(row = 2, column =0)
            push_no = Button(push_window,text = "두번째",command = no)
            push_no.grid(row = 2, column = 1)
            push_window.mainloop()
        
            return int(c)