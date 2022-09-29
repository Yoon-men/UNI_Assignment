#include <stdio.h>
#include <stdlib.h>				// For rand
#include <Windows.h>			// For GoToXY
#include <time.h>

int p1_x = 0, p1_y = 3;
int p2_x = 0, p2_y = 6;
int p3_x = 0, p3_y = 9;
int p4_x = 0, p4_y = 12;

int rank_1, rank_2, rank_3, rank_4;


void GoToXY(int x, int y)
{
	COORD pos = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}

void DrawLine()				// 결승선을 그려요
{
	for (int y = 0;y < 15;y++)
	{
		GoToXY(100, y);
		printf("|");
	}
}

void DrawP(int x, int y, char ch)				// Draw Player
{
	GoToXY(x, y);
	printf("%c", ch);
}

void DrawPs()					// Draw Players, 커서 이동하고 플레이어를 그려요
{
	DrawP(p1_x, p1_y, '1');		// 큰 따옴표로 감싸면 글자가 깨져요
	DrawP(p2_x, p2_y, '2');
	DrawP(p3_x, p3_y, '3');
	DrawP(p4_x, p4_y, '4');
}

void DelPreviousPs()				// 이전 모습 삭제
{
	DrawP(p1_x, p1_y, ' ');
	DrawP(p2_x, p2_y, ' ');
	DrawP(p3_x, p3_y, ' ');
	DrawP(p4_x, p4_y, ' ');
}

void MoveP()
{
	int rank = 1;
	int status_1 = 1, status_2 = 1, status_3 = 1, status_4 = 1;
	while (p1_x < 100 | p2_x < 100 | p3_x < 100 | p4_x < 100)
	{
		Sleep(100);
		DelPreviousPs();

		p1_x += (p1_x < 100) ? rand() % 3 + 1 : 0;
		p2_x += (p2_x < 100) ? rand() % 3 + 1 : 0;
		p3_x += (p3_x < 100) ? rand() % 3 + 1 : 0;
		p4_x += (p4_x < 100) ? rand() % 3 + 1 : 0;

		DrawPs();

		if (status_1 && p1_x >= 100)
		{
			GoToXY(0, 16);
			printf(">>> 1번 선수 : %d등", rank);
			rank++;
			status_1 = 0;
		}
		if (status_2 && p2_x >= 100)
		{
			GoToXY(0, 17);
			printf(">>> 2번 선수 : %d등", rank);
			rank++;
			status_2 = 0;
		}
		if (status_3 && p3_x >= 100)
		{
			GoToXY(0, 18);
			printf(">>> 3번 선수 : %d등", rank);
			rank++;
			status_3 = 0;
		}
		if (status_4 && p4_x >= 100)
		{
			GoToXY(0, 19);
			printf(">>> 4번 선수 : %d등", rank);
			rank++;
			status_4 = 0;
		}
	}
}

void main()
{
	srand(time(NULL));
	system("mode CON COLS=110 LINES=25");
	DrawLine();
	DrawPs();
	MoveP();

	GoToXY(0, 20);
	printf(" ");
}