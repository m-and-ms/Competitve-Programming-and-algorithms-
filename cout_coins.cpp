#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int bank_notes[]={1,5,10} ;
int n=sizeof(bank_notes)/sizeof(bank_notes[0]);

int count_coins(int Money){
    vector<int>ans ;
    int count =0 ;
    for (int i=n-1;i>=0;i--){
        
        while (Money>=bank_notes[i]){
            Money -=bank_notes[i] ;
            
            count +=1 ;
            ans.push_back(bank_notes[i]) ;
            
            
        }
        
        
    }
    
    

    return count ;
    
}


int main()
{
    
    int V ;
    cin >>V ;
    
    cout<<count_coins(V);

    return 0;
}
