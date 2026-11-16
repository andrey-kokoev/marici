"""Finite Ramsey (3,6;17) nerve and Mayer--Vietoris certificates.

Graph6 inputs: B. McKay, https://users.cecs.anu.edu.au/~bdm/data/ramsey.html

For each graph the displayed blue K5 family F is a nonextension certificate:
    K = Ind(G) = union_{f in F} K[V minus f].
All independent vertex sets, including the empty set, are tested.  For every
nonempty intersection of these induced subcomplexes this script computes all
F2 Betti numbers.  It separately computes the nerve's F2 homology.

The non-acyclic intersections are so sparse that the Mayer--Vietoris spectral
sequence degenerates in total degree three.  Hence the direct count
    beta3(K) = beta3(nerve) + sum(exceptional positive-degree Betti numbers)
holds for these specific covers. This is NOT claimed for arbitrary covers.

Optional --optimize: verify minimum number of blue K5 certificate facets via
SciPy's HiGHS integer optimizer (the normal audit uses only stdlib).
"""
from collections import Counter
from itertools import combinations
import sys

GRAPH6 = [
    'P??GaOo`XMGsIcT?pSLaGuA?',
    'P?C?I_h`SDEQQcLAh`dU?tG?',
    'P@oGQA?`ACcdCtDYC]Ah?goC',
    'PG?OSAKccKGiGwJSI[@oWUA_',
    'PGD?OkeO_WAEGQobP_s`cgU?',
    'Ps`A?WIDGeCdGsQEKK?oLL_O',
    'Ps`A?_KChFCiBoQSKCOoXL_O',
]

# Each row gives blue K5's. Zero-based vertex names refer to the graph6 input.
COVERS = [
    [(0,1,5,6,8), (2,5,6,7,16), (3,10,11,12,14),
     (4,9,10,11,13), (5,6,8,15,16)],
    [(0,1,2,3,6), (1,4,5,10,11), (1,4,6,9,13),
     (2,7,12,14,16), (3,8,12,14,15), (4,7,11,13,16)],
    [(0,1,6,11,13), (0,2,6,13,15), (2,5,8,10,12),
     (3,5,7,8,10), (4,9,11,13,16), (4,10,12,14,16)],
    [(0,3,11,12,13), (1,7,8,9,10), (2,3,4,10,11),
     (5,9,12,14,15), (6,7,8,15,16)],
    [(0,1,4,8,12), (1,7,8,10,14), (2,3,5,9,13),
     (2,7,10,11,15), (3,5,6,12,16), (4,5,13,15,16)],
    [(0,5,6,13,14), (1,7,9,15,16), (1,8,10,12,16),
     (2,3,5,6,13), (4,9,11,14,16)],
    [(0,5,6,13,14), (1,8,11,12,16), (2,3,5,6,13),
     (2,5,7,9,15), (4,5,9,10,14)],
]
EXPECTED_NERVE_BETA3 = [1,1,0,1,0,1,1]
EXPECTED_K_BETA3 = [1,2,1,1,1,3,1]
# Intersection indices are 1-based, like the entries in the accompanying discussion.
EXPECTED_EXCEPTIONS = [
    [],
    [((1,4),2,1)],
    [((1,3,5),1,1)],
    [],
    [((1,),3,1)],
    [((1,2),2,1), ((1,3),2,1)],
    [],
]


def decode_graph6(code):
    n = ord(code[0])-63
    bits = ''.join(f'{ord(c)-63:06b}' for c in code[1:])
    red = {frozenset((i,j)) for bit,(i,j) in zip(bits,
        ((i,j) for j in range(1,n) for i in range(j))) if bit=='1'}
    return n,red


def independent_faces(n,red,k):
    return [f for f in combinations(range(n),k) if all(
        frozenset(e) not in red for e in combinations(f,2))]


