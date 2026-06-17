#include <stdio.h>
int main() {
    int decimal;
    printf("Enter a decimal number: ");
    scanf("%d",&decimal);
    if (decimal == 0) {
        printf("Binary: 0\n");
        printf("invalid input\n"); 
        return 0;
    }
    int binary[32];
    int index = 0;
    int count_ones = 0;
    while (decimal > 0) {
        binary[index] = decimal % 2;
        if (binary[index] == 1) {
            count_ones++;
        }
        decimal /= 2;
        index++;
    }
    printf("Binary: ");
    for (int i = index - 1; i >= 0; i--) {
        printf("%d", binary[i]);
    }
    printf("\n");
    if (count_ones > 0) {
        printf("Count of 1's: %d\n", count_ones);
    } else {
        printf("invalid input\n");
    }
    return 0;
}
