#include <rpc/rpc.h>
#include "math.h"
 
          main(argc, argv)
          int argc;
          char *argv[];
          {
               CLIENT *cl;
               intpair pair;
               int *result;
 
               if (argc != 4) {
                    fprintf(stderr, "usage: prog server num1 num2\n");
                    exit(1);
               }
 
               cl = clnt_create(argv[1], MATHPROG, MATHVERS, "udp");
               if (cl == NULL) {
                    clnt_pcreateerror(argv[1]);
                    exit(1);
               }
               pair.a = atoi(argv[2]);
               pair.b = atoi(argv[3]);
 
               result = mathproc_add_1(&pair, cl);
               if (result == NULL) {
                    clnt_perror(cl, "add");
                    exit(1);
               }
               printf("the addition returned %d\n", *result);
 
               result = mathproc_mult_1(&pair, cl);
               if (result == NULL) {
                    clnt_perror(cl, "mult");
                    exit(1);
               }
               printf("the multiplication returned %d\n", *result);
          }
 
 
