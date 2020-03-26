#include "lista.h"

static No * CriarElemento( Lista * pLista , void * pValor  ) ;

static void LimparCabeca( Lista * pLista ) ;

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
    if(new == NULL)
    new = malloc(sizeof(Lista));
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

void lst_insIni(Lista* lis, void* elem) {
    No new;
    if(new = NULL)
}

void lst_insIni( Lista * pLista , void * pValor )
{

    No * pElem;

    pElem = CriarElemento( pLista , pValor ) ;
    if ( pElem == NULL )
    {
        exit(0);
    } 

    if ( pLista->ini == NULL )
    {
        pLista->ini = pElem ;
        pLista->fin = pElem ;
    } 
    else
    {
        pElem->prox = pLista->ini;
        pLista->ini = pElem;

        } 

}

void lst_insFin( Lista * pLista , void * pValor )
    
{

    No * pElem ;

    pElem = CriarElemento( pLista , pValor ) ;
    if ( pElem == NULL )
    {
        printf("\n Faltou memoria \n");
        exit(0);
    }

    if ( pLista->fin == NULL )
    {
        pLista->ini = pElem ;
        pLista->fin = pElem ;
    } 
    else
    {
        pLista->fin->prox = pElem;
        pLista->fin = pElem;

    }

} 

void* lst_retIni( Lista * pLista )
    
{

    No * pElem ;
    void * elem ;

    if(pLista == NULL)
    {
        printf("\n Lista vazia \n");
        return NULL;
    }

    if ( pLista->ini == NULL )
    {
        printf("\n Nao ha elemento no inicio da lista \n") ;
        return NULL;
    } 
    else
    {
        pElem = pLista->ini;
        pLista->ini = pLista->ini->prox;
        pLista->fin->prox = pElem;
        elem = pElem->info;
        free(pElem);
        (pLista->tam)--;

        return elem;

    } 
}

/*****  Código das funções encapsuladas no módulo  *****/

No * CriarElemento( Lista * pLista , void * pValor  )
{

    No * pElem ;

    pElem = ( No * ) malloc( sizeof( No )) ;
    if ( pElem == NULL )
    {
        return NULL ;
    } /* if */

    pElem->info = pValor ;
    pElem->prox  = NULL  ;

    pLista->tam ++ ;

    return pElem ;

}

void LimparCabeca( Lista * pLista )
{

    pLista->ini = NULL ;
    pLista->fin = NULL ;
    pLista->corr = NULL ;
    pLista->tam   = 0 ;

}