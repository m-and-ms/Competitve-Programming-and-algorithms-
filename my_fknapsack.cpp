#include <iostream>
#include <vector>
#include<algorithm>

using namespace std;
using std::vector;
int get_w(double sorted_wpv,vector <double> wpv,vector<int> weights,int n){
  vector<double>::iterator it;


  it = find (wpv.begin(), wpv.end(), sorted_wpv);
//    sorted_w.push_back(weights[*it]);
//    sorted_v.push_back(values[*it]);

int j=std::distance(wpv.begin(), it);



  return weights[j];
    
    
}

int get_v(double sorted_wpv,vector <double> wpv, vector<int> values,int n){
  vector<double>::iterator it;


  it = find (wpv.begin(), wpv.end(), sorted_wpv);
//    sorted_w.push_back(weights[*it]);
//    sorted_v.push_back(values[*it]);

int j=std::distance(wpv.begin(), it);



  return values[j];
    
    
}

double get_optimal_value(int capacity, vector<int> weights, vector<int> values,int n) {
    int curWeight = 0;  // Current weight in knapsack 
    double finalvalue = 0.0; 
    vector <double> wpv;

vector<double>wpv_ns;
vector<int>sorted_w;
vector<int>sorted_v;
for (int i=0;i<n;i++){
    
 wpv.push_back(values[i]/weights[i]);
}
wpv_ns=wpv;
sort(wpv.begin(), wpv.end(),greater<double>());



for(int i=0;i<n;i++){
    
 int s_w;
 int s_v;
 
 s_w=get_w(wpv[i], wpv_ns, weights,n);   
s_v=get_v(wpv[i], wpv_ns,  values,n);

sorted_w.push_back(s_w);

sorted_v.push_back(s_v);

}

for (int i=0;i<n;i++){
    
  if (curWeight + sorted_w[i] <= capacity) 
        { 
            curWeight += sorted_w[i]; 
            finalvalue += sorted_v[i]; 
        } 
  
        // If we can't add current Item, add fractional part of it 
        else
        { 
            int remain = capacity - curWeight; 
            finalvalue += sorted_v[i] * ((double) remain / sorted_w[i]); 
            break; 
        } 
    } 



 

  return finalvalue;
}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values,n);

 std::cout.precision(10);
  std::cout << optimal_value << std::endl;
  return 0;
}
