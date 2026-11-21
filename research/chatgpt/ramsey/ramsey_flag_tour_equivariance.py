"""Test equivariant ordered-flag -> full triangle-tour selectors in the direct four-column bridge. Use seed's directed tour normalization and sewing reader; distinguish path reversal from projection onto cyclic words."""
from itertools import permutations,product
from pathlib import Path
import json,sys
D=Path(__file__).resolve().parent;sys.path.insert(0,str(D.parents[1]/'nima/checkers'))
from check_seed_typed_execution import tours,sew_at,normalize,registry,swap,moved_tour
from ramsey_seed_affine_witness import r

def run():
    pair=(((0,16),(7,29)),((0,17),(4,29)));assert tuple(tuple(r[i] for i in f) for f in pair[0])==pair[1]
    seam=lambda w:next(i for i in 'AB' if normalize(w) in sew_at(i));rows=[]
    for p in permutations('ABCD'):
        perm=dict(zip(p,[p[0],p[2],p[1],p[3]]));rev=lambda e:perm[e[1]]+perm[e[0]]
        if {rev(e) for e in ('AB','BC','CA')}!={'AD','DB','BA'} or {rev(e) for e in registry}!=set(registry):continue
        action=lambda w:tuple(rev(e) for e in reversed(w));im=[normalize(action(t)) for t in tours];assert im==list(tours);mark=p[0];maps=[]
        for u,v in product(tours,repeat=2):
            if normalize(action(u))!=v:continue
            maps.append(dict(seams=[seam(u),seam(v)],outputs=[int(seam(t)==mark) for t in (u,v)]))
        # Check naturality on all 12 based presentations; normalizing drops just the cursor.
        for t in tours:
            for k in range(6):
                w=t[k:]+t[:k];y=action(w);assert all(registry[a][1]==registry[b][0] for a,b in zip(y,y[1:]+y[:1]));assert seam(y)==perm[seam(w)]
        rows.append(dict(binding=''.join(p),equivariant_assignments=maps));
    assert len(rows)==4 and all(m['outputs'][0]==m['outputs'][1] for row in rows for m in row['equivariant_assignments']);return dict(directed_flags=pair,tour_classes=tours,bindings=rows,proper_seed_swap_seams=[seam(moved_tour(w,swap)) for w in tours])
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_flag_tour_equivariance.json').write_text(json.dumps(out)+'\n')
