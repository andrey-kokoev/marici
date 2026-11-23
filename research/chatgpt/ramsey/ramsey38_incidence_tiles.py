"""Compare coincidence of typed incidences, not merely group orders. Use static common-red values on the archived layer split; ask whether the two degree-one relations cut out canonical four-point substructures. Do not insert the PNE matching into the Ramsey graph."""
import json,itertools
from pathlib import Path
D=Path(__file__).parent;W=sorted(json.loads((D/'ramsey_seven_all_wirings.json').read_text())['wirings']);L,R=map(set,json.loads((D/'ramsey38_layer_signature.json').read_text())['layers']);score=lambda i,j:(W[i]&W[j]).bit_count();s={i:{j for j in R if score(i,j)!=35} for i in L};tiles=[]
for b in {frozenset(t) for t in s.values()}:
 a={i for i in L if s[i]==b};tiles.append([sorted(a),sorted(b)])
assert len(tiles)==2 and all(len(a)==len(b)==2 for a,b in tiles);assert all(score(i,j)==35 for a,b in tiles for i in a for j in R-set(b));p=(D.parent.parent/'voevodsky/results/pne_joint_role_quotient.json');q=json.loads(p.read_text());C=sorted({c for c,m in q['incident']});M=sorted({m for c,m in q['incident']});yes=set(map(tuple,q['incident']));no=set(map(tuple,q['absent']));assert yes|no==set(itertools.product(C,M)) and not yes&no
res=[]
for a,b in sorted(tiles):
 iso={}
 for v in (20,22):
  maps=[dict(zip(C+M,aa+bb)) for aa in itertools.permutations(a) for bb in itertools.permutations(b)];ok=[h for h in maps if all((score(h[c],h[m])==v)==((c,m) in yes) for c,m in yes|no)];assert len(ok)==2;iso[v]=ok
 res.append(dict(left=a,right=b,shared_red=[[score(i,j) for j in b] for i in a],isomorphisms=iso))
o=dict(tiles=res,cross_tile_value=35,limitations='Isomorphisms of derived typed incidence only; neither a choice between the two Ramsey predicates nor a map from a common-red address to a PNE role is supplied.');print(o);(D/'ramsey38_incidence_tiles.json').write_text(json.dumps(o,indent=2)+'\n')
