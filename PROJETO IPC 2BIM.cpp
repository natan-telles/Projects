#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

int main()
{
    float n, soma10, soma11, x, y;
    float dpu1, dpu2, dig1, dig2, resto10, resto11;
    int totalcpf = 0, cpfinvalido = 0, cpfvalido = 0, cont;
    float pctcpfinv, pctcpfval;
    char resp[2];

    do
    {
        x = 10;
        y = 11;
        soma10 = soma11 = 0;
        for (cont = 1; cont <= 9; cont++)
        {
            printf("Digite o %d numero do seu CPF: ", cont);
            scanf("%f", &n);
            while(n <0 || n >9){
                printf("Digite algarismo por algarismo\n");
                scanf("%f",&n);
            }
            soma10 += n * x;
            soma11 += n * y;
            x--;
            y--;
        }

        if ((fmod(soma10, 11) < 2))
        {
            dig1 = 0;
        }
        else
        {
            resto10 = fmod(soma10, 11);
            dig1 = 11 - resto10;
            soma11 += dig1 * 2;
            if (fmod(soma11, 11) < 2)
            {
                dig2 = 0;
            }
            else
            {
                resto11 = fmod(soma11, 11);
                dig2 = 11 - resto11;
            }
        }

        printf("Digite o 10 numero do seu CPF: ");
        scanf("%f", &dpu1);
        while(dpu1<0 || dpu1 >9){
            printf("Digite algarismo por algarismo!");
            scanf("%f",&dpu1);
        }
        printf("Digite o 11 numero do seu CPF: ");
        scanf("%f", &dpu2);
        while(dpu2<0 || dpu2 >9){
            printf("Digite algarismo por algarismo!");
            scanf("%f",&dpu2);
        }
        if ((dig1 == dpu1) && (dig2 == dpu2))
        {
            printf("\nSeu CPF e valido");
            cpfvalido++;
        }
        else
        {
            printf("\nSeu CPF e invalido");
            cpfinvalido++;
        }

        totalcpf++;
        printf("\nDeseja continuar testando CPF? [S ou N]: ");
        scanf("%s", resp);
    } while (strcmp(resp, "N") != 0);

    printf("\nTotal de CPF's lidos = %d", totalcpf);
    printf("\nTotal de CPF's invalidos lidos = %d", cpfinvalido);
    pctcpfinv = (float)cpfinvalido / totalcpf * 100;
    printf("\nA porcentagem de CPF's invalidos lidos = %f %%", pctcpfinv);
    printf("\nTotal de CPF's valido lidos = %d", cpfvalido);
    pctcpfval = (float)cpfvalido / totalcpf * 100;
    printf("\nA porcentagem de CPF's valido lidos = %f %%", pctcpfval);

    return 0;
}
