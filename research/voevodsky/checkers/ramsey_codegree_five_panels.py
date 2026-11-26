"""Global codegree-five test, with no singleton or pair-mask assumption. Two blue vertices share five red neighbors C, have U,V of size three exclusive to each root, and common blue H on 22 vertices. e(H)=52+e(U,V). Only 60 and 61 occur in the catalogue up to the maximum 61. Thus the cross-graph is K3,3 minus one edge or K3,3. Each exclusive vertex needs an independent H-support of size 7 minus its cross-degree. Each side's triple must extend H inside a (3,8) core. Enumerate all unordered within-degree support triples, allowing repeated sets: every pair must jointly hit every blue six; triple must hit every blue five. Then check triangle-free cross compatibility between two valid triples on SAME H. No other endpoint restrictions at this stage."""
import itertools,json,collections,sys,time
from ramsey_retention_slice import CAT,D,decode
P=D.parent

def panels(h,k):
 I=[0]
 for j,v in enumerate(h):I.extend([s|1<<j for s in I if not s&v]);
 G={j:[s for s in I if s.bit_count()==j] for j in (4,5,6)};miss={j:{s:sum(1<<i for i,q in enumerate(G[j]) if not s&q) for s in G[4]+G[5]} for j in (5,6)};m5,m6=miss[5],miss[6];out=[];np=0
 for i,a in enumerate(G[4]):
  for z in range(i,len(G[4])):
   b=G[4][z];q6=m6[a];
   if q6&m6[b]:continue
   np+=1;f=q6|m6[b];g=m5[a]&m5[b]
   for c in (G[4][z:] if k==9 else G[5]):
    if not (f&m6[c] or g&m5[c]):out.append((a,b,c))
 return out,np

def run(j,h):
 e=sum(s.bit_count() for s in h)//2;k=e-52;ss,np=panels(h,k);U=[a|b|c for a,b,c in ss];T=[a|b for a,b,c in ss];# All matched cross pairs must have disjoint supports. If k=8 only the two last sets may overlap. Index by bits rather than quadratic panels.
 allp=(1<<len(ss))-1;inc=lambda vs:[sum(1<<i for i,u in enumerate(vs) if u>>v&1) for v in range(22)];
 # pack index via bytes to handle large panel pools
 def index(vs):
  rows=[bytearray((len(ss)+7)//8) for _ in range(22)]
  for i,u in enumerate(vs):
   while u:v=u&-u;u-=v;rows[v.bit_length()-1][i//8]|=1<<(i%8)
  return [int.from_bytes(row,'little') for row in rows]
 iu,it=index(U),index(T);cross=0;examples=[]
 for i,(a,b,c) in enumerate(ss):
  x=allp
  for v in range(22):
   if T[i]>>v&1:x &= ~iu[v]
   elif c>>v&1:x &= ~(iu if k==9 else it)[v]
   if not x:break
  cross+=x.bit_count()
  if x and len(examples)<3:examples.append((ss[i],ss[(x&-x).bit_length()-1]))
 return dict(catalogue_index=j,edges=e,matched_4_pairs=np,panels=len(ss),ordered_compatible=cross,examples=examples)
if __name__=='__main__':
 H=list(map(decode,(CAT/'r37_22.g6').read_text().splitlines()));hist=collections.Counter(sum(s.bit_count() for s in h)//2 for h in H);assert min(hist)==60 and len(H)==191;out=[]
 for j,h in enumerate(H):
  if sum(s.bit_count() for s in h)//2<=61:
   z=run(j,h);print(z,flush=True);out.append(z)
 (P/'ramsey_codegree_five_panels.json').write_text(json.dumps(dict(catalogue=hist,layers=out))+'\n')
