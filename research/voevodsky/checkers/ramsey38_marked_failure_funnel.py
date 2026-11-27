"""Where do legal two-edit, two-edge requests fail on the outcome-blind index holdout?"""
from collections import Counter
from functools import lru_cache
from itertools import permutations
from ramsey38_boundary_ball_index import candidates,shared_index,p
from ramsey38_boundary_index_holdout import P


def run():
    es=p.json.loads(P.read_text())['entries'];ids={e['record'] for e in es};words={}
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in ids:words[i]=line.strip()
            if i==max(ids):break
    idx=shared_index();tot=Counter();roots=Counter();dist=Counter();report=[]
    levels=['no compatible boundaries','empty first filler pool','empty final filler pool','both filler pools empty','no strict containment','route']
    # Root classes combine empty-pool categories; they are not ordered relative to one another.
    for e in es:
        g=p.graph(words[e['record']]);u=e['root'];L,rows,_,dec,stage,_=p.prepare(g,u);cnt=Counter();best=None;nearest=None;pairs=set()
        @lru_cache(None)
        def pool(req,bs):return {frozenset(ts) for bd in bs for ts in candidates(idx,L,req,set(map(dec,bd)))}
        for a in p.setup(g,u)[2]:
            r,S=stage((a,))
            for b in p.setup(p.add(g,a),u)[2]:
                q,T=stage(tuple(sorted((a,b))))
                for j,k in permutations(rows,2):
                    src=S.get(frozenset([j]),());dst=T.get(frozenset([j,k]),());n=0
                    if src and dst:
                        starts=pool(r,tuple(src));ends=pool(q,tuple(dst));n=(4 if starts and ends else 2 if starts else 1 if ends else 3)
                        if n==4:
                            nested={(A,B) for A in starts for B in ends if A<B}
                            if nested:pairs.update(nested);n=5
                            else:
                                A,B=min(((A,B) for A in starts for B in ends),key=lambda z:(len(z[0]-z[1]),len(z[1]-z[0]),p.faces(z[0]),p.faces(z[1])))
                                score=(len(A-B),len(B-A));dist[score[0]]+=1
                                if best is None or score<best:best=score;nearest=dict(moves=[a,b],goal=[j,k],start=p.faces(A),end=p.faces(B),remove=p.faces(A-B),add=p.faces(B-A))
                    cnt[levels[n]]+=1
        root='route' if pairs else 'no strict containment' if cnt[levels[4]] else 'empty filler pool' if any(cnt[s] for s in levels[1:4]) else levels[0];tot.update(cnt);roots[root]+=1;report.append(dict(record=e['record'],root=u,category=root,pairs=len(pairs),counts=dict(cnt),nearest_miss=nearest))
    expected=p.json.loads((p.prev.out/'ramsey38_boundary_index_holdout.json').read_text());assert sum(e['pairs'] for e in report)==expected['pairs'] and roots['route']==expected['roots_with_routes'];print(tot,roots,dist);p.prev.save(p.prev.out/'ramsey38_marked_failure_funnel.json',dict(source_sha=p.prev.sha(P.read_bytes()),counts=dict(tot),roots=dict(roots),minimum_removals=dict(dist),details=report))
if __name__=='__main__':run()
