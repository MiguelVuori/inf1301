#include "lista.h"
#include <stdio.h>
#include <stdlib.h>

static No * CriarElemento( Lista * lis , void * elem  ) ;

static void LimparCabeca( Lista * lis ) ;

struct no {
    void* info;
    struct no* prox;
};
struct lista {
    int tam;
    No* ini;
    No* fin;
    No* corr;
};

Lista* lst_cria(void) {
    Lista* new;
    new = malloc(sizeof(Lista));
    if(new == NULL){
        printf("\n Não foi possível alocar espaço na memória! \n");
        exit(1);
    }
    return new;
}

int lst_vazia(Lista* lis) {
    if (lis == NULL)
        return 1;
    else if (lis->tam != 0)
    {
        return 0;
    }
    return 1;
}

void lst_insIni( Lista * lis , void * elem )
{

    No * pElem;

    pElem = CriarElemento( lis , elem ) ;
    if ( pElem == NULL )
    {
        printf("\n Não foi possível alocar espaço na memória! \n");
        exit(1);
    } 

    if ( lis->ini == NULL )
    {
        lis->ini = pElem ;
        lis->fin = pElem ;
    } 
    else
    {
        pElem->prox = lis->ini;
        lis->ini = pElem;

    } 

}

void lst_insFin( Lista * lis , void * elem )
    
{

    No * pElem ;

    pElem = CriarElemento( lis , elem ) ;
    if ( pElem == NULL )
    {
        printf("\n Faltou memoria \n");
        exit(0);
    }

    if ( lis->fin == NULL )
    {
        lis->ini = pElem ;
        lis->fin = pElem ;
    } 
    else
    {
        lis->fin->prox = pElem;
        lis->fin = pElem;

    }

} 

void* lst_retIni( Lista * lis )
    
{

    No * pElem ;
    void * elem ;

    if(lis == NULL)
    {
        printf("\n Lista vazia \n");
        return NULL;
    }

    if ( lis->ini == NULL )
    {
        printf("\n Nao ha elemento no inicio da lista \n") ;
        return NULL;
    } 
    else
    {
        pElem = lis->ini;
        lis->ini = lis->ini->prox;
        elem = pElem->info;
        free(pElem);
        (lis->tam)--;

        return elem;

    } 
}

void* lst_retFin (Lista* lis) {
    void *elem;
    if  (lis == NULL) {
        printf("\n Lista vazia \n");
        return NULL;
    }
    if  (lis->fin == NULL) {
        printf("\n Nao ha elemento no fim da lista! \n");
        return NULL;
    }
    elem = lis->fin->info;
    if  (lis->fin == lis->ini) {
        free(lis->fin);
        lis->fin = NULL;
        lis->ini = NULL;
        return elem;
    }
    lis->corr = lis->ini;
    while(lis->corr->prox != lis->fin)
        lis->corr = lis->corr->prox;
    free(lis->fin);
    lis->fin = lis->corr;
    lis->fin->prox = NULL;
    (lis->tam)--;
    return elem;
    
}

void lst_posIni(Lista* lis) {
    if (lis == NULL){
        printf("\n Lista vazia! \n");
    }
    lis->corr = lis->ini;
}

void *lst_prox(Lista* lis){
    void *aux;
    if (lis == NULL){
        printf("\n Lista vazia! \n");
        return NULL;
    }
    if (lis->corr == NULL){
        printf("\n Corrente vazio! \n");
        return NULL;
    }
    aux = lis->corr->info;
    lis->corr = lis->corr->prox;
    return aux;
}

void lst_libera(Lista* lis){
    No *aux;
    if(lis == NULL)
        return;
    if(lis->ini == NULL) {
        LimparCabeca(lis);
        free(lis);
        return;
    }
    lst_posIni(lis);
    while(lis->corr != NULL)
    {
        aux = lis->corr;
        free(lis->corr->info);
        lis->corr = lis->corr->prox;
        free(aux);
    }
    LimparCabeca(lis);
    free(lis);
}

/*****  Código das funções encapsuladas no módulo  *****/

No * CriarElemento( Lista * lis , void * elem  )
{

    No * pElem ;

    pElem = ( No * ) malloc( sizeof( No )) ;
    if ( pElem == NULL )
    {
        return NULL ;
    } /* if */

    pElem->info = elem ;
    pElem->prox  = NULL  ;

    lis->tam ++ ;

    return pElem ;

}

void LimparCabeca( Lista * lis )
{

    lis->ini = NULL ;
    lis->fin = NULL ;
    lis->corr = NULL ;
    lis->tam   = 0 ;

}