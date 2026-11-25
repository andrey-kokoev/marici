"""Test common-port choices for fixed exclusive attachments at t=3. No solver required."""
from itertools import product
from ramsey310_matching_sides import F,sets,bits,instances,decode,side
from pathlib import Path
from collections import Counter
import json,sys

def joint(A,E,deep=True):
    C=list(sets(A,F,7));need=[9-a.bit_count()-sum(s>>i&1 for s in E) for i,a in enumerate(A)]
    if min(need)<1 or max(need)>6:return 'coverage'
    sing=sum(1<<i for i,k in enumerate(need) if k==1)
    gap=[F&~(a|b|c) for a,b,c in product(*zip(E[:3],E[3:]))]
    if any((sing&g).bit_count()>6 for g in gap):return 'singletons'
    if not deep:return 'local_pass'
    # A common support cannot assign two singleton vertices to the same
    # transversal gap. Also exclude any independent set already extendible
    # to nine with the exclusive vertices and disjoint from this support.
    cand=[s for s in C if all((s&sing&g).bit_count()<=1 for g in gap)]
    for k in (7,6):
        for t in sets(A,F,k):
            both=sum(bool(t&a and t&b) for a,b in zip(E[:3],E[3:]))
            if k+3-both>=9:cand=[s for s in cand if s&t]
    inc=[sum(1<<i for i,s in enumerate(cand) if s>>v&1) for v in range(26)]
    if any(m.bit_count()<n for m,n in zip(inc,need)):return 'support_shortage'
    # Every independent T imposes a miss budget: |T| + (3-both) + misses <= 9.
    lim=[]
    for k in range(1,8):
        for t in sets(A,F,k):
            cap=6-k+sum(bool(t&a and t&b) for a,b in zip(E[:3],E[3:]))
            assert cap>=0
            if cap<6:lim.append((t,cap))
    # For each support a bit set per budget of the constraints it misses.
    def rec(pool,rows,needs):
        left=6-len(rows)
        if not left:return rows if not any(needs) else None
        for v,x in enumerate(needs):
            if x<0 or x>left:return None
            if x==0:pool &= ~inc[v]
            if x==left:pool &= inc[v]
        if pool.bit_count()<left:return None
        opts=pool
        for v,x in enumerate(needs):
            if x:
                b=pool&inc[v]
                if b.bit_count()<x:return None
                if b.bit_count()<opts.bit_count():opts=b
        for i in bits(opts):
            pool ^= 1<<i;s=cand[i];new=rows+[s]
            if any((s&r).bit_count()>4 for r in rows):continue
            if any(not t&s and sum(not t&r for r in new)>cap for t,cap in lim):continue
            ans=rec(pool,new,[x-(s>>v&1) for v,x in enumerate(needs)])
            if ans:return ans
        return None
    ans=rec((1<<len(cand))-1,[],need)
    return {'common':ans,'exclusive':E} if ans else 'joint_failure'

if __name__=='__main__':
    src=Path(__file__).resolve().parents[1]/'results/ramsey38_26_e73_hog.g6';lim=int(sys.argv[1]);start=int(sys.argv[2]);stop=int(sys.argv[3]);
    for n,line in enumerate(src.read_bytes().splitlines(),1):
        if not start<=n<=stop:continue
        A=next(instances(decode(line)));hist=Counter();seen=0;witness=[]
        def test(E):
            global seen
            # Cheap test before building the costly common-support index.
            if any(9-a.bit_count()-sum(s>>i&1 for s in E)<1 for i,a in enumerate(A)):tag='coverage'
            else:tag=joint(A,E)
            if isinstance(tag,dict):witness.append(tag);return True
            hist[tag]+=1;seen+=1;return seen>=lim
        capacity_first='cap' in sys.argv;stopped=side(A,True,test,cap=capacity_first);print(json.dumps(dict(parent=n,tested=seen,capacity_first=capacity_first,exhausted=not stopped,counts=dict(hist),witness=witness)),flush=True)
