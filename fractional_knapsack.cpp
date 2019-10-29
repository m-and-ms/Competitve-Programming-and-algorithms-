#include <iostream>
#include <bits/stdc++.h>   
#include<vector>
#include<algorithm>
using namespace std;

struct Item { 
    int value, weight; 
}; 
  

bool compare( Item a, Item b)


{ 
    double r1 = (double)a.value / a.weight; 
    double r2 = (double)b.value / b.weight; 
    return r1 > r2; 
}     
    
    
double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  double tvalue = 0.0;
  int curr_w =0 ;
  
   int n=values.size(); 
   vector<Item>vect ;   
   for (int i=0; i<n; i++) {
        vect.push_back({values[i],weights[i]} );     
}
sort(vect.begin(), vect.end(), compare);    
for (int j=0;j<n;j++){
    
    if( curr_w +vect[j].weight <= capacity){
        curr_w +=vect[j].weight;
        tvalue +=vect[j].value;
        
    }
    else {
        
        int left =capacity-curr_w;
     
        
        tvalue +=vect[j].value *((double)left/vect[j].weight) ;
        curr_w =capacity;
       
        
    }
    
}

    return tvalue ;
    
}    
    


 
 
 
 
    


int main()
{
    


  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }    
    
    



    
 double optimal_value = get_optimal_value(capacity, weights, values);

  std::cout.precision(10);
  std::cout << optimal_value << std::endl;
  return 0;


}

