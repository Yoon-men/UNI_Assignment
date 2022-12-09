#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>
#include <Windows.h>

#define KEY_ESC 27
#define KEY_UP (256 + 72)
#define KEY_DOWN (256 + 80)
#define KEY_LEFT (256 + 75)
#define KEY_RIGHT (256 + 77)
#define KEY_SPACE 32

int GetKey(void)
{
    int ch = _getch();

    if (ch == 0 || ch == 224) // 방향키의 경우 0 또는 224의 값이 먼저 입력됨
        ch = 256 + _getch(); // 그 다음에 해당 방향키에 따라 72(Up), 80(Down), 75(Left), 77(Right) 값이 입력됨
    return ch;
}

void GotoXY(int x, int y)
{
    COORD pos = { x, y }; // COORD 구조체 변수를 통해 이동할 위치 설정
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}

void SetCursorVisible(int visible)
{
    CONSOLE_CURSOR_INFO ci = { 100, visible };
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &ci);
}


void DrawBoard(int** p);
void Shuffle(int** p);
void Swap(int* x, int* y);
int CheckSuccess(void);
int Cheat(void);

int** target_board = NULL;
int** current_board = NULL;
int row_cnt = 3;
int zero_x, zero_y;

void initialize(int count)
{
    zero_x = row_cnt - 1, zero_y = row_cnt - 1;
    target_board = malloc(sizeof(int) * row_cnt);
    current_board = malloc(sizeof(int) * row_cnt);
    for (int i = 0; i < row_cnt; i++)
    {
        target_board[i] = malloc(sizeof(int) * row_cnt);
        current_board[i] = malloc(sizeof(int) * row_cnt);
    }

    int num = 1;
    for (int i = 0; i < row_cnt; i++)
    {
        for (int j = 0; j < row_cnt; j++)
        {
            target_board[i][j] = num;
            current_board[i][j] = num;
            num++;
        }
    }
    target_board[row_cnt - 1][row_cnt - 1] = 0;
    current_board[row_cnt - 1][row_cnt - 1] = 0;
}

void Redraw(int x, int y, int value)
{
    int pos_x = y * row_cnt;
    int pos_y = x;

    GotoXY(pos_x, pos_y);
    if (value == 0)
    {
        switch (row_cnt)
        {
        case 3 : 
            printf("%3s", "   ");
            break;
        case 4 : 
            printf("%4s", "    ");
            break;
        case 5 : 
            printf("%5s", "     ");
            break;
        }
    }
        
    else
    {
        switch (row_cnt)
        {
        case 3:
            printf("%3d", value);
            break;
        case 4:
            printf("%4d", value);
            break;
        case 5:
            printf("%5d", value);
            break;
        }
    }
}

int main(void)
{
    srand(time(NULL));
    SetCursorVisible(0);

    while (1)
    {
        system("cls");
        initialize(row_cnt);
        Shuffle(current_board);
        DrawBoard(current_board);

        while (1)
        {
            if (_kbhit())                      // 키 입력이 있었다면
            {
                int key = GetKey();
                if (key == KEY_SPACE)
                    Cheat();
                else if (key == KEY_ESC)
                    break;
                else if (key == KEY_RIGHT)
                {
                    if (zero_x <= row_cnt - 2)
                    {
                        Swap(&current_board[zero_y][zero_x], &current_board[zero_y][zero_x + 1]);
                        Redraw(zero_y, zero_x, current_board[zero_y][zero_x]);
                        Redraw(zero_y, zero_x + 1, current_board[zero_y][zero_x + 1]);
                        zero_x++;
                    }
                }
                else if (key == KEY_LEFT)
                {
                    if (zero_x >= 1)
                    {
                        Swap(&current_board[zero_y][zero_x], &current_board[zero_y][zero_x - 1]);
                        Redraw(zero_y, zero_x, current_board[zero_y][zero_x]);
                        Redraw(zero_y, zero_x - 1, current_board[zero_y][zero_x - 1]);
                        zero_x--;
                    }
                }
                else if (key == KEY_DOWN)
                {
                    if (zero_y <= row_cnt - 2)
                    {
                        Swap(&current_board[zero_y][zero_x], &current_board[zero_y + 1][zero_x]);
                        Redraw(zero_y, zero_x, current_board[zero_y][zero_x]);
                        Redraw(zero_y + 1, zero_x, current_board[zero_y + 1][zero_x]);
                        zero_y++;
                    }
                }
                else if (key == KEY_UP)
                {
                    if (zero_y >= 1)
                    {
                        Swap(&current_board[zero_y][zero_x], &current_board[zero_y - 1][zero_x]);
                        Redraw(zero_y, zero_x, current_board[zero_y][zero_x]);
                        Redraw(zero_y - 1, zero_x, current_board[zero_y - 1][zero_x]);
                        zero_y--;
                    }
                }

                if (CheckSuccess())
                {
                    GotoXY(0, 10);
                    printf(">>> 성공!!!\n");
                    if (row_cnt < 5)
                    {
                        row_cnt += 1;
                        printf("[ 다음 단계 %d X %d ]", row_cnt, row_cnt);
                        Sleep(1000);
                    }
                    break;
                }
            }
        }
    }

    printf("프로그램 종료\n");

    return 0;
}

void DrawBoard(int** p)
{
    for (int i = 0; i < row_cnt; i++)
    {
        for (int j = 0; j < row_cnt; j++)
        {
            if (p[i][j] == 0)
            {
                switch (row_cnt)
                {
                case 3:
                    printf("%3s", "   ");
                    break;
                case 4:
                    printf("%4s", "    ");
                    break;
                case 5:
                    printf("%5s", "     ");
                }
            }
            else
            {
                switch (row_cnt)
                {
                case 3:
                    printf("%3d", p[i][j]);
                    break;
                case 4:
                    printf("%4d", p[i][j]);
                    break;
                case 5:
                    printf("%5d", p[i][j]);
                }
            }
        }
        printf("\n");
    }
}

void Shuffle(int** p)
{
    for (int i = 0; i < 100; i++)
    {
        int direction = rand() % 4;   // 0(동), 1(서), 2(남), 3(북)
        if (direction == 0)
        {
            if (zero_x <= row_cnt - 2)
            {
                Swap(&p[zero_y][zero_x], &p[zero_y][zero_x + 1]);
                zero_x++;
            }
        }
        else if (direction == 1)
        {
            if (zero_x >= 1)
            {
                Swap(&p[zero_y][zero_x], &p[zero_y][zero_x - 1]);
                zero_x--;
            }
        }
        else if (direction == 2)
        {
            if (zero_y <= row_cnt - 2)
            {
                Swap(&p[zero_y][zero_x], &p[zero_y + 1][zero_x]);
                zero_y++;
            }
        }
        else if (direction == 3)
        {
            if (zero_y >= 1)
            {
                Swap(&p[zero_y][zero_x], &p[zero_y - 1][zero_x]);
                zero_y--;
            }
        }
    }
}

void Swap(int* x, int* y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

int CheckSuccess(void)
{
    for (int i = 0; i < row_cnt; i++)
    {
        for (int j = 0; j < row_cnt; j++)
        {
            if (current_board[i][j] != target_board[i][j])
                return 0;
        }
    }

    return 1;
}

int Cheat(void)
{
    for (int i = 0; i < row_cnt; i++)
    {
        for (int j = 0; j < row_cnt; j++)
            current_board[i][j] = target_board[i][j];
    }
 
    GotoXY(0, 8);
    printf(">> Cheat has been activated.");

    return 1;
}