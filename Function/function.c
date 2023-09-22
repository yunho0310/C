#include <stdio.h>

int pp(void)
{
    printf("나는 할 수 있다! \n");
}

int main(void)
{
    int i;
    printf("오늘 많이 힘드셨나요? 힘드셨다면 0을 입력해주세요! 아니시면 1을 입력해주세요!");
    scanf("%d", &i);

    if(i == 0)
    {
        pp();
    }

    else
    {
        printf("여태한만큼 좀 더 힘내봐요!");
    }

    printf("오늘도 모두 수고하셨습니다!!!");
}