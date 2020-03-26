#include "lista.h"

struct no {
    void* info;
    struct no* prox;
};
struct lista {
    int tam;
    No* ini;
    No* fin;
    No* corr;
};Lista* lst_cria(void) {
    Lista* new;    if(new == NULL)    new = malloc(sizeof(Lista));    return new;}int lst_vazia(Lista* lis) {
    if (lis == NULL)
        return 1;
    else if (lis->tam != 0)
    {
        return 0;
    }
    return 1;
}

void lst_insIni(Lista* lis, void* elem) {
    No new;
    if(new = NULL)
}