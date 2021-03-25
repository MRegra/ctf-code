#include <stdio.h>
#include <stdlib.h>


long get_random(){
	return rand() % 100;
}

int main(){
	int i = 0;
	while(i < 10){
		printf("%d\n",get_random()+1);
		i++;
	}
	return 0;
}
