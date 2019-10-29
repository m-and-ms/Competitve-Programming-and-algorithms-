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
long lcm(long a, long b){

long gcd;
gcd=fast_gcd(a,b);
long lcmu=a*b/gcd;
return lcmu;
}


int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << lcm(a, b) << std::endl;
  return 0;
}
