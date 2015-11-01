#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#define MAXLINE 20

int main()
{
    int fd[2],n;
    char c;
    pid_t childpid;

    if (pipe(fd) == -1) {
       perror("pipe");
       exit(EXIT_FAILURE);
    }

    childpid = fork();

    if (childpid == -1) {
       perror("fork");
       exit(EXIT_FAILURE);
    }

    if (childpid==0)
    {
        if ( (n=read(fd[0],&c,1))!=1)
            perror("child: read returned");
        else
            printf("child read %c\n",c);
        write(fd[1],"c",1);
        exit(0);
    }

    write(fd[1],"p",1);
    if ( (n=read(fd[0],&c,1))!=1)
        perror("parent: read returned");
    else
        printf("parent read %c\n",c);
    exit(0);

       
}