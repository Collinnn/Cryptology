#include <stdio.h>

int main(){
    
    long long N = 4294967317;
    int c = 17;
    int e =(2^16)+1;
    long a*;
    a = trialDivision(N);
    for(int i =0;i<128;i++){
        printf(a[i]);
    }
    return 0;
}

long * trialDivision(long N){
    long a [128];
    long i = 0;
    long f= 2;
    while (N>1){
        if(N % f == 0){
            a[i] = f;
            i++;

        }else{
            f+=2;
        }
    }
    if(N != 1){
        a[i] = N;
    }
    return a;
}