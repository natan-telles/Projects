#include<stdio.h>
#include<string.h>
int pontosturno[4][2], totalpontos[4], desempate1=2;
char times[4][20], classificacao[4][20];
int x,y,turno = 1;
char campeao[20], vicecampeao[20], piortime[20];
main(){	
	printf("DIGITE OS NOMES DOS 4 TIMES PARTICIPANTES: \n");
	for (x=0;x<=3;x++){
		gets(times[x]);
	}
	printf("\n\n");
	
	printf("DIGITE AS PONTUACOES EM CADA TURNO: \n\n");
	for (y=0;y<=1;y++){
		printf("Pontuacao do %d turno: \n",turno);
		for (x=0;x<=3;x++){
			printf("%s : ",times[x]);
			scanf("%d",&pontosturno[x][y]);
			totalpontos[x] = totalpontos[x] + pontosturno[x][y];	
		}
		turno++;
		printf("\n\n");
	}		
	printf("===========================================================");
	printf("\n\n");
	
	printf("PONTUACAO TOTAL DOS TIMES: \n\n");
	for(x=0;x<=3;x++){
		printf("%s : %d \n",times[x],totalpontos[x]);
	}
	printf("\n\n");
	printf("CLASSIFICACAO FINAL DO CAMPEONATO: \n\n");
	
	//classificação
	for (x = 0; x < 3; x++) {
        for (y = x + 1; y < 4; y++) {
            if (totalpontos[y] > totalpontos[x]) {
                int temp_pontos = totalpontos[x];
                char temp_time[20];
                strcpy(temp_time, times[x]);

                totalpontos[x] = totalpontos[y];
                strcpy(times[x], times[y]);

                totalpontos[y] = temp_pontos;
                strcpy(times[y], temp_time);
            }
        
            //desempate pelo segundo turno     
			    
            //se o total entre dois times for igual
            if(totalpontos[y] == totalpontos[x]){
				//verfica quem pontuou melhor no 2º turno
    			if(pontosturno[y][1] > pontosturno[x][1]){
    				//troca os times de classificação
        			int temp_pontos = totalpontos[x];
        			char temp_time[20];
        			strcpy(temp_time, times[x]);

			        totalpontos[x] = totalpontos[y];
			        strcpy(times[x], times[y]);
			
			        totalpontos[y] = temp_pontos;
			        strcpy(times[y], temp_time);
			        
			        //se mesmo assim for igual, verifica quem pontuou melhor no 1º turno
    			} else if(pontosturno[y][1] == pontosturno[x][1]){
	        		if(pontosturno[y][0] > pontosturno[x][0]){
	        			//se for igual no 2º, porém, maior no 1º, ele realiza a troca também
	        			
			           	int temp_pontos = totalpontos[x];
			            char temp_time[20];
			            strcpy(temp_time, times[x]);
			
			            totalpontos[x] = totalpontos[y];
			            strcpy(times[x], times[y]);
			
			            totalpontos[y] = temp_pontos;
			            strcpy(times[y], temp_time);
	        		}
    			}
			}		
        }
    }
    
    // Preencher a classificação com os times ordenados
    for (x = 0; x < 4; x++) {
        strcpy(classificacao[x], times[x]);
        if(x==0){
        	strcpy(campeao,times[x]);
		}
		if(x==1){
			strcpy(vicecampeao,times[x]);
		}
		if(x==3){
			strcpy(piortime,times[x]);
		}
    }
    
    for (x = 0; x < 4; x++) {
        printf("%s : %d\n", classificacao[x], totalpontos[x]);
    }
	
	printf("\n");
	printf("Campeao: %s [%d pts]\n",campeao,totalpontos[0]);	
	printf("Vice-campeao: %s [%d pts]\n",vicecampeao,totalpontos[1]);
	printf("Pior time: %s [%d pts]\n",piortime,totalpontos[3]);			
}
