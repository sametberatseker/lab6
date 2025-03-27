
#include <iostream>
using namespace std;

double overone(double numberToCalculate) {
    if (numberToCalculate == 0) {
        return 0;
    } else {
        return 1/numberToCalculate + overone(numberToCalculate - 1);
    }
}

int main() {

    cout << "the sum from 1 to " << 2 << " is " << overone(2) << endl;

    double numero;

    cout << "enter a number to calculate sum recursively: ";
    cin >> numero;
    cout << "the sum from 1 to " << numero << " is " << overone(numero) << endl;

    return 0;




}




