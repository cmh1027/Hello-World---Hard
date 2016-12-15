import random

def confirm():
    print("")
    print("원하는 기능에 해당하는 숫자를 입력하세요.")
    print("1 : 복권 시작  2 : 소지금 확인  3 : 당첨 금액 목록 보기")
    print("4 : 종료")

def Showlist():
    print("당첨 금액 목록")
    print("")
    print("6 : 10000      16 : 72")
    print("7 : 36         17 : 180")
    print("8 : 720        18 : 119")
    print("9 : 360        19 : 36")
    print("10 : 80        20 : 306")
    print("11 : 252       21 : 1080")
    print("12 : 108       22 : 144")
    print("13 : 72        23 : 1800")
    print("14 : 54        24 : 3600")
    print("15 : 180")

def play():						#복권 처리 함수

    i = 0
    j = 0
    num = 0
    turn = 0
    value = 1
    money = 0
	
#숫자가 가려진 배열  
    blind = [[0]*3 for i in range(3)]		
	
#모든 숫자가 적혀있는 답안 배열
    mainarr = [[0]*3 for i in range(3)]			 
	
	
    Shuarr = [1,2,3,4,5,6,7,8,9]
    random.shuffle(Shuarr)
		
# 섞인 배열을 답안 배열판에 대입

    for x in range(3):          
        for y in range(3):
            mainarr[i][j] = Shuarr[num]
            num = num + 1
            j = j + 1
        i = i + 1
        j = 0
        
    j = 0
    i = 0
	
# 가려진 배열 출력
    
    a = random.randrange(0, 3)
    b = random.randrange(0, 3)
    blind[a][b] = mainarr[a][b]# 가려진 배열 중 한칸을 무작위로 공개
    for b in range(3):
        print(blind[i][j], blind[i][j+1], blind[i][j+2])
        print("")
        i = i + 1
        j = 0
        
    i = 0
    j = 0
    print("공개를 원하는 곳의 번호를 입력하세요.");
    print("");
    print("위치 번호");
    print("1 2 3");
    print("4 5 6");
    print("7 8 9");

        # 가려진 배열 중 한칸을 무작위로 공개
    while turn<3:
        sel_num = int(input())

        if((sel_num == 1) & (blind[0][0] == 0)):
            blind[0][0] = mainarr[0][0]
            for b in range(3):
                print(blind[i][j], blind[i][j+1], blind[i][j+2])
                print("")
                i = i + 1
                j = 0
            i = 0
            j = 0
            turn = turn + 1
            
        elif((sel_num == 2) & (blind[0][1] == 0)):
            blind[0][1] = mainarr[0][1]
            for b in range(3):
                print(blind[i][j], blind[i][j+1], blind[i][j+2])
                print("")
                i = i + 1
                j = 0
            i = 0
            j = 0
            turn = turn + 1

        elif((sel_num == 3) & (blind[0][2] == 0)):
            blind[0][2] = mainarr[0][2]
            for b in range(3):
                print(blind[i][j], blind[i][j+1], blind[i][j+2])
                print("")
                i = i + 1
                j = 0
            i = 0
            j = 0
            turn = turn + 1

        elif((sel_num == 4) & (blind[1][0] == 0)):
            blind[1][0] = mainarr[1][0]
            for b in range(3):
                print(blind[i][j], blind[i][j+1], blind[i][j+2])
                print("")
                i = i + 1
                j = 0
            i = 0
            j = 0
            turn = turn + 1

        elif((sel_num == 5) & (blind[1][1] == 0)):
            blind[1][1] = mainarr[1][1]
            for b in range(3):
                print(blind[i][j], blind[i][j+1], blind[i][j+2])
                print("")
                i = i + 1
                j = 0
            i = 0
            j = 0
            turn = turn + 1

        elif((sel_num == 6) & (blind[1][2] == 0)):
            blind[1][2] = mainarr[1][2]
            for b in range(3):
                print(blind[i][j], blind[i][j+1], blind[i][j+2])
                print("")
                i = i + 1
                j = 0
            i = 0
            j = 0
            turn = turn + 1

        elif((sel_num == 7) & (blind[2][0] == 0)):
            blind[2][0] = mainarr[2][0]
            for b in range(3):
                print(blind[i][j], blind[i][j+1], blind[i][j+2])
                print("")
                i = i + 1
                j = 0
            i = 0
            j = 0
            turn = turn + 1

        elif((sel_num == 8) & (blind[2][0] == 0)):
            blind[2][0] = mainarr[2][0]
            for b in range(3):
                print(blind[i][j], blind[i][j+1], blind[i][j+2])
                print("")
                i = i + 1
                j = 0
            i = 0
            j = 0
            turn = turn + 1
            
        elif((sel_num == 9) & (blind[2][2] == 0)):
            blind[2][2] = mainarr[2][2]
            for b in range(3):
                print(blind[i][j], blind[i][j+1], blind[i][j+2])
                print("")
                i = i + 1
                j = 0
            i = 0
            j = 0
            turn = turn + 1

        else:
            print("번호를 잘못 입력하셨거나 이미 공개된 자리입니다.")
            
    print("원하는 행 또는 열 하나를 고르십시오.")
    print("")
    print("행렬 번호")
    print("7	1	2	3	8")
    print("")
    print("4	*	*	*")
    print("")
    print("5	*	*	*")
    print("")
    print("6	*	*	*")

    while value == 1:
        lot_num = int(input())

        if lot_num == 1:
            result = mainarr[0][0] + mainarr[1][0] + mainarr[2][0]
            value = 0
        elif lot_num == 2:
            result = mainarr[0][1] + mainarr[1][1] + mainarr[2][1]
            value = 0
        elif lot_num == 3:
            result = mainarr[0][2] + mainarr[1][2] + mainarr[2][2]
            value = 0
        elif lot_num == 4:
            result = mainarr[0][0] + mainarr[0][1] + mainarr[0][2]
            value = 0

        elif lot_num == 5:
            result = mainarr[1][0] + mainarr[1][1] + mainarr[1][2]
            value = 0

        elif lot_num == 6:
            result = mainarr[2][0] + mainarr[2][1] + mainarr[2][2]
            value = 0

        elif lot_num == 7:
            result = mainarr[0][0] + mainarr[1][1] + mainarr[2][2]
            value = 0
        elif lot_num == 8:
            result = mainarr[0][2] + mainarr[1][1] + mainarr[0][2]
            value = 0
        else:
            print("잘못 입력하셨습니다. 다시 입력하세요.")
    for a in range(3):
        print(mainarr[i][j], mainarr[i][j+1], mainarr[i][j+2])
        print("")
        i = i + 1
        j = 0
        
    i = 0
    j = 0
    print("고객님께서 고르신 행 또는 열의 합은", result, "입니다.")
    print("")

