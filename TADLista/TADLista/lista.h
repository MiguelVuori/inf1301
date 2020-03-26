#pragma once
typedef struct no No;
typedef struct lista Lista;

/* cria o header de uma lista(lista vazia) e retorna o endereço da lista criada(endereço do header).*/
Lista* lst_cria(void);
                  
/*– retorna 1 se a lista estiver vazia ou 0, caso contrário.*/
int lst_vazia(Lista* lis);

/*– insere um elemento(void*) no início da lista(Lista*).*/
void lst_insIni(Lista* lis, void* elem);

 /*– insere um elemento(void*) no final da lista(Lista*).*/
void lst_insFin(Lista* lis, void* elem);

/*– retira o primeiro elemento da lista(Lista*) e retorna o seu endereço.
Caso a lista esteja vazia a função deve retornar NULL.Obviamente, esta função deve manter o
encadeamento da lista recebida como parâmetro.*/
void* lst_retIni(Lista* lis);

/*– retira o último elemento da lista(Lista*) e retorna o seu endereço.
Caso a lista esteja vazia a função deve retornar NULL.Obviamente, esta função deve manter o
encadeamento da lista recebida como parâmetro.*/
void* lst_retFin(Lista* lis);

/*– esta função será usada para percorrer sequencialmente uma lista.
Quando ela for executada o primeiro elemento da lista passará a ser o elemento corrente
(campo corr).Caso a lista esteja vazia, o campo corr irá conter o valor NULL após a execução
desta função.*/
void lst_posIni(Lista* lis);

/*– esta função será usada para percorrer sequencialmente uma lista.Ela
retorna o endereço do elemento armazenado no nó corrente(campo corr) e faz com que o
campo corr referencie o próximo nó da lista.Caso a campo corr contenha o valor NULL esta
operação deverá retornar o valor NULL*/
void* lst_prox(Lista* lis);