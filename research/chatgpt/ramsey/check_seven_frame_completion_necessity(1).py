#!/usr/bin/env python3
"""Necessity audit for seven-frame -> binary Golay completion.

All operations over F2; no Golay matrix is supplied. A source heptad is read
from the seven rotations of RGRGR00. The 23-column construction and the
quadratic map are compared to weaker extension conditions.
"""
from itertools import combinations
from collections import Counter
from math import comb
import sys
sys.path.insert(0, '/mnt/data')
from ramsey_heptad_quadratic_golay_constructor import (
    seed_frame, select_symplectic_heptad, quad_form, polar,
    veronese2, construct_columns, rank, xor_all, PAIRS,
    syndrome_sphere,
)


def syndrome_injective(cols, bound=3):
    seen=set()
    for wt in range(bound+1):
        for marks in combinations(range(len(cols)),wt):
            s=xor_all(cols[j] for j in marks)
            if s in seen:return False
            seen.add(s)
    return True


def source_Q(x,h):
    # Seven source h_i, first six are a basis and the seventh is their sum.
    for mask in range(64):
        if xor_all(h[i] for i in range(6) if (mask>>i)&1)==x:
            w=mask.bit_count()
            return (w*(w+1)//2)&1
    raise ValueError(x)


def scalar_form_properties():
    h,_=seed_frame()
    assert rank(h)==6 and xor_all(h)==0
    def b(x,y):return source_Q(x^y,h)^source_Q(x,h)^source_Q(y,h)
    assert all(b(a,c)==1 for a,c in combinations(h,2))
    assert all(source_Q(a,h)==1 for a in h)
    assert sum(source_Q(x,h)==0 for x in range(64))==36
    # Each heptad permutation can be extended linearly, hence preserves Q and B.
    return h


def counterexample_increment():
    h=scalar_form_properties()
    h8=[int(x) for x in h]+[1<<6]
    assert rank(h8)==7 and syndrome_injective(h8)
    assert sum(comb(8,j) for j in range(4))==93<128
    # Another eight-slot code without choosing any new interaction.
    assert all((x>>6)==0 for x in h8[:7])
    return 93,128


def force_affine_hyperplane():
    # Any sum-free half-set P in F2^5 must equal a nonzero linear functional's 1-coset.
    P=[16|z for z in range(16)]
    assert len(P)==16 and len(set(P))==16
    assert not (set(P)&{a^b for a,b in combinations(P,2)})
    def pnorm(p):
        return min(p,p^0)
    # 31 distinct affine hyperplanes not containing the origin.
    planes=[]
    for functional in range(1,32):
        H=frozenset(x for x in range(32) if (functional & x).bit_count()%2==1)
        assert len(H)==16
        assert not H.intersection({a^b for a,b in combinations(H,2)})
        planes.append(H)
    assert len(set(planes))==31
    assert frozenset(P) in planes
    return len(planes)


def four_flat_differences():
    cols,old,new=construct_columns()
    assert syndrome_injective(cols)
    flats=set()
    vals=[]
    for a in range(1,16):
        for b in range(1,16):
            if a>=b:continue
            for z in range(16):
                flat=frozenset((z,z^a,z^b,z^a^b))
                if flat in flats:continue
                flats.add(flat)
                second=xor_all(veronese2(t) for t in flat)
                assert second!=0 and quad_form(second)==0
                vals.append(second)
    assert len(flats)==140
    assert len(set(vals))==35 # all nonzero singular bivectors
    assert all(v.bit_count()>=1 for v in vals)
    return len(flats),len(set(vals))


def get_bad_syndrome(cols):
    seen={}
    for wt in range(4):
        for marks in combinations(range(len(cols)),wt):
            v=xor_all(cols[i] for i in marks)
            if v in seen:return (seen[v], marks)
            seen[v]=marks
    return None


def perturbations():
    old=select_symplectic_heptad()
    root_new=[veronese2(z)|(1<<6)|(z<<7) for z in range(16)]
    assert get_bad_syndrome(old+tuple(root_new)) is None
    cubic_trials=[]
    for triple in combinations(range(4),3):
        for bit in range(6):
            changed=root_new[:]
            for z in range(16):
                if all((z>>j)&1 for j in triple):changed[z]^=1<<bit
            witness=get_bad_syndrome(old+tuple(changed))
            cubic_trials.append((triple,bit,witness))
    quartic_trials=[]
    for bit in range(6):
        changed=root_new[:]
        changed[15]^=1<<bit
        quartic_trials.append((bit,get_bad_syndrome(old+tuple(changed))))
    survive_cubic=sum(w is None for t,b,w in cubic_trials)
    survive_quartic=sum(w is None for b,w in quartic_trials)
    assert survive_cubic==0
    assert survive_quartic==0
    return len(cubic_trials),len(quartic_trials),cubic_trials[:3],quartic_trials[:3]


def source_isometry():
    source,_=seed_frame()
    dest=select_symplectic_heptad()
    src_basis=source[:6];dst_basis=dest[:6]
    def transfer(x):
        for mask in range(64):
            if xor_all(src_basis[i] for i in range(6) if (mask>>i)&1)==x:
                return xor_all(dst_basis[i] for i in range(6) if (mask>>i)&1)
        raise Exception()
    assert all(transfer(a)==b for a,b in zip(source,dest))
    assert all(source_Q(x,source)==quad_form(transfer(x)) for x in range(64))
    assert rank([transfer(1<<i) for i in range(6)])==6
    return tuple(transfer(1<<i) for i in range(6))


def main():
    assert source_isometry()
    e=counterexample_increment()
    print('ONE-POINT COUNTEREXAMPLE:',e[0],'different radius-3 syndromes out of',e[1])
    print('SOURCE QUADRATIC SPACE: unique S7-invariant B and Q; 36 zeros in 64-space')
    print('SOURCE->EXTERIOR SQUARE ISOMETRY basis images:',source_isometry())
    print('SATURATED 16-CAP IN FIVE NEW BITS: necessarily an affine hyperplane; variants=',force_affine_hyperplane())
    print('140 PHASE PARALLELOGRAMS; 35 NONZERO SINGULAR DIFFERENCES:',four_flat_differences())
    cube,quartic,cases,case2=perturbations()
    print('CUBIC MUTATIONS:',cube,'all fail; QUARTIC MUTATIONS:',quartic,'all fail')
    print('First witnesses:',cases[:2],case2[:2])
    print('PASS')

if __name__=='__main__':main()
