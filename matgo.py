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
        self.__mulitple = 1 # 배율
        self.__field=[[], [], [], [], [], [], [], [], [], [], [], []]
        if first==2:
            self.__first=0
        if first!=2:
            self.__first=first
        self.__was_playerscore=0
        self.__was_computerscore=0
        self.__nagari=nagari
        self.__playermoney=playermoney
        self.__computermoney=computermoney
        self.__fliped=PhotoImage(file = "./img_matgo/뒤집은거.png")
        self.__img_field = PhotoImage(file = "./img_matgo/Field.png")
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
    def play(self,a): # 판돈*score, 누가 이겼는지 return
        if self.__nagari==0:
            self.__panmoney=Reader.panmoney(self.__playermoney, self.__computermoney,root)
        self.__panmoney=self.__panmoney*2**(self.__nagari)
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
        if self.__first==1:
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

        for i in range(12): # 총통인 4개의 카드를 GUI로 출력해야 함
            if len(player.month_arrange()[i])==4:
                player_4cards=True
                store_mi = i
            if len(computer.month_arrange()[i])==4:
                computer_4cards=True
                store_ci = i
        for i in range(8): # 필드에 총통
            if len(self.__field[i])==4:
                if self.__first==0:
                    if computer_4cards == 'True':
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
                        chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
                        chongtong_button.pack()
                        
                        def finish():
                            chongtong_window.destroy()
                            chongtong_window.quit()
                        chongtong_window.mainloop()
                        return ["double"]
                    else:
                        chongtong_window = Toplevel(a)
                        chongtong_label = Label(chongtong_window,text = "플레이어 총통!")
                        chongtong_label.pack()
                        my_img = []
                        my =[]
                        for j in range(len(self.__field[i])):
                            my_img.append(PhotoImage("./img_matgo/"+self.field[i][j].img))
                            my.append(Label(chongtong_window,image= my_img[j]))
                            my[j].pack()
                        chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
                        chongtong_button.pack()
                        def finish():
                            chongtong_window.destroy()
                            chongtong_window.quit()
                        chongtong_window.mainloop()
                        return ["player", 10*self.__panmoney]
                else:
                    if player_4cards:
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
                        chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
                        chongtong_button.pack()
                        def finish():
                            chongtong_window.destroy()
                            chongtong_window.quit()
                        chongtong_window.mainloop()
                        return ["double"]
                    else:
                        chongtong_window = Toplevel(a)
                        chongtong_label = Label(chongtong_window,text = "컴퓨터 총통!")
                        chongtong_label.pack()
                        cm_img = []
                        cm =[]
                        for j in range(len(self.__field[i])):
                            cm_img.append(PhotoImage("./img_matgo/"+self.field[i][j].img))
                            cm.append(Label(chongtong_window,image= cm_img[j]))
                            cm[j].pack()
                        chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
                        chongtong_button.pack()
                        def finish():
                            chongtong_window.destroy()
                            chongtong_window.quit()
                        chongtong_window.mainloop()
                        return ["computer", 10*self.__panmoney]
        if player_4cards and not computer_4cards:
            chongtong_window = Toplevel(a)
            chongtong_label = Label(chongtong_window,text = "플레이어 총통!")
            chongtong_label.pack()
            my_img = []
            my =[]
            for i in range(len(player.month_arrange()[store_mi])):
                my_img.append(PhotoImage("./img_matgo/"+player.month_arrange()[store_mi][i].img))
                my.append(Label(chongtong_window,image= my_img[i]))
                my[i].pack()
            chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
            chongtong_button.pack()
            def finish():
                chongtong_window.destroy()
                chongtong_window.quit()
            chongtong_window.mainloop()
            return ["player", 10*self.__panmoney]
        elif not player_4cards and computer_4cards:
            chongtong_window = Toplevel(a)
            chongtong_label = Label(chongtong_window,text = "컴퓨터 총통!")
            chongtong_label.pack()
            cm_img = []
            cm =[]
            for i in range(len(computer.month_arrange()[store_ci])):
                cm_img.append(PhotoImage("./img_matgo/"+computer.month_arrange()[store_ci][i].img))
                cm.append(Label(chongtong_window,image= cm_img[i]))
                cm[i].pack()
            chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
            chongtong_button.pack()
            def finish():
                chongtong_window.destroy()
                chongtong_window.quit()
            chongtong_window.mainloop()
            return ["computer", 10*self.__panmoney]
        elif player_4cards and computer_4cards:
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
            chongtong_button = Button(chongtong_window,text = "끄기",command=finish)
            chongtong_button.pack()
            def finish():
                chongtong_window.destroy()
                chongtong_window.quit()
            chongtong_window.mainloop()
            return ["double"]
        else: # 게임 시작
            for child in a.winfo_children():
                child.destroy()
            for _ in range(10):
                if self.__first==0: # 플레이어 선공
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
                        fuckwin_btn = Button(fuckwin_window,text = "끄기",command = finish)
                        fuckwin_btn.pack()
                        fuckwin_window.mainloop()
                        return ["player", 10*self.__panmoney]
                    if len(player.hand)==0:
                        if player.score>=7 and player_score_last < player.score:
                            self.__multiple=Score(player).multiple(computer)[0]
                            win_window = Toplevel(a)
                            def finish():
                                win_window.destroy()
                                win_window.quit()
                            win_label = Label(win_window,text="플레이어 승리 !")
                            win_money = Label(win_window,text="player get money : "+str(self.__multiple*Score(player).result_end()*self.__panmoney))
                            win_label.pack()
                            win_money.pack()
                            win_btn = Button(win_window,text = "끄기",command = finish)
                            win_btn.pack()
                            win_window.mainloop()
                            return ["player", self.__multiple*Score(player).result_end()*self.__panmoney]
                    copyfield = copy.deepcopy(self.__field)
                    copyplayer = copy.deepcopy(player)
                    copycomputer = copy.deepcopy(computer)
                    check = Turn.player_go_stop(player,a)
                    # check = Turn.computer_go_stop(player, computer, self.__field, self.__deck, self.__ai)
                    if not check:
                        self.__multiple=Score(player).multiple(computer)[0]
                        win_window = Toplevel(a)
                        def finish():
                            win_window.destroy()
                            win_window.quit()
                        win_label = Label(win_window,text="플레이어 승리 !")
                        win_money = Label(win_window,text="player get money : "+str(self.__multiple*Score(player).result_end()*self.__panmoney))
                        win_label.pack()
                        win_money.pack()
                        win_btn = Button(win_window,text = "끄기",command = finish)
                        win_btn.pack()
                        win_window.mainloop()
                        return ["player", self.__multiple*Score(player).result_end()*self.__panmoney]
                    
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
                            if copyplayer.hand[k].month==putcard.month:
                                bombcheck+=1
                                bombsave.append(k)
                        if bombcheck==3: # 폭탄
                            for k in range(12):
                                if copyfield[k]!=[]:
                                    if check and copyfield[k][0].month==putcard.month:
                                        for _ in range(3):
                                            copyfield[k].append(copycomputer.hand[bombsave[0]])
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
                    if len(player.hand)%3!=2:
                        time.sleep(1)
                    elif len(player.hand)%3==2:
                        time.sleep(0.2)
                    if computer.fuck_display==3:
                        fuckwin_window = Toplevel(a)
                        def finish():
                            fuckwin_window.destroy()
                            fuckwin_window.quit()
                        fuckwin_label = Label(fuckwin_window,text="컴퓨터 3뻑 승리 !")
                        fuckwin_label.pack()
                        fuckwin_btn = Button(fuckwin_window,text = "끄기",command = finish)
                        fuckwin_btn.pack()
                        fuckwin_window.mainloop()
                        return ["computer", 10*self.__panmoney]
                    if len(computer.hand)==0:
                        if computer.score>=7 and computer_score_last < computer.score:
                            self.__multiple=Score(computer).multiple(player)[0]
                            win_window = Toplevel(a)
                            def finish():
                                win_window.destroy()
                                win_window.quit()
                            win_label = Label(win_window,text="컴퓨터 승리 !")
                            win_money = Label(win_window,text="Computer get money : "+str(self.__multiple*Score(computer).result_end()*self.__panmoney))
                            win_label.pack()
                            win_money.pack()
                            win_btn = Button(win_window,text = "끄기",command = finish)
                            win_btn.pack()
                            win_window.mainloop()
                            return ["computer", self.__multiple*Score(computer).result_end()*self.__panmoney]
                        else:
                            nagari_window = Toplevel(a)
                            nagari_label = Label(nagari_window,text="나가리입니다")
                            nagari_label.pack()
                            def finish():
                                nagari_window.destroy()
                                nagari_window.quit()
                            nagari_btn = Button(nagari_window,text = "끄기",command = finish)
                            nagari_btn.pack()
                            nagari_window.mainloop()
                            return ["nagari"]
                    check = Turn.computer_go_stop(computer, player, self.__field, self.__deck, self.__ai)
                    if not check:
                        self.__multiple=Score(computer).multiple(player)[0]
                        win_window = Toplevel(a)
                        def finish():
                            win_window.destroy()
                            win_window.quit()
                        win_label = Label(win_window,text="컴퓨터 승리 !")
                        win_money = Label(win_window,text="Computer get money : "+str(self.__multiple*Score(computer).result_end()*self.__panmoney))
                        win_label.pack()
                        win_money.pack()
                        win_btn = Button(win_window,text = "끄기",command = finish)
                        win_btn.pack()
                        win_window.mainloop()
                        return ["computer", self.__multiple*Score(computer).result_end()*self.__panmoney]
                    player_score_last=player.score
                    computer_score_last=computer.score
                    
                else: # 컴퓨터 선공
                    if len(computer.hand)%3==2:
                        for child in a.winfo_children():
                            child.destroy()
                    self.gui(player, computer, self.__field, player, computer, a)
                    if len(computer.hand)==10:
                        time.sleep(1)
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
                                            copyfield[k].append(copycomputer.hand[bombsave[0]])
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
                    
                    #self.printscreen()
                    if computer.fuck_display==3:
                        fuckwin_window = Toplevel(a)
                        def finish():
                            fuckwin_window.destroy()
                            fuckwin_window.quit()
                        fuckwin_label = Label(fuckwin_window,text="컴퓨터 3뻑 승리 !")
                        fuckwin_label.pack()
                        fuckwin_btn = Button(fuckwin_window,text = "끄기",command = finish)
                        fuckwin_btn.pack()
                        fuckwin_window.mainloop()
                        return ["computer", 10*self.__panmoney]
                    if len(computer.hand)==0:
                        if computer.score>=7 and computer_score_last < computer.score:
                            self.__multiple=Score(computer).multiple(player)[0]
                            win_window = Toplevel(a)
                            def finish():
                                win_window.destroy()
                                win_window.quit()
                            win_label = Label(win_window,text="컴퓨터 승리 !")
                            win_money = Label(win_window,text="Computer get money : "+str(self.__multiple*Score(computer).result_end()*self.__panmoney))
                            win_label.pack()
                            win_money.pack()
                            win_btn = Button(win_window,text = "끄기",command = finish)
                            win_btn.pack()
                            win_window.mainloop()
                            return ["computer", self.__multiple*Score(computer).result_end()*self.__panmoney]
                    self.gui(player, computer, self.__field, player, computer, a)
                    copyfield = copy.deepcopy(self.__field)
                    copyplayer = copy.deepcopy(player)
                    copycomputer = copy.deepcopy(computer)
                    check = Turn.computer_go_stop(computer, player, self.__field, self.__deck, self.__ai)
                    if not check:
                        self.__multiple=Score(computer).multiple(player)[0]
                        win_window = Toplevel(a)
                        def finish():
                            win_window.destroy()
                            win_window.quit()
                        win_label = Label(win_window,text="컴퓨터 승리 !")
                        win_money = Label(win_window,text="Computer get money : "+str(self.__multiple*Score(computer).result_end()*self.__panmoney))
                        win_label.pack()
                        win_money.pack()
                        win_btn = Button(win_window,text = "끄기",command = finish)
                        win_btn.pack()
                        win_window.mainloop()
                        return ["computer", self.__multiple*Score(computer).result_end()*self.__panmoney]
                    time.sleep(1)
                    copyfield = copy.deepcopy(self.__field)
                    copyplayer = copy.deepcopy(player)
                    copycomputer = copy.deepcopy(computer)
                    self.__field, putcard, next = Turn.playerturn(player, computer, self.__field, self.__deck,root)
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
                    if len(computer.hand)%3!=2:
                        time.sleep(1)
                    elif len(computer.hand)%3==2:
                        time.sleep(0.2)

                    if player.fuck_display==3:
                        fuckwin_window = Toplevel(a)
                        def finish():
                            fuckwin_window.destroy()
                            fuckwin_window.quit()
                        fuckwin_label = Label(fuckwin_window,text="플레이어 3뻑 승리 !")
                        fuckwin_label.pack()
                        fuckwin_btn = Button(fuckwin_window,text = "끄기",command = finish)
                        fuckwin_btn.pack()
                        fuckwin_window.mainloop()
                        return ["player", 10*self.__panmoney]
                    if len(player.hand)==0:
                        if player.score>=7 and player_score_last < player.score:
                            self.__multiple=Score(player).multiple(computer)[0]
                            win_window = Toplevel(a)
                            def finish():
                                win_window.destroy()
                                win_window.quit()
                            win_label = Label(win_window,text="플레이어 승리 !")
                            win_money = Label(win_window,text="player get money : "+str(self.__multiple*Score(player).result_end()*self.__panmoney))
                            win_label.pack()
                            win_money.pack()
                            win_btn = Button(win_window,text = "끄기",command = finish)
                            win_btn.pack()
                            win_window.mainloop()
                            return ["player", self.__multiple*Score(player).result_end()*self.__panmoney]
                        else:
                            nagari_window = Toplevel(a)
                            nagari_label = Label(nagari_window,text="나가리입니다")
                            nagari_label.pack()
                            def finish():
                                nagari_window.destroy()
                                nagari_window.quit()
                            nagari_btn = Button(nagari_window,text = "끄기",command = finish)
                            nagari_btn.pack()
                            nagari_window.mainloop()
                            return ["nagari"]
                    
                    check = Turn.player_go_stop(player,a)
                    # check = Turn.computer_go_stop(player, computer, self.__field, self.__deck, self.__ai)
                    if not check:
                        self.__multiple=Score(player).multiple(computer)[0]
                        win_window = Toplevel(a)
                        def finish():
                            win_window.destroy()
                            win_window.quit()
                        win_label = Label(win_window,text="플레이어 승리 !")
                        win_money = Label(win_window,text="player get money : "+str(self.__multiple*Score(player).result_end()*self.__panmoney))
                        win_label.pack()
                        win_money.pack()
                        win_btn = Button(win_window,text = "끄기",command = finish)
                        win_btn.pack()
                        win_window.mainloop()
                        return ["player", self.__multiple*Score(player).result_end()*self.__panmoney]
                    player_score_last=player.score
                    computer_score_last=computer.score
            nagari_window = Toplevel(a)
            nagari_label = Label(nagari_window,text="나가리입니다")
            nagari_label.pack()
            def finish():
                nagari_window.destroy()
                nagari_window.quit()
            nagari_btn = Button(nagari_window,text = "끄기",command = finish)
            nagari_btn.pack()
            nagari_window.mainloop()
            return ["nagari"]

    def gui(self, handplayer, handcomputer, field, player, computer, a):
        img_field = self.__img_field
        x = Label(image = img_field)
        x.place(x =0, y=0)
        ph =[]
        ch =[]
        plhand_img = []
        comhand_img = []
        for i in range(len(handplayer.hand)):
            plhand_img.append(self.card(handplayer.hand[i].img))
            ph.append(Label( image = plhand_img[i]))
            ph[i].place(x=3+(i)*40,y=391)
        for i in range(len(handcomputer.hand)):
            comhand_img.append(self.__fliped)
            ch.append(Label( image = comhand_img[i]))
            ch[i].place(x=3+(i)*40,y=5)
        fd =[[],[],[],[],[],[],[],[],[],[],[],[]]
        fdhand_img = [[],[],[],[],[],[],[],[],[],[],[],[]]
        cnt=0
        a_cnt=0
        for i in field:
            for j in range(len(i)):
                fdhand_img[cnt].append(self.card(i[j].img))
                fd[cnt].append(Label( image = fdhand_img[cnt][j]))
                if 0<=cnt<=5:
                    fd[cnt][j].place(x= 15+cnt*55+5*j-a_cnt*45, y=150+5*j)
                else:
                    fd[cnt][j].place(x= 45+(cnt-6)*55+5*j-a_cnt*45, y=225+5*j)
            cnt+=1
        c_gotgwang_img = []
        c_gotgwang = []
        for i in range(len(computer.gwang)):
            c_gotgwang_img.append(self.card(computer.gwang[i].img))
            c_gotgwang.append(Label( image = c_gotgwang_img[i]))
            c_gotgwang[i].place(x= 15+i*13, y=75)
        c_gotbeegwang_img = []
        c_gotbeegwang = []
        for i in range(len(computer.beegwang)):
            c_gotbeegwang_img.append(self.card(computer.beegwang[i].img))
            c_gotbeegwang.append(Label( image = c_gotbeegwang_img[i]))
            c_gotbeegwang[i].place(x= 15+i*13 + 13*(len(computer.gwang)), y=75)
        c_gotreddan_img = []
        c_gotreddan = []
        for i in range(len(computer.reddan)):
            c_gotreddan_img.append(self.card(computer.reddan[i].img))
            c_gotreddan.append(Label( image = c_gotreddan_img[i]))
            c_gotreddan[i].place(x= 100+i*13, y=75)
        c_gotbluedan_img = []
        c_gotbluedan = []
        for i in range(len(computer.bluedan)):
            c_gotbluedan_img.append(self.card(computer.bluedan[i].img))
            c_gotbluedan.append(Label( image = c_gotbluedan_img[i]))
            c_gotbluedan[i].place(x= 100+i*13 +(len(computer.reddan))*13 , y=75)
        c_gotchodan_img = []
        c_gotchodan = []
        for i in range(len(computer.chodan)):
            c_gotchodan_img.append(self.card(computer.chodan[i].img))
            c_gotchodan.append(Label( image = c_gotchodan_img[i]))
            c_gotchodan[i].place(x= 100+i*13 +(len(computer.reddan))*13 + (len(computer.bluedan))*13 , y=75)
        c_gotdan_img = []
        c_gotdan = []
        for i in range(len(computer.dan)):
            c_gotdan_img.append(self.card(computer.dan[i].img))
            c_gotdan.append(Label( image = c_gotdan_img[i]))
            c_gotdan[i].place(x= 100+i*13 +(len(computer.reddan))*13 + (len(computer.bluedan))*13 +(len(computer.chodan))*13 , y=75)
        c_gotgodori_img = []
        c_gotgodori = []
        for i in range(len(computer.godori)):
            c_gotgodori_img.append(self.card(computer.godori[i].img))
            c_gotgodori.append(Label( image = c_gotgodori_img[i]))
            c_gotgodori[i].place(x= 220+i*13, y=75)
        c_gotanimal_img = []
        c_gotanimal = []
        for i in range(len(computer.animal)):
            c_gotanimal_img.append(self.card(computer.animal[i].img))
            c_gotanimal.append(Label( image = c_gotanimal_img[i]))
            c_gotanimal[i].place(x= 220+i*13 + len(computer.godori)*13, y=75)
        c_gotpee_img = []
        c_gotpee = []
        for i in range(len(computer.pee)):
            c_gotpee_img.append(self.card(computer.pee[i].img))
            c_gotpee.append(Label( image = c_gotpee_img[i]))
            c_gotpee[i].place(x= 340+i*13, y=75)
        c_gotdoublepee_img = []
        c_gotdoublepee = []
        for i in range(len(computer.doublepee)):
            c_gotdoublepee_img.append(self.card(computer.doublepee[i].img))
            c_gotdoublepee.append(Label( image = c_gotdoublepee_img[i]))
            c_gotdoublepee[i].place(x= 340+i*13+ 13*len(computer.pee), y=75)
        gotgwang_img = []
        gotgwang = []
        for i in range(len(player.gwang)):
            gotgwang_img.append(self.card(player.gwang[i].img))
            gotgwang.append(Label( image = gotgwang_img[i]))
            gotgwang[i].place(x= 15+i*13, y=325)
        gotbeegwang_img = []
        gotbeegwang = []
        for i in range(len(player.beegwang)):
            gotbeegwang_img.append(self.card(player.beegwang[i].img))
            gotbeegwang.append(Label( image = gotbeegwang_img[i]))
            gotbeegwang[i].place(x= 15+i*13 + 13*(len(player.gwang)), y=325)
        gotreddan_img = []
        gotreddan = []
        for i in range(len(player.reddan)):
            gotreddan_img.append(self.card(player.reddan[i].img))
            gotreddan.append(Label( image = gotreddan_img[i]))
            gotreddan[i].place(x= 100+i*13, y=325)
        gotbluedan_img = []
        gotbluedan = []
        for i in range(len(player.bluedan)):
            gotbluedan_img.append(self.card(player.bluedan[i].img))
            gotbluedan.append(Label( image = gotbluedan_img[i]))
            gotbluedan[i].place(x= 100+i*13 +(len(player.reddan))*13 , y=325)
        gotchodan_img = []
        gotchodan = []
        for i in range(len(player.chodan)):
            gotchodan_img.append(self.card(player.chodan[i].img))
            gotchodan.append(Label( image = gotchodan_img[i]))
            gotchodan[i].place(x= 100+i*13 +(len(player.reddan))*13 + (len(player.bluedan))*13 , y=325)
        gotdan_img = []
        gotdan = []
        for i in range(len(player.dan)):
            gotdan_img.append(self.card(player.dan[i].img))
            gotdan.append(Label( image = gotdan_img[i]))
            gotdan[i].place(x= 100+i*13 +(len(player.reddan))*13 + (len(player.bluedan))*13 +(len(player.chodan))*13 , y=325)
        gotgodori_img = []
        gotgodori = []
        for i in range(len(player.godori)):
            gotgodori_img.append(self.card(player.godori[i].img))
            gotgodori.append(Label( image = gotgodori_img[i]))
            gotgodori[i].place(x= 220+i*13, y=325)
        gotanimal_img = []
        gotanimal = []
        for i in range(len(player.animal)):
            gotanimal_img.append(self.card(player.animal[i].img))
            gotanimal.append(Label( image = gotanimal_img[i]))
            gotanimal[i].place(x= 220+i*13 + len(player.godori)*13, y=325)
        gotpee_img = []
        gotpee = []
        for i in range(len(player.pee)):
            gotpee_img.append(self.card(player.pee[i].img))
            gotpee.append(Label( image = gotpee_img[i]))
            gotpee[i].place(x= 340+i*13, y=325)
        gotdoublepee_img = []
        gotdoublepee = []
        for i in range(len(player.doublepee)):
            gotdoublepee_img.append(self.card(player.doublepee[i].img))
            gotdoublepee.append(Label( image = gotdoublepee_img[i]))
            gotdoublepee[i].place(x= 340+i*13+ 13*len(player.pee), y=325)
        if not (handplayer.hand==[] and handcomputer.hand==[]):
            dec_img= self.__fliped
            dec = Label( image = dec_img)
            dec.place(x = 500,y = 200)
        playerfuck = Label(text = "뻑 갯수 : "+str(player.fuck_display))
        playerfuck.place(x= 530, y=280)
        playerscore = Label(text = "점수 : "+str(player.score))
        playerscore.place(x=530,y=300)
        playershake = Label(text = "흔들기 : " + str(player.shake_display))
        playershake.place(x=530,y=320)
        playergwang = Label(text = "광 : " + str(len(player.gwang)+len(player.beegwang)))
        playergwang.place(x=530,y=360)
        playeranimal = Label(text = "열끗 : " + str(len(player.animal)+len(player.godori)))
        playeranimal.place(x=530,y=380)
        playerdan = Label(text = "단 : " + str(len(player.reddan)+len(player.bluedan)+len(player.chodan)+len(player.dan)))
        playerdan.place(x=530,y=400)
        playerpee = Label(text = "피 : " + str(len(player.pee)+2*len(player.doublepee)))
        playerpee.place(x=530,y=420)
        computerfuck = Label(text = "뻑 갯수 : "+str(computer.fuck_display))
        computerfuck.place(x= 530, y= 10)
        computerscore = Label(text = "점수 : "+str(computer.score))
        computerscore.place(x=530,y=30)
        computershake = Label(text = "흔들기 : " + str(computer.shake_display))
        computershake.place(x=530,y=50)
        playergo = Label(text = "고 : " + str(player.go_display))
        playergo.place(x = 530, y=340)
        computergo = Label(text="고 :" +str(computer.go_display))
        computergo.place(x=530,y=70)
        computergwang = Label(text = "광 : " + str(len(computer.gwang)+len(computer.beegwang)))
        computergwang.place(x=530,y=90)
        computeranimal = Label(text = "열끗 : " + str(len(computer.animal)+len(computer.godori)))
        computeranimal.place(x=530,y=110)
        computerdan = Label(text = "단 : " + str(len(computer.reddan)+len(computer.bluedan)+len(computer.chodan)+len(computer.dan)))
        computerdan.place(x=530,y=130)
        computerpee = Label(text = "피 : " + str(len(computer.pee)+2*len(computer.doublepee)))
        computerpee.place(x=530,y=150)
        a.update()



