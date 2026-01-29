#include <iostream>

using namespace std;

using calculator = int(*)(int, int);

int add(int a, int b){return a + b;}
int substract(int a, int b){return a - b;}
int miltiply(int a, int b){return a * b;}
int divide(int a, int b) {
    if (b==0) {cout << "Нельзя делить на 0!" << endl;}
    return a / b;
}

void calculator_app(calculator func){
    int a;
    int b;
    cout << "Введите значение a: ";
    cin >> a;
    cout << "Введите значение b: ";
    cin >> b;

    int choice;
    cout << "1. +\n2. -\n3. *\n4. /\nВыберите операцию: ";
    cin >> choice;

    switch (choice)
    {
    case 1:
        func = add;
        cout << "Результат: " << func(a, b);
        break;

    case 2:
        func = substract;
        cout << "Результат: " << func(a, b);
        break;
        
    case 3:
        func = miltiply;
        cout << "Результат: " << func(a, b);
        break;

    case 4:
        func = divide;
        cout << "Результат: " << func(a, b);
        break;

    default:
        cout << "Ошибка!";
        break;
    }
}

int main(){
    calculator_app(nullptr);
}