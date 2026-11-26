"""Index the degree-four closed-neighborhood deletion deck of the 21-catalogue, restricted only by marked signatures actually requested by the K3,3 (2,2) side enumeration. Transport the four support masks to the SAME coordinates as the corresponding stored 16-type and keep all placements via base automorphisms (later). Every candidate's two doubled pairs must find the same opposite base type."""
from ramsey_retention_slice import CAT,D,decode
import sys,gzip,collections,itertools,json,igraph as ig,os
from pathlib import Path
P=D.parent;T=Path(os.environ['TEMP']);comb=itertools.combinations

def graphs():return [decode(l.strip()) for l in gzip.open(CAT.parent/'r36_16.g6.gz','rt')]
def canonical(a,vs):
 g=ig.Graph(len(vs),[(i,j) for i,j in comb(range(len(vs)),2) if a[vs[i]]>>vs[j]&1]);p=g.canonical_permutation();return tuple(sorted(g.permute_vertices(p).get_edgelist())),p

def process():
 H=graphs();bases={};
 for i,h in enumerate(H):
  key,p=canonical(h,list(range(16)));assert key not in bases;bases[key]=(i,p)
 rows=[tuple(map(int,l.split())) for l in (T/'k22sides.txt').read_text().splitlines()];needed=set()
 for i,a,b,c,opp,e1,e2 in rows:
  for y,z,e in [(b,c,e1),(c,b,e2)]:needed.add((e,*sorted(8-(v&(a|y)).bit_count() for j,v in enumerate(H[i]) if z&~(a|y)&1<<j)))
 counts=collections.Counter();out=collections.defaultdict(set);trans=bytes((x-63).bit_count() if 63<=x<127 else 0 for x in range(256));emax=max(s[0] for s in needed)
 for l in gzip.open(CAT.parent/'r37_21.g6.gz','rb'):
  l=l.strip();e=sum(l[1:].translate(trans));
  if e>emax:continue
  a=decode(l.decode());ds=list(map(int.bit_count,a))
  for r,v in enumerate(a):
   if ds[r]!=4:continue
   w=[i for i in range(21) if v>>i&1];sig=(e,*sorted(ds[i] for i in w));
   if sig not in needed:continue
   vs=[i for i in range(21) if i!=r and not v>>i&1];key,p=canonical(a,vs);idx,b=bases[key];panel=tuple(sorted(sum(1<<b[j] for j,old in enumerate(p) if a[i]>>vs[old]&1) for i in w));assert all(all(not (s>>i&1 and s&H[idx][i]) for i in range(16)) for s in panel);counts[e]+=1;out[idx,e].add(panel)
 print(counts,len(out),sum(map(len,out.values())),flush=True);records=[dict(i=i,e=e,panels=sorted(v)) for (i,e),v in sorted(out.items())];(T/'k22deck.json').write_text(json.dumps(records)+'\n');(P/'ramsey_k33_22_deck_counts.json').write_text(json.dumps(dict(sides=len(rows),signatures=len(needed),marks=counts,base_layers=len(out),placed=sum(map(len,out.values()))))+'\n');return records
if __name__=='__main__':process()
