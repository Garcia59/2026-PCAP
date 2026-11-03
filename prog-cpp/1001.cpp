/*
*Disciplina: 2026-PCAP
* Problema : beecrowd 1001 - Extremamente Basico
* Autor    : Matheus Felipe Garcia
* LIAC     : Le dois inteiros A eB, um por linha. imprime a soma no
*            formato "X = soma", com espacos em volta so sinal de igual.
*/
#include <iostream>
using namespace std;

int main() {
    int a, b;

    std::cin >> a >> b;
    std::cout << "X = "<< a + b << endl;

    return 0;
}