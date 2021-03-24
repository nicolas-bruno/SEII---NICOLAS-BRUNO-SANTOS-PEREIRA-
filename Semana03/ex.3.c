#include <stdio.h>

void hanoi(int n,char origem,char destino,char auxiliar){
	if(n==1){ 
		printf("\nmova o disco 1 da base %c para a base %c",origem ,destino);
		return;
	}
	hanoi(n-1,origem,auxiliar,destino);
	printf("\nmova o disco %d da base %c para a base %c",n,origem,destino);
	hanoi(n-1,auxiliar,destino,origem);
}

main(){
	int n;
	printf("digite o numero de discos : ");
	scanf("%d",&n);
	hanoi(n,'A','C','B');
	printf("\n");
	return 0;
}