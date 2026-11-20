"""Target-only two-ring construction. No catalogue, witness order or offset input.
Bound from R(3,k)<=binom(k+1,2). Output first witness at largest order in the model.
Centered reflection on both rings. Standard library only.
"""
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path
import sys
from pauli_realization_audit import triangle_free, independent_witness


def find(k, probe_factory=None, write_csv=True):
    for n in range((comb(k+1,2)-1)//2,0,-1):
        full=(1<<n)-1
        def rot(m,i):return ((m<<i)|(m>>(n-i)))&full
        def sets(zero):
            S=[0]
            for j in range(0 if zero else 1,n//2+1):
                pair=1<<j|1<<((-j)%n);S.extend([m|pair for m in S])
            return sorted(S,key=lambda x:(x.bit_count(),x))
        internal=[]
        for a in sets(False):
            r=[rot(a,i) for i in range(n)]
            if a.bit_count()<k and triangle_free(r) and independent_witness(r,k) is None:internal.append((a,r))
        offsets=[(d,[rot(d,i) for i in range(n)]) for d in sets(True) if d.bit_count()<k]
        probe = probe_factory(n, offsets) if probe_factory is not None else None
        checked=0
        for (a,ra),(b,rb) in combinations_with_replacement(internal,2):
            for d,rd in offsets:
                if max(a.bit_count(),b.bit_count())+d.bit_count()>=k:continue
                if (probe(a|b,d,rd) if probe is not None else any((a|b)>>j&1 and (d&rd[j]) for j in range(n))):continue
                rows=[x|(y<<n) for x,y in zip(ra,rd)]+[y|(x<<n) for x,y in zip(rb,rd)];checked+=1
                # Translation carries a vertex of any independent set to one of these roots.
                if any(independent_witness(rows,k-1,((1<<(2*n))-1)&~(rows[v]|1<<v)) is not None for v in (0,n)):continue
                assert triangle_free(rows) and independent_witness(rows,k) is None
                print('k,n',k,n,'offsets',[[i for i in range(n) if m>>i&1] for m in (a,b,d)],flush=True)
                if write_csv:
                    Path(__file__).with_name(f'ramsey_3_{k}_target_two_rings_{2*n}.csv').write_text(''.join(','.join(str(row>>j&1) for j in range(2*n))+'\n' for row in rows))
                return rows
        print('excluded ring size',n,'tables after pruning',checked,flush=True)

if __name__=='__main__':find(int(sys.argv[1]))
