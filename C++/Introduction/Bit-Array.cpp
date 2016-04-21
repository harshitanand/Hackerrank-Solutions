#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_set>
using namespace std;


int main() {
  
  const int Z=10000;
  int N,S,P,Q,i=1;
  scanf("%d%d%d%d",&N,&S,&P,&Q);
  unordered_set<int> se={S};
  
  for(;i<min(N,Z);i++){
      S=((long long)S*P+Q)%0x80000000;
      if(se.find(S)!=se.end())break;
      se.insert(S);
    }
  
  printf("%d\n",i==Z ? N : i);   
  return 0;
}