def main(root):
    # main procedure
    window = tk.Toplevel(root)
    def close_window():
        window.destroy()
        window.quit()
    window.title("<<<맞고>>>")
    btn_label = Label(window, text = "맞고 게임을 시작하시겠습니까?")
    btn_label.grid(row=0,column=0)
    btn_start = Button(window, text = "Start",command =close_window)
    btn_start.grid(row = 1,column=0)
    btn_quit = Button(window, text = "Quit",command = quit)
    btn_quit.grid(row = 1, column = 1)
    window.mainloop()
    while True:
        ask = Reader.load(root)
        if ask:
            slot_window = Toplevel(root)
            for i in range(1,6):
                text=open("save"+str(i)+".txt", "a")
                text.close()
                text=open("save"+str(i)+".txt", "r")
                player_money=text.readline()[:-1]
                computer_money=text.readline()[:-1]
                ai=text.readline()[:-1]
                name=text.readline()[:-1]
                slot_label = Label(slot_window,text = "[ 슬롯"+str(i)+" ]")
                slot_label.pack()
                if player_money=="":
                    slot_label['text'] = slot_label['text'] + " 비었음"
                else:
                    slot_label['text'] = slot_label['text'] + " 저장된 파일 있음"
                    if name=="":
                        slot_label['text'] = slot_label['text'] + "\n이름 : ???"
                    else:
                        slot_label['text'] = slot_label['text'] + "\n이름 : "+name
                    if not (ai=="easy" or ai=="normal" or ai=="hard" or ai=="hell" or ai=="impossible"):
                        slot_label['text'] = slot_label['text'] + "\n난이도 : ???"
                    else:
                        slot_label['text'] = slot_label['text'] + "\n난이도 : "+ai
                text.close()
            def finish():
                slot_window.destroy()
                slot_window.quit()
            slot_button = Button(slot_window,text = "끄기",command = finish)
            num=Reader.load_num(root)
            
            slot_button.pack()
            slot_window.mainloop()
            slot1_window = Toplevel(root)
            text=open("save"+str(num)+".txt", "r")
            player_money=text.readline()[:-1]
            computer_money=text.readline()[:-1]
            ai=text.readline()[:-1]
            name=text.readline()[:-1]
            text.close()
            if not (player_money.isdigit() and computer_money.isdigit()) or \
            not (ai=='easy' or ai=='normal' or ai=='hard' or ai=='hell' or ai=='impossible') or \
            name=="":
                label = Label(slot1_window,text = "세이브 파일이 없거나 손상되었습니다")
                label.pack()
            else:
                label1 = Label(slot1_window,text = "성공적으로 불러왔습니다.")
                label2 = Label(slot1_window,text = name+"님의 돈 :"+str(player_money))
                label3 = Label(slot1_window,text = "컴퓨터의 돈 :"+str(computer_money))
                label4 = Label(slot1_window,text = "난이도 :"+ai)
                label1.pack()
                label2.pack()
                label3.pack()
                label4.pack()
                player_money=int(player_money)
                computer_money=int(computer_money)
                break
            def finish():
                slot1_window.destroy()
                slot1_window.quit()
            button = Button(slot1_window,text = "제출", command=finish)
            button.pack()
            slot1_window.mainloop()
        else:        
            player_money=Reader.init_money(root)
            computer_money=player_money
            ai=Reader.ai(root)
            name=Reader.name(root)
            break
    first=2
    while True:
        nagari=0
        while True:
            ready=MatgoController(name, ai, nagari, player_money, computer_money,first)
            result=ready.play(root)
            computer = ready.computer()
            player = ready.player()
            result_window = Toplevel(root)
            if result[0]=="player":
                (player_money, computer_money) = (player_money+result[1], computer_money-result[1])
                result_label1 = Label(result_window,text="승리했습니다. "+str(result[1])+" 원을 얻었습니다.")
                multiplearr = []
                for x in range(len(Score(player).multiple(computer)[1])):
                    multiplearr.append(Label(result_window,text =Score(player).multiple(computer)[1][x]))
                    multiplearr[x].pack()
                print(len(Score(player).multiple(computer)[1]))
                result_label2 = Label(result_window,text="플레이어 소지금:"+str(player_money))
                result_label3 = Label(result_window,text="컴퓨터 소지금:"+str(computer_money))
                result_label1.pack()
                result_label2.pack()
                result_label3.pack()
                break
            elif result[0]=="computer":
                (player_money, computer_money) = (player_money-result[1], computer_money+result[1])
                result_label1 = Label(result_window,text="패배했습니다. "+str(result[1])+" 원을 잃었습니다.")
                multiplearr = []
                for x in range(len(Score(computer).multiple(player)[1])):
                    multiplearr.append(Label(result_window,text =Score(computer).multiple(player)[1][x]))
                    multiplearr[x].pack()
                print(len(Score(computer).multiple(player)[1]))
                result_label2 = Label(result_window,text="플레이어 소지금:"+str(player_money))
                result_label3 = Label(result_window,text="컴퓨터 소지금:"+str(computer_money))
                result_label1.pack()
                result_label2.pack()
                result_label3.pack()
                break
            elif result[0]=="double": # 양측 총통
                result_label1 = Label(result_window,text="무승부입니다.")
                result_label2 = Label(result_window,text="플레이어 소지금:"+str(player_money))
                result_label3 = Label(result_window,text="컴퓨터 소지금:"+str(computer_money))
                result_label1.pack()
                result_label2.pack()
                result_label3.pack()
                break
            else: # result[0]=="nagari"
                result_label1 = Label(result_window,text="나가리입니다. 다음판은 판돈 2배입니다.")
                result_label2 = Label(result_window,text="플레이어 소지금:"+str(player_money))
                result_label3 = Label(result_window,text="컴퓨터 소지금:"+str(computer_money))
                result_label1.pack()
                result_label2.pack()
                result_label3.pack()
                def finish():
                    result_window.destroy()
                    result_window.quit()
                result_button = Button(result_window,text = "네",command = finish)
                result_button.pack()
                ready.nagari()
            def finish():
                result_window.destroy()
                result_window.quit()
            result_button = Button(result_window,text = "네",command = finish)
            result_button.pack()
            result_window.mainloop()
        
        if player_money <= 0:
            pasan_window = Toplevel(root)
            pasan_label1 = Label(pasan_window,text="플레이어가 파산했습니다.")
            pasan_label1.pack()
            def finish():
                root.destroy()
                root.quit()
            pasan_button = Button(pasan_window,text = "끄기",command=finish)
            pasan_button.pack()
            pasan_window.mainloop()
            break
        if computer_money <= 0:
            pasan_window = Toplevel(root)
            pasan_label2 = Label(pasan_window,text="컴퓨터가 파산했습니다.")
            pasan_label2.pack()
            def finish():
                root.destroy()
                root.quit()
            pasan_button = Button(pasan_window,text = "끄기",command=finish)
            pasan_button.pack()
            pasan_window.mainloop()
            break

        save_complete=False
        if not Reader.again(root): # 다시 안할래요    
            while True:
                if Reader.save(root):
                    save_window = Toplevel(root)
                    print_label1 = []
                    for i in range(1,6):
                        text=open("save"+str(i)+".txt", "a+")
                        text.close()
                        text=open("save"+str(i)+".txt", "r")
                        print_label1.append(Label(save_window,text= "["+str(i)+"]"))
                        print_label1[i-1].pack()
                        space_label = Label(save_window)
                        if text.readline()[:-1]=="":
                            space_label['text'] = "비었음"
                        else:
                            space_label['text'] = "저장됨"
                        space_label.pack()
                        text.close()
                    number=Reader.save_num(root)
                    def finish():
                        save_window.destroy()
                        save_window.quit()
                    print_button = Button(save_window,text = "끄기",command = finish)
                    print_button.pack()
                    save_window.mainloop()
                    save1_window = Toplevel(root)
                    text=open("save"+str(number)+".txt", "r+")
                    if text.readline()[:-1]!="":
                        if Reader.re_check(root):
                            text.close()
                            text1=open("save"+str(number)+".txt", "w")
                            text1.write(str(player_money)+"\n"+str(computer_money)+"\n"+ai+"\n"+name+"\n")
                            text1.close()
                            save_complete=True
                            save_label=Label(save1_window,text = "저장되었습니다.")
                            save_label.pack()
                            def finish():
                                save1_window.destroy()
                                save1_window.quit()
                            save_button = Button(save1_window,text = "끄기",command = finish)
                            save_button.pack()
                            break
                    else:
                        text.write(str(player_money)+"\n"+str(computer_money)+"\n"+ai+"\n"+name+"\n")
                        text.close()
                        save_complete=True
                        save_label=Label(save1_window,text = "저장되었습니다.")
                        save_label.pack()
                        def finish():
                            save1_window.destroy()
                            save1_window.quit()
                        save_button = Button(save1_window,text = "끄기",command = finish)
                        save_button.pack()
                        break
                    save1_window.mainloop()
                else: # 저장 안할래요
                    save_complete=True
                    goodbye_window = Toplevel(root)
                    goodbye_label=Label(goodbye_window,text = "잘가요!")
                    goodbye_label.pack()
                    def finish():
                        root.quit()
                    goodbye_button = Button(goodbye_window,text = "끄기",command=finish)
                    goodbye_button.pack()
                    goodbye_window.mainloop()
                    break
        if save_complete:
            root.destroy()
            root.quit()
            break
root = Tk()
root.title("맞고")
root.geometry("600x500")
img_field = PhotoImage(file = "./img_matgo/Field.png")
x = Label(image = img_field)
x.place(x =0, y=0)
root.update()
main(root)
root.mainloop()