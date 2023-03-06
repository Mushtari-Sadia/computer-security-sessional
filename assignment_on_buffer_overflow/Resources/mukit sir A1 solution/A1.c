
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int foo(char *str)
{
    int arr[40];
    char buffer[308+21];

    /* The following statement has a buffer overflow problem */ 
    strcpy(buffer, str);

    return 1;
}

int main(int argc, char **argv)
{
    char str[528];
    FILE *badfile;

    badfile = fopen("badfile", "r");
    fread(str, sizeof(char), 528, badfile);
    foo(str);

    printf("Try Again\n");
    return 1;
}

