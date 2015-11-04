#include <stdio.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include  <sys/shm.h>

int main()
    {
    int id,semid,count=0,i=1,j;
    int *ptr;
    id=shmget(8078,sizeof(int),IPC_CREAT|0666);
    ptr=(int *)shmat(id,NULL,0);
    union semun
    {
        int val;
        struct semid_ds *buf;
        ushort *array;
    }u;
    struct sembuf sem;
    semid=semget(1011,1,IPC_CREAT|0666);
    ushort a[1]={1};
    u.array=a;
    semctl(semid,0,SETALL,u);
    while(1)
    {
        sem.sem_num=0;
        sem.sem_op=-1;
        sem.sem_flg=0;
        semop(semid,&sem,1);
        *ptr=*ptr+1;
        printf("process id:%d countis :%d \n",getpid(),*ptr);

        for(j=1;j<=1000000;j++)
        {
         sem.sem_num=0;
         sem.sem_op=+1;
         sem.sem_flg=0;
         semop(semid,&sem,1);
        }
    }
    shmdt(ptr);

    }