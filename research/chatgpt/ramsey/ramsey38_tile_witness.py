"""Joint site masks; witness predicates derived from source strata and their automorphism orbits. Calibrate only on first tile. Validate second tile, distinguishing positive witnesses from undifferentiated common support."""
import json,itertools,collections
from pathlib import Path
D=Path(__file__).parent;load=lambda n:json.loads((D/n).read_text());r=load('ramsey_seven_all_wirings.json');S=r['address_masks'];E=list(map(tuple,r['edge_order']));W=sorted(r['wirings']);tiles=load('ramsey38_incidence_tiles.json')['tiles'];q,=[a for a in S if a.bit_count()==4];z,=[1<<i for i in range(7) if all((1<<i|1<<j) in S for j in range(7) if i!=j)];b=127^z^q;at=lambda s:''.join(k*(s&mask).bit_count() for k,mask in [('Z',z),('B',b),('Q',q)]);edges_by=collections.defaultdict(set)
for k,(i,j) in enumerate(E):edges_by['-'.join(sorted((at(S[i]),at(S[j]))))].add(k)
out=[];candidates=None;fixed=None
for t in tiles:
 a,c=t['left'];b1,d=t['right'];vs=[a,c,b1,d];sets={i:{k for k in range(len(E)) if W[i]>>k&1} for i in vs};common=set.intersection(*sets.values());recs=[]
 for i,j in itertools.product(vs[:2],vs[2:]):
  hit=sets[i]&sets[j];ex=hit-set.union(*(sets[u] for u in vs if u not in (i,j)));recs.append(dict(pair=[i,j],total=len(hit),exclusive=len(ex),type_hits={s:sorted(ks&hit) for s,ks in edges_by.items() if ks&hit},exclusive_types={s:sorted(ks&ex) for s,ks in edges_by.items() if ks&ex}))
 select={(mode,s,h) for mode in ('type_hits','exclusive_types') for s in edges_by for h in (20,22) if all((s in r[mode])==(r['total']==h) for r in recs)};candidates=select if candidates is None else candidates&select;fixed=common if fixed is None else fixed&common;out.append(dict(common=sorted(common),pairs=recs))
layers=load('ramsey38_layer_signature.json')['layers'];zone=edges_by['BQ-ZB'];counts=collections.defaultdict(set)
for i,j in itertools.product(*layers):
 h=W[i]&W[j];counts[h.bit_count()].add(sum((h>>k)&1 for k in zone))
assert dict(counts)=={20:{0},22:{4},35:{2}};r=dict(probe_counts={k:sorted(v) for k,v in counts.items()},all_eight_common=sorted(fixed),common_per_tile=[len(t['common']) for t in out],predicates=sorted(candidates),edge_addresses=[[[i for i in range(7) if S[v]>>i&1] for v in e] for e in E],tiles=out);print(r['common_per_tile'],len(fixed),r['predicates']);print([(s['total'],s['exclusive'],s['exclusive_types']) for s in out[0]['pairs']]);(D/'ramsey38_tile_witness.json').write_text(json.dumps(r,indent=2)+'\n')
