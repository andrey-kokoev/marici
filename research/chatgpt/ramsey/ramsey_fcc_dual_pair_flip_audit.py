"""Distinguish root steps, rechartings, and the octahedron-local complement on the FCC receipt."""
from itertools import combinations,product
from pathlib import Path
import json

def main():
    d=json.loads((Path(__file__).resolve().parents[2]/'strominger/results/fcc-first-transport.json').read_text());cells={}
    for rec in d['coarse_cells']:
        if not rec['id'].startswith('oct-'):continue
        V=list(map(tuple,rec['vertices']));b=tuple(map(min,zip(*V)));cells[b]={v:frozenset(i for i in range(4) if v[i]-b[i]) for v in V};assert set(cells[b].values())==set(map(frozenset,combinations(range(4),2)))
    U=frozenset(range(4));pairs=[(s,U-s) for s in cells[next(iter(cells))].values() if 0 in s];pairs.sort(key=lambda p:sorted(p[0]));faces=[set(f) for f in product(*pairs)]
    perms=[a['permutation'] for a in d['frame_actions']];pure=set();actions=set();star=lambda f:bool(set.intersection(*map(set,f)))
    for p in perms:
        act=lambda s:frozenset(p[i] for i in s);actions.add(tuple(act(s) for pair in pairs for s in pair));assert all(star(f)==star({act(s) for s in f}) for f in faces)
        if all(act(s) in pair for pair in pairs for s in pair):pure.add(tuple(int(act(s)!=s) for s,_ in pairs))
    assert len(actions)==24 and pure=={q for q in product(range(2),repeat=3) if sum(q)%2==0}
    assert all(star(f)!=star({U-s for s in f}) for f in faces)
    by_id={v['id']:tuple(v['barycentric']) for v in d['vertices']};moves={(by_id[m['source']],*m['sector']):by_id[m['target']] for m in d['directed_moves']};steps=0;opposites={}
    for b,C in cells.items():
        for v,s in C.items():opposites.setdefault(v,set()).add(next(w for w,t in C.items() if t==U-s))
        for i,j in product(range(4),repeat=2):
            if i==j:continue
            if not all((v,i,j) in moves for v in C):continue
            b2=tuple(x+(h==j)-(h==i) for h,x in enumerate(b));assert b2 in cells and all(cells[b2][moves[v,i,j]]==s for v,s in C.items());steps+=1
    print('octahedra',len(cells),'whole-cell root transports',steps,'all preserve local 2-subset labels');print('frame pure flips',sorted(pure),'frame actions',len(actions));print('sites with multiple local opposites',sum(len(s)>1 for s in opposites.values()));print('with complement',sorted(pure|{tuple(1-x for x in m) for m in pure}))
if __name__=='__main__':main()