#합에 따른 당첨금 판별 
    if result == 6:
        money += 10000
        
    elif (result == 7) | (result == 19):
        money += 36
        
    elif result == 8:
        money += 720
        
    elif result == 9:
        money += 360
        
    elif result == 10:
        money += 80
        
    elif result == 11:
        money += 252
        
    elif result == 12:
        money += 108
        
    elif(result == 13) | (result == 16):
        money += 72
        
    elif result == 14:
        money += 54

    elif(result == 15) | (result == 17):
        money += 180

    elif result == 18:
        money += 119

    elif result == 20:
        money += 306

    elif result == 21:
        money += 1080

    elif result == 22:
        money += 144
        
    elif result == 23:
        money += 1800
        
    elif result == 24:
        money += 3600

    else:
        print("오류 : 숫자 합계가 당첨표와 일치하지 않습니다.")
        print("")
    return money

def yesno():
    a = input("일일복권에 도전하시겠습니까? 예 : Y, 아니오 : N입력")
    return a
    

money = 100
value2 = 1
playnum = 0
cost = 100
print("일일복권 프로그램 ver 1.1")
print("")
print("")
confirm()
while value2 == 1:
              select = int(input())
              if select == 1:
                  print("일일복권은 3번 도전할 수 있습니다.")
                  print("현재 도전 횟수 :", playnum, "번")
                  while playnum < 3:
                      answer = yesno()
                      if (answer == 'Y') or (answer == 'y'):
                          if money < cost:
                              print("소지금이 부족합니다.")
                              break
                          print("소지금이", cost, "만큼 지불되었습니다.")
                          plus_money = play()
                          money += plus_money
                          cost = cost + 100
                          print("현재 고객님의 소지금은", money, "원 입니다.")
                      elif(answer == 'N') or (answer == 'n'):
                          break
                      else:
                          print("잘못 입력하셨습니다. 다시 입력해주세요.")
                          yseno()

                  confirm()
              elif select == 2:
                  print("현재 고객님의 소지금은", money, "원 입니다.")
                  confirm()
              elif select == 3:
                  Showlist()
                  confirm()
              elif select == 4:
                  print("프로그램을 종료합니다.")
                  value2 = 0
              else:
                  print("잘못 입력하셨습니다. 다시 입력해주세요.")
