#include<stdio.h>
#include<math.h>

int main()
{
    int b[]={7,11,19,39,79,157,313};
    int p[]={4,2,5,3,1,7,6};
    int n=900;
    int r=37;
    int t[7],a[7];
    int i,num,rem,sum=0,po=0;
    char ch;
    char str[7];
    int r_in,s_inv,temp[7];
    for(i=0;i<7;i++)
    {
        t[i]=(b[i]*r)%n;
    }
    for(i=0;i<7;i++)
    {
        a[i]=t[p[i]-1];
    }
    printf("t: ");
    for(i=0;i<7;i++)
    {
        printf("%d ",t[i]);
    }
    printf("\na: ");
    for(i=0;i<7;i++)
    {
        printf("%d ",a[i]);
    }
    printf("\n");
    printf("enter message: ");
    scanf("%c",&ch);
    printf("msg: %c",ch);
    num=ch;
    printf("\nmsg binary: ");
    for(i=6;i>=0;i--)
    {
        rem=num%2;
        num=num/2;
        printf("%d",rem);
        if(rem)
        {
            sum=sum+a[i];
        }
    }
    printf("\nencoded: %d\n",sum);
    for(i=0;i<n;i++)
    {
        if((i*r)%n==1)
            {
                r_in=i;
                break;
            }
    }
    i=6;
    s_inv=(sum*r_in)%n;
    while(i>=0)
    {
        if((s_inv-b[i])>=0)
        {
            str[i]='1';
            s_inv=s_inv-b[i];
        }
        else
            str[i]='0';
        i--;
    }
    printf("s`: ");
    for(i=0;i<7;i++)
    printf("%c",str[i]);
    ///permute
    printf("\n");
    for(i=0;i<7;i++)
    {
        temp[i]=str[p[i]-1]-48;
    }
    printf("inverse knapsack sum: ");
    for(i=0;i<7;i++)
    {
        printf("%d",temp[i]);
    }
    sum = 0;
    for(i=6;i>=0;i--)
    {
        sum=sum+temp[i]*pow(2,po);
        po++;
    }
    printf("\ndecoded:%c\n",sum);
    return 0;




}
