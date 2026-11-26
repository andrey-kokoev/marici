"""Detect an irreversible sign conflict in a PARTIAL link; compare with full S3 transport.
The artificial exterior vertex 0 caps the known boundary rim, not a Ramsey vertex.
"""
from collections import Counter,deque
from itertools import combinations
from ramsey38_signed_swap_transport import replay,setup,cf,json,boundary

def group(fs):
    faces=sorted(tuple(sorted(t)) for t in fs);adj={t:[] for t in faces}
    for a,b in combinations(faces,2):
        shared=set(a)&set(b)
        if len(shared)!=2:continue
        for f,g in ((a,b),(b,a)):
            new,=set(g)-shared;adj[f].append((g,tuple(g.index(v if v in shared else new) for v in f)))
    unseen=set(faces);groups=[]
    while unseen:
        start=min(unseen);q=deque([(start,0,(0,1,2))]);seen=set();returns=set()
        while q:
            t,l,p=q.popleft()
            if (t,l,p) in seen:continue
            seen.add((t,l,p));unseen.discard(t)
            if t==start:returns.add((l,p))
            for s,h in adj[t]:q.append((s,1-l,tuple(h[i] for i in p)))
        groups.append(returns)
    return groups

def conflict(groups):return any((l+sum(i>j for i,j in combinations(p,2)))%2 for G in groups for l,p in G)

def first_conflict(ts,rr,bd,cap):
    v=19;allf={s-{v} for s in ts if v in s};fixed={s-{v} for s in rr.values() if len(s)==4 and v in s};rim={f-{v}|{0} for f in bd if v in f} if cap else set();extra=sorted(allf-fixed,key=sorted)
    assert not conflict(group(fixed|rim));
    for k in range(len(extra)+1):
        bad=[ss for ss in combinations(extra,k) if conflict(group(fixed|rim|set(ss)))]
        if bad:return k,len(bad),[sorted(s) for s in bad[0]],len(extra)

def sig(ts,bd):
    fs={s-{19} for s in ts if 19 in s};cap={s-{19}|{0} for s in bd if 19 in s};G,=group(fs|cap)
    return sorted((l,''.join(map(str,p))) for l,p in G)
if __name__=='__main__':
    rr,bd=setup(5);cases=list(replay(rr,bd));assert len(cases)==4
    v=19;cap={f-{v}|{0} for f in bd if v in f};seed=frozenset((12,26,27));move=frozenset((4,26,27));assert seed|{v} in rr.values()
    cycle=(4,26,9,27,12);assert {f-{0} for f in cap}=={frozenset((x,cycle[i-1])) for i,x in enumerate(cycle)}
    assert all(move|{v} in ts for ts in cases) and conflict(group(cap|{seed,move})) and not conflict(group(cap|{seed})) and not conflict(group(cap|{move}))
    for ts in cases:
        print(len(ts),'tets; plain/capped min conflicts',first_conflict(ts,rr,bd,False),first_conflict(ts,rr,bd,True),'group',sig(ts,bd))
    good=list(map(frozenset,next(x for x in json.loads(cf.read_text())['certificates'] if x['record']==5 and x['root']==8)['actual_hidden']['24']));print('good group',sig(good,boundary(good)));assert not conflict(group({s-{19} for s in good if 19 in s}|{f-{19}|{0} for f in boundary(good) if 19 in f}))
