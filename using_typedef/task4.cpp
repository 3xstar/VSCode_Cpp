#include <iostream>
#include <vector>

using namespace std;

template<typename T>

using Vec = std::vector<T>;

int main(){
    Vec<int> numbers{1,2,3,4,5};
    Vec<std::string> words{"sasha", "kevin", "zahar"};

    cout << "Номера из вектора: ";
    for(int n : numbers){
        cout << n;
    }

    cout << endl;

    cout << "Слова из вектора: " << endl;
    for(string w : words){
        cout << w << endl;
    }
}