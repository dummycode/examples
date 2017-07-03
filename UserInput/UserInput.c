#include <stdio.h>
#include <string.h>

#define MAX 100

int main(int argc, char *argv[]) {
	char input[MAX] = "String";
	printf("Input: ");
	fgets(input, sizeof input, stdin);
	if ((strlen(input) > 0) && (input[strlen(input) -1] == '\n')) {
		input[strlen(input) -1] = 0;
    }
	printf("You entered, \"%s\"\n", input);
	return 0;
}