def f2rank(columns):
    pivots={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p not in pivots:
                pivots[p]=x
                break
            x^=pivots[p]
    return len(pivots)


def betti(face_lists):
    # face_lists[j] is the list of j-VERTEX simplices; face_lists[0] = [].
    d=len(face_lists)-2
    ranks=[0]*(d+2)
    for k in range(2,d+2):
        codomain={f:i for i,f in enumerate(face_lists[k-1])}
        columns=[sum(1<<codomain[sub] for sub in combinations(f,k-1))
                 for f in face_lists[k]]
        ranks[k-1]=f2rank(columns)
    return [len(face_lists[k])-ranks[k-1]-ranks[k]
            for k in range(1,d+2)]


def verify(i):
    n,red=decode_graph6(GRAPH6[i]); assert n==17
    faces=[[]]+[independent_faces(n,red,k) for k in range(1,7)]+[[]]
    assert not faces[6]
    fs=tuple(COVERS[i]); assert len(fs)==len(set(fs))
    assert all(f in faces[5] for f in fs)

    # A face S belongs to K[V\F] precisely when S intersects F trivially.
    # This checks all faces; no maximality assumption is needed.
    assert all(any(set(S).isdisjoint(F) for F in fs)
               for k in range(1,6) for S in faces[k])

    nerve=[[]]
    exceptions=[]
    for r in range(1,len(fs)+1):
        layer=[]
        for ids in combinations(range(len(fs)),r):
            permitted=set(range(n)) - set().union(*(set(fs[j]) for j in ids))
            if not permitted:
                continue
            layer.append(ids)
            subfaces=[[]]+[[f for f in faces[k] if set(f)<=permitted]
                           for k in range(1,6)]+[[]]
            b=betti(subfaces)
            assert b[0]==1
            for dim in range(1,5):
                if b[dim]:
                    exceptions.append((tuple(j+1 for j in ids),dim,b[dim]))
        nerve.append(layer)
    nerve.append([])
    exceptions.sort()
    assert exceptions==sorted(EXPECTED_EXCEPTIONS[i])
    nerve_b=betti(nerve)
    K_b=betti(faces)
    assert nerve_b[3]==EXPECTED_NERVE_BETA3[i]
    assert K_b[3]==EXPECTED_K_BETA3[i]
    assert K_b[3]==nerve_b[3]+sum(m for _,_,m in exceptions)
    assert all(p==0 for p in nerve_b[1:3]+nerve_b[4:])
    print(f'graph {i+1}: cover size {len(fs)}, beta3(K)={K_b[3]}, '
          f'beta3(nerve)={nerve_b[3]}, higher intersection homology={exceptions}, '
          f'nerve f-vector={[len(x) for x in nerve[1:-1]]}')
    if len(fs)==5 and not exceptions:
        assert [len(x) for x in nerve[1:-1]]==[5,10,10,5,0]
        print('    Homological good cover with nerve boundary of 4-simplex')
    return n,red,faces


def optimize(n,faces,fs):
    from scipy.optimize import milp,Bounds,LinearConstraint
    from scipy.sparse import csr_matrix
    import numpy as np
    S=[s for k in range(1,6) for s in faces[k]]
    F=faces[5]
    M=csr_matrix(np.asarray([[int(set(s).isdisjoint(f)) for f in F]
                              for s in S],dtype=float))
    ans=milp(np.ones(len(F)),integrality=np.ones(len(F)),
             bounds=Bounds(np.zeros(len(F)),np.ones(len(F))),
             constraints=LinearConstraint(M,np.ones(len(S)),np.inf),
             options={'mip_rel_gap':0,'time_limit':60})
    assert ans.success and abs(ans.fun-len(fs))<1e-6
    assert abs(ans.mip_dual_bound-len(fs))<1e-6
    print(f'    MINIMUM blue K5 cover cardinality: {len(fs)}, exactly certified')


if __name__=='__main__':
    for i in range(7):
        n,red,faces=verify(i)
        if '--optimize' in sys.argv: optimize(n,faces,COVERS[i])
