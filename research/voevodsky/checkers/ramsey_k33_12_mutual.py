"""Reciprocal candidate grouping for asymmetric 1,2 side counts. Build the degree-four star deck to the original 16 catalogue independently of the (2,2) census; do not reuse its restrictive set of degree signatures."""
from ramsey_k33_12_deck import *
from functools import lru_cache
H=graphs();J=[list(map(int,l.split())) for l in (T/'k12graphs15.txt').read_text().splitlines()];edges=lambda h:sum(map(int.bit_count,h))//2
@lru_cache(None)
def aut(n,i):
 a=(H if n==16 else J)[i];return ig.Graph(n,[(j,k) for j,k in comb(range(n),2) if a[j]>>k&1]).get_automorphisms_vf2()
def mor(x,p):return sum(1<<p[k] for k in range(len(p)) if x>>k&1)
def symrep(i,n,row,seen):
 a,b,c=row[:3];q=(a,min(b,c),max(b,c));
 if q in seen:return False
 for p in aut(n,i):bb=mor(b,p);cc=mor(c,p);seen.add((mor(a,p),min(bb,cc),max(bb,cc)))
 return True

def reverse(deck,G):
 rev=collections.defaultdict(set);size=list(map(edges,G))
 for d in deck:
  i=d['i'];e=d['e'];revkeys={tuple(sorted(1+s.bit_count() for s in row)) for row in d['panels']}
  for sig in revkeys:rev[size[i],e,sig].add(i)
 return rev

def prepare():
 left=collections.defaultdict(list);rev=reverse(json.loads((T/'k12deck5.json').read_text()),J);old=None
 for l in (T/'k12sides.txt').open():
  i,a,b,c,ee,e=map(int,l.split());
  if i!=old:seen=set();old=i
  if not symrep(i,16,(a,b,c),seen):continue
  sg=tuple(sorted(8-(s&(b|c)).bit_count() for k,s in enumerate(H[i]) if a>>k&1))
  for j in rev[ee,e,sg]:left[i,j].append((a,b,c,e))
 print('left blocks',len(left),flush=True);avail=collections.defaultdict(set)
 for i,j in left:avail[j].add(edges(H[i]))
 need=set();right=[];old=None
 for l in (T/'k12sides15.txt').open():
  j,a,b,c,ee,e1,e2=map(int,l.split());
  if ee not in avail[j]:continue
  if j!=old:seen=set();old=j
  if not symrep(j,15,(a,b,c),seen):continue
  sig=lambda x,y:tuple(sorted(8-(h&(a|x)).bit_count() for v,h in enumerate(J[j]) if y&~(a|x)&1<<v));s1=sig(b,c);s2=sig(c,b);need.update([(e1,s1),(e2,s2)]);right.append((j,a,b,c,ee,e1,e2,s1,s2))
 print('right',len(right),len(need),flush=True);roots={};
 for i in {i for i,j in left}:k,p=canonical(H[i],range(16));roots[k]=(i,p)
 trans=bytes((x-63).bit_count() if 63<=x<127 else 0 for x in range(256));out=collections.defaultdict(set);mx=max(e for e,s in need)
 for line in gzip.open(CAT.parent/'r37_21.g6.gz','rb'):
  l=line.strip();e=sum(l[1:].translate(trans));
  if e>mx:continue
  g=decode(l.decode());ds=list(map(int.bit_count,g))
  for r,s in enumerate(g):
   if ds[r]!=4:continue
   w=[k for k in range(21) if s>>k&1];sig=tuple(sorted(ds[k] for k in w))
   if (e,sig) not in need:continue
   vs=[k for k in range(21) if k!=r and not s>>k&1];key,p=canonical(g,vs)
   if key not in roots:continue
   i,b=roots[key];ms=tuple(sorted(sum(1<<b[k] for k,old in enumerate(p) if g[x]>>vs[old]&1) for x in w));out[i,e].add(ms)
 deck=[dict(i=i,e=e,panels=sorted(v)) for (i,e),v in out.items()];(T/'k12deck4.json').write_text(json.dumps(deck)+'\n');back=reverse(deck,H);idx=collections.defaultdict(list)
 for j,a,b,c,ee,e1,e2,s1,s2 in right:
  for i in back[ee,e1,s1]&back[ee,e2,s2]:
   if (i,j) in left:idx[i,j].append((a,b,c,e1,e2))
 blocks=[(i,j,left[i,j],r) for (i,j),r in idx.items()];print(len(blocks),sum(len(l)*len(r) for i,j,l,r in blocks),flush=True);(T/'k12mutual.json').write_text(json.dumps(blocks)+'\n');(P/'ramsey_k33_12_mutual_counts.json').write_text(json.dumps(dict(blocks=len(blocks),pairs=sum(len(l)*len(r) for i,j,l,r in blocks),required_signatures=len(need)))+'\n')
if __name__=='__main__':prepare()
