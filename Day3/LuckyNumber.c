#include <stdio.h>

int main() {
    int car_no;
    printf("Enter the car no:");
    scanf("%d",&car_no);
    if (car_no < 1000 || car_no > 9999) {
        printf("%d is not a valid car number\n", car_no);
        return 0;
    }
    int temp = car_no;
    int sum = 0;
    while (temp > 0) {
        sum += temp % 10; 
        temp /= 10;      
    }
    if (sum % 3 == 0 || sum % 5 == 0 || sum % 7 == 0) {
        printf("Lucky Number\n");
    } else {
        printf("Sorry its not my lucky number\n");
    }

    return 0;
}
