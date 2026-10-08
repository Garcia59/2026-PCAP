/*
 * Disciplina: 2026-PCAP
 * Probelma  : beecrowd 1164 - Numero Primo
 * Autor     : Matheus Felipe Garcia
 * LIAC      : Leia N casos de teste. Para cada inteiro X, diga se X e perfeito: 
               um numero e perfeito quando e igual a soma dos seus divisores menores que ele (6 = 1 + 2 + 3).
 */
 #include <stdio.h>

 int eh_perfeito(int n) {
    int i, soma = 0;

    for (i = 1; i < n; i++) {
        if (n % i == 0) {
            soma = soma + i;
        }
    }  
    return soma == n;
}

int main() {
    int casos, k, x;

    scanf("%d", &casos);

    for (k = 0; k < casos; k++) {
        scanf("%d", &x);  
        if (eh_perfeito(x)) {
            printf("%d eh perfeito\n", x);
        } else {
            printf("%d nao eh perfeito\n", x);
        }
    }

    return 0;
}