#include "pilha.h"
#include "lista.h"

struct pilha {
    Lista* lst;
};

Pilha* pilha_cria(void)
{
    Pilha* new;
    new = malloc(sizeof(Pilha));
    Lista lista = lst_cria();

    if(new == NULL){
        printf("\n Não foi possível alocar espaço na memória! \n");
        exit(1);
    }

    new->lst = lista;

    return new;
}

int pilha_vazia(Pilha* p);
{
    if (p == NULL || lst_vazia(p->lst))
        return 1;
    else
        return 0;
}

void pilha_push(Pilha* p, void* v)
{
    if(p != NULL)
        lst_insIni( p->lis , v );
    
}

void *pilha_pop(Pilha* p)
{

}

void pilha_libera(Pilha *p)
{
    if (p != NULL)
    {
        lst_libera(p->lis);
        free(p);
    }

}