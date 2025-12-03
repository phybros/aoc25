#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    FILE* file = fopen("input.txt", "r");

    long total = 0;
    char *pend;
    char line[200];

    if (file != NULL) {

        while (fgets(line, sizeof(line), file)) {
            long largest = 0;

            // chop off the newline
            size_t ln = strlen(line) - 1;
            if (line[ln] == '\n')
                line[ln] = '\0';


            for (int i = 0; i < strlen(line); i++) {
                char digit[2];
                digit[0] = line[i];
                digit[1] = '\0';

                long thisdigit = strtol(digit, &pend, 10);

                // stop the second loop
                if (i == strlen(line) - 1) {
                    break;
                }

                // go through every subsequent char
                for (int j = i + 1; j < strlen(line); j++) {
                    char nextdigitstr[2];
                    nextdigitstr[0] = line[j];
                    nextdigitstr[1] = '\0';

                    long nextdigit = strtol(nextdigitstr, &pend, 10);

                    if (thisdigit * 10 + nextdigit > largest) {
                        largest = thisdigit * 10 + nextdigit;
                    }
                }
            }
    
            total += largest;
            printf("%s: %d\n", line, largest);
        }

        printf("Total: %d\n", total);
        fclose(file);
    }
    else {
        fprintf(stderr, "Unable to open file!\n");
    }

    return 0;
}
