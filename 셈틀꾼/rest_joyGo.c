#include <stdio.h>
int main()
{
    int ones, tens, hundreds, thousands, tenThousands;
    for (int i=10;i<100000;i++)
    {
        tenThousands=i/10000 ; thousands=(i%10000)/1000 ; hundreds=(i%1000)/100 ; tens=(i%100)/10 ; ones=i%10;

        if (i >= 10000)
        {
            if (thousands==0 && hundreds==0 && tens==0 && ones==0)
                continue;
            if (i%(thousands*1000 + hundreds*100 + tens*10 + ones) == 1)
                printf("%d\n", i);
        }
        else if (i >= 1000)
        {
            if (hundreds==0 && tens==0 && ones==0)
                continue;
            if (i%(hundreds*100 + tens*10 + ones) == 1)
                printf("%d\n", i);
        }
        else if (i >= 100)
        {
            if (tens==0 && ones==0)
                continue;
            if (i%(tens*10 + ones) == 1)
                printf("%d\n", i);
        }
        else
        {
            if (ones==0)
                continue;
            if (i%(ones) == 1)
                printf("%d\n", i);
        }
    }
    return 0;
}