#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <argument>\n", argv[0]);
        return 1;
    }

    char *arg = argv[1];
    char *reserved_memory = (char *)malloc(strlen(arg) + 1);
    strcpy(reserved_memory, arg);
    printf("%s\n", reserved_memory);
    free(reserved_memory);

    return 0;
}
