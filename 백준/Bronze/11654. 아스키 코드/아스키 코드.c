#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main() {
	char ch;
	ch = fgetc(stdin);
	printf("%d", ch);
}