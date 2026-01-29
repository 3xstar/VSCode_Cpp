#include <iostream>
#include <vector>

using namespace std;

using Matrix = std::vector<std::vector<int>>;

int matrix_size(Matrix matrix_test){
    int rows = matrix_test.size();
    int sum = 0;

    for(auto& row : matrix_test){
        for(int element : row){
            sum += element;
        }
    }
    return sum;
};

int main(){
    Matrix matrix = {
        {3, 9, 5},
         {4, 1, 7},
          {2, 6, 8}};
    cout << "Сумма элементов в матрице: " << matrix_size(matrix);
}