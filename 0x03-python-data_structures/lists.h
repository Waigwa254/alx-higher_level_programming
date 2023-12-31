#ifndef LISTS_H
#define LISTS_H
#include <stddef.h>
#include <Python.h>

/**
 * struct listint_s - sit
 * @n: int
 * @next: po
 * Description: scture
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
void print_python_list_info(PyObject *p);
int is_palindrome(listint_t **head);

#endif
