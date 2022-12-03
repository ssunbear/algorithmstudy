#include <stdio.h>
#include <stdlib.h>

int main() {
	int h,m, total, time;
	scanf("%d %d", &h, &m);
	scanf("%d", &time);
	if (h == 0) h = 24;
	total = h * 60 + m +time;
	h =total / 60;
	if (h >= 24) h = h%24;
	m = total % 60;
	printf("%d %d", h, m);
	return 0;
}