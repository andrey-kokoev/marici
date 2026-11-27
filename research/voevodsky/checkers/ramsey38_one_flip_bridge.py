"""Relax append-only by one interior 2<->3 flip, with monotone endpoint additions otherwise."""
from itertools import combinations,permutations
from functools import lru_cache
from collections import Counter
from ramsey38_marked_failure_funnel import shared_index,candidates,p,P
from ramsey38_append_holdout import attaches
from ramsey38_compare_support_fillings import boundary


def run(temp_budget=0):
    assert temp_budget in (0,1,2)
    es=p.json.loads(P.read_text())['entries'];ids={e['record'] for e in es};words={}
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in ids:words[i]=line.strip()
            if i>=max(ids):break
    idx=shared_index();counts=Counter();gates=Counter();report=[]
    for e in es:
        g=p.graph(words[e['record']]);u=e['root'];L,rows,_,dec,stage,_=p.prepare(g,u);flips=[]
        for vs in map(frozenset,combinations(L,5)):
            for edge in map(frozenset,combinations(vs,2)):
                tri=vs-edge;two=frozenset(vs-{v} for v in edge);three=frozenset(vs-{v} for v in tri);flips.extend([(two,three,tri,edge),(three,two,edge,tri)])
        @lru_cache(None)
        def pool(req,bs):return frozenset(frozenset(ts) for bd in bs for ts in candidates(idx,L,req,set(map(dec,bd))))
        @lru_cache(None)
        def bridge(A,B,req):
            # Off-endpoint starting cell must be removed by the unique flip.
            gates['distinct_pair_and_support_queries']+=1
            for old,new,pivot,dual in flips:
                if not A-B<=old or len(old-(A|B))>temp_budget or not new<=B:continue
                gates['candidate_flips']+=1
                if any(dual<=t for t in A):continue
                gates['absent_dual']+=1
                @lru_cache(None)
                def search(M):
                    if old<=M and not any(pivot<=t for t in M-old):
                        gates['reachable_flip_sites']+=1;N=(M-old)|new
                        assert N<=B
                        missing=[s for s in req if not any(s<=t for t in N)]
                        if missing:gates['sites_losing_support']+=1
                        if not missing:
                            assert boundary(M)==boundary(N) and p.shelling(N);post=p.extend(N,B)
                            if post is not None:return (),p.faces(old),p.faces(new),[sorted(t) for t in post]
                            gates['no_completion']+=1
                    # Every temporary cell must be consumed by the sole flip.
                    for t in sorted((B|old)-M,key=sorted):
                        if not dual<=t and attaches(M,t):
                            ans=search(M|{t})
                            if ans:return (sorted(t),)+ans[0],*ans[1:]
                ans=search(A)
                if ans:return ans
        for a in p.setup(g,u)[2]:
            r,S=stage((a,))
            for b in p.setup(p.add(g,a),u)[2]:
                q,T=stage(tuple(sorted((a,b))))
                for j,k in permutations(rows,2):
                    starts=pool(r,tuple(S.get(frozenset([j]),())));ends=pool(q,tuple(T.get(frozenset([j,k]),())))
                    if not starts or not ends or any(A<B for A in starts for B in ends):continue
                    close=[(A,B) for A in starts for B in ends if len(A-B)==1];
                    if not close:continue
                    counts['requests']+=1;counts['nearest_pairs']+=len(close)
                    for A,B in sorted(close,key=lambda x:(p.faces(x[0]),p.faces(x[1]))):
                        ans=bridge(A,B,r)
                        if ans:
                            pre,old,new,post=ans
                            M=A
                            for t in map(frozenset,pre):assert t not in M and attaches(M,t);M=M|{t}
                            O,I=map(lambda side:frozenset(map(frozenset,side)),(old,new));N=(M-O)|I
                            assert O<=M and not I&M and len(M-(A|B))<=temp_budget and boundary(M)==boundary(N) and p.shelling(N)
                            assert all(any(s<=t for t in N) for s in r)
                            for t in map(frozenset,post):assert t not in N and attaches(N,t);N=N|{t}
                            assert N==B
                            counts['bridged']+=1;report.append(dict(record=e['record'],root=u,moves=[a,b],goal=[j,k],start=p.faces(A),end=p.faces(B),pre=pre,remove=old,insert=new,post=post));break
    assert counts['requests']==116;print(counts,gates,Counter((len(z['pre']),len(z['remove'])) for z in report));p.prev.save(p.prev.out/(f'ramsey38_flip_bridge_temp{temp_budget}_audit.json' if temp_budget else 'ramsey38_one_flip_bridge_gates.json'),dict(source_sha=p.prev.sha(P.read_bytes()),counts=dict(counts),gates=dict(gates),witnesses=report))
if __name__=='__main__':
    import sys
    run(int(sys.argv[1]) if len(sys.argv)>1 else 0)
