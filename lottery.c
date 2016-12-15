#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void confirm()								/* 메뉴 함수 */ 
{
	int num;	
	printf("원하는 기능에 해당하는 숫자를 입력하세요.\n");
	printf("1 : 복권 시작  2 : 소지금 확인  3 : 당첨 금액 목록 보기\n");
	printf("4 : 종료\n");
}


void ShowList()								/* 당첨 금액 목록 표시 함수 */ 
{
	printf("당첨 금액 목록\n");
	printf("\n");
	printf("6 : 10000      16 : 72\n");
	printf("7 : 36         17 : 180\n");
	printf("8 : 720        18 : 119\n");
	printf("9 : 360        19 : 36\n");
	printf("10 : 80        20 : 306\n");
	printf("11 : 252       21 : 1080\n");
	printf("12 : 108       22 : 144\n");
	printf("13 : 72        23 : 1800\n");
	printf("14 : 54        24 : 3600\n");
	printf("15 : 180\n");
}



void Shuffle(int *index) /* 배열 섞기 함수. 함수 출처 : http://bestitem.kr/102 */ 
{
	/* index : 원소들을 섞을 배열 */ 
	/* nMax : 배열 길이 */ 
	int i, n;
	int nTmp;
	
	srand(time(NULL));
	
	for(i = 9-1; i>=0; i--)
	{
		n = rand()% 9;
		nTmp = index[i];
		index[i]= index[n];
		index[n]= nTmp;
	}
	
	return index;
	
}

int play()							/* 복권 처리 함수 */ 
{
	int i, j;
	int a, b;
	int x, y;
	int num = 0;
	int turn = 0;
	int ran_num;
	int sel_num;
	int lot_num;
	int result;
	int money;
	
	srand(time(NULL));
	
	
	int blind[3][3] = 				/* 숫자가 가려진 배열 */ 
	{
		{0, 0, 0},
		{0, 0, 0},
		{0, 0, 0}
	};
	
	int  mainarr[3][3] = 			/* 모든 숫자가 적혀있는 답안 배열 */ 
	{
		{0, 0, 0},
		{0, 0, 0},
		{0, 0, 0},
	};
	
	int exarr[] = {1,2,3,4,5,6,7,8,9};
	
	int Shuarr[] = Shuffle(exarr);
		
	
	for(i=0; i<3; i++)			/* 섞인 배열을 답안 배열판에 대입 */ 
	{
		for(j=0; j<3; j++)
		{
			mainarr[i][j] = Shuarr[num];
			num++;
		}
	}
	
	
	for(i=0; i<3; i++)			/* 가려진  2*2 배열 출력 */ 
	{
		for(j=0; j<3; j++)
		{
			printf("%d ", blind[i][j]);
			if(j == 2)
			{
				printf("\n");
			}
		}
	}
	
	a = rand() % 3;
	b = rand() % 3;
	
	blind[a][b] = mainarr[a][b];			/* 가려진 배열 중 한칸을 무작위로 공개 */ 
	
	
	printf("공개를 원하는 곳의 번호를 입력하세요.\n");
	printf("\n");
	printf("위치 번호\n");
	printf("1 2 3\n");
	printf("4 5 6\n");
	printf("7 8 9\n");
	
	
	while(turn<3)								/* 추가로 알고 싶은 배열칸 3개 정하기 */ 
	{
		scanf("%d", &sel_num);
		
		if((sel_num == 1) && (blind[0][0] == 0))
		{
			blind[0][0] = mainarr[0][0];
			turn++;
		}
		
		else if(sel_num == 2 && blind[0][1] == 0)
		{
			blind[0][1] = mainarr[0][1];
			turn++;
		}
		
		else if(sel_num == 3 && blind[0][2] == 0)
		{
			blind[0][2] = mainarr[0][2];
			turn++;
		}
		
		else if(sel_num == 4 && blind[1][0] == 0)
		{
			blind[1][0] = mainarr[1][0];
			turn++;
		}
		
		else if(sel_num == 5 && blind[1][1] == 0)
		{
			blind[1][1] = mainarr[1][1];
			turn++;
		}
		
		else if(sel_num == 6 && blind[1][2] == 0)
		{
			blind[1][2] = mainarr[1][2];
			turn++;
		}
		
		else if(sel_num == 7 && blind[2][0] == 0)
		{
			blind[2][0] = mainarr[2][0];
			turn++;
		}
		
		else if(sel_num == 8 && blind[2][1] == 0)
		{
			blind[2][1] = mainarr[2][1];
			turn++;
		}
		
		else if(sel_num == 9 && blind[2][2] == 0)
		{
			blind[2][2] = mainarr[2][2];
			turn++;
		}
		
		else
		{
			printf("번호를 잘못 입력하셨거나 이미 공개된 자리입니다.\n");
		}
		
		
		printf("원하는 행 또는 열 하나를 고르십시오.\n");
		printf("\n");
		printf("행렬 번호\n");
		printf("7	1	2	3	8\n");
		printf("\n"); 
		printf("4	*	*	*\n");
		printf("\n");
		printf("5	*	*	*\n");
		printf("\n");
		printf("6	*	*	*\n");
		
		while(1)
		{
			scanf("%d", &lot_num);
			
			if(lot_num == 1)
			{
				result = mainarr[0][0] + mainarr[1][0] + mainarr[2][0];
				break;
			}
			
			else if(lot_num == 2)
			{
				result = mainarr[0][1] + mainarr[1][1] + mainarr[2][1];
				break;
			}
			
			else if(lot_num == 3)
			{
				result = mainarr[0][2] + mainarr[1][2] + mainarr[2][2];
				break;
			}
			
			else if(lot_num == 4)
			{
				result = mainarr[0][0] + mainarr[0][1] + mainarr[0][2];
				break;
			}
			
			else if(lot_num == 5)
			{
				result = mainarr[1][0] + mainarr[1][1] + mainarr[1][2];
				break;
			}
			
			else if(lot_num == 6)
			{
				result = mainarr[2][0] + mainarr[2][1] + mainarr[2][2];
				break;
			}
			
			else
			{
				printf("잘못 입력하셨습니다. 다시 입력하세요.\n");
			}
		}
		
		printf("고객님께서 고르신 행 또는 열의 합은 %d 입니다.", result);
		
		
		if(result == 6)						/* 합에 따른 당첨금 판별 */ 
		{
			money += 10000;
		}
		
		else if(result == 7 || result == 19)
		{
			money += 36;
		}
		
		else if(result == 8)
		{
			money += 720;
		}
		
		else if(result == 9)
		{
			money += 360;
		}
		
		else if(result == 10)
		{
			money += 80;
		}
		
		else if(result == 11)
		{
			money += 252;
		}
		
		else if(result == 12)
		{
			money += 108;
		}
		
		else if(result == 13 || result == 16)
		{
			money += 72;
		}
		
		else if(result == 14)
		{
			money += 54;
		}
		
		else if(result == 15 || result == 17)
		{
			money += 180;
		}
		
		else if(result == 18)
		{
			money += 119;
		}
		
		else if(result == 20)
		{
			money += 306;
		}
		
		else if(result == 21)
		{
			money += 1080;
		}
		
		else if(result == 22)
		{
			money += 144;
		}
		
		else if(result == 23)
		{
			money += 1800;
		}
		
		else if(result == 24)
		{
			money += 3600;
		}
		
		else
		{
			printf("오류 : 숫자 합계가 당첨표와 일치하지 않습니다.\n");
		}
		
		return money; 
	}
	
	
	
	
}
		
int main()							/* 메인 함수 */ 
{			
	int i = 0;
	int money = 100;
	int plus_money;
	int select;
	printf("일일복권 프로그램\n");
	printf("\n");
	printf("\n");
	confirm();
	while(1)
	{
		scanf("%d", &select);
		if(select == 1)
		{
			plus_money = play();
			money += plus_money;
			printf("현재 고객님의 소지금은 %d 원입니다.\n", money);
		}
		
		else if(select == 2)
		{
			break;
		}
		
		else if(select == 3)
		{
			ShowList();
		}
		
		else if(select == 4)
		{
			printf("프로그램을 종료합니다.\n");
			break;
		}
		
		else
		{
			printf("잘못 입력하셨습니다.\n");
			printf("다시 압력해주세요.\n");
		}
			
	}

	
	return 0;
	
}


