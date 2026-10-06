/*
 * Disciplina: 2026-PCAP
 * Probelma  : beecrowd 1178 - Array Fill lll
 * Autor     : Matheus Felipe Garcia
 * LIAC      : Leia um valor real e guarde em N[0]. Preencha as posições de 1 a 99 com a metade da posição anterior. 
 *             mostre as cem posições com quatro casas decimais.
 */
#include <stdio.h>

int main() {
    double n[100];
    int i;

    scanf("%lf", &n[0]);

    for (i = 1; i < 100; i++) {
        n[i] = n[i - 1] / 2;
    }

    for (i = 0; i < 100; i++) {
        printf("N[%d] = %.4f\n", i, n[i]);
    }

    return 0;
}