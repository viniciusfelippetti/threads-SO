#ALUNO: VINICIUS DE ANDRADE FELIPPETTI
#MATRICULA: 20220080383

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

struct condvar {
    pthread_mutex_t mutex;
    pthread_cond_t condition;
};

void condvar_init(struct condvar *c) {
    pthread_mutex_init(&c->mutex, NULL);
    pthread_cond_init(&c->condition, NULL);
}

void condvar_wait(struct condvar *c, struct mutex *m) {
    pthread_mutex_unlock(&m->mutex);
    pthread_mutex_lock(&c->mutex);

    pthread_cond_wait(&c->condition, &c->mutex);

    pthread_mutex_lock(&m->mutex);
    pthread_mutex_unlock(&c->mutex);
}

void condvar_signal(struct condvar *c) {
    pthread_mutex_lock(&c->mutex);
    pthread_cond_signal(&c->condition);
    pthread_mutex_unlock(&c->mutex);
}

void condvar_broadcast(struct condvar *c) {
    pthread_mutex_lock(&c->mutex);
    pthread_cond_broadcast(&c->condition);
    pthread_mutex_unlock(&c->mutex);
}
