#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/msg.h>
#include<sys/stat.h>
#include<string.h>
#define KEY 500
struct msg
{
 long int type;
 char a[1024];
 int pid;
}p;
int main()
{
 int m,n,fd,m1;
 m=msgget(KEY,0666|IPC_CREAT);
 while(1)
 {
 msgrcv(m,&p,sizeof(p),1,0);
 printf("Filename from Client: %s\n",p.a);
 fd=open(p.a,O_RDONLY);
 n=read(fd,p.a,1024);
 p.type=p.pid;
 p.pid=getpid();
 msgsnd(m,&p,sizeof(p),0);
 
 }
}