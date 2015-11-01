//Pipe
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#define MAXLINE 20

void client(int,int);
void server(int,int);


int main()
{
    int pipe1[2],pipe2[2];
    pid_t childpid;

    childpid = fork();
    if (childpid == 0)
    {
        close(pipe1[1]);
        close(pipe2[0]);
        server(pipe1[0],pipe2[1]);
        exit(0);
    }
    else if (childpid == -1)
    {
        printf("couldnt fork\n");
    }
    close(pipe1[0]);
    close(pipe2[1]);
    client(pipe2[0],pipe1[1]);
    exit(0);

}

void client(int readfd, int writefd)
{
    size_t len;
    ssize_t n;
    char buff[MAXLINE];

    printf("enter file name:\n");
    fgets(buff,MAXLINE,stdin);
    len = strlen(buff);
    if (buff[len-1]=='\n')
        len--;
    write(writefd,buff,len);

    printf("\nhere\n");

    int fd;
    fd=open("new.txt","w");
    printf("\nfdc:%d",fd);
    while ((n=read(readfd,buff,MAXLINE))>0)
    {
        printf("\nyo\n");
        write(fd,buff,n);
    }
    close(fd);
    printf("\nend client\n");
}

void server(int readfd, int writefd)
{
    int fd;
    ssize_t n;
    char buff[MAXLINE+1];

    if ((n=read(readfd,buff,MAXLINE))==0)
    {
        printf("eof");
        exit(1);
    }
    buff[n]='\0';

    fd=open(buff,"r");
    printf("\nfds:%d",fd);
    
    if ( fd<0)
    {
        printf("\nbo\n");
        snprintf(buff+n,sizeof(buff)-n,":cant open  \n");
        n = strlen(buff);
        write(writefd,buff,n);
        printf("\nbo2\n");
        
    }
    else
    {
       printf("\nbo3\n");
        while( (n=read(fd,buff,MAXLINE))>0 )
       {
            printf("\nboga\n");
            write(writefd,buff,n);
        }
        close(fd); 
    }
    printf("\nend server\n");
}
