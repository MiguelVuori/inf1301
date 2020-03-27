#include <stdio.h>
#include <stdlib.h>
#include "lista.h"
void exibeLista(Lista* f) {
	int* aux;
	puts("=== Elementos da Lista ***");
	lst_posIni(f);
	aux = (int*)lst_prox(f);
	while (aux) {
		printf("%d\n", *aux);
		aux = (int*)lst_prox(f);
	}
}
int main(void) {
	Lista* f = lst_cria();
	int* a = (int*)malloc(sizeof(int));
	int* b = (int*)malloc(sizeof(int));
	int* c = (int*)malloc(sizeof(int));
	int* d = (int*)malloc(sizeof(int));
	int* aux;
	*a = 10;
	*b = 20;
	*c = 30;
	*d = 40;
	lst_insFin(f, a);
	lst_insFin(f, b);
	lst_insFin(f, c);
	lst_insFin(f, d);
	exibeLista(f);
	aux = lst_retIni(f);
	printf("*** Elemento Retirado %d ***\n", *aux);
	exibeLista(f);
	free(aux);
	aux = lst_retIni(f);
	printf("*** Elemento Retirado %d ***\n", *aux);
	exibeLista(f);
	free(aux);
	aux = lst_retFin(f);
	printf("*** Elemento Retirado %d ***\n", *aux);
	exibeLista(f);
	free(aux);
	aux = lst_retFin(f);
	printf("*** Elemento Retirado %d ***\n", *aux);
	exibeLista(f);
	exibeLista(f);
	free(aux);
	lst_libera(f);
	free(a);
	free(b);
	free(c);
	free(d);
	return 0;
}