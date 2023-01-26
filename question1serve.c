#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
int main(){
int sockfd, newsockfd, portno = 8080;
struct sockaddr_in serv_addr, cli_addr;
socklen_t clilen;
int u;

sockfd = socket(AF_INET, SOCK_STREAM, 0);

memset((char*) &serv_addr, 0, sizeof(serv_addr));

serv_addr.sin_family = AF_INET;
serv_addr.sin_addr.s_addr = INADDR_ANY;
serv_addr.sin_port = htons(8080);

bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr));

listen(sockfd, 5);
clilen = sizeof(cli_addr);
for (int i; i < 20; i++) {

newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, 
&clilen);

int rand_num =rand() %900 + 100;

u = write(newsockfd, &rand_num, sizeof(rand_num));
}

close(newsockfd);
4
close(sockfd);
return 0;
}
