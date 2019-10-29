#include<iostream>
using namespace std;
int sum_dig(int d1,int d2){
int sum =0;

sum=d1+d2;

return sum;




}
int main(){
int d1,d2,sum;

cin>>d1;
cin>>d2;
sum =sum_dig(d1,d2);
cout<<sum ;
return 0;
}
