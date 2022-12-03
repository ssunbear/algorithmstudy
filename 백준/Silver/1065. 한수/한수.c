#include <stdio.h>
int checkhansu(int n);

int main() {
	int n, cnt1=0;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		if (checkhansu(i) == 1) {
			cnt1+=1;
		}
	}
	printf("%d", cnt1);
}
int checkhansu(int n){
	if (n < 100){
		return 1;
	}
	else {
		int cnt = 0, p[1000] = {0}, tmp;
		while (n > 0) {
			p[cnt++] = n % 10;
			n /= 10;
		}
		int d = p[cnt - 1] - p[cnt - 2];
		for (int i = cnt - 2; i >= 1; i--) {
			if (d != (p[i] - p[i - 1])) return 0;
		}
		return 1;
	}
}