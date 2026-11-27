"""Geometry-first census: all shellable endpoints on <=7 labels, through 12 tetrahedra, modulo relabeling."""
from itertools import permutations,combinations,product
from collections import Counter,defaultdict
from functools import lru_cache
from ramsey38_shared_peel_trial import Peeler
from ramsey38_compare_support_fillings import boundary
from ramsey38_nested_ball_obstruction_trial import prev,faces,shelling,extend

def run(limit=12, audit_greedy=False, representatives=None):
    p=Peeler(True);ts=p.ts;bits={t:1<<i for i,t in enumerate(ts)};verts=list(range(7));edges=list(map(frozenset,combinations(verts,2)));tri=list(map(frozenset,combinations(verts,3)));car=lambda s:sum(b for t,b in bits.items() if s<=t);ec=[car(e) for e in edges];fc=[car(f) for f in tri];rimfac=[[c for f,c in zip(tri,fc) if e<=f] for e in edges];vc=[car({v}) for v in verts];ALL=(1<<35)-1
    @lru_cache(None)
    def canonical(m):
        groups=defaultdict(list)
        for v,cv in zip(verts,vc):groups[((cv&m).bit_count(),tuple(sorted((m&c).bit_count() for e,c in zip(edges,ec) if v in e)))].append(v)
        gs=[groups[k] for k in sorted(groups)];cand=[t for t,b in bits.items() if m&b];best=None
        for g in product(*(permutations(s) for s in gs)):
            ix={v:i for i,v in enumerate(sum(g,()))};y=sum(bits[frozenset(ix[v] for v in t)] for t in cand);best=y if best is None else min(best,y)
        return best
    def legal(m,i):
        adj,rules=p.tab[i];k=0
        for j,a in enumerate(adj):
            h=m&a
            if h&(h-1):return False
            if h:k|=1<<j
        return not rules[k]&m
    def tet(m):return frozenset(t for t,b in bits.items() if m&b)
    @lru_cache(maxsize=400000)
    def interior(m):return any(m&c and not any((m&f).bit_count()==1 for f in fs) for c,fs in zip(ec,rimfac))
    layer={canonical(1)};counts=[];obs=[];greedy_counts=Counter();unsafe=[]
    for n in range(1,limit+1):
        nxt=set();cnt=Counter(endpoints=len(layer))
        for B in sorted(layer):
            # Inspect only subballs containing an interior edge. Reverse reachability is
            # not used in eligibility. Greedy failure is never counted as a trap.
            if representatives is not None:representatives.append(B)
            sub=(B-1)&B if representatives is None else 0;candidates=[]
            while sub:
                if interior(sub) and p.peel(sub,sub):candidates.append(sub)
                sub=(sub-1)&B
            cnt['edge_subballs']+=len(candidates)
            if candidates:
                seen={B};stack=[B]
                while stack:
                    m=stack.pop();q=m
                    while q:
                        b=q&-q;q^=b;r=m^b
                        if r and r not in seen and legal(r,b.bit_length()-1) and p.peel(r,r):seen.add(r);stack.append(r)
                for A in candidates:
                    if A in seen:continue
                    cnt['traps']+=1;immediate=not any(legal(A,i) for i in range(35) if (B^A)>>i&1);cnt['immediate']+=immediate;T,U=tet(A),tet(B);assert shelling(T) and shelling(U) and extend(T,U) is None;obs.append(dict(start=faces(T),end=faces(U),immediate=immediate))
            if audit_greedy and candidates:
                # Increasing size is a topological order. A start is safe for arbitrary
                # choices iff it has successors and every successor is safe.
                safe={B};eligible=set(candidates)|{B}
                for A in sorted(candidates,key=int.bit_count,reverse=True):
                    successors=[A|(1<<i) for i in range(35) if (B^A)>>i&1 and legal(A,i)]
                    assert set(successors)<=eligible
                    if successors and all(s in safe for s in successors):safe.add(A)
                    else:unsafe.append(dict(start=faces(tet(A)),end=faces(tet(B)),extendible=A in seen,options=[sorted(ts[(s^A).bit_length()-1]) for s in successors]))
                    greedy_counts['transitions']+=len(successors);greedy_counts['starts']+=1;greedy_counts['all_choices_safe']+=A in safe
            if n<limit:
                for i in range(35):
                    if not B>>i&1 and legal(B,i):nxt.add(canonical(B|1<<i))
            if limit==35 and n>=12:
                from ramsey38_append_holdout import attaches
                U=tet(B)
                assert all(legal(B,i)==bool(attaches(U,t)) for i,t in enumerate(ts) if t not in U)
        print(n,dict(cnt),flush=True);counts.append(dict(size=n,**cnt));layer=nxt
        if not nxt:break
    if representatives is not None:
        assert limit==35 and n<limit and not layer
        return
    if audit_greedy:
        assert limit==35 and n<limit and not layer
        prev.save(prev.out/'ramsey38_forward_greedy_closure.json',dict(counts=dict(greedy_counts),unsafe=unsafe));print(greedy_counts,len(unsafe));return
    if limit==35:
        assert n<limit and not layer
        prev.save(prev.out/'ramsey38_interior_edge_trap_closure.json',dict(max_cells=n,first_empty_layer=n+1,counts=counts,traps=obs))
    else:prev.save(prev.out/'ramsey38_interior_edge_trap_census.json',dict(max_cells=limit,counts=counts,traps=obs))
if __name__=='__main__':
    import sys
    run(35 if set(sys.argv)&{'--closure','--greedy'} else 12,'--greedy' in sys.argv)
