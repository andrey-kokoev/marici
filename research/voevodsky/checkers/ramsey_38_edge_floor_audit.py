"""Eliminate external (3,7) edge-minimum inputs to the 28-vertex reduction. Enumerate all <=44-edge 20-cores from minimum-degree roots, then derive weaker sufficient 21/22 floors by degree histograms. Uses stored smaller catalogues; not a proof of their completeness."""
import gzip,json,itertools,collections,hashlib
import igraph as ig
from pathlib import Path
from ramsey_retention_slice import CAT,D
P=D.parent
# Independent graph6 decoder via igraph's native graph6 alternative: implement graph6 bit order explicitly.
def decode(line):
 n=ord(line[0])-63;vs=[ord(t)-63 for t in line[1:]];assert n<63 and len(vs)==(n*(n-1)//2+5)//6;return [sum(1<<j for j in range(n) if i!=j and vs[(k:=max(i,j)*(max(i,j)-1)//2+min(i,j))//6]>>(5-k%6)&1) for i in range(n)]
def unpack(m,n):return [sum(1<<j for j in range(n) if i!=j and m>>(max(i,j)*(max(i,j)-1)//2+min(i,j))&1) for i in range(n)]
def key(a):
 n=len(a);g=ig.Graph(n,[(i,j) for i in range(n) for j in range(i) if a[i]>>j&1]);return sum(1<<(max(i,j)*(max(i,j)-1)//2+min(i,j)) for i,j in g.permute_vertices(g.canonical_permutation()).get_edgelist())
files=[P/'ramsey_38_degree4_children49.json',CAT.parent/'r36_16.g6.gz',CAT/'r36_17.g6',CAT.parent/'ramsey_37_20_44_cores.txt'];cs={15:[unpack(int(h,16),15) for h in json.loads(files[0].read_text())],16:[decode(s.strip()) for s in gzip.open(files[1],'rt')],17:[decode(s) for s in files[2].read_text().splitlines()]};mins={n:min(sum(x.bit_count() for x in a)//2 for a in graphs) for n,graphs in cs.items()};mins[14]=13 # Mantel/Turan complement: 14 vertices in five balanced classes force >=13 edges for alpha<=5.
def degree_floor(n):
 poss=[]
 for seq in itertools.combinations_with_replacement(range(n-18,7),n):
  if sum(seq)%2:continue
  e=sum(seq)//2
  if n*e>=sum(d*d+mins[n-d-1] for d in seq):poss.append(e)
 return min(poss)
floors={n:degree_floor(n) for n in (21,22)};found=set();hist=collections.Counter()
for d in (2,3,4):
 n=19-d
 for a in cs[n]:
  cap=44-d-sum(x.bit_count() for x in a)//2
  if cap<d*(d-1):continue
  I=[0]
  for i,x in enumerate(a):I.extend([s|1<<i for s in I if not s&x])
  S=[s for s in I if d-1<=s.bit_count()<=cap-(d-1)**2];Q=[q for q in I if q.bit_count()+d>=7];M=[sum(1<<k for k,q in enumerate(Q) if not q&s) for s in S];bad=[sum(1<<k for k,q in enumerate(Q) if q.bit_count()+t>=7) for t in range(d+1)]
  def visit(rows,idx,left,miss):
   if len(rows)==d:
    b=a.copy()+[0]*(d+1)
    for j,s in enumerate(rows,n):
     b[j]=s|1<<19;b[19]|=1<<j
     for i in range(n):b[i]|=(s>>i&1)<<j
    if min(v.bit_count() for v in b)==d:found.add(key(b));hist[d]+=1
    return
   for k in range(idx,len(S)):
    w=S[k].bit_count()
    if left-w<(d-len(rows)-1)*(d-1):continue
    new=[miss[0]]+[miss[t]|(miss[t-1]&M[k]) for t in range(1,d+1)]
    if any(new[t]&bad[t] for t in range(1,len(rows)+2)):continue
    visit(rows+[S[k]],k,left-w,new)
  visit([],0,cap,[(1<<len(Q))-1]+[0]*d)
ref={key(unpack(int(h,16),20)) for h in files[3].read_text().split()};assert found==ref and len(found)==15 and all(m.bit_count()==44 for m in found);assert floors[21]>48 and floors[22]>45;print(mins,floors,hist,len(found));(P/'ramsey_38_edge_floor_audit.json').write_text(json.dumps(dict(small_minima=mins,derived_floors=floors,root_presentations=hist,types=sorted(map(hex,found)),hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}))+'\n')
