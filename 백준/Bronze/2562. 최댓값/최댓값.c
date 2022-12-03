#include <stdio.h>
#include <stdlib.h>

int main() {
	int* p = NULL;

	p = (int*)malloc(10 * sizeof(int));
	if (p == NULL) {
		return 0;
	}

	for (int i = 0; i < 9; i++) {
		scanf("%d", &p[i]);
	}
	int max = p[0], idx=1;
	for (int i = 0; i < 9; i++) {
		if (max < p[i]) {
			idx = i + 1;
			max = p[i];
		}
	}
	free(p);
	printf("%d\n%d", max, idx);
	return 0;
}
