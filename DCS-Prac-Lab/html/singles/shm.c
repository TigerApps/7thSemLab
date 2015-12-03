/*
 * shared-mem.c  - demonstrates basic usage of shared memory.
 */

#include <stdio.h>	 /* standard I/O routines.               */
#include <sys/types.h>   /* various type definitions.            */
#include <sys/ipc.h>     /* general SysV IPC structures          */
#include <sys/shm.h>	 /* shared memory functions and structs. */

/* define a structure to be used in the given shared memory segment. */
struct country {
    char name[30];
    char capital_city[30];
    char currency[30];
    int population;
};

int main(int argc, char* argv[])
{
    int shm_id;	      	      /* ID of the shared memory segment.   */
    char* shm_addr; 	      /* address of shared memory segment.  */
    int* countries_num;       /* number of countries in shared mem. */
    struct country* countries; /* countries array in shared mem.    */
    struct shmid_ds shm_desc;
    int i;		      /* counter for loop operation.       */

    /* allocate a shared memory segment with size of 2048 bytes. */
    shm_id = shmget(100, 2048, IPC_CREAT | IPC_EXCL | 0600);
    if (shm_id == -1) {
        perror("main: shmget: ");
        exit(1);
    }

    /* attach the shared memory segment to our process's address space. */
    shm_addr = shmat(shm_id, NULL, 0);
    if (!shm_addr) { /* operation failed. */
        perror("main: shmat: ");
        exit(1);
    }

    /* create a countries index on the shared memory segment. */
    countries_num = (int*) shm_addr;
    *countries_num = 0;
    countries = (struct country*) ((void*)shm_addr+sizeof(int));

    strcpy(countries[0].capital_city, "U.S.A");
    strcpy(countries[0].capital_city, "Washington");
    strcpy(countries[0].currency, "U.S. Dollar");
    countries[0].population = 250000000;
    (*countries_num)++;

    strcpy(countries[1].capital_city, "Israel");
    strcpy(countries[1].capital_city, "Jerusalem");
    strcpy(countries[1].currency, "New Israeli Shekel");
    countries[1].population = 6000000;
    (*countries_num)++;

    strcpy(countries[1].capital_city, "France");
    strcpy(countries[1].capital_city, "Paris");
    strcpy(countries[1].currency, "Frank");
    countries[1].population = 60000000;
    (*countries_num)++;

    /* now, print out the countries data. */
    for (i=0; i < (*countries_num); i++) {
        printf("Countery %d:\n", i+1);
        printf("  name: %s:\n", countries[i].name);
        printf("  capital city: %s:\n", countries[i].capital_city);
        printf("  currency: %s:\n", countries[i].currency);
        printf("  population: %d:\n", countries[i].population);
    }

    /* detach the shared memory segment from our process's address space. */
    if (shmdt(shm_addr) == -1) {
        perror("main: shmdt: ");
    }

    /* de-allocate the shared memory segment. */
    if (shmctl(shm_id, IPC_RMID, &shm_desc) == -1) {
        perror("main: shmctl: ");
    }

    return 0;
}

