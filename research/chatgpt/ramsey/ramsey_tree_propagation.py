"""Seed-only matrix deductions. No SAT library. Counts relaxed signed cases."""
from itertools import combinations
from collections import Counter
from ramsey_matrix_zero import matrices,orbit_table


def main():
    stats=Counter();res=[]
    for B in matrices(None):
        Bt=[sum(1<<i for i,m in enumerate(B) if m>>j&1) for j in range(14)]
        rt,re,tr=orbit_table(B,True);ct,ce,tc=orbit_table(Bt)
        # Relax: allow every Gram-compatible row edge simultaneously.
        hits=set()
        for k in (2,4):
            for I in combinations(range(8),k):
                if re(I):continue
                neighbors=0
                for i in I:neighbors |= B[i]
                for J in combinations([j for j in range(14) if not neighbors>>j&1],7-k):hits.add(ce(J))
        hits=sorted(hits,key=int.bit_count);on=off=0
        def force():
            nonlocal on,off
            while True:
                old=(on,off)
                for h in hits:
                    if h&on:continue
                    x=h&~off
                    if not x:return False
                    if x.bit_count()==1:on|=x
                for t in tc:
                    x=t&~on
                    if not x:return False
                    if x.bit_count()==1:off|=x
                if off&on:return False
                if old==(on,off):return True
        if not force():
            stats['no candidate edge' if 0 in hits else 'contradiction after deduction']+=1
            continue
        def defects(i):return sum(set(ct.get((2*a,2*b+h),0) for a,b in [(3,4),(i,3),(i,4)] for h in (0,1)))&~off
        rr=[(i,j) for i,j in combinations(range(6),2) if i//2!=j//2 and (i,j) in rt]
        defects_ab=[defects(i) for i in [0,1]]
        stats['tree certified' if not rr and min(defects_ab)==0 else 'undecided']+=1
        res.append((B,rr,[x.bit_count() for x in defects_ab]))
    assert sum(stats.values())==256 and stats['tree certified']==4 and not stats['undecided']
    assert Counter(tuple(c) for B,r,c in res)=={(0,3):2,(3,0):2}
    print(stats);print('surviving shapes',Counter((len(r),tuple(c)) for B,r,c in res));return res

if __name__=='__main__':main()
