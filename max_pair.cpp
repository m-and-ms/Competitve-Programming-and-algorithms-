#include<iostream>
using namespace std;

int max_pr(int arr[10]){
int res=0;
for (int i=0;i<sizeof(arr);++i){
for (int j=i+1;j<sizeof(arr);++j){
if(arr[i]*arr[j]>res){
res=(arr[i])*arr[j];

}



}

}

return res; 
}

int main() {


    int arr [10];
    for (int i = 0; i < 10; ++i) {
        cin >> arr[i];
    }

    int result = max_pr(arr);
    cout << result << "\n";
    return 0;
}

