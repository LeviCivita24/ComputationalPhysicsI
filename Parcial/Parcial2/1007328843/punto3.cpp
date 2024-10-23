#include <iostream>
//#include <cstdlib> 
#include <ctime>

using namespace std; 

void adivinaNumero(){
    int k; int i; int p; 
    srand(time(0)); 
    p = 1 + rand() % 1001;
    cout << "Ingrese el primer numero: " << endl; 
    cin >> i; 
    if (p==i){
        cout << "Adivinaste el numero a la primera. Felicitaciones" <<endl; 
    }

    if (p!=i){
        cout << "Debes ingresar otro numero: " << endl; 
    }

    while (p!=i){
        cin >> k; 
        if (p > k){
            cout << "Ingrese un numero mayor" << endl;
        }
        if (p < k){
            cout << "Ingrese un numero menor" << endl; 
        }
        if (p == k){
            cout << "Adivinaste el numero" << endl;
        }
        i=k; 
    } 

}

int main()
{
    char opcion; 
    cout << "Para jugar presione S, para no seguir N" << endl;
    cin >> opcion; 
    while (opcion == 'S'){ 
        adivinaNumero();
        cout << "Para jugar presione S, para no seguir N" << endl;
        cin >> opcion; 
    }
    if (opcion == 'N'){
        cout << "Gracias por participar" << endl; 
    } 
    return 0; 
}
