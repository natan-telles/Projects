#include<omp.h>
#include<stdio.h>
int a = 0;
int x, ndig, ant, atu, prox;


main(){
	omp_set_num_threads(12);
	
	printf("Digite um numero: \n");
	scanf("%d", &ndig);
	
	ant = 0;
	atu = 1;
	prox = ant+atu;
	
	while(atu <= ndig){
		a++;
		ant = atu;
		atu = prox;
		prox = ant+atu;
	}		
	
	ant = 0;
	atu = 1;
	prox = ant + atu;
	
	#pragma omp parallel for
	for(x=1; x<=a; x++){
		#pragma omp critical
		printf("Atual: %d\n", atu);
		ant = atu;
		atu = prox;
		prox = ant + atu;
		
	}
}

	
