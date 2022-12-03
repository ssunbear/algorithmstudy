#include <stdio.h>
#include <stdlib.h>

int main() {
	int p[10], n, remainder[10], cnt = 0, cnt1 = 1;
	
	for (int i = 0; i < 10; i++) {
		scanf("%d", &n);
		p[i] = n % 42;
	}
	remainder[0] = p[0];
	for (int i = 1; i < 10; i++) {
		for (int j = 0; j < cnt1; j++) {
			if (p[i] == remainder[j]) {
				cnt = 0;
				break;
			}
			else {
				cnt++;
			}
		}
		if (cnt == cnt1) {
			remainder[cnt1++] = p[i];
		}
		cnt = 0;
	}
	printf("%d", cnt1);
	return 0;
}
