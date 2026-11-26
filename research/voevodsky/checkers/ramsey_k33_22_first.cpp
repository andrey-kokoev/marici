// stdin: 16-vertex adjacency rows per catalogue graph. argv1: degree-four mark signatures of 21-catalogue layers 51..57, encoded e followed by four sorted neighbor degrees. Enumerate (2,2) local sides modulo permutations of roots. No symmetry quotient of catalogue vertices here. Only use necessary conditions.
#include <cstdio>
#include <cstdlib>
#include <array>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <iostream>
using namespace std;int pc(int s){return __builtin_popcount((unsigned)s);}int key(int e,int a[]){sort(a,a+4);for(int j=0;j<4;j++)e=e*9+a[j];return e;}int main(int ac,char**av){FILE*f=fopen(av[1],"r");if(!f)return 1;unordered_set<int> marks;int e,dd[4];while(fscanf(f,"%d%d%d%d%d",&e,dd,dd+1,dd+2,dd+3)==5)marks.insert(key(e,dd));int nbase=ac>2?atoi(av[2]):16;if(nbase!=15&&nbase!=16)return 2;int h[16],ix=-1;int T[16][16];while(cin>>h[0]){ix++;for(int j=1;j<nbase;j++)cin>>h[j];vector<int>S;vector<array<int,5>>vs;int ne=0;for(int j=0;j<nbase;j++){ne+=pc(h[j]);for(int k=0;k<nbase;k++)T[j][k]=pc(h[j]&h[k]);}ne/=2;for(int s=31;s<(1<<nbase);s++)if(pc(s)==5){bool ok=true;array<int,5> rr;int t=0;for(int q=s;q;q&=q-1){int j=__builtin_ctz(q);if(s&h[j]){ok=false;break;}rr[t++]=j;}if(ok){S.push_back(s);vs.push_back(rr);}}int n=S.size();vector<vector<int>> K(n,vector<int>(n,-1));for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){int u=pc(S[i]&S[j]);if(u>1)continue;int c=0;for(int v:vs[i])c+=pc(h[v]&S[j]);if(u&&(c<7||c>13))continue;K[i][j]=K[j][i]=c;}
 // choose the middle five (intersects both others); outer fives must be disjoint.
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(K[i][j]>=7&&(S[i]&S[j]))for(int k=j+1;k<n;k++)if(!(S[j]&S[k])&&(S[i]&S[k])&&K[i][k]>=7){int ms[3]={S[i],S[j],S[k]};bool ok=true;for(int q=1;q<=2;q++){int s=ms[0]|ms[q],u=ms[3-q]&~s,t=0;for(;u;u&=u-1)dd[t++]=8-pc(h[__builtin_ctz(u)]&s);if(!marks.count(key(44+K[i][q==1?j:k],dd))){ok=false;break;}}if(!ok)continue;int x=ms[0]|ms[1]|ms[2],z=65535^x,ee=0;for(int u=x;u;u&=u-1)ee+=pc(h[__builtin_ctz(u)]&x);ee=ee/2+12;if(ee<32||ee>40)continue;
 // Each five is the neighbor set of one root. For v outside it, 5 common H-neighbors with the root is impossible. And each two cells in the five get an extra common root.
 for(int s:ms){for(int v=0;v<nbase&&ok;v++)if(pc(h[v]&s)>4)ok=false;for(int u=s;u&&ok;u&=u-1)for(int w=u&(u-1);w;w&=w-1)if(T[__builtin_ctz(u)][__builtin_ctz(w)]>=4)ok=false;}if(ok)printf("%d %d %d %d %d %d %d\n",ix,S[i],S[j],S[k],ee,44+K[i][j],44+K[i][k]);}
}}
