       #include <sys/wait.h>
       #include <stdio.h>
       #include <stdlib.h>
       #include <unistd.h>
       #include <string.h>

       int main(int argc, char *argv[])
       {
           int pipefd[2];
           pid_t cpid;
           char buf;

           
           char inp[50];
           printf("Enter input\n");
           scanf("%[^\n]s",inp);
           if (pipe(pipefd) == -1) {
               perror("pipe");
               exit(EXIT_FAILURE);
           }
           
           cpid = fork();
           if (cpid == -1) {
               perror("fork");
               exit(EXIT_FAILURE);
           }

           if (cpid == 0) {    /* Child reads from pipe */
               close(pipefd[1]);   
               printf("That is what the child  process with  id  %d with parent id %d  read \n",getpid(),getppid())  ;     /* Close unused write end */
 int count=0;
 while (read(pipefd[0], &buf, 1) > 0){
                   write(STDOUT_FILENO, &buf, 1);
                   count++;
                 }

               write(STDOUT_FILENO, "\n", 1);
               printf("These many bytes were written %d\n",count);
               close(pipefd[0]);
               _exit(EXIT_SUCCESS);

           } else {    
                   /* Parent writes argv[1] to pipe */
            printf("That is what the Parent  process with  id  %d with parent id %d wrote \n%s\n",getpid(),getppid(),inp) ;
               close(pipefd[0]);          /* Close unused read end */
               write(pipefd[1], inp, strlen(inp));
               close(pipefd[1]);          /* Reader will see EOF */
               wait(NULL);                /* Wait for child */
               exit(EXIT_SUCCESS);
           }
       }
