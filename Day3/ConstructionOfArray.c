#include <stdio.h>

void solve() {
    int n;
    scanf("%d", &n);
    
   
    for (int i = 0; i < n; i++) {
        
        printf("%d ", 2 * i + 1); 
    }
    printf("\n");
}

int main() {
    int t;
    scanf("%d", &t);
    
    while (t--) {
        solve();
    }
    
    return 0;
}
