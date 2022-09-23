#include <stdio.h>
#include <stdlib.h>

int main(){
	int size;
	scanf_s ("%d", &size);
	int *arr = malloc(sizeof(int) * size);
	
	for (int i=0; i < size; i++){
		scanf_s("%d", &arr[i]);
	}

	int tem;
	for (int i=0; i < size; i++){
		for (int j=0; j < size-1; j++){
			if (arr[i]>arr[i+1]){
				tem = arr[i];
				arr[i] = arr[i+1];
				arr[i+1] = tem;
			}
		}
	}

	if (size%2==0){
		int mid = (arr[size/2-1] + arr[size/2])/2;
		printf("%d",mid);
	}
	else{
		int mid = arr[size/2];
		printf("%d",mid);
	}
	free (arr);
	return 0;
}