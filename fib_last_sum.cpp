// Example program
#include <iostream>
#include <string>
#include <vector>
using namespace std ;

 long solve( long n){
 vector< long> v;
     v={1,1};

 int pisano=60;
 if(n<2){
     
    return n;
 }
    n=n%pisano;



    for (long i =0;i<=n-1 ;i++){
        
        
    v.push_back((v[v.size() - 1]+v[v.size()-2])%10);
    
    
    }
    //cout<< (v[sz-1]-1)%10;
    if ((v[v.size()-1]-1)%10 <0){
        return ((v[v.size()-1]-1)%10)+10;
    }
    
    return ((v[v.size()-1]-1)%10);
    
    
}    

int main() {
    long long n;
    std::cin >> n;
    std::cout << solve(n);
}


