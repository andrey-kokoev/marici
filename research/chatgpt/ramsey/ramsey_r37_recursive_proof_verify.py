"""Independent standard-library verifier for the Ramsey(3,7) recursive proof.

Inputs: McKay's 16-vertex (3,6) graph6 catalogue, seven 17-vertex
(3,6) graph6 records, one or more 22-vertex (3,7) graph6 records, and
39 exact rational fractional-coverage certificates. Classification
COMPLETENESS is an external assumption, not derived by this script.

Example: python ramsey_r37_recursive_proof_verify.py \
  r36_16.g6.gz ramsey36_all7.g6 ramsey37_first5.g6 \
  ramsey_r37_full_catalogue_certificates.json
"""
from pathlib import Path
from collections import Counter
from itertools import combinations
import hashlib, gzip, json, sys

SHA16='5fd4e68d880e1d4ed05337b97cba0ce15387e1f545744aed80b91bb4b2186f25'


def graph6(line):
    line=line.strip()
    if line.startswith(b'>>graph6<<'):line=line[10:]
    n=line[0]-63
    assert n<63 and len(line)==1+(n*(n-1)//2+5)//6
    A=[0]*n
    for k,(i,j) in enumerate(( (i,j) for j in range(1,n) for i in range(j) )):
        if (line[1+k//6]-63) >> (5-k%6)&1:
            A[i]|=1<<j;A[j]|=1<<i
    return A


def independent_k(A,k):
    # Maximum independent set via memoized include/exclude bitset recursion.
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def maximum(candidates):
        if not candidates:return 0
        bit=candidates & -candidates
        v=bit.bit_length()-1
        rest=candidates-bit
        take=1+maximum(rest & ~A[v])
        if take>=k:return take
        return max(take,maximum(rest))
    return maximum((1<<len(A))-1)>=k


def triangle_free(A):
    return all((A[i]&A[j])==0 for i in range(len(A)) for j in range(i+1,len(A)) if A[i]>>j&1)


def independent_fives(A):
    return [sum(1<<i for i in C) for C in combinations(range(16),5)
            if all(not(A[i]>>j&1) for i,j in combinations(C,2))]


def verify_fractional(A,cert):
    assert len(A)==16 and sum(a.bit_count() for a in A)==66
    assert triangle_free(A) and not independent_k(A,6)
    F=independent_fives(A)
    W={int(k):v for k,v in cert['weights'].items()}
    assert set(W)<=set(F)
    assert all(isinstance(z,int) and z>0 for z in W.values())
    d=cert['denominator']
    assert 0<sum(W.values())<6*d
    for T in F:
        assert sum(w for I,w in W.items() if not (T&I))>=d
    return sum(W.values())/d


def main(p16,p17,p22,pcert):
    p16,p17,p22,pcert=map(Path,(p16,p17,p22,pcert))
    assert hashlib.sha256(p16.read_bytes()).hexdigest()==SHA16
    catalogue16=[line.strip() for line in gzip.open(p16,'rb') if line.strip()]
    assert len(catalogue16)==2576
    G16=[graph6(line) for line in catalogue16]
    assert all(len(A)==16 and triangle_free(A) and not independent_k(A,6) for A in G16)
    E=Counter(sum(x.bit_count() for x in A)//2 for A in G16)
    assert E=={32:5,33:39,34:200,35:547,36:803,37:634,38:275,39:62,40:11}
    records=json.loads(pcert.read_text())['records']
    assert len(records)==39
    D={rec['graph6'].encode():rec['cert'] for rec in records}
    R=[(line,A) for line,A in zip(catalogue16,G16) if sum(x.bit_count() for x in A)==66]
    assert len(R)==39 and set(D)=={line for line,A in R}
    weights=[verify_fractional(A,D[line]) for line,A in R]

    G17=[graph6(line) for line in p17.read_bytes().splitlines() if line.strip()]
    assert len(G17)==7
    assert all(len(A)==17 and triangle_free(A) and not independent_k(A,6) for A in G17)
    types=Counter((sum(x.bit_count() for x in A)//2,tuple(sorted(Counter(x.bit_count() for x in A).items()))) for A in G17)
    assert types=={
      (40,((4,5),(5,12))):2,
      (41,((4,3),(5,14))):3,
      (42,((4,1),(5,16))):2,
    }

    G22=[graph6(line) for line in p22.read_bytes().splitlines() if line.strip()]
    assert G22
    assert all(len(A)==22 and triangle_free(A) and not independent_k(A,7) and independent_k(A,6) for A in G22)
    print('16-vertex catalogue: 2576 all triangle-free/alpha<6; edge=33 precisely 39')
    print('All 39 fractional coverage inequalities: exact integer pass; max total',max(weights))
    print('17-vertex catalogue: 7 all triangle-free/alpha<6; degree distributions confirmed')
    print('22-vertex lower witnesses:',len(G22),'all triangle-free/alpha=6')
    print('COMPUTER-ASSISTED R(3,7)=23: verification conditions satisfied, assuming completeness of the 16- and 17-vertex classifications and the accompanying combinatorial argument')


if __name__=='__main__':
    if len(sys.argv)!=5:raise SystemExit('usage: verify.py r36_16.g6.gz ramsey36_all7.g6 ramsey37_first5.g6 full_certificates.json')
    main(*sys.argv[1:])
