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


string largest_number(vector<string> a) {
vector<int>single;
vector<int>duble;
string result="";
int maxi;
for (int i=0;i<a.size();i++){
 if (a[i].size()>1){
     stringstream geek(a[i]); 
  int x = 0; 

    // The object has the value 12345 and stream 
    // it to the integer x 
    
    geek >> x; 
     
     duble.push_back(x);
     
 }    

else{
      stringstream geek(a[i]); 
  int x = 0; 

    // The object has the value 12345 and stream 
    // it to the integer x 
    
    geek >> x; 
     
     single.push_back(x);
     
    
}
}
sort(single.begin(), single.end(),greater<int>());
sort(duble.begin(), duble.end(),greater<int>());


for (int i=0;i<single.size();i++){
    
 cout<<"s"<<single[i]<<"\n";   
}

for (int i=0;i<duble.size();i++){
    
 cout<<"d"<<duble[i]<<"\n";   
}
//stringstream result_s;
//copy(single.begin(), single.end(), ostream_iterator<int>(result_s, " "));

//std::stringstream result_d;
//std::copy(duble.begin(), duble.end(), ostream_iterator<int>(result_d, " "));
//int bigger=max(result_d.str().size(),result_s.str().size());
//string maxi;
int bigger=max(single.size(),duble.size());
//string temp=result_d.str();
//const char* cstr = temp.c_str();

//string temp_s=result_s.str();
//const char* cstr_s = temp_s.c_str();
for(int i=0;i<duble.size();i++){
   for(int j=0;j<single.size();j++){
//    if(strcmp(to_string(single[i]).c_str(),to_string(duble[i]).c_str())>0){
        
//    result+=result_s.str()[i];
//result+=to_string(single[i]);
//    pop_front(single);
//}
//else{
//        result+=to_string(duble[i]);
//    pop_front(duble);
char c=to_string(duble[i]).c_str()[0];
cout<<"c"<<c<<"\n";
char cc=to_string(duble[i]).c_str()[1];
cout<<"cc"<<cc<<"\n";

maxi=max(single[i],(int)c)    ;
if(single[i]>(int)c){
    
result+=to_string(single[j]);
    pop_front(single);
}
 else if((int)c==single[j])
{
if((int)cc>single[j]){

    result+=to_string(duble[i]);
    pop_front(duble);
}
else{
    result+=to_string(single[j]);
    pop_front(single);
    
    }
}
    else if(single[i]<(int)c){
    result+=to_string(duble[i]);
    pop_front(duble);
    
}

}
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


