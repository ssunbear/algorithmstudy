#include <stdio.h>

int dN(int n);

int main() {
	int a[10001] = {0}, res = 0;
	for (int i = 0; i < 10001; i++) {
		res = dN(i);
		if (res < 10001) a[res] = 1;
	}
	for (int i = 0; i < 10001; i++) {
		if (a[i] != 1) {
			printf("%d\n", i);
		}
	}
}

int dN(int n) {
	int total = n;
	while (n > 0) {
		total += n % 10;
		n /= 10;
	}
	return total;
}