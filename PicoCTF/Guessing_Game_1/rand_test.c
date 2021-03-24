#include <stdio.h>
#include <stdlib.h>


long get_random(){
	return rand() % 100;
}

int main(){
	int i = 0;
	while(i < 100){
		printf("%d\n",get_random());
		i++;
	}
	return 0;
}
