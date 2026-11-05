/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1168 - Twitting
 * Autor     : Matheus Felipe Garcia
 * LIAC      : Considerando a configuração dos leds dos números abaixo, faça um algoritmo que ajude
 *             João a descobrir a quantidade de leds necessário para montar o valor.
*/
#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, total;
    string valor;

    int leds[] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> valor;
        total = 0;

        for (int j = 0; j < valor.size(); j++) {
            total += leds[valor[j] - '0'];
        }

        cout << total << " leds" << endl;
    }

    return 0;
}
