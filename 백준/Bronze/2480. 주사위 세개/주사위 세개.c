#include <stdio.h>

int main() {
	int a, b, c, price=0;
	scanf("%d %d %d", &a, &b, &c);

	if (a == b && b == c) price = 1000 * a + 10000;

	else if (a == b) price = 100 * b + 1000;
	else if (a == c) price = 100 * c + 1000;
	else if (b == c) price = 100 * b + 1000;

	else {
		int max = 0;
		max = a > b ? (b > c ? a : ((a > c) ? a : c)) : (a > c ? b : ((b > c) ? b : c));
		price = 100 * max;
	}
	printf("%d", price);
}
