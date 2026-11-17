#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    int n;
    string codigo;
    vector<string> livros;

    while (cin >> n) {
        livros.clear();

        for (int i = 0; i < n; i++) {
            cin >> codigo;
            livros.push_back(codigo);
        }

        sort(livros.begin(), livros.end());

        for (int i = 0; i < n; i++) {
            cout << livros[i] << endl;
        }
    }

    return 0;
}