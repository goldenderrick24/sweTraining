#include <iostream>

using namespace std;

enum class Goldens {
    derrick = 1, alyssa, joel, babyG25,
};

ostream& operator<<(ostream& os, Goldens g){
    switch(g){
        case Goldens::derrick: os << "Derrick"; break;
        case Goldens::alyssa: os <<"Alyssa"; break;
};};



int main()
{

    Goldens g1 = Goldens::derrick;
    cout<<g1<<endl;
    return 0;
    
};