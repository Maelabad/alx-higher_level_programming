#include <stdio.h>
#include "python3.10/Python.h"
/**
 * print_python_list_info - print all python list info
 * @python_list: Py-Object
 * Return: Nothing
 */
void print_python_list_info(PyObject *python_list)
{
	long int size, i;
	PyListObject *list_obj;
	PyObject *item;

	size = Py_SIZE(python_list);
	printf("[*] Size of the Python List = %ld\n", size);

	list_obj = (PyListObject *)python_list;
	printf("[*] Allocated = %ld\n", list_obj->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(python_list, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
