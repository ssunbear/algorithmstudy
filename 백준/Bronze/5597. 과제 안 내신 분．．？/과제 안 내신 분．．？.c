#include <stdio.h>
#include <stdlib.h>

int main() {
	int p[30], q[28];
	int arr[2] = { 0,0 }, cnt = 0, cnt1=0;
	for (int i = 0; i < 30; i++) {
		p[i] = i + 1;
	}
	for (int i = 0; i < 28; i++) {
		scanf("%d", &q[i]);
	}
	for (int i = 0; i < 30; i++) {
		for (int j = 0; j < 28; j++) {
			if (p[i] == q[j]) {
				break;
			}
			else {
				cnt++;
			}
		}
		if (cnt == 28) {
			arr[cnt1++] = i + 1;
		}
		cnt = 0;
	}

	printf("%d\n%d", arr[0], arr[1]);
	return 0;
}