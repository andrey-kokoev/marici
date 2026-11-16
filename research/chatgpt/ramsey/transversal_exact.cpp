#include <bits/stdc++.h>
using namespace std;
using u64=uint64_t;
static constexpr int N=35, W=53;
u64 adj[N], fullmask=(1ULL<<N)-1;
vector<u64> independent8;
void independent_sets(u64 available,u64 chosen,int remaining){
 if(remaining==0){independent8.push_back(chosen);return;}
 if(__builtin_popcountll(available)<remaining)return;
 while(available){
  u64 b=available&-available; available-=b;
  int v=__builtin_ctzll(b);
  independent_sets(available & ~adj[v],chosen|b,remaining-1);
 }
}
array<array<u64,W>,N> avoid;
long long tested=0, hitting=0;
bool recurse(int start,int left,const array<u64,W>& bitset){
 if(left==0){
  tested++;
  bool has_avoiding=false;
  for(int i=0;i<W;i++)has_avoiding |= bool(bitset[i]);
  if(!has_avoiding){hitting++;return true;}
  return false;
 }
 for(int v=start;v<=35-left;v++){
  array<u64,W> next;
  for(int k=0;k<W;k++)next[k]=bitset[k]&avoid[v][k];
  if(recurse(v+1,left-1,next))return true;
 }
 return false;
}
int main(){
 for(int v=0;v<N;v++)for(int d:{1,7,11,16}){
  adj[v]|=1ULL<<((v+d)%N);
  adj[v]|=1ULL<<((v+N-d)%N);
 }
 independent_sets(fullmask,0,8);
 if(independent8.size()!=3360){cerr<<"unexpected I8="<<independent8.size()<<"\n";return 1;}
 for(int v=0;v<N;v++)for(int i=0;i<(int)independent8.size();i++)
  if(!(independent8[i]&(1ULL<<v)))avoid[v][i/64] |= 1ULL<<(i%64);
 // Any nonempty 8-vertex hitting set translates to one containing vertex zero.
 bool found=recurse(1,7,avoid[0]);
 cout<<"independent8="<<independent8.size()<<"\n";
 cout<<"8-subsets containing vertex0 tested="<<tested<<" expected="<<5379616LL<<"\n";
 cout<<"8-vertex hitting set exists="<<found<<"\n";
 if(found || tested!=5379616LL)return 2;
 vector<int> nine={0,2,6,7,11,18,19,25,26};
 auto b=avoid[nine[0]];
 for(int j=1;j<(int)nine.size();j++)for(int k=0;k<W;k++)b[k]&=avoid[nine[j]][k];
 bool covers=true;for(auto z:b)covers &= z==0;
 cout<<"9-set is hitting="<<covers<<"\n";
 return covers?0:3;
}
