#include <iostream>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>    // std::max
#include <cstdlib> 
  #include <iterator>
  #include <stdio.h>
#include <string.h>
# include <assert.h> 

#include <string>
using namespace std;
using std::vector;
using std::string;
int to_int(char c) { return c; }

template<typename T>
void pop_front(std::vector<T>& vec)
{
    assert(!vec.empty());
    vec.erase(vec.begin());
}
string comp(string a,string b){
    a=string(a);
    b=string(b);
    string t=a+b;
    string z=b+a;
     if(t.compare( z ) > 0){
 
      return a;   
     }
     else{
    

      return b;   
         
     }
}

std::pair<string,int> find_max(vector<string>a){
  string  maxi=a[0];
  int idx=0;
 for (int i=1;i<a.size();i++){
    maxi=comp(maxi,a[i]); 
   if(maxi==a[i]){
       idx=i;
       
   }

 }
 return  make_pair(maxi,idx);
    
}


string largest_number(vector<string> a) {
pair<string,int>paire;
string maxi;
int idx ;

string result="";
int i=0;
while(a.size()){
    i+=1;

     paire = find_max(a);
     maxi=paire.first;
     idx=paire.second;
    result+=maxi;
    
    a.erase(a.begin()+idx);
    
}


    
    





return result ;

}
int main() {
  int n;
  std::cin >> n;
  vector<string> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  std::cout << largest_number(a);
}

