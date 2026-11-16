"""Screen the complete McKay (3,6;16) catalogue for a six-port obstruction.

Usage:
    python ramsey_six_port_catalogue_check.py r36_16.g6.gz

The catalogue at https://users.cecs.anu.edu.au/~bdm/data/ramsey.html
contains 2,576 nonisomorphic (3,6;16) graphs. This program checks the
STRONG conjecture that no relevant 16-vertex graph has six distinct,
pairwise rank-5-compatible independent five-sets. It flags repeated-row
exceptions instead of silently declaring the strong conjecture proved.

No catalogue-run result is asserted in this file.
"""
from itertools import combinations
import gzip, sys


def decode_g6(line):
    s = line.strip()
    if s.startswith(b'>>graph6<<'):
        s = s[len(b'>>graph6<<'):]
    if not s:
        return None
    vals = [c - 63 for c in s]
    if vals[0] >= 63:
        raise ValueError('Only short graph6 files supported')
    n = vals[0]
    A = [0]*n
    bits = [((x >> shift) & 1) for x in vals[1:] for shift in range(5,-1,-1)]
    assert len(bits) >= n*(n-1)//2
    k = 0
    for j in range(1,n):
        for i in range(j):
            if bits[k]:
                A[i] |= 1 << j
                A[j] |= 1 << i
            k += 1
    return A


def indep5(H):
    out=[]
    for C in combinations(range(len(H)),5):
        if all(not (H[u] >> v & 1) for u,v in combinations(C,2)):
            out.append(sum(1<<u for u in C))
    return out


def clique_witness(K, r):
    def run(av,found):
        if len(found)==r:
            return found
        while av.bit_count()>=r-len(found):
            b = av & -av
            v = b.bit_length()-1
            av ^= b
            ans = run(av & K[v], found+[v])
            if ans is not None:return ans
        return None
    return run((1<<len(K))-1, [])


def examine(H):
    F=indep5(H)
    D=[sum(1<<j for j,b in enumerate(F) if (a&b)==0) for a in F]
    K=[0]*len(F)
    for i,j in combinations(range(len(F)),2):
        if (D[i]&D[j])==0:
            K[i] |= 1<<j
            K[j] |= 1<<i
    witness=clique_witness(K,6)
    return len(F), witness, sum(d==0 for d in D),F


def main(path):
    counts={'all':0,'33edges':0,'relevant':0,'six_cliques':0,'self_compatible':0}
    opening=gzip.open if path.endswith('.gz') else open
    with opening(path,'rb') as f:
        for raw in f:
            H=decode_g6(raw)
            if H is None:continue
            counts['all']+=1
            assert len(H)==16
            if sum(x.bit_count() for x in H)!=66:continue
            counts['33edges']+=1
            if not all(2<=x.bit_count()<=5 for x in H):continue
            counts['relevant']+=1
            assert all((H[u]&H[v])==0 for u in range(16)
                       for v in range(u+1,16) if H[u]>>v&1)
            nF,W,nself,F=examine(H)
            if nself:
                counts['self_compatible']+=1
            if W is not None:
                counts['six_cliques']+=1
                print('SIX-CLIQUE COUNTEREXAMPLE:',raw.strip().decode(),
                      'I5-neighborhoods:', [F[i] for i in W])
    print('Catalogue counts:',counts)
    if counts['all']!=2576:
        print('WARNING: input was not the complete expected catalogue')
    if counts['six_cliques'] == 0 and counts['self_compatible'] == 0 and counts['all']==2576:
        print('CERTIFIED: all relevant H exclude six compatible port neighborhoods')
    else:
        print('NO universal exclusion asserted; inspect exceptions and coverage')

if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit('Usage: python ramsey_six_port_catalogue_check.py r36_16.g6.gz')
    main(sys.argv[1])
