/*
Problema 1002 BeeCrowd
2026.09.22
Matheus Felipe Garcia
*/

#include <stdio.h>

int main() {
    double raio, area;
    double pi = 3.14159;

    // Leitura do valor de dupla precisão (double)
    scanf("%lf", &raio);

    // Cálculo da área (raio ao quadrado multiplicado por pi)
    area = pi * raio * raio;

    // Impressão do resultado com 4 casas decimais e a quebra de linha (\n)
    printf("A=%.4lf\n", area);

    return 0;
}