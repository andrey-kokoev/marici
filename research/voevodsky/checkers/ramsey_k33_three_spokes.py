"""One fully doubled side A (all three pairs of A have one extra common red neighbor). Its three single-only groups X_i of size three attach as degree-three stars to the SAME (3,6) graph H=Y+Z of order 17. Obtain every attachment from marked closed-neighborhood deletions in the complete (3,7) 21-catalogue. The three opposite 21 edge counts equal 44+k_ij. Within X (12 vertices), e(X)=e(H)-20. Each X edge counts once in sum k_ij, except the edges from each double ij to the three singles in group k, counted twice. There are at most nine of these. No 21-type <=52 has a degree-3 vertex, so k>=9 and each k<=e(H)-20+9-18<=13. Screen simultaneous extension degree requirements and triangle-free cross edges on X without assuming ANY intersections on the B side."""
import itertools,json,gzip,collections,igraph as ig,sys,time
from ramsey_retention_slice import CAT,D,decode
auto=lambda key:ig.Graph(17,key).get_automorphisms_vf2();P=D.parent;comb=itertools.combinations

def deck():
 base={};rows=list(map(decode,(CAT/'r36_17.g6').read_text().splitlines()))
 for i,h in enumerate(rows):
  g=ig.Graph(17,[(j,k) for j,k in comb(range(17),2) if h[j]>>k&1]);base[tuple(sorted(g.permute_vertices(g.canonical_permutation()).get_edgelist()))]=i
 out=collections.defaultdict(set);trans=bytes((x-63).bit_count() if 63<=x<127 else 0 for x in range(256));marks=collections.Counter()
 for line in gzip.open(CAT.parent/'r37_21.g6.gz','rb'):
  l=line.strip();e=sum(l[1:].translate(trans));
  if e>57:continue
  h=decode(l.decode());
  for r,s in enumerate(h):
   if s.bit_count()!=3:continue
   W=[i for i in range(21) if s>>i&1];vs=[i for i in range(21) if i!=r and i not in W];g=ig.Graph(17,[(i,j) for i,j in comb(range(17),2) if h[vs[i]]>>vs[j]&1]);p=g.canonical_permutation();key=tuple(sorted(g.permute_vertices(p).get_edgelist()));assert key in base;mask=lambda w:sum(1<<j for j,old in enumerate(p) if h[w]>>vs[old]&1);ms=tuple(sorted(mask(w) for w in W));assert all(all(not (v>>i&1 and v>>j&1) for i,j in key) for v in ms);out[key].add((e-44,ms));marks[e]+=1
 print('marks',marks,flush=True);rec=[]
 for key,i in sorted(base.items(),key=lambda z:z[1]):
  G=auto(key);opts={};seen=set()
  for k,row in sorted(out[key]):
   if row in seen:continue
   full={tuple(sorted(sum(1<<p[j] for j in range(17) if s>>j&1) for s in row)) for p in G};assert not any(x in seen for x in full);seen|=full;opts[row]=(k,full)
  rec.append(dict(i=i,h=key,panels=[dict(k=k,rows=sorted(f)) for k,f in opts.values()]));print(i,collections.Counter(k for k,f in opts.values()),sum(len(f) for k,f in opts.values()),flush=True)
 (P/'ramsey_k33_three_spokes.json').write_text(json.dumps(rec)+'\n')
if __name__=='__main__':deck()
