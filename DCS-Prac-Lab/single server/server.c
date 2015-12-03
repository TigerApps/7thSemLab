#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>  //for perror
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <sys/wait.h>
#include <signal.h>

#define PORT "3490"  // the port users will be connecting to

#define BACKLOG 10	 // how many pending connections queue will hold


// get sockaddr, IPv4 or IPv6:
void *get_in_addr(struct sockaddr *sa)
{
	if (sa->sa_family == AF_INET) {
		return &(((struct sockaddr_in*)sa)->sin_addr);
	}

	return &(((struct sockaddr_in6*)sa)->sin6_addr);
}

int main(void)
{
	int sockfd, new_fd;  // listen on sock_fd, new connection on new_fd
	struct addrinfo hints, *servinfo, *p; //servinfo will point to hints
	struct sockaddr_storage their_addr; // connector's address information
	socklen_t sin_size;
	int yes=1;
	char buf[100];
	char s[INET6_ADDRSTRLEN];   //#define in netinet/in.h Value is 46.INET_ADDRSTRLEN 16
	int rv;

	memset(&hints, 0, sizeof hints);
	hints.ai_family = AF_UNSPEC;    //IP can be either IPv4 or IPv6
	hints.ai_socktype = SOCK_STREAM;    // Stream socket
	hints.ai_flags = AI_PASSIVE; // use my IP.attach IP of host to structure

	if ((rv = getaddrinfo(NULL, PORT, &hints, &servinfo)) != 0) //servinfo stores info of all IP associate with host
	{
		fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(rv));
		return 1;
	}

	// loop through all the results and bind to the first we can
	for(p = servinfo; p != NULL; p = p->ai_next)
    {
		if ((sockfd = socket(p->ai_family, p->ai_socktype,p->ai_protocol)) == -1) //Socket Connection is being established
		{
			perror("server: socket");
			continue;
	    }   

		if (bind(sockfd, p->ai_addr, p->ai_addrlen) == -1)  //binding to the host
		{
			close(sockfd);
			perror("server: bind");
			continue;
		}

		break;
	}

	if (p == NULL) 
	{
		fprintf(stderr, "server: failed to bind\n");
		return 2;
	} 

	freeaddrinfo(servinfo); // all done with this structure

	if (listen(sockfd, BACKLOG) == -1)
    {
		perror("listen");
		exit(1);
	}


	printf("server: waiting for connections...\n");
    int num;
	while(1)
    {  // main accept() loop
		sin_size = sizeof their_addr;
		new_fd = accept(sockfd, (struct sockaddr *)&their_addr, &sin_size);
		if (new_fd == -1)
	    {
			perror("accept");
			continue;
	    }

		inet_ntop(their_addr.ss_family,get_in_addr((struct sockaddr *)&their_addr),s, sizeof s);
		char Msg[100];
		printf("server: got connection from %s\n", s);
        while(1)
        {
        
            num = recv(new_fd,buf,sizeof(buf),0);
            buf[num] = '\0';
            if(strcmp(buf,"close") == 0)
            {
                printf("Connection closed\n");
                return 0;
            }
            else
                printf("Message received from client : %s\n",buf);
            
            printf("Enter Message to be send: ");
            gets(Msg);
            send(new_fd, Msg, sizeof(Msg), 0);    
            
        }
      close(new_fd);  // parent doesn't need this
	}

	return 0;
}

