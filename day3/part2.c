#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    FILE *file = fopen("input.txt", "r");

    double total = 0.0;
    char *pend;
    char line[200];

    if (file != NULL)
    {
        long total = 0;

        while (fgets(line, sizeof(line), file))
        {
            
            long linetotal = 0;
            
            // chop off the newline
            size_t ln = strlen(line) - 1;
            if (line[ln] == '\n')
            line[ln] = '\0';
            
            printf("\n%s", line);

            int startindex = 0;
            char final[13];

            // we need 12 digits
            for (int i = 0; i < 12; i++)
            {
                long largestdigit = 0;
                long limit = strlen(line) - 12 + i;

                for (int j = startindex; j <= limit; j++)
                {
                    char digit[2];
                    digit[0] = line[j];
                    digit[1] = '\0';

                    long thisdigit = strtol(digit, &pend, 10);

                    if (thisdigit > largestdigit)
                    {
                        largestdigit = thisdigit;
                        startindex = j + 1;
                        continue;
                    }
                }

                long imult = 1;
                for (int m = 12 - i - 1; m > 0; m--) {
                    imult *= 10;
                }

                linetotal += largestdigit * imult;
            }
            printf(" = %ld\n", linetotal);
            total += linetotal;
        }
        printf("Total: %ld\n", total);
        fclose(file);
    }
    else
    {
        fprintf(stderr, "Unable to open file!\n");
    }

    return 0;
}
