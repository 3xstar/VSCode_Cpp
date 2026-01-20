#include <iostream>
#include <vector>

using std::cout; // 1
using namespace std; // 2

int add(int a, int b)
{return a + b;};

int main(){
    setlocale(LC_ALL, " ");

    // typedef

    // Синтаксис: typedef какой_тип_переименовываем название_нового_типа

    typedef int Scope;
    Scope x = 5;
    cout << "Значение x: " << x << "\n";

    typedef int* intPointer;
    intPointer p = &x;
    cout << "Получаем значение x через указатель p: " << *p << "\n";


    // using

    // Синтаксис: using новое_имя = существующий_тип_данных
    using number = int;
    number a = 12;

    cout << "Получаем значение a: " << a;

    // Страшно вырубай: std::vector<std::pair<std::string, int>>
    // Переписываем

    using Group = pair<string, int>; // Создаем группу
    using Groups = vector<Group>;

    Groups list_groups = {
        {"РПО", 1},
        {"КГиД", 2}
    };

    // Работа с функциями

    //typedef int (*Operation)(int, int); // Typedef
    using Operation = int(*)(int, int); // Using

    Operation op = add;
    op(12, 3);
}   