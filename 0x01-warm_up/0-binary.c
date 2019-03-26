#include "search_algos.h"
/**
 * binary_search - searches for a value in a sorted array of ints
 * using the binary search algorithm
 * @array: pointer to the first element of the array to search in
 * @size: the number of elements in array
 * @value: value to search for in array
 *
 * Return: index where value is located or -1 if DNE
 */

int binary_search(int *array, size_t size, int value)
{
	int left = 0;
	int right = size - 1;
	int middle = (left + right) / 2;
	int i;

	if (array && value)
	{
		while (left <= right)
		{
			printf("Searching in array: ");
			i = left;
			while (i <= right)
			{
				if (i != right)
					printf("%d, ", array[i]);
				else
				  printf("%d\n", array[i]);
				i++;
			}
			middle = (left + right) / 2;
			if (array[middle] < value)
				left = middle + 1;
			else if (array[middle] > value)
				right = middle;
			else
				return (middle);
		}
	}
	return (-1);
}
