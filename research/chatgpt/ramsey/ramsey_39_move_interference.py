"""Relax only three-move triangle clauses for balanced sets; screen one-defect representatives."""
from ramsey_39_twelve_order_sat import *
from ast import literal_eval
from ramsey_39_degree_budget_sample import deficiency,B
D=Path(__file__).parent;mode=sys.argv[1];pair=mode=='pair';prefix='balanced' if pair else 'one_defect';masks=(D/f'ramsey_39_{prefix}_masks.txt').read_text().split();path=D/f'ramsey_39_{mode}_screen.json';results=json.loads(path.read_text()) if path.exists() else {};end=monotonic()+float(sys.argv[2]);
for m in masks:
    if m in results:continue
    W=[i for i in range(39) if int(m)>>i&1]
    if not pair:
        h=Counter((a+b)%39 for a in W for b in W);caps=tuple(sorted(min(9,2*x) for x in h.values()))
        if not deficiency(caps,338):results[m]={'status':'deficiency obstruction'};continue
    floors=None
    if not pair:
        score=lambda d:2*(d*d+B[d])-39*d
        cap=[min(9,2*h[p]) for p in range(39)];mins=[min(score(d) for d in range(3,c+1)) for c in cap];total=sum(mins)
        floors=[min(d for d in range(3,c+1) if total-mn+score(d)<=0) for c,mn in zip(cap,mins)]
    result=test(W,degree_budget=True,pair_only=pair,degree_floors=floors);r={'status':result.split(':')[0]}
    if result.startswith('candidate'):
        es=list(combinations(W,2));rim=[es[i-1] for i in literal_eval(result.split(':')[1])];sources=defaultdict(set)
        for a,b in rim:
            for t in W:sources[tuple(sorted(((a+t)%39,(b+t)%39)))].add((a,b))
        tri=next((U for U in combinations(range(39),3) if all(e in sources for e in combinations(U,2))),None);r.update(rim=rim,edges=len(sources),triangle=tri)
        if tri:r['sources']=[sorted(sources[e]) for e in combinations(tri,2)]
    results[m]=r
    if len(results)%50==0:path.write_text(json.dumps(results))
    if monotonic()>=end:break
path.write_text(json.dumps(results));print(mode,len(results),'of',len(masks),Counter(r['status'] for r in results.values()));print(next((r for r in results.values() if 'rim' in r),None))
