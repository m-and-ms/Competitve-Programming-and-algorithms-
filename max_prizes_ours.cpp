#include <iostream>
#include <vector>
#include<algorithm>

using namespace std;
using std::vector;



vector<int> optimal_summands(int n) {
    int sum ;
    int rem ;
    int k;
    
  vector<int> summands;
  if(n<=2){
      summands.push_back(n);
return summands;
}

   
summands.push_back(1);
//summands.push_back(2);
sum=1;
rem=n-1;
int i=1;
while(rem>0){
    int key;
   

     key=rem-(summands[i-1]+1);
       
              if (key>summands[i-1]+1){   
                  
                  


      

         k=summands[i-1]+1;
        summands.push_back(k);
    rem-=k;
    sum+=k;
    }
   


    else {

                


    k=rem;
     rem-=k;
     sum+=k;
   summands.push_back(k);   

    }


    
 i+=1;   
}    

  return summands;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> summands = optimal_summands(n);
  std::cout << summands.size() << '\n';
  for (size_t i = 0; i < summands.size(); ++i) {
    std::cout << summands[i] << ' ';
  }
}

