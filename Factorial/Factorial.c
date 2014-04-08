#include <stdio.h>
int getFactorial(int i);
int main(int argc, char *argv[]) {
    if(argc == 2) 
        printf("%i\n", getFactorial(atoi(argv[1])));
    else
        printf("Invalid arguments");
    return 0;
}
int getFactorial(int i) {
    if(i < 1) 
        return 1;
    else
        return i *= getFactorial(i - 1);
}
