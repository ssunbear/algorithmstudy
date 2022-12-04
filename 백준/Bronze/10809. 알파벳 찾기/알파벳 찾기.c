#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	char ch[101];
	int n[26] = {-1};

	scanf("%s", ch);
	for (int i = strlen(ch) - 1; i > 0; i--) {
		n[ch[i] - 'a'] = i;
	}
	for (int i = 0; i < 26; i++) {
		if (n[i] == 0) {
			n[i] = -1;
		}
	}
	n[ch[0] - 'a'] = 0;
	for (int i = 0; i < 26; i++) {
		printf("%d ", n[i]);
	}
}