from matgohand import *
from matgoai import *
from matgocard import *
from matgoview import *
from matgofield import *
from matgoturn import *
from matgoscore import *
from tkinter import *
import tkinter as tk
import random
import time
import copy
"""
MatgoController Main Class
"""
# MatgoController Main Class
class MatgoController:
    def __init__(self, name, ai, nagari, playermoney, computermoney, first):
        self.__ai=AI(ai)
        self.__player = got(name)
        self.__computer = got("Computer")
        self.__deck = Deck()
        self.__cardimg=[]
        for k in self.__deck.current:
            self.__cardimg.append([PhotoImage(file = "./img_matgo/"+k.img), k.img])
        self.__bombimg=PhotoImage(file = "./img_matgo/폭탄.png")
        self.__mulitple = 1 
        self.__field=[[], [], [], [], [], [], [], [], [], [], [], []]
        if first==2:
            self.__first=0
        if first!=2:
            self.__first=first
        self.__was_playerscore=0
        self.__was_computerscore=0
        self.__nagari=nagari
        self.playermoney=playermoney
        self.computermoney=computermoney
        self.__fliped=PhotoImage(file = "./img_matgo/뒤집은거.png")
        self.__img_field = PhotoImage(file = "./img_matgo/Field.png")
        self.playerimage = PhotoImage(file = "./img_matgo/Gony.png")
        self.computerimage = PhotoImage(file = "./img_matgo/monkfish.png")
        self.mission=[]
    """
    Return card's image
    """
    # Return card's image
    def card(self, imgname):
        for k in self.__cardimg:
            if imgname=="폭탄":
                return self.__bombimg
            elif imgname==k[1]:
                return k[0]
    def player(self):
        return self.__player
    def computer(self):
        return self.__computer
    def nagari(self):
        self.__nagari+=1
    """
    Play Matgo by this
    """
    # Play Matgo by this
    def play(self,a):
        if self.__nagari==0:
            self.__panmoney=100000
        self.__panmoney=self.__panmoney*2**(self.__nagari)
        overlap=[]
        for i in range(4):
            number=random.randrange(48)
            while(number in overlap):
                number=random.randrange(48)
            overlap.append(number)
            self.mission.append([self.__deck.current[number], PhotoImage(file = "./img_matgo/"+self.__deck.current[number].img)])
        deck = self.__deck
        play_window = Toplevel(a)
        new_label = Label(play_window,text = "새로운 게임을 시작합니다.")
        new_label.pack()
        def finish():
            play_window.destroy()
            play_window.quit()
        new_quitbut = Button(play_window,text= "종료", command =finish)
        if self.__first==0:
            firstattack = Label(play_window, text = "플레이어가 선공합니다.")
            firstattack.pack()
        else:
            firstattack = Label(play_window, text = "컴퓨터가 선공합니다.")
            firstattack.pack()
        new_quitbut.pack()
        play_window.mainloop()
        player = self.__player
        computer = self.__computer
        player_4cards=False
        computer_4cards=False
        for _ in range(5):
            player.get(deck.next())
        for _ in range(5):
            computer.get(deck.next(open=False))
        for _ in range(5):
            player.get(deck.next())
        for _ in range(5):
            computer.get(deck.next(open=False))
        player.hand_set(player.sequence_arrange())
        computer.hand_set(computer.sequence_arrange())
        for i in range(4):
            self.__field[i].append(deck.next())
        for i in range(6, 10):
            self.__field[i].append(deck.next())
        for i in range(12):
            for k in range(12):
                if i!=k and self.__field[i]!=[] and self.__field[k]!=[] and self.__field[i][0].month==self.__field[k][0].month:
                    self.__field[i].append(self.__field[k].pop())

        for i in range(12):
            if len(player.month_arrange()[i])==4:
                player_4cards=True
                store_mi = i
            if len(computer.month_arrange()[i])==4:
                computer_4cards=True
                store_ci = i
        for i in range(8):
            if len(self.__field[i])==4:
                if self.__first==0:
                    if computer_4cards == 'True':
                        self.gui(player, computer, self.__field, player, computer, a)
                        chongtong_window = Toplevel(a)
                        chongtong_label = Label(chongtong_window,text = "양쪽총통!")
                        chongtong_label.pack()
                        my_img = []
                        my =[]
                        for j in range(len(self.__field[i])):
                            my_img.append(PhotoImage("./img_matgo/"+self.field[i][j].img))
                            my.append(Label(chongtong_window,image= my_img[j]))
                            my[j].pack()
                        cm_img = []
                        cm =[]
                        for i in range(len(computer.month_arrange()[store_ci])):
                            cm_img.append(PhotoImage("./img_matgo/"+computer.month_arrange()[store_ci][i].img))
                            cm.append(Label(chongtong_window,image= cm_img[i]))
                            cm[i].pack()
                        chongtong_button = Button(chongtong_window,text = "확인",command=finish)
                        chongtong_button.pack()
                        def finish():
                            chongtong_window.destroy()
                            chongtong_window.quit()
                        chongtong_window.mainloop()
                        flag=False
                        return ["double", 0, flag]
                    else:
                        self.gui(player, computer, self.__field, player, computer, a)
                        chongtong_window = Toplevel(a)
                        chongtong_label = Label(chongtong_window,text = "플레이어 총통!")
                        chongtong_label.pack()
                        my_img = []
                        my =[]
                        for j in range(len(self.__field[i])):
                            my_img.append(PhotoImage("./img_matgo/"+self.field[i][j].img))
                            my.append(Label(chongtong_window,image= my_img[j]))
                            my[j].pack()
                        chongtong_button = Button(chongtong_window,text = "확인",command=finish)
                        chongtong_button.pack()
                        def finish():
                            chongtong_window.destroy()
                            chongtong_window.quit()
                        chongtong_window.mainloop()
                        flag=False
                        return ["player", 10*self.__panmoney, flag]
                else:
                    if player_4cards:
                        self.gui(player, computer, self.__field, player, computer, a)
                        chongtong_window = Toplevel(a)
                        chongtong_label = Label(chongtong_window,text = "양측 총통!")
                        chongtong_label.pack()
                        my_img = []
                        my =[]
                        for i in range(len(player.month_arrange()[store_mi])):
                            my_img.append(PhotoImage("./img_matgo/"+player.month_arrange()[store_mi][i].img))
                            my.append(Label(chongtong_window,image= my_img[i]))
                            my[i].pack()
                        cm_img = []
                        cm =[]
                        for j in range(len(self.__field[i])):
                            cm_img.append(PhotoImage("./img_matgo/"+self.field[i][j].img))
                            cm.append(Label(chongtong_window,image= cm_img[j]))
                            cm[j].pack()
                        chongtong_button = Button(chongtong_window,text = "확인",command=finish)
                        chongtong_button.pack()
                        def finish():
                            chongtong_window.destroy()
                            chongtong_window.quit()
                        chongtong_window.mainloop()
                        flag=False
                        return ["double", 0, flag]
                    else:
                        self.gui(player, computer, self.__field, player, computer, a)
                        chongtong_window = Toplevel(a)
                        chongtong_label = Label(chongtong_window,text = "컴퓨터 총통!")
                        chongtong_label.pack()
                        cm_img = []
                        cm =[]
                        for j in range(len(self.__field[i])):
                            cm_img.append(PhotoImage("./img_matgo/"+self.field[i][j].img))
                            cm.append(Label(chongtong_window,image= cm_img[j]))
                            cm[j].pack()
                        chongtong_button = Button(chongtong_window,text = "확인",command=finish)
                        chongtong_button.pack()
                        def finish():
                            chongtong_window.destroy()
                            chongtong_window.quit()
                        chongtong_window.mainloop()
                        flag=False
                        return ["computer", 10*self.__panmoney, flag]
        if player_4cards and not computer_4cards:
            self.gui(player, computer, self.__field, player, computer, a)
            chongtong_window = Toplevel(a)
            chongtong_label = Label(chongtong_window,text = "플레이어 총통!")
            chongtong_label.pack()
            my_img = []
            my =[]
            for i in range(len(player.month_arrange()[store_mi])):
                my_img.append(PhotoImage("./img_matgo/"+player.month_arrange()[store_mi][i].img))
                my.append(Label(chongtong_window,image= my_img[i]))
                my[i].pack()
            chongtong_button = Button(chongtong_window,text = "확인",command=finish)
            chongtong_button.pack()
            def finish():
                chongtong_window.destroy()
                chongtong_window.quit()
            chongtong_window.mainloop()
            flag=False
            return ["player", 10*self.__panmoney, flag]
        elif not player_4cards and computer_4cards:
            self.gui(player, computer, self.__field, player, computer, a)
            chongtong_window = Toplevel(a)
            chongtong_label = Label(chongtong_window,text = "컴퓨터 총통!")
            chongtong_label.pack()
            cm_img = []
            cm =[]
            for i in range(len(computer.month_arrange()[store_ci])):
                cm_img.append(PhotoImage("./img_matgo/"+computer.month_arrange()[store_ci][i].img))
                cm.append(Label(chongtong_window,image= cm_img[i]))
                cm[i].pack()
            chongtong_button = Button(chongtong_window,text = "확인",command=finish)
            chongtong_button.pack()
            def finish():
                chongtong_window.destroy()
                chongtong_window.quit()
            chongtong_window.mainloop()
            flag=False
            return ["computer", 10*self.__panmoney, flag]
        elif player_4cards and computer_4cards:
            self.gui(player, computer, self.__field, player, computer, a)
            chongtong_window = Toplevel(a)
            chongtong_label = Label(chongtong_window,text = "양측 총통!")
            chongtong_label.pack()
            my_img = []
            my =[]
            for i in range(len(player.month_arrange()[store_mi])):
                my_img.append(PhotoImage("./img_matgo/"+player.month_arrange()[store_mi][i].img))
                my.append(Label(chongtong_window,image= my_img[i]))
                my[i].pack()
            cm_img = []
            cm =[]
            for i in range(len(computer.month_arrange()[store_ci])):
                cm_img.append(PhotoImage("./img_matgo/"+computer.month_arrange()[store_ci][i].img))
                cm.append(Label(chongtong_window,image= cm_img[i]))
                cm[i].pack()
            chongtong_button = Button(chongtong_window,text = "확인",command=finish)
            chongtong_button.pack()
            def finish():
                chongtong_window.destroy()
                chongtong_window.quit()
            chongtong_window.mainloop()
            flag=False
            return ["double", 0, flag]
        else: # 게임 시작
            for child in a.winfo_children():
                child.destroy()
            for _ in range(10):
                if True:
                    if len(player.hand)%3==2:
                        for child in a.winfo_children():
                            child.destroy()
                    self.gui(player, computer, self.__field, player, computer, a)
                    copyfield = copy.deepcopy(self.__field)
                    copyplayer = copy.deepcopy(player)
                    copycomputer = copy.deepcopy(computer)
                    self.__field, putcard, next = Turn.playerturn(player, computer, self.__field, self.__deck,a)
                    if putcard.special=="폭탄":
                        check=True
                        check2=True
                        for k in range(12):
                            if copyfield[k]!=[]:
                                if copyfield[k][0].month==next.month:
                                    copyfield[k].append(next)
                                    check=False
                        if check:
                            for i in range(12):
                                if copyfield[i]==[] and check2:
                                    copyfield[i].append(next)
                                    check2=False
                        self.gui(player, computer, copyfield, copyplayer, copycomputer, a)
                        time.sleep(1)
                        
                    if putcard.special!="폭탄":
                        check=True
                        check2=True
                        bombcheck=0
                        bombsave=[]
                        for k in range(len(copyplayer.hand)):
                            if copyplayer.hand[k].month==putcard.month:
                                bombcheck+=1
                                bombsave.append(k)
                        if bombcheck==3: # 폭탄
                            for k in range(12):
                                if copyfield[k]!=[]:
                                    if check and copyfield[k][0].month==putcard.month:
                                        for _ in range(3):
                                            copyfield[k].append(copyplayer.hand[bombsave[0]])
                                            copyplayer.comput(bombsave[0])
                                            self.gui(player, computer, copyfield, copyplayer, copycomputer, a)
                                            time.sleep(0.3)
                                            check2=False
                                        check=False
                            if not check2:
                                time.sleep(0.7)
                            if check2:
                                for i in range(12):
                                    if copyfield[i]==[] and check2:
                                        copyfield[i].append(putcard)
                                        self.gui(player, computer, copyfield, copyplayer, copycomputer, a)
                                        check2=False                           
                                        time.sleep(1)
                            check=True
                            check2=True
                            for k in range(12):
                                if copyfield[k]!=[]:
                                    if copyfield[k][0].month==next.month:
                                        copyfield[k].append(next)
                                        check=False
                            if check:
                                for i in range(12):
                                    if copyfield[i]==[] and check2:
                                        copyfield[i].append(next)
                                        check2=False
                            self.gui(player, computer, copyfield, copyplayer, copycomputer, a)
                            time.sleep(1)
                        else: # 폭탄 아님
                            check=True
                            check2=True
                            for k in range(12):
                                if copyfield[k]!=[]:
                                    if copyfield[k][0].month==putcard.month:
                                        copyfield[k].append(putcard)
                                        check=False
                            if check:
                                for i in range(12):
                                    if copyfield[i]==[] and check2:
                                        copyfield[i].append(putcard)
                                        check2=False
                            self.gui(player, computer, copyfield, copyplayer, copycomputer, a)
                            time.sleep(1)
                            check=True
                            check2=True
                            for k in range(12):
                                if copyfield[k]!=[]:
                                    if copyfield[k][0].month==next.month:
                                        copyfield[k].append(next)
                                        check=False
                            if check:
                                for i in range(12):
                                    if copyfield[i]==[] and check2:
                                        copyfield[i].append(next)
                                        check2=False
                            self.gui(player, computer, copyfield, copyplayer, copycomputer, a)
                            time.sleep(1)
                    self.gui(player, computer, self.__field, player, computer, a)
                    if player.fuck_display==3:
                        fuckwin_window = Toplevel(a)
                        def finish():
                            fuckwin_window.destroy()
                            fuckwin_window.quit()
                        fuckwin_label = Label(fuckwin_window,text="플레이어 3뻑 승리 !")
                        fuckwin_label.pack()
                        fuckwin_btn = Button(fuckwin_window,text = "확인",command = finish)
                        fuckwin_btn.pack()
                        fuckwin_window.mainloop()
                        return ["player", 10*self.__panmoney]
                    if len(player.hand)==0:
                        if player.score>=7 and player_score_last < player.score:
                            self.__multiple=Score(player).multiple(computer)[0]
                            flag = False
                            if(player.check(self.mission[0][0]) and player.check(self.mission[1][0]) and player.check(self.mission[2][0]) and player.check(self.mission[3][0])):
                                self.__multiple*=5
                                flag = True
                            win_window = Toplevel(a)
                            def finish():
                                win_window.destroy()
                                win_window.quit()
                            win_label = Label(win_window,text="플레이어 승리 !")
                            win_money = Label(win_window,text="player get money : "+str(self.__multiple*Score(player).result_end()*self.__panmoney))
                            win_label.pack()
                            win_money.pack()
                            win_btn = Button(win_window,text = "확인",command = finish)
                            win_btn.pack()
                            win_window.mainloop()
                            return ["player", self.__multiple*Score(player).result_end()*self.__panmoney, flag]
                    copyfield = copy.deepcopy(self.__field)
                    copyplayer = copy.deepcopy(player)
                    copycomputer = copy.deepcopy(computer)
                    check = Turn.player_go_stop(player,a)
                    # check = Turn.computer_go_stop(player, computer, self.__field, self.__deck, self.__ai)
                    if not check:
                        self.__multiple=Score(player).multiple(computer)[0]
                        flag = False
                        if(player.check(self.mission[0][0]) and player.check(self.mission[1][0]) and player.check(self.mission[2][0]) and player.check(self.mission[3][0])):
                            self.__multiple*=5
                            flag = True
                        win_window = Toplevel(a)
                        def finish():
                            win_window.destroy()
                            win_window.quit()
                        win_label = Label(win_window,text="플레이어 승리 !")
                        win_money = Label(win_window,text="player get money : "+str(self.__multiple*Score(player).result_end()*self.__panmoney))
                        win_label.pack()
                        win_money.pack()
                        win_btn = Button(win_window,text = "확인",command = finish)
                        win_btn.pack()
                        win_window.mainloop()
                        return ["player", self.__multiple*Score(player).result_end()*self.__panmoney, flag]
                    
                    time.sleep(2)
                    copyfield = copy.deepcopy(self.__field)
                    copyplayer = copy.deepcopy(player)
                    copycomputer = copy.deepcopy(computer)
                    self.__field, putcard, next = Turn.computerturn(player, computer, self.__field, self.__deck, self.__ai)
                    if putcard.special=="폭탄":
                        check=True
                        check2=True
                        for k in range(12):
                            if copyfield[k]!=[]:
                                if copyfield[k][0].month==next.month:
                                    copyfield[k].append(next)
                                    check=False
                        if check:
                            for i in range(12):
                                if copyfield[i]==[] and check2:
                                    copyfield[i].append(next)
                                    check2=False
                        self.gui(player, computer, copyfield, copyplayer, copycomputer, a)
                        
                    if putcard.special!="폭탄":
                        check=True
                        check2=True
                        bombcheck=0
                        bombsave=[]
                        for k in range(len(copyplayer.hand)):
                            if copycomputer.hand[k].month==putcard.month:
                                bombcheck+=1
                                bombsave.append(k)
                        if bombcheck==3: # 폭탄
                            for k in range(12):
                                if copyfield[k]!=[]:
                                    if check and copyfield[k][0].month==putcard.month:
                                        for _ in range(3):
                                            copyfield[k].append(copycomputer.hand[bombsave[0]])
                                            copycomputer.comput(bombsave[0])
                                            self.gui(player, computer, copyfield, copyplayer, copycomputer, a)
                                            time.sleep(0.3)
                                            check2=False
                                        check=False
                            if not check2:
                                time.sleep(0.7)
                            if check2:
                                for i in range(12):
                                    if copyfield[i]==[] and check2:
                                        copyfield[i].append(putcard)
                                        self.gui(player, computer, copyfield, copyplayer, copycomputer, a)
                                        check2=False                                
                                        time.sleep(1)
                            check=True
                            check2=True
                            for k in range(12):
                                if copyfield[k]!=[]:
                                    if copyfield[k][0].month==next.month:
                                        copyfield[k].append(next)
                                        check=False
                            if check:
                                for i in range(12):
                                    if copyfield[i]==[] and check2:
                                        copyfield[i].append(next)
                                        check2=False
                            self.gui(player, computer, copyfield, copyplayer, copycomputer, a)
                        else: # 폭탄 아님
                            check=True
                            check2=True
                            for k in range(12):
                                if copyfield[k]!=[]:
                                    if copyfield[k][0].month==putcard.month:
                                        copyfield[k].append(putcard)
                                        check=False
                            if check:
                                for i in range(12):
                                    if copyfield[i]==[] and check2:
                                        copyfield[i].append(putcard)
                                        check2=False
                            self.gui(player, computer, copyfield, copyplayer, copycomputer, a)
                            time.sleep(1)
                            check=True
                            check2=True
                            for k in range(12):
                                if copyfield[k]!=[]:
                                    if copyfield[k][0].month==next.month:
                                        copyfield[k].append(next)
                                        check=False
                            if check:
                                for i in range(12):
                                    if copyfield[i]==[] and check2:
                                        copyfield[i].append(next)
                                        check2=False
                            self.gui(player, computer, copyfield, copyplayer, copycomputer, a)
                    time.sleep(1)
                    if computer.fuck_display==3:
                        self.gui(player, computer, self.__field, player, computer, a)
                        fuckwin_window = Toplevel(a)
                        def finish():
                            fuckwin_window.destroy()
                            fuckwin_window.quit()
                        fuckwin_label = Label(fuckwin_window,text="컴퓨터 3뻑 승리 !")
                        fuckwin_label.pack()
                        fuckwin_btn = Button(fuckwin_window,text = "확인",command = finish)
                        fuckwin_btn.pack()
                        fuckwin_window.mainloop()
                        return ["computer", 10*self.__panmoney]
                    if len(computer.hand)==0:
                        if computer.score>=7 and computer_score_last < computer.score:
                            self.gui(player, computer, self.__field, player, computer, a)
                            self.__multiple=Score(computer).multiple(player)[0]
                            flag = False
                            if(computer.check(self.mission[0][0]) and computer.check(self.mission[1][0]) and computer.check(self.mission[2][0]) and computer.check(self.mission[3][0])):
                                self.__multiple*=5
                                flag = True
                            win_window = Toplevel(a)
                            def finish():
                                win_window.destroy()
                                win_window.quit()
                            win_label = Label(win_window,text="컴퓨터 승리 !")
                            win_money = Label(win_window,text="Computer get money : "+str(self.__multiple*Score(computer).result_end()*self.__panmoney))
                            win_label.pack()
                            win_money.pack()
                            win_btn = Button(win_window,text = "확인",command = finish)
                            win_btn.pack()
                            win_window.mainloop()
                            return ["computer", self.__multiple*Score(computer).result_end()*self.__panmoney, flag]
                        else:
                            self.gui(player, computer, self.__field, player, computer, a)
                            nagari_window = Toplevel(a)
                            nagari_label = Label(nagari_window,text="나가리입니다")
                            nagari_label.pack()
                            self.gui(player, computer, copyfield, copyplayer, copycomputer, a)
                            def finish():
                                nagari_window.destroy()
                                nagari_window.quit()
                            nagari_btn = Button(nagari_window,text = "확인",command = finish)
                            nagari_btn.pack()
                            nagari_window.mainloop()
                            return ["nagari"]
                    check = Turn.computer_go_stop(computer, player, self.__field, self.__deck, self.__ai)
                    if not check:
                        self.gui(player, computer, self.__field, player, computer, a)
                        self.__multiple=Score(computer).multiple(player)[0]
                        flag = False
                        if(computer.check(self.mission[0][0]) and computer.check(self.mission[1][0]) and computer.check(self.mission[2][0]) and computer.check(self.mission[3][0])):
                            self.__multiple*=5
                            flag = True
                        win_window = Toplevel(a)
                        def finish():
                            win_window.destroy()
                            win_window.quit()
                        win_label = Label(win_window,text="컴퓨터 승리 !")
                        win_money = Label(win_window,text="Computer get money : "+str(self.__multiple*Score(computer).result_end()*self.__panmoney))
                        win_label.pack()
                        win_money.pack()
                        win_btn = Button(win_window,text = "확인",command = finish)
                        win_btn.pack()
                        win_window.mainloop()
                        return ["computer", self.__multiple*Score(computer).result_end()*self.__panmoney, flag]
                    player_score_last=player.score
                    computer_score_last=computer.score
            nagari_window = Toplevel(a)
            nagari_label = Label(nagari_window,text="나가리입니다")
            nagari_label.pack()
            def finish():
                nagari_window.destroy()
                nagari_window.quit()
            nagari_btn = Button(nagari_window,text = "확인",command = finish)
            nagari_btn.pack()
            nagari_window.mainloop()
            return ["nagari"]

    """
    Draw a field every moment
    """
    # Draw a field every moment
    def gui(self, handplayer, handcomputer, field, player, computer, a):
        for child in a.winfo_children():
            child.destroy()
        img_field = self.__img_field
        x = Label(a, image = img_field)
        x.place(x =0, y=0)
        mission1=Label(a, image=self.mission[0][1])
        mission1.place(x=496, y=200)
        mission2=Label(a, image=self.mission[1][1])
        mission2.place(x=536, y=200)
        mission3=Label(a, image=self.mission[2][1])
        mission3.place(x=576, y=200)
        mission4=Label(a, image=self.mission[3][1])
        mission4.place(x=616, y=200)
        if handplayer.check(self.mission[0][0]):
            Label(a, text="▼").place(x=496, y=200)            
        if handplayer.check(self.mission[1][0]):
            Label(a, text="▼").place(x=536, y=200)
        if handplayer.check(self.mission[2][0]):
            Label(a, text="▼").place(x=576, y=200)
        if handplayer.check(self.mission[3][0]):
            Label(a, text="▼").place(x=616, y=200)
        if handcomputer.check(self.mission[0][0]):
            Label(a, text="X").place(x=496, y=200)
        if handcomputer.check(self.mission[1][0]):
            Label(a, text="X").place(x=536, y=200)
        if handcomputer.check(self.mission[2][0]):
            Label(a, text="X").place(x=576, y=200)
        if handcomputer.check(self.mission[3][0]):
            Label(a, text="X").place(x=616, y=200)
        ph =[]
        ch =[]
        plhand_img = []
        comhand_img = []
        for i in range(len(handplayer.hand)):
            plhand_img.append(self.card(handplayer.hand[i].img))
            ph.append(Label(a,  image = plhand_img[i]))
            if 0<=i<5:
                ph[i].place(x=476+(i)*40,y=325)
            else:
            	ph[i].place(x=476+(i-5)*40,y=395)
        for i in range(len(handcomputer.hand)):
            comhand_img.append(self.__fliped)
            ch.append(Label(a,  image = comhand_img[i]))
            if 0<=i<5:
                ch[i].place(x=476+(i)*40,y=4)
            else:
            	ch[i].place(x=476+(i-5)*40,y=74)
        fd =[[],[],[],[],[],[],[],[],[],[],[],[]]
        fdhand_img = [[],[],[],[],[],[],[],[],[],[],[],[]]
        Label(a, image=self.playerimage).place(x = 379, y = 368)
        Label(a, image=self.computerimage).place(x = 379, y = 2)
        cnt=0
        for i in field:
            for j in range(len(i)):
                fdhand_img[cnt].append(self.card(i[j].img))
                fd[cnt].append(Label(a, image = fdhand_img[cnt][j]))
                if 0<=cnt<=5:
                    fd[cnt][j].place(x= 10+cnt*66+5*j, y=150+5*j)
                else:
                    fd[cnt][j].place(x= 40+(cnt-6)*66+5*j, y=235+5*j)
            cnt+=1
        c_gotgwang_img = []
        c_gotgwang = []
        for i in range(len(computer.gwang)):
            c_gotgwang_img.append(self.card(computer.gwang[i].img))
            c_gotgwang.append(Label(a,  image = c_gotgwang_img[i]))
            c_gotgwang[i].place(x= 5+i*7, y=3)
        c_gotbeegwang_img = []
        c_gotbeegwang = []
        for i in range(len(computer.beegwang)):
            c_gotbeegwang_img.append(self.card(computer.beegwang[i].img))
            c_gotbeegwang.append(Label(a,  image = c_gotbeegwang_img[i]))
            c_gotbeegwang[i].place(x= 5+i*7 + 7*(len(computer.gwang)), y=3)
        c_gotreddan_img = []
        c_gotreddan = []
        for i in range(len(computer.reddan)):
            c_gotreddan_img.append(self.card(computer.reddan[i].img))
            c_gotreddan.append(Label(a,  image = c_gotreddan_img[i]))
            c_gotreddan[i].place(x=115+i*7, y=3)
        c_gotbluedan_img = []
        c_gotbluedan = []
        for i in range(len(computer.bluedan)):
            c_gotbluedan_img.append(self.card(computer.bluedan[i].img))
            c_gotbluedan.append(Label(a,  image = c_gotbluedan_img[i]))
            c_gotbluedan[i].place(x=115+i*7 +(len(computer.reddan))*7 , y=3)
        c_gotchodan_img = []
        c_gotchodan = []
        for i in range(len(computer.chodan)):
            c_gotchodan_img.append(self.card(computer.chodan[i].img))
            c_gotchodan.append(Label(a,  image = c_gotchodan_img[i]))
            c_gotchodan[i].place(x=115+i*7 +(len(computer.reddan))*7 + (len(computer.bluedan))*7 , y=3)
        c_gotdan_img = []
        c_gotdan = []
        for i in range(len(computer.dan)):
            c_gotdan_img.append(self.card(computer.dan[i].img))
            c_gotdan.append(Label(a,  image = c_gotdan_img[i]))
            c_gotdan[i].place(x=115+i*7 +(len(computer.reddan))*7 + (len(computer.bluedan))*7 +(len(computer.chodan))*7 , y=3)
        c_gotgodori_img = []
        c_gotgodori = []
        for i in range(len(computer.godori)):
            c_gotgodori_img.append(self.card(computer.godori[i].img))
            c_gotgodori.append(Label(a,  image = c_gotgodori_img[i]))
            c_gotgodori[i].place(x=237+i*7, y=3)
        c_gotanimal_img = []
        c_gotanimal = []
        for i in range(len(computer.animal)):
            c_gotanimal_img.append(self.card(computer.animal[i].img))
            c_gotanimal.append(Label(a,  image = c_gotanimal_img[i]))
            c_gotanimal[i].place(x=237+i*7 + len(computer.godori)*7, y=3)
        c_gotpee_img = []
        c_gotpee = []
        for i in range(len(computer.pee)):
            c_gotpee_img.append(self.card(computer.pee[i].img))
            c_gotpee.append(Label(a,  image = c_gotpee_img[i]))
            c_gotpee[i].place(x=5+i*7, y=75)
        c_gotdoublepee_img = []
        c_gotdoublepee = []
        for i in range(len(computer.doublepee)):
            c_gotdoublepee_img.append(self.card(computer.doublepee[i].img))
            c_gotdoublepee.append(Label(a,  image = c_gotdoublepee_img[i]))
            c_gotdoublepee[i].place(x=5+i*7+ 7*len(computer.pee), y=75)
        gotgwang_img = []
        gotgwang = []
        for i in range(len(player.gwang)):
            gotgwang_img.append(self.card(player.gwang[i].img))
            gotgwang.append(Label(a,  image = gotgwang_img[i]))
            gotgwang[i].place(x= 5+i*7, y=395)
        gotbeegwang_img = []
        gotbeegwang = []
        for i in range(len(player.beegwang)):
            gotbeegwang_img.append(self.card(player.beegwang[i].img))
            gotbeegwang.append(Label(a,  image = gotbeegwang_img[i]))
            gotbeegwang[i].place(x= 5+i*7 + 7*(len(player.gwang)), y=395)
        gotreddan_img = []
        gotreddan = []
        for i in range(len(player.reddan)):
            gotreddan_img.append(self.card(player.reddan[i].img))
            gotreddan.append(Label(a,  image = gotreddan_img[i]))
            gotreddan[i].place(x= 120+i*7, y=395)
        gotbluedan_img = []
        gotbluedan = []
        for i in range(len(player.bluedan)):
            gotbluedan_img.append(self.card(player.bluedan[i].img))
            gotbluedan.append(Label(a,  image = gotbluedan_img[i]))
            gotbluedan[i].place(x= 120+i*7 +(len(player.reddan))*7 , y=395)
        gotchodan_img = []
        gotchodan = []
        for i in range(len(player.chodan)):
            gotchodan_img.append(self.card(player.chodan[i].img))
            gotchodan.append(Label(a,  image = gotchodan_img[i]))
            gotchodan[i].place(x= 120+i*7 +(len(player.reddan))*7 + (len(player.bluedan))*7 , y=395)
        gotdan_img = []
        gotdan = []
        for i in range(len(player.dan)):
            gotdan_img.append(self.card(player.dan[i].img))
            gotdan.append(Label(a,  image = gotdan_img[i]))
            gotdan[i].place(x= 120+i*7 +(len(player.reddan))*7 + (len(player.bluedan))*7 +(len(player.chodan))*7 , y=395)
        gotgodori_img = []
        gotgodori = []
        for i in range(len(player.godori)):
            gotgodori_img.append(self.card(player.godori[i].img))
            gotgodori.append(Label(a,  image = gotgodori_img[i]))
            gotgodori[i].place(x= 242+i*7, y=395)
        gotanimal_img = []
        gotanimal = []
        for i in range(len(player.animal)):
            gotanimal_img.append(self.card(player.animal[i].img))
            gotanimal.append(Label(a,  image = gotanimal_img[i]))
            gotanimal[i].place(x= 242+i*7 + len(player.godori)*7, y=395)
        gotpee_img = []
        gotpee = []
        for i in range(len(player.pee)):
            gotpee_img.append(self.card(player.pee[i].img))
            gotpee.append(Label(a,  image = gotpee_img[i]))
            gotpee[i].place(x=5+i*7, y=325)
        gotdoublepee_img = []
        gotdoublepee = []
        for i in range(len(player.doublepee)):
            gotdoublepee_img.append(self.card(player.doublepee[i].img))
            gotdoublepee.append(Label(a,  image = gotdoublepee_img[i]))
            gotdoublepee[i].place(x=5+i*7+ 7*len(player.pee), y=325)
        playerfuck = Label(a, text = "뻑 : "+str(player.fuck_display))
        playerfuck.place(x=401, y=235)
        playerscore = Label(a, text = "점수 : "+str(player.score))
        playerscore.place(x=401,y=255)
        playershake = Label(a, text = "흔들기 : " + str(player.shake_display))
        playershake.place(x=401,y=275)
        playergo = Label(a, text = "고 : " + str(player.go_display))
        playergo.place(x=401, y=295)
        if len(player.gwang)+len(player.beegwang)>0:
            playergwang = Label(a, text = str(len(player.gwang)+len(player.beegwang)))
            playergwang.place(x=5, y=395)
        if len(player.animal)+len(player.godori)>0:
            playeranimal = Label(a, text = str(len(player.animal)+len(player.godori)))
            playeranimal.place(x=242, y=395)
        if len(player.reddan)+len(player.bluedan)+len(player.chodan)+len(player.dan):
            playerdan = Label(a, text= str(len(player.reddan)+len(player.bluedan)+len(player.chodan)+len(player.dan)))
            playerdan.place(x=120, y=395)
        if len(player.pee)+len(player.doublepee)>0:
            playerpee = Label(a, text = str(len(player.pee)+2*len(player.doublepee)))
            playerpee.place(x=5, y=325)
        computerfuck = Label(a, text = "뻑 : "+str(computer.fuck_display))
        computerfuck.place(x=401, y= 142)
        computerscore = Label(a, text = "점수 : "+str(computer.score))
        computerscore.place(x=401,y=162)
        computershake = Label(a, text = "흔들기 : " + str(computer.shake_display))
        computershake.place(x=401,y=182)
        computergo = Label(a, text="고 :" +str(computer.go_display))
        computergo.place(x=401,y=202)
        playermoney = Label(a, text="소지금\n"+str(self.playermoney))
        computermoney = Label(a, text="소지금\n"+str(self.computermoney))
        playermoney.place(x=396, y=328)
        computermoney.place(x=396, y=97)
        playermoney.place()
        if len(computer.gwang)+len(computer.beegwang)>0:
            computergwang = Label(a, text = str(len(computer.gwang)+len(computer.beegwang)))
            computergwang.place(x=5, y=3)
        if len(computer.animal)+len(computer.godori)>0:
            computeranimal = Label(a, text = str(len(computer.animal)+len(computer.godori)))
            computeranimal.place(x=237, y=3)
        if len(computer.dan)+len(computer.reddan)+len(computer.bluedan)+len(computer.chodan)>0:
            computerdan = Label(a, text = str(len(computer.reddan)+len(computer.bluedan)+len(computer.chodan)+len(computer.dan)))
            computerdan.place(x=115, y=3)
        if len(computer.pee)+len(computer.doublepee):
            computerpee = Label(a, text = str(len(computer.pee)+2*len(computer.doublepee)))
            computerpee.place(x=5, y=75)
        a.update()


"""
Make MatgoController Object, play, and return its result
"""
# Make MatgoController Object, play, and return its result
def matgomain(window, money):
    player_money=money
    computer_money=player_money
    ai="impossible"
    name="Player"
    first=2
    nagari=0
    while True:
        nagari=0
        while True:
            ready=MatgoController(name, ai, nagari, player_money, computer_money,first)
            result=ready.play(window)
            computer = ready.computer()
            player = ready.player()
            result_window = Toplevel(window)
            if result[0]=="player":
                money=result[1]
                (player_money, computer_money) = (player_money+result[1], computer_money-result[1])
                result_label1 = Label(result_window,text="승리했습니다. "+str(result[1])+" 원을 얻었습니다.")
                multiplearr = []
                for x in range(len(Score(player).multiple(computer)[1])):
                    multiplearr.append(Label(result_window,text =Score(player).multiple(computer)[1][x]))
                    multiplearr[x].pack()
                if result[2]:
                	mis=Label(result_window, text="미션 성공")
                	mis.pack()
                result_label1.pack()
                first=2
                break
            elif result[0]=="computer":
                money=result[1]*(-1)
                (player_money, computer_money) = (player_money-result[1], computer_money+result[1])
                result_label1 = Label(result_window,text="패배했습니다. "+str(result[1])+" 원을 잃었습니다.")
                multiplearr = []
                for x in range(len(Score(computer).multiple(player)[1])):
                    multiplearr.append(Label(result_window,text =Score(computer).multiple(player)[1][x]))
                    multiplearr[x].pack()
                if result[2]:
                	mis=Label(result_window, text="미션 성공")
                	mis.pack()
                result_label1.pack()
                first=3
                break
            elif result[0]=="double": # 양측 총통
                result_label1 = Label(result_window,text="무승부입니다.")
                money=0
                result_label1.pack()
                break
            else: # result[0]=="nagari"
                result_label1 = Label(result_window,text="나가리입니다. 다음판은 판돈 2배입니다.")
                result_label2 = Label(result_window,text="플레이어 소지금:"+str(player_money))
                result_label3 = Label(result_window,text="컴퓨터 소지금:"+str(computer_money))
                result_label1.pack()
                def finish():
                    result_window.destroy()
                    result_window.quit()
                result_button = Button(result_window,text = "확인",command = finish)
                result_button.pack()
                ready.nagari()
            def finish():
                result_window.destroy()
                result_window.quit()
            result_button = Button(result_window,text = "확인",command = finish)
            result_button.pack()
            result_window.mainloop()
        break
    window.destroy()
    window.quit()
    return money

"""
Make Matgo gui window and invoke Matgomain method
"""
# Make Matgo gui window and invoke Matgomain method
def matgostart(root, money):
    matgoroot = Toplevel(root)
    matgoroot.title("맞고")
    matgoroot.geometry("680x465")
    img_field = PhotoImage(file = "./img_matgo/Field.png")
    x = Label(matgoroot, image = img_field)
    x.place(x = 0, y=0)
    matgoroot.update()
    result=matgomain(matgoroot, money)
    return result
    matgoroot.mainloop()