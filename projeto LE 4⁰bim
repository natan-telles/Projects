#include<stdio.h>
#include<string.h>
int cont;
char disciplinas[3];
float mediasbimestrais[3][4],totalpontosano[3],notaexame;

void ler_disciplinas(){
	printf("Digite as 3 materias tecnicas: \n");
	for(cont=1;cont<=3;cont++){
		printf("%d.a: ",cont);
		scanf("%s",&disciplinas[cont]);
	}	
}

void ler_medias(char x){
	int c;
	printf("%s :",x);
	for(c=1;c<=4;c++){
		printf("%d bimestre: ",c);
		scanf("%f",&mediasbimestrais[cont][c]);
		/*
		while((mediasbimetrais[cont][c] < 0) || (mediasbimestrais[cont][c]>10)){
			printf("\nDigite notas entre 0 e 10!!!");
			scanf("%f",&mediasbimestrais[cont][c]);	
		}
		*/	
	}
}

float somarpontosano(int x){
	int c;
	for(c=1;c<=4;c++){
		totalpontosano[x] = totalpontosano[x] + mediasbimestrais[cont][c];
	}
	return totalpontosano[x];
}

void examefinal(float &notanecessaria, int cont){
	notanecessaria = 10-(notanecessaria/4);
}

main(){
	ler_disciplinas();
	
	printf("\n");
	printf("Digite as medias bimestrais: \n");
	for(cont=1;cont<=3;cont++){
		printf("\n");
		ler_medias(disciplinas[cont]);
		printf("Total Pontos[%s] : %f",disciplinas[cont],somarpontosano[cont]);
	}
	
	printf("\n");
	for(cont=1;cont<=3;cont++){
		if(totalpontosano[cont] >= 24 ){
			printf("\nAPROVADO em %s",disciplinas[cont]);			
		}
		if(totalpontosano[cont] < 15){
			printf("\nREPROVADO em %s",disciplinas[cont]);
		}
		if(totalpontosano[cont] >= 15){
			printf("\nEXAME FINAL em %s",disciplinas[cont]);
		}
	}
	printf("\n");
	
	for(cont=1;cont<=3;cont++){
		if(totalpontosano[cont] >= 15 && totalpontosano[cont] < 24){
			examefinal(totalpontosano[cont],cont);
			printf("\nnota necessaria: %f",totalpontosano[cont]);
			printf("\nDigite nota de EXAME em %s:",disciplinas[cont]);
			scanf("%f",&notaexame);
			while(notaexame < 0 || notaexame > 10){
				printf("\nDigite notas entre 0 e 10!!!");
				scanf("%f",&notaexame);
			}
			if(notaexame >= totalpontosano[cont]){
				printf("\nRESULTADO APOS EXAME: APROVADO em %s\n",disciplinas[cont]);
			} else {
				printf("\nRESULTADO APOS EXAME: RETIDO em %s\n",disciplinas[cont]);
			}
		}
	}
}
