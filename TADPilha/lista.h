
typedef struct no No;
typedef struct lista Lista;

/* cria o header de uma lista(lista vazia) e retorna o endere�o da lista criada(endere�o do header).*/
Lista* lst_cria(void);
                  
/*� retorna 1 se a lista estiver vazia ou 0, caso contr�rio.*/
int lst_vazia(Lista* lis);

/*� insere um elemento(void*) no in�cio da lista(Lista*).*/
void lst_insIni(Lista* lis, void* elem);

 /*� insere um elemento(void*) no final da lista(Lista*).*/
void lst_insFin(Lista* lis, void* elem);

/*� retira o primeiro elemento da lista(Lista*) e retorna o seu endere�o.
Caso a lista esteja vazia a fun��o deve retornar NULL.Obviamente, esta fun��o deve manter o
encadeamento da lista recebida como par�metro.*/
void* lst_retIni(Lista* lis);

/*� retira o �ltimo elemento da lista(Lista*) e retorna o seu endere�o.
Caso a lista esteja vazia a fun��o deve retornar NULL.Obviamente, esta fun��o deve manter o
encadeamento da lista recebida como par�metro.*/
void* lst_retFin(Lista* lis);

/*� esta fun��o ser� usada para percorrer sequencialmente uma lista.
Quando ela for executada o primeiro elemento da lista passar� a ser o elemento corrente
(campo corr).Caso a lista esteja vazia, o campo corr ir� conter o valor NULL ap�s a execu��o
desta fun��o.*/
void lst_posIni(Lista* lis);

/*� esta fun��o ser� usada para percorrer sequencialmente uma lista.Ela
retorna o endere�o do elemento armazenado no n� corrente(campo corr) e faz com que o
campo corr referencie o pr�ximo n� da lista.Caso a campo corr contenha o valor NULL esta
opera��o dever� retornar o valor NULL*/
void* lst_prox(Lista* lis);

// – esta função deverá percorrer sequencialmente uma lista recebida
// como parâmetro (Lista *) e para cada nó encontrado ela deverá: a) liberar a área de memória
// referente ao elemento apontado pelo nó (info) e b) liberar a área de memória do próprio nó.
// Após todos os nós terem sido liberados, o header da lista deverá ser liberado.
void lst_libera(Lista *);