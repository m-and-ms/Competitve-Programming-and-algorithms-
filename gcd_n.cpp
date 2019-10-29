#include <iostream>
using namespace std ;

int gcd(int a,int b){
int b_gcd=1;

for (int d=2;d<=a&&d<=b;d++){
if((a%d==0)&&(b%d==0)){
if(d>b_gcd){
b_gcd=d;
}


}   
}
return b_gcd;

}
int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << gcd(a, b) << std::endl;
  return 0;
}
