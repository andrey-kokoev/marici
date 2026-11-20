"""Unlabelled one-face-neighbor incidence and bounded transfer-mask decoder control."""
from itertools import permutations,combinations
from pathlib import Path
from collections import Counter
import json
HOME=Path(__file__).resolve().parents[1];d=json.loads((HOME/'results/esd7_explicit_analytical_census.json').read_text());cell=next(t for t in d['tetrahedra'] if t['id']=='T184');V=cell['vertices'];outer=[]
for v in V:
    f=set(V)-{v};across=[q for q in d['tetrahedra'] if q!=cell and f<=set(q['vertices'])];assert len(across)==1;outer.append(next(iter(set(across[0]['vertices'])-f)))
roles=V+outer;assert len(set(roles))==8
pairs=list(combinations(range(8),2));labels={tuple(sorted(roles.index(v) for v in e['vertices'])):e['transfer_mask'] for e in d['edges'] if set(e['vertices'])<=set(roles)};L=[labels.get(e,'absent') for e in pairs];types=sorted(set(L));S=[{i,4+i} for i in range(4)];assert all(s==set(range(8))-{b if a==i else a for a,b in labels if i in (a,b)} for i,s in enumerate(S))

def group(tagged):
    gs=[]
    for p in permutations(range(4)):
        def g(i):return p[i%4]+4*(i//4)
        if all((labels.get(tuple(sorted((g(a),g(b)))))==z if tagged else tuple(sorted((g(a),g(b)))) in labels) for (a,b),z in labels.items()):gs.append(p)
    return gs
G=group(False);assert len({p[0] for p in G})==4
# Additional test: red iff link type belongs to a chosen subset (one type for all absent links).
valid=squares=0;outputs=Counter()
for m in range(1<<len(types)):
    E={p for p,z in zip(pairs,L) if m>>types.index(z)&1};cl=lambda s,r,red:any(all((e in E)==red for e in combinations(t,2)) for t in combinations(sorted(s),r));U=set(range(8))
    if cl(U,3,True) or cl(U,7,False):continue
    valid+=1;vs=[('−' if cl(s,2,True) else '+')+('−' if cl(U-s,6,False) else '+') for s in S];outputs[len(set(vs))]+=1;squares+=len(set(vs))==4
res=dict(center=V,across=outer,untyped_edges=len(labels),untyped_automorphisms=G,typed_automorphisms=group(True),xor_of_four_attachment_masks=255,decoder_count=1<<len(types),admissible_decoders=valid,distinct_verdict_histogram=outputs,four_verdict_decoders=squares);print(json.dumps(res));(HOME/'results/ramsey_t184_verdict_square_probe.json').write_text(json.dumps(res,indent=2)+'\n')
