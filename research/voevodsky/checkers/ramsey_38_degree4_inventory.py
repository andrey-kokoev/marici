"""Two nested minimum-degree root decompositions. Generate every 15-vertex (3,6) core with <=29 edges from 11..13-vertex (3,5) catalogue layers. Then enumerate four support rows for the 20-vertex, 45-edge, minimum-degree-four case. All child tests include empty Q. Store a resumable result per child."""
import itertools,collections,json,sys,igraph as ig
from pathlib import Path
from ramsey_retention_slice import D,CAT,check,decode
P=D.parent;work=P/'ramsey_38_degree4_parts';work.mkdir(exist_ok=True)
def independent(a):
 I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v])
 return I
def key(a):
 G=ig.Graph(len(a),[(i,j) for i,j in itertools.combinations(range(len(a)),2) if a[i]>>j&1]);return sum(1<<(max(i,j)*(max(i,j)-1)//2+min(i,j)) for i,j in G.permute_vertices(G.canonical_permutation()).get_edgelist())
def unpack(m,n):return [sum(1<<j for j in range(n) if j!=i and m>>(max(i,j)*(max(i,j)-1)//2+min(i,j))&1) for i in range(n)]
def grow(a,d,k,emin,emax): # endpoint avoids blue k; root has minimum degree d
 n=len(a);I=independent(a);base=d+sum(v.bit_count() for v in a)//2;S=sorted((s for s in I if s.bit_count()>=d-1 and s.bit_count()+(d-1)**2<=emax-base),key=int.bit_count);sizes=[s.bit_count() for s in S];q=[s for s in I if s.bit_count()+d>=k];miss=[sum(1<<j for j,t in enumerate(q) if not s&t) for s in S];buckets=[sum(1<<j for j,t in enumerate(q) if t.bit_count()>=k-u) for u in range(d+1)];p=(1<<len(q))-1
 def rec(sel,j,cost,over):
  left=d-len(sel)
  if not left:
   if cost<emin:return
   b=list(a)+[0]*(d+1);root=n+d
   for h,ix in enumerate(sel,n):
    s=S[ix];b[h]=s|1<<root;b[root]|=1<<h
    while s:v=s&-s;s^=v;b[v.bit_length()-1]|=1<<h
   if min(x.bit_count() for x in b)==d:yield b
   return
  for l in range(j,len(S)):
   w=sizes[l]
   if cost+w*left>emax:break
   if cost+w+(left-1)*sizes[-1]<emin:continue
   m=miss[l];v=[p]+[over[u]|(over[u-1]&m) for u in range(1,len(sel)+2)]
   if any(v[u]&buckets[u] for u in range(1,len(v))):continue
   yield from rec(sel+[l],l,cost+w,v+[0])
 yield from rec([],0,base,[p,0])
if '--regular46' in sys.argv:
 # Delete a root of a 4-regular 15-core. Four independent neighbors each send three edges into a legal 10-core, leaving exactly 14 edges there.
 layer={0};counts=[]
 for n in range(10):
  nxt=set()
  for m in layer:
   a=unpack(m,n);I=independent(a);four=[q for q in I if q.bit_count()==4]
   for s in I:
    if s.bit_count()>4 or m.bit_count()+s.bit_count()>14 or any(not q&s for q in four):continue
    if any(s>>i&1 and v.bit_count()==4 for i,v in enumerate(a)):continue
    nxt.add(key([v|((s>>i&1)<<n) for i,v in enumerate(a)]+[s]))
  layer=nxt;counts.append(len(layer))
 seeds=[m for m in layer if m.bit_count()==14];regular={key(b) for m in seeds for b in grow(unpack(m,10),4,6,30,30)}
 children={key(c) for m in regular for c in grow(unpack(m,15),4,7,46,46)}
 assert all(check(unpack(m,15),(1<<15)-1,3,6) and all(v.bit_count()==4 for v in unpack(m,15)) for m in regular)
 assert all(check(unpack(m,20),(1<<20)-1,3,7) for m in children)
 res=dict(layer_counts=counts,seeds=len(seeds),regular=sorted(map(hex,regular)),extensions=sorted(map(hex,children)));(P/'ramsey_38_regular46.json').write_text(json.dumps(res)+'\n');print(counts,len(seeds),len(regular),len(children));sys.exit()
target=49 if '--manifest49' in sys.argv else 48 if '--manifest48' in sys.argv else 47 if '--manifest47' in sys.argv else 46 if '--46' in sys.argv else 45
if target==46:
 sys.argv.remove('--46');work=P/'ramsey_38_degree4_parts46';work.mkdir(exist_ok=True)
def extensions46(a):
 I=independent(a);budget=target-4-sum(x.bit_count() for x in a)//2;S=[s for s in I if 3<=s.bit_count()<=budget-9];Q=[[q for q in I if q.bit_count()==z] for z in (3,4,5)];M=[[sum(1<<j for j,q in enumerate(qs) if not s&q) for s in S] for qs in Q];N=len(S);adj=[sum(1<<j for j in range(i,N) if not M[2][i]&M[2][j] and S[i].bit_count()+S[j].bit_count()<=budget-6) for i in range(N)]
 def ids(bits):
  while bits:v=bits&-bits;bits^=v;yield v.bit_length()-1
 for i,ai in enumerate(adj):
  for j in ids(ai):
   ij=ai&adj[j];four=M[1][i]&M[1][j]
   for k in ids(ij):
    if four&M[1][k]:continue
    need=budget-sum(S[t].bit_count() for t in (i,j,k));block=four|((M[1][i]|M[1][j])&M[1][k]);three=M[0][i]&M[0][j]&M[0][k]
    for l in ids(ij&adj[k]):
     if S[l].bit_count()!=need or M[1][l]&block or M[0][l]&three:continue
     b=a.copy()+[0,0,0,0,15<<15]
     for h,t in enumerate((i,j,k,l),15):
      b[h]=S[t]|1<<19
      for v in ids(S[t]):b[v]|=1<<h
     if min(v.bit_count() for v in b)==4:yield b
layers={n:{key(r['core']):r['core'] for r in json.loads((P/'ramsey_frontier_transfer.json').read_text()) if r['n']==n} for n in (11,12)};layers[13]={0:decode((CAT/'r35_13.g6').read_text().strip())};children=set()
for d in (1,2,3):
 for a in layers[14-d].values():
  for b in grow(a,d,6,0,target-16):children.add(key(b))
if target>=47:
 # A degree-four root in a 15-core leaves ten vertices. The four neighbors need >=12 edges to them, so <=15 edges remain. Generate every legal ten-core in that budget by vertex addition.
 layer={0}
 for n in range(10):
  nxt=set()
  for m in layer:
   a=unpack(m,n);I=independent(a);fours=[q for q in I if q.bit_count()==4]
   for s in I:
    if m.bit_count()+s.bit_count()<=target-32 and all(s&q for q in fours):nxt.add(key([v|((s>>i&1)<<n) for i,v in enumerate(a)]+[s]))
  layer=nxt
 high={key(b) for m in layer for b in grow(unpack(m,10),4,6,30,target-16)};assert not high&children
 all15=children|high;print('15-core counts by min degree / edge count',collections.Counter((min(x.bit_count() for x in unpack(m,15)),m.bit_count()) for m in all15),flush=True)
 (P/f'ramsey_38_degree4_children{target}.json').write_text(json.dumps(sorted(map(hex,all15)))+'\n')
 if target==49:sys.exit()
 end={key(b) for m in high for b in extensions46(unpack(m,15))};assert all(check(unpack(m,20),(1<<20)-1,3,7) for m in end);print('children',len(children),len(high),'high extensions',len(end));(P/f'ramsey_38_high_children{target}.json').write_text(json.dumps(dict(children=sorted(map(hex,high)),extensions=sorted(map(hex,end))))+'\n');sys.exit()
print('children',len(children),flush=True)
if target==46 and '--manifest' in sys.argv:
 (P/'ramsey_38_degree4_nonregular46.json').write_text(json.dumps(sorted(map(hex,children)))+'\n');sys.exit()
for i,m in enumerate(sorted(children)):
 if len(sys.argv)>1 and i%4!=int(sys.argv[1]):continue
 path=work/f'{m:x}.json'
 if path.exists():continue
 a=unpack(m,15);found={key(b) for b in (extensions46(a) if target==46 else grow(a,4,7,45,45))};path.write_text(json.dumps(sorted(map(hex,found))))
 if i%100==0:print(i,flush=True)
if len(sys.argv)>1:sys.exit()
alltypes={int(s,16) for m in children for s in json.loads((work/f'{m:x}.json').read_text())};res=[]
for m in sorted(alltypes):
 a=unpack(m,20);assert check(a,2**20-1,3,7);Q=[s for s in independent(a) if s.bit_count()==5];
 if all(any(not t&(a[i]|a[j]|1<<i|1<<j) for t in Q) for i,j in itertools.combinations(range(20),2) if a[i]>>j&1):res.append(a)
print('all',len(alltypes),'resistant',len(res));(P/('ramsey_38_degree4_inventory46.json' if target==46 else 'ramsey_38_degree4_inventory.json')).write_text(json.dumps(dict(children=len(children),types=len(alltypes),resistant=res))+'\n')
