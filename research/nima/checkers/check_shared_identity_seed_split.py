"""Test two sectors assembled from the same triangle seed with shared identity.

Use the three cyclic spectral modes already in each triangle. No additional
particle, atlas, or independently supplied companion geometry is introduced.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from check_twelve_triangle_positive_geometry import (
    ONE, ZERO, OMEGA, POINTS, LABELS, I, C, mean, compose, transpose,
    zadd, zmul, zconj, zscale, zmm, zreal, projector,
)


def plus(a,b): return tuple(tuple(zadd(x,y) for x,y in zip(r,s)) for r,s in zip(a,b))
def times(a,c): return tuple(tuple(zscale(z,c) for z in r) for r in a)
def conj(a): return tuple(tuple(zconj(z) for z in r) for r in a)
def trace(a):
    value=ZERO
    for i in range(len(a)): value=zadd(value,a[i][i])
    return value


def main():
    c=(ONE,OMEGA,zmul(OMEGA,OMEGA))
    E0=projector((ONE,)*3);Ep=projector(c);Em=projector(tuple(zconj(z) for z in c))
    zero=times(E0,0)
    for E in (E0,Ep,Em):
        assert zmm(E,E)==E and trace(E)==ONE
    for E,Fm in ((E0,Ep),(E0,Em),(Ep,Em)):
        assert zmm(E,Fm)==zero and zmm(Fm,E)==zero
    assert plus(plus(E0,Ep),Em)==zreal(I)
    assert zmm(zreal(C),Ep)==tuple(tuple(zmul(OMEGA,z) for z in row) for row in Ep)
    A=plus(E0,Ep);B=plus(E0,Em)
    assert zmm(A,A)==A and zmm(B,B)==B
    assert zmm(A,B)==E0 and zmm(B,A)==E0
    # One coherent copy of each mode across the twelve seed-generated cells.
    def lift(E):
        return tuple(tuple(zscale(E[i%3][j%3],F(1,12)) for j in range(36)) for i in range(36))
    LA,LB,L0=map(lift,(A,B,E0))
    assert zmm(LA,LA)==LA and zmm(LB,LB)==LB and zmm(LA,LB)==L0
    assert trace(LA)==(F(2),F(0)) and trace(LB)==(F(2),F(0)) and trace(L0)==ONE
    group={(0,1,2,3)};front=list(group)
    while front:
        p=front.pop()
        for g in ((1,2,0,3),(3,0,2,1)):
            q=compose(g,p)
            if q not in group: group.add(q);front.append(q)
    assert len(group)==12
    reconstructions=0;copies={};scaled_copies={}
    for p in sorted(group):
        a,b,cname=[LABELS[p[i]] for i in range(3)]
        face='F_'+''.join(sorted((a,b,cname)))
        f=mean([POINTS[k] for k in (a,b,cname)])
        X=zreal(transpose((f,POINTS[a],POINTS[b])))
        M=zmm(X,E0);Yp=zmm(X,A);Ym=zmm(X,B)
        assert Ym==conj(Yp)
        # Both sectors independently reconstruct the SAME real corner data:
        # X = Y + conjugate(Y) - shared identity contribution.
        assert plus(plus(Yp,conj(Yp)),times(M,-1))==X
        assert plus(plus(Ym,conj(Ym)),times(M,-1))==X
        reconstructions+=1
        # An independently enlarged companion with the same shared centroid
        # gives X'=2X-M. Check whether its incident corners still sew.
        enlarged=plus(times(X,2),times(M,-1))
        for j,label in enumerate((face,a,b)):
            copies.setdefault(label,set()).add(tuple(X[i][j] for i in range(3)))
            scaled_copies.setdefault(label,set()).add(tuple(enlarged[i][j] for i in range(3)))
    assert all(len(v)==1 for v in copies.values())
    splits={k:len(v) for k,v in scaled_copies.items() if len(v)>1}
    assert splits
    # General real scale s: at a shared corner, mismatch is
    # (1-s)*(centroid_of_triangle_g-centroid_of_triangle_h).
    # Distinct incident centroids force s=1 for this uniform scaling family.
    result={'audit_assertions_passed':True,'triangles_from_seed':12,
            'shared_seed_sectors':{'positive':'E0+Eomega','negative':'E0+Eomega_bar',
                                   'each_idempotent':True,'each_coherent_rank':2,
                                   'intersection':'E0','intersection_rank':1,
                                   'union_rank':3},
            'geometric_reconstruction':{'triangles_checked':reconstructions,
                                        'both_sectors_recover_same_source_geometry':True,
                                        'conjugate_data_relation':True,
                                        'distinct_companion_body_established':False},
            'independent_size_control':{'factor':2,'shared_vertices_split':splits,
                                        'uniform_scale_seam_condition':'(1-s)*(m_g-m_h)=0; distinct incident centroids force s=1'},
            'conclusion':'The existing seed supports stable conjugate sectors sharing one identity. They encode the same body. A geometrically distinct companion requires additional independent seed/incidence structure; it does not follow from these two conjugate presentations.'}
    dest=Path(__file__).resolve().parents[1]/'results'/'shared-identity-seed-split.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: seed splits into two idempotent conjugate sectors sharing rank-one identity. Both reconstruct the same twelve-triangle body; independent resizing breaks seams.')

if __name__=='__main__': main()
