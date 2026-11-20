"""Test frozen offsets and a certified quotient lift. No offset search."""
from itertools import combinations
from pauli_realization_audit import independent_witness,triangle_free
OFF=({-3,-1,1,3},{-4,-1,1,4},{-3,3})

def graph(n,mod):
    sets=[{x%mod for x in ds} for ds in OFF]
    return [sum(1<<j for j in range(2*n) if i!=j and (j%n-i%n)%mod in sets[i//n if i//n==j//n else 2]) for i in range(2*n)]

def main():
    base=graph(11,11);assert triangle_free(base) and independent_witness(base,7) is None and independent_witness(base,6) is not None
    for k in range(8,21):
        n=2*k-3;rows=graph(n,n);w=list(range(0,n-3,2))+[n,n+2,n+8];assert len(w)==k and all(not (rows[i]>>j&1) for i,j in combinations(w,2))
    # Check all edges in the first nontrivial periodic lift against projection.
    n=22;rows=graph(n,11);proj=lambda v:(v//n)*11+(v%n)%11
    assert all((rows[i]>>j&1)==(base[proj(i)]>>proj(j)&1) for i,j in combinations(range(2*n),2));assert triangle_free(rows)
    print('Base alpha=6; frozen-offset obstructions verified for k=8..20; 44-vertex quotient lift verified.')

if __name__=='__main__':main()
