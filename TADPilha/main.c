#include <stdio.h>
#include <stdlib.h>
#include "pilha.h"
#include "vetor.h"

int main(void) {
    printf("teste");
    Pilha *p=pilha_cria();
    printf("teste1");
    Vetor *v1=vet_cria(1.0,1.0);
    printf("teste2");
    Vetor *v2=vet_cria(2.0,2.0);
    printf("teste4");
    Vetor *v3=vet_cria(3.0,3.0);
    printf("teste5");
    pilha_push(p,v3);
    printf("teste6");
    pilha_push(p,v2);
    printf("teste7");
    pilha_push(p,v1);
    printf("teste8");
    while(!pilha_vazia(p)) {
        printf("teste");
        Vetor *aux=(Vetor *) pilha_pop(p);
        char vet[20];
        puts(vet_format(aux,vet));
    }
    pilha_libera(p);
    return 0;
}