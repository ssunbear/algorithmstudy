#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	int n;
	char* ch = NULL;

	scanf("%d", &n);

	ch = (char*)malloc((n+1) * sizeof(char));
	if (ch == NULL) {
		return -1;
	}
	scanf("%s", ch);
	int res = 0;
	for (int i = 0; i < strlen(ch); i++) {
		res += (ch[i]-'0');
	}
	free(ch);
	printf("%d", res);
}