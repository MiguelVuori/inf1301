
typedef struct pilha Pilha;


/* cria o header de uma pilha e uma lista vazia, que deve ser apontada
pelo campo lst da struct pilha. */

Pilha* pilha_cria(void);

/* retorna 1 se a pilha estiver vazia ou 0, caso contrário. */ 

int pilha_vazia(Pilha* p);

/* insere (empilha) um elemento (void *) na pilha (Pilha *). */

void pilha_push(Pilha* p, void* v);

/* retira (desempilha) o primeiro elemento da pilha (Pilha *) e
retorna o seu endereço. Caso a pilha esteja vazia a função deve retornar NULL. */

void *pilha_pop(Pilha* p);

/* esta função libera todos os elementos da lista e, em
seguida, liberar o header da pilha. */

void pilha_libera(Pilha *p);

