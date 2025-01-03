#include <stdio.h>
#include <string.h>
#define N strlen(gen_poly)

int data[28],check[28],gen_poly[10];
int data_len,i,j;

void XOR(){
    for(j = 0; j<N;j++){
        if(check[j] == gen_poly[j]){
            check[j] = '0';
        } else{
            check[j] = '1';
        }
    }
}

void crc(){
    for(i = 0; i<N;i++){
        check[i] = data[i];
    }
    do{
        if(check[j] == '1'){
            XOR();
        }
        for(j = 0; j<N-1; i++){
            check[j] = check[j+1];
        }
        check[j] = data[i++];
    }
    while(i <= data_len + N - 1);
}

void reciever(){
    printf("\nData recieved: ");
    scanf("%s",data);

    crc();
    for(i = 0; i<N-1;i++){
        if (check[i] == '1'){
            break;
        }
    if (i < N-1){
        printf("\nERROR!");
        }else{
            printf("\nNO ERROR!");
        }   
    }
}

int main(){
    printf("\nEnter data:");
    scanf("%s",data);
    printf("\nEnter generator:");
    scanf("%s",gen_poly);
    data_len = strlen(data);
    for(i = 0; i<data_len+N-1;i++){
        data[i] = '0';
    }
    printf("\nData with padded 0's: %s",data);
    crc();
    printf("\nCheck sum: %s",check);

    for(i = data_len; i<data_len+N-1; i++){
        data[i] = check[i-data_len];
    }
    reciever();
}