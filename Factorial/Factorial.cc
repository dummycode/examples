#include <iostream>

int getFactorial(int i);

int main(int argc, char *argv[]) {
    if (argc == 2) {
        std::cout << getFactorial(atoi(argv[1])) << std::endl;
    } else 
        std::cout << "Invalid arguments" << std::endl;
    }
    return 0;
}

int getFactorial(int i) {
    if (i < 1) {
        return 1;
    } else 
        return i *= getFactorial(i - 1);
    }
}
