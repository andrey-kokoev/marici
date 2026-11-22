"""Fresh generated cores (no catalogue or previously tuned core). Screen 4 maximal independent ports at k=alpha+2 >=5. Verify one counterexample exhaustively, reporting witnesses for every screen survivor."""
from itertools import combinations,combinations_with_replacement
from random import Random
from collections import Counter
from ramsey_fork_audit_uniform import inds,D,json

def test(H):
    I=inds(H);k=max(map(int.bit_count,I))+2
    if k<5:return 'out_of_scope'
    M=[s for s in I if all(s>>v&1 or s&r for v,r in enumerate(H))];rows={t:[s for s in I if s.bit_count()==t] for t in [k-2,k-3,k-4]};miss={s:{t:sum(1<<i for i,r in enumerate(T) if not s&r) for t,T in rows.items()} for s in M};cnt=Counter();sur=[]
    for q in combinations_with_replacement(M,4):
        if any(miss[a][k-2]&miss[b][k-2] for a,b in combinations(q,2)):continue
        if any(r.bit_count()+sum(s>>v&1 for s in q)>=k for v,r in enumerate(H)):continue
        for t in (k-3,k-4):
            w=next((m for p in combinations(q,k-t) if (m:=intersect(miss[s][t] for s in p))),0)
            if w:cnt[t]+=1;sur.append(dict(ports=q,missed=rows[t][(w&-w).bit_length()-1]));break
        else:return 'verified_extension'
    if sur:return dict(core=H,k=k,maximal=M,counts=cnt,survivors=sur)
    return 'screen_reject'

def intersect(it):
    a=next(it)
    for b in it:a&=b
    return a

def run():
    rng=Random(20261122);count=0;stats=Counter();seen=set()
    for n in range(4,17):
        for trial in range(300):
            H=[0]*n;edges=list(combinations(range(n),2));rng.shuffle(edges)
            for x,y in edges:
                if not H[x]&H[y] and rng.random()<0.65:H[x]|=1<<y;H[y]|=1<<x
            key=tuple(H)
            if key in seen:continue
            seen.add(key);count+=1;r=test(H)
            if isinstance(r,dict):return dict(tested=count,**r)
            stats[r]+=1
    targets={}
    for name in ['r34_8','r35_13','r36_17']:
        counts=Counter()
        for record,line in enumerate((D/'pauli-realization-catalogues'/f'{name}.g6').read_bytes().splitlines(),1):
            n=line[0]-63;H=[0]*n
            for t,(v,u) in enumerate((v,u) for u in range(n) for v in range(u)):
                if (line[1+t//6]-63)>>(5-t%6)&1:H[u]|=1<<v;H[v]|=1<<u
            r=test(H)
            if isinstance(r,dict):return dict(random_stats=stats,target=name,record=record,**r)
            counts[r]+=1
        targets[name]=counts
    return dict(random_stats=stats,targets=targets)
if __name__=='__main__':
    out=run();print({k:v for k,v in out.items() if k!='survivors'},out.get('survivors',[])[:1]);(D/'ramsey_capacity_fresh_falsifier.json').write_text(json.dumps(out)+'\n')
