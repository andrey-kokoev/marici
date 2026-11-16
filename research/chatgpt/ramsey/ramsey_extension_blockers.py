"""Test independent-transversal obstructions on extremal R(3,k) graphs.

Usage: python ramsey_extension_blockers.py r37_22.g6 7
       python ramsey_extension_blockers.py r36_17.g6 6
Input: McKay's public graph6 files; use k=6 or k=7.

For each extremal (3,k)-graph H, a new red neighborhood S must be
independent, and must intersect every independent (k-1)-set.
The bound R(3,k-1) forces |S| >= |V(H)|-R(3,k-1)+1.
A blocking witness is an independent (k-1)-set T disjoint from S.
A greedy cover selects T's such that every candidate S is blocked.
The greedy cover is NOT claimed to be minimum or uniform.
"""
import sys


def parse_g6(line):
    b = line.strip().encode('ascii')
    if not b or b.startswith(b'>>'):
        raise ValueError('Expected one standard graph6 line')
    n = b[0] - 63
    if not 0 <= n <= 62:
        raise ValueError('Only short graph6 format supported')
    bits = []
    for c in b[1:]:
        x = c - 63
        bits.extend((x >> j) & 1 for j in range(5, -1, -1))
    if len(bits) < n*(n-1)//2:
        raise ValueError('Truncated graph6 line')
    A = [0]*n
    p=0
    for j in range(1,n):
        for i in range(j):
            if bits[p]:
                A[i] |= 1<<j
                A[j] |= 1<<i
            p+=1
    return A


def independent_sets(A,k):
    n=len(A); results=[]
    def go(S, available, remaining):
        if remaining==0:
            results.append(S)
            return
        while available.bit_count() >= remaining:
            bit=available & -available
            available-=bit
            u=bit.bit_length()-1
            go(S|bit, available & ~A[u], remaining-1)
    go(0,(1<<n)-1,k)
    return results


def greedy_certificate(A,k):
    n=len(A)
    r_previous={6:14,7:18}[k]
    min_size=n-r_previous+1
    if (k,n) not in [(6,17),(7,22)]: raise ValueError('Expected (k,n)=(6,17) or (7,22)')
    # Triangle-free test.
    for i in range(n):
        for j in range(i+1,n):
            if (A[i]>>j)&1 and (A[i]&A[j]):
                raise ValueError('Triangle detected')
    if independent_sets(A,k):
        raise ValueError('Forbidden independent k-set detected')
    groups={q:independent_sets(A,q) for q in range(min_size,k)}
    full=groups[k-1]
    candidates=[s for q in sorted(groups) for s in groups[q]]
    universe=(1<<len(candidates))-1
    blockers=[]
    for t in full:
        covered=0
        for i,s in enumerate(candidates):
            if not (t&s):
                covered|=1<<i
        blockers.append(covered)
    picked=[]
    while universe:
        j=max(range(len(full)), key=lambda j:(universe & blockers[j]).bit_count())
        score=(universe & blockers[j]).bit_count()
        if score==0: raise AssertionError('Found extendible neighborhood')
        picked.append(full[j]); universe &= ~blockers[j]
    # Exact verification of every admissible neighborhood being blocked.
    assert all(any(not (s&t) for t in picked) for s in candidates)
    return {q:len(groups[q]) for q in groups},picked


def vertices(mask,n=22):
    return [i for i in range(n) if mask>>i&1]


def main(path,k):
    with open(path,encoding='ascii') as f:
        lines=[line.strip() for line in f if line.strip()]
    covers=[]
    for i,line in enumerate(lines,1):
        A=parse_g6(line)
        counts,cert=greedy_certificate(A,k)
        covers.append(len(cert))
        print(f'{i:3d}: E={sum(a.bit_count() for a in A)//2:2d} '
              f'I={counts} greedy_cover={len(cert):2d}')
        if i==1: print('  first certificate:',
                       [vertices(s,n=len(A)) for s in cert])
    print('SUMMARY:',len(lines),'graphs; greedy cover sizes:',
          {k:covers.count(k) for k in sorted(set(covers))})
    expected={6:7,7:191}[k]
    if len(lines)==expected:
        print(f'FULL {expected}-GRAPH INPUT TESTED. No one-vertex extension.')
    else:
        print('PARTIAL SAMPLE: do not infer full-catalogue results.')


if __name__=='__main__':
    if len(sys.argv)!=3 or sys.argv[2] not in ('6','7'): raise SystemExit(__doc__)
    main(sys.argv[1],int(sys.argv[2]))
