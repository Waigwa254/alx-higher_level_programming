#include "lists.h"

/**
 * check_cycle - checkcle
 * @list: link
 *
 * Return: 1 
 */
int check_cycle(listint_t *list)
{
        listint_t *slow = list;
        listint_t *fast = list;

        if (!list)
                return (0);

        while (slow && fast && fast->next)
        {
                slow = slow->next;
                fast = fast->next->next;
                if (slow == fast)
                        return (1);
        }

        return (0);
}
root@e024474929d2:~/alx-higher_level_programming/0x00-python-hello_world# cat lists.h
#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly
 * @n: eger
 * @next: poiode
 *
 * Description: singly l for ect
 */
typedef struct listint_s
{
        int n;
        struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif

