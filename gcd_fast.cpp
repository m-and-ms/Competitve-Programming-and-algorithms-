#include <iostream>

//gcd(a,b)=gcd(r,b) where a%b=r
static long fast_gcd(long a,long b){
    long r;
while(b!=0){
r=a%b;
a=b;
b=r;
}

return a;
}
int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << fast_gcd(a, b) << std::endl;
  return 0;
}
