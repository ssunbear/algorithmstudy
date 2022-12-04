#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	int t, n;
	char* p = NULL, arr[21] = {'\0'};
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%d %s", &n, arr);
		p = (char*)malloc((n * strlen(arr) + 1) * sizeof(char));
		if (p == NULL) return -1;
		int cnt = 0;
		for (int i = 0; i < strlen(arr); i++) {
			for (int j = 0; j < n; j++) {
				p[cnt++] = arr[i];
			}
		}
		p[n * strlen(arr)] = '\0';
		printf("%s\n", p);
		free(p);
	}
}