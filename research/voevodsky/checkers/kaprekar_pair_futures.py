"""Set-valued matchings on standard output places; all future prefixes through first repeated numeric state. Compare information in current gaps vs next pairing, not decorated lineages."""
from itertools import permutations,product
from collections import defaultdict
from pathlib import Path
import json
P=list(permutations(range(4)));X=list(product(range(10),repeat=4));digits=lambda n:tuple(map(int,f'{n:04d}'));gap=lambda x:(max(x)-min(x),sorted(x)[2]-sorted(x)[1]);key=lambda p:tuple(sorted((tuple(sorted((p[0],p[3]))),tuple(sorted((p[1],p[2]))))));fmt=lambda x:''.join(map(str,x));
K={x:digits(int(fmt(sorted(x,reverse=True)))-int(fmt(sorted(x)))) for x in X};M={y:tuple(sorted({key(p) for p in P if list(y[i] for i in p)==sorted(y)})) for y in set(K.values())}
def future(y):
 seen=set();out=[]
 while y not in seen:seen.add(y);out.append(M[y]);y=K[y]
 return tuple(out)
G=defaultdict(set);MG=defaultdict(set);F={y:future(y) for y in M};demo={};witness=None
for x in X:
 y=K[x];g=gap(x);seq=F[y];G[g].add(seq);MG[g,M[y]].add(seq);z=K[y];
 if len(set(x))==len(set(y))==len(set(z))==4 and witness is None:
  pair=M[y];rec=dict(input=fmt(x),gaps=g,first=fmt(y),first_matching=pair,second=fmt(z),second_matching=M[z]);old=demo.setdefault(pair,rec)
  if old['second_matching']!=M[z]:witness=[old,rec]
assert all(len(s)==1 for s in G.values());o=dict(inputs=len(X),gap_keys=len(G),augmented_keys=len(MG),next_pairing_keys=len(set(M.values())),max_itineraries_per_gap=max(map(len,G.values())),distinct_itineraries=len(set(F.values())),reverse_example=witness);print(o);(Path(__file__).resolve().parents[1]/'results/kaprekar_pair_futures.json').write_text(json.dumps(o,indent=2)+'\n')
