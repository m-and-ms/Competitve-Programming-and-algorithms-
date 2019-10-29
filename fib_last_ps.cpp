// Example program
#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>      /* printf */
#include <assert.h> 
using namespace std ;

 long solve( long  from , long to){
     int pisano=60;

assert(from<=to);
vector<long>fib;
fib={0,1};
for (long i=0;i<=pisano-2;i++){
 fib.push_back((fib[fib.size()-1]+fib[fib.size()-2])%10);   
    
    
}
from=from%pisano;
to=to%pisano;
if(from>to){
 to=to+pisano;
 
    
}
long p_sum=0;
for (long j=from;j<=to;j++){
 p_sum=p_sum+fib[j%pisano];
 
    
}
return p_sum%10;
}

int main() {
    long long from, to;
    std::cin >> from >> to;
    std::cout << solve(from, to) << '\n';
}


