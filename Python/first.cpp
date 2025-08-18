
#include <iostream>
using namespace std;

// Function example: square
int square(int n) {
    return n * n;
}

int main() {
    //  Print with space (like Python end=" ")
    cout << "Hello" << " ";
    cout << "C++ World!" << endl;

    //  Variables
    int x = 10;
    string name = "Kush";
    double pi = 3.1415;
    cout << "My name is " << name << ", x=" << x << ", pi=" << pi << endl;

    //  Loops
    cout << "Numbers from 1 to 5: ";
    for (int i = 1; i <= 5; i++) {
        cout << i << " ";
    }
    cout << endl;

    //  Function usage
    cout << "Square of 7 is: " << square(7) << endl;

    // Day 1 Challenge: print numbers 1 to 10
    cout << "Numbers 1 to 10: ";
    for (int i = 1; i <= 10; i++) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
