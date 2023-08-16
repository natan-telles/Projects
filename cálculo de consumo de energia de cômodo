#include <stdio.h>
#include <string.h>
#include <math.h>

char comodo[20];
float largura,comprimento,area, valor_lampada,potencia_n, maodeobra, valort, potencia_l, valorm_q, custototallampadas, custototal;
int lampadas;
bool verificar = true;

int main() {
	potencia_l = 60.0;
//leitura dos cômodos
    printf("Insira o nome do comodo: [QUARTO, SALA DE TV, SALAS, COZINHA, VARANDA, ESCRITORIO, BANHEIRO]\n");
    fgets(comodo, 20, stdin);
    strtok(comodo, "\n");

    if (strcmp(comodo, "QUARTO") == 0 || strcmp(comodo, "SALA DE TV") == 0) {
        valorm_q = 15.0;
    } else 
	if (strcmp(comodo, "SALAS") == 0 || strcmp(comodo, "COZINHA") == 0 || strcmp(comodo, "VARANDA") == 0) {
        valorm_q = 18.0;
    } else 
	if (strcmp(comodo, "ESCRITORIO") == 0 || strcmp(comodo, "BANHEIRO") == 0) {
      	valorm_q = 20.0;
    } else {
        printf("Erro ao identificar o comodo.");
        verificar = false;
    }
//coleta as medidas do cômodo
    if (verificar == true) {
        float largura, comprimento;
        printf("Insira a largura: ");
        scanf("%f", &largura);
        printf("Digite o comprimento: ");
        scanf("%f", & comprimento);
		if((largura >0 ) && (comprimento > 0)) { 			
        area = largura * comprimento;
        potencia_n = (area*valorm_q);
        
        
        printf("Insira o valor da lampada [R$]: ");
        scanf("%f", &valor_lampada);

//calcula a quantidade INTEIRA de lâmpadas necessárias 
        lampadas = (int)ceil(potencia_n / potencia_l);
        custototallampadas = lampadas * valor_lampada;
		maodeobra = lampadas*5;
		custototal = maodeobra + custototallampadas;

//exibição para o usuário
        printf("\n    |Resultados|\n");
        printf("Comodo:                    \t%s\n", comodo);
        printf("Area:                      \t%.2fm2\n", area);
        printf ("Potencia necessaria :           \%.2fW\n", valorm_q);
        printf("Consumo:                   \t%.2fW\n", potencia_n);
        printf("Lampada(s):                \t%d unidades\n", lampadas);
        printf("Custo da(s) lampada(s):    \tR$%.2f\n", custototallampadas );
        printf("Custo de mao de obra:      \tR$%.2f\n", maodeobra);
        printf("Custo total de instalacao:      R$%.2f \n", custototal);
    }else
    	printf("Largura ou comprimento invalidos");
	}
}
