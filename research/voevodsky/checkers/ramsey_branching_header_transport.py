"""Frozen rule: all nonbacktracking continuations in a fixed header's monochromatic link, with simple return at target minus one steps. Test predictions against independent clique check. n=6 exhausts all labeled inputs."""
import itertools,json
from collections import Counter
from ramsey_retention_slice import D,check

def returns(a,k):
 # Keep header, first port, and visited ports. No tests of chords.
 for L in a:
  def walk(start,last,used,depth):
   if depth==k-1:return bool(a[last]>>start&1)
   opts=L&a[last]&~used
   while opts:
    b=opts&-opts;opts^=b
    if walk(start,b.bit_length()-1,used|b,depth+1):return True
   return False
  ports=L
  while ports:
   b=ports&-ports;ports^=b;i=b.bit_length()-1
   if walk(i,i,b,1):return True
 return False
if __name__=='__main__':
 n=6;E=list(itertools.combinations(range(n),2));p=(1<<n)-1;stats={k:Counter() for k in [(4,4),(5,4)]}
 for m in range(1<<len(E)):
  g=[0]*n
  for j,(u,v) in enumerate(E):
   if m>>j&1:g[u]|=1<<v;g[v]|=1<<u
  blue=[p^(v|1<<i) for i,v in enumerate(g)];b4=returns(blue,4)
  for k,l in stats:
   pred=not b4 and not returns(g,k);truth=check(g,p,k,l);stats[k,l][('agree' if truth==pred else 'false_rejection' if truth else 'false_acceptance')]+=1
 # Six-vertex wheel with a four-port rim and a red leaf at one rim port (branching also within the header link via the sixth port).
 g=[0]*6
 for i,j in [(0,i) for i in range(1,6)]+[(1,2),(2,3),(3,4),(4,1),(1,5)]:g[i]|=1<<j;g[j]|=1<<i
 assert returns(g,5) and check(g,p,5,4);out=dict(stats={str(k):v for k,v in stats.items()},counterexample=g);print(out);(D.parent/'ramsey_branching_header_transport.json').write_text(json.dumps(out,indent=1)+'\n')
