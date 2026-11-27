"""8->9: compare two label-free transports BEFORE loading the 35-vertex constructor."""
from itertools import combinations,product
from pathlib import Path
import runpy,json
from collections import Counter
D=Path(__file__).resolve().parent

def cube(a):return set(product(*(range(i,i+2) for i in a)))
def mirror(r):return tuple(10-i for i in reversed(r))
def local(a,r):return tuple(i-j for i,j in zip(r,a))
def parity(a,r):return tuple((i-j)%2 for i,j in zip(r,(1,4,7)))
def signature(f):return ''.join(str(next(iter(s))) if len(s)==1 else '*' for s in map(set,zip(*f)))

def main():
    starts=[a for a in combinations(range(1,9),3) if min(a[1]-a[0],a[2]-a[1])>=3];assert starts==[(1,4,7),(1,4,8),(1,5,8),(2,5,8)]
    seen=set();patch=[]
    for a in starts:
        rows=cube(a);new=rows-seen;seen|=rows
        if a==starts[0]:continue
        assert len(new)==4;patch.extend([(a,new),(tuple(9-i for i in reversed(a)),set(map(mirror,new)))])
    out={}
    for rule in (local,parity):
        fs=[frozenset(rule(a,r) for r in fresh) for a,fresh in patch];assert all(len(f)==4 for f in fs);inter=Counter(len(f&g) for f,g in combinations(fs,2));out[rule.__name__]=dict(faces=list(map(signature,fs)),pairwise_intersections=dict(inter))
    # Preserve the SAME literal row on the overlap of the old cube and its neighbor?
    r=(1,4,8);out['shared_row']={f.__name__:[f(a,r) for a in starts[:2]] for f in (local,parity)}
    assert len(set(out['local']['faces']))==6 and len(set(out['parity']['faces']))==3
    F=[frozenset(local(a,r) for r in rows) for a,rows in patch];corners=set.union(*(set(s) for s in F));pairs={f&g for f,g in combinations(F,2) if f&g};assert len(pairs)==12 and all(len(p)==2 for p in pairs)
    core={signature(c) for c in [*F,*pairs,*[(v,) for v in corners]]};assert len(core)==26
    g=runpy.run_path(str(D/'ramsey_cube_construct35.py'));assert core==set(g['cells']);checks=0
    for i,s in enumerate(g['cells']):
        expected={''.join(map(str,v)) for v in corners if all(x=='*' or x==str(b) for x,b in zip(s,v))};actual={v for j,v in enumerate(g['corner'],26) if g['G'][i]>>j&1};assert actual==expected;checks+=len(actual)
    out['matched_core_to_newcomer_red_incidences']=checks;assert checks==56;print(json.dumps(out,indent=2));dest=D.parent/'results/ramsey_excel_successor_chart_audit.json';text=json.dumps(out,indent=2)+'\n';assert not dest.exists() or dest.read_text()==text;dest.write_text(text)
if __name__=='__main__':main()
