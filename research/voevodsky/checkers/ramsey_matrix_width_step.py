"""Ordered, unfolded Excel matrices; distinguish transport of labels from transport of occurrences."""
from itertools import combinations,product
from collections import defaultdict,Counter
from pathlib import Path
import json
from ramsey_table_cube_differences import analyze


def matrix(k):
    pos=[(a,b+1,c+2) for a,b,c in combinations(range(1,k-1),3)];flip=lambda r:tuple(k+1-v for v in reversed(r))
    def build(lo,hi):
        if lo>hi:return []
        hit=pos[lo]==flip(pos[hi]);i=lo+1
        if lo==hi:return [i] if hit else [i,-i]
        return [i]+build(lo+1,hi-hit)+([hi+1] if hit else [-i])
    src=build(0,len(pos)-1);rows=[pos[i-1] if i>0 else flip(pos[-i-1]) for i in src];X=[[int(v in r) for v in range(1,k+1)] for r in rows];t=analyze(k);u=sorted([r for p in t['pieces'] for r in p['new']]+t['leftover']);assert rows==u+t['center']+list(map(flip,reversed(u)));idx=defaultdict(list)
    for i,r in enumerate(rows,1):idx[r].append(i)
    charts=[]
    for p in t['pieces']:
        for mirror in [False,True]:
            a=tuple(k-i for i in reversed(p['start'])) if mirror else p['start'];lookup={}
            for bits in product(range(2),repeat=3):
                r=tuple(v+b for v,b in zip(a,bits));upper=flip(r) if mirror else r;i=u.index(upper)+1;i=len(rows)+1-i if mirror else i;assert rows[i-1]==r;lookup[''.join(map(str,bits))]=i
            swaps=[(v,lookup[key[:j]+'1'+key[j+1:]],a[j],a[j]+1) for key,v in lookup.items() for j in range(3) if key[j]=='0'];charts.append(dict(start=a,half='mirror' if mirror else 'upper',corner_occurrence=lookup,directed_swaps=swaps))
    return dict(width=k,columns=list(range(1,k+1)),source_triples=pos,signed_source_ids=src,X=X,charts=charts),idx


def run():
    old,ix=matrix(8);new,iy=matrix(9);transport=[iy[tuple(i for i,v in enumerate(row,1) if v)] for row in old['X']];assert all(transport);U=[c for c in old['charts'] if c['half']=='upper'];V=[c for c in new['charts'] if c['half']=='upper'];role=[dict(old_start=c['start'],new_start=d['start'],occurrences=[(i,d['corner_occurrence'][b]) for b,i in c['corner_occurrence'].items()]) for c in U for d in V];out=dict(layers=[old,new],literal_successor_occurrences=transport,upper_relative_role_maps=role,indexing='One-based occurrence IDs. Literal successors retain the same sites after adding a zero column. Role maps preserve directed bits even when sites change. Neither map is a graph red edge.');print([(len(x['X']),len(x['source_triples']),len(x['charts'])) for x in (old,new)],Counter(map(len,transport)),len(role));(Path(__file__).resolve().parents[1]/'results/ramsey_matrix_width_step.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
