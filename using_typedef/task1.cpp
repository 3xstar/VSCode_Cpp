#include <iostream>

using namespace std;

typedef unsigned int id;
typedef int Score;
typedef std::string Name;

struct Player{
    id player_id;
    Score player_score;
    Name player_name;
};

int main(){
    Player Sanya{69, 3000, "Саша"};
    Player Borya{67, 5000, "Боря"};
    Player Zahar{25, 10000, "Захар"};

    cout << "Игроки:"<< endl;
    cout << Sanya.player_name << " | " << Borya.player_name << " | " << Zahar.player_name;
}