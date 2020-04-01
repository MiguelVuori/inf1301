#include "pilha.h"
#include "lista.h"
#include "stdlib.h"
#include <stdio.h>

struct pilha {
    Lista* lst;
};

Pilha* pilha_cria(void)
{
    Pilha* new;
    new = malloc(sizeof(Pilha));
    Lista *lista = lst_cria();

    if(new == NULL){
        printf("\n Não foi possível alocar espaço na memória! \n");
        exit(1);
    }

    new->lst = lista;

    return new;
}

int pilha_vazia(Pilha* p)
{
    if (p == NULL || lst_vazia(p->lst))
        return 1;
    else
        return 0;
}

void pilha_push(Pilha* p, void* v)
{
    if(p != NULL)
        lst_insIni( p->lst , v );
    else
    {
        printf("Nada inserido pois endereço da pilha está errado!");
    }
    
}

void *pilha_pop(Pilha* p)
{
    if (p != NULL || !lst_vazia(p->lst))
    {
        lst_retIni(p->lst);
    }
    return NULL;    
}

void pilha_libera(Pilha *p)
{
    if (p != NULL)
    {
        lst_libera(p->lst);
        free(p);
    }

}