#include <iostream>

using namespace std;

int unusedFunction(int x){
    int unused_var = 12; // Неуспользуемая переменная
    return x;
}

int main(){
    int a; // Неициализирована
    int b = 10;

    if(a > b){
        cout << "Балдеж";
    }

    unsigned int un_int = 10;
    int i = -1;

    // Сравнение int и unsigned int
    if(i < un_int){
        cout << "Положительна против отрицательной";
    }

    double d = 3.12;
    int truncated = d; // Конвертация

    if(true)
    cout << "Привет";
    cout << "Всегда печатается"; // Вне условия

    int arr[3];
    cout << arr[5] << endl;
}