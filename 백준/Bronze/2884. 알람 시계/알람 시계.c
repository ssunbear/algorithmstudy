#include <stdio.h>
#include <stdlib.h>

int main() {
	int h,m, total;
	scanf("%d %d", &h, &m);
	if (h == 0) h = 24;
	total = h * 60 + m -45;
	h =total / 60;
	if (h == 24) h = 0;
	m = total % 60;
	printf("%d %d", h, m);
	return 0;
}
