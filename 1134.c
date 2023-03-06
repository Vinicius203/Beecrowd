#include <stdio.h>
#include <stdlib.h>

int main()
{
    int tipo_combustivel;
    int alcool = 0, gasolina = 0, diesel = 0;

    do
    {
        scanf("%d", &tipo_combustivel);
        switch (tipo_combustivel)
        {
        case (1):
            alcool++;
            break;
        case (2):
            gasolina++;
            break;
        case (3):
            diesel++;
            break;
        case (4):
            break;
        default:
            continue;
        }

    } while (tipo_combustivel != 4);

    printf("MUITO OBRIGADO\n");
    printf("Alcool: %d\nGasolina: %d\nDiesel: %d\n", alcool, gasolina, diesel);

    return 0;
}