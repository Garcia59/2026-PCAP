/*
 * Disciplina: 2026-PCAP
 * Probelma  : beecrowd 1132 - Array Replacement I
 * Autor     : Matheus Felipe Garcia
 * LIAC      : Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma
               dos numeros que nao sao multiplos de 13 entre X e Y, incluindo ambos.
 */
#include <stdio.h>

int main() {
    int X, Y, i, soma = 0;

    scanf("%d", &X);
    scanf("%d", &Y);

    if (X > Y) {
        int temp = X;
        X = Y;
        Y = temp;
    }

    for (i = X; i <= Y; i++) {
        if (i % 13 != 0) {
            soma += i;
        }
    }

    printf("%d\n", soma);

    return 0;
}