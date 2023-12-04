#include <stdlib.h>
#include <stdio.h>
#include <python.h>

/**
 * print_python_list_info -print python lists
 * @p: python 
 */
void print_python_list_info(PyObject*p)
{
	int elem;
	printf("[*]Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*]Allocated = %lu\n",((PyListObject*)p)->allocated):
	for (elem = 0; elem < Py_SIZE(p); elem++)
		printf("Element %d: %s\n", elem, Py_TYPE(PyList_Getltem(p, elem))->tp_name);
}
