#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>      /* printf */
#include <assert.h> 
using namespace std ;

int min_change(int moeny){
int coins[3]={1,5,10};
int num_coins=0;
int n=3;
vector<int>change;
for (int i=n;i>=0;i--){
    while(moeny>=coins[i]){
        moeny=moeny-coins[i];
        change.push_back(coins[i]);
    }
}
for(int i=0;i<change.size();i++){
    
    num_coins+=1;
    
//        std::cout<<change[i]<< '\n';  
    }
            return num_coins;

        
    
    
    
}


int main() {
  int m;
  std::cin >> m;
  std::cout << min_change(m) << '\n';
}

