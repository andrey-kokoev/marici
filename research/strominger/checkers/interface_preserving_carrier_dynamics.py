"""Classify declared S4 skew-action combinations fixing an omitted arrow.

Source actions and the reference-arrow constraint determine a LINE of
candidates, not an energy scale, physical Hamiltonian or selected controller.
"""
from itertools import permutations
from functools import reduce
from math import gcd
import sympy as S


def classify(vertices=tuple('ABCD'), omitted='AB'):
    vertices=tuple(vertices)
    edges=tuple(a+b for a in vertices for b in vertices if a!=b)
    group=tuple(permutations(vertices))
    raw=[]
    points=[]
    for perm in group:
        relabel=dict(zip(vertices,perm))
        C=S.Matrix(12,12,lambda i,j:int(edges[i]==relabel[edges[j][0]]+relabel[edges[j][1]]))
        Cv=S.Matrix(4,4,lambda i,j:int(vertices[i]==relabel[vertices[j]]))
        raw.append(C-C.T)
        points.append(Cv-Cv.T)
    columns=S.Matrix.hstack(*(S.Matrix(144,1,list(D)) for D in raw))
    _,pivots=columns.rref()
    basis=[raw[i] for i in pivots]
    boundary=S.Matrix.hstack(*(D[:,edges.index(omitted)] for D in basis))
    nullspace=boundary.nullspace()
    if len(nullspace)!=1:
        raise ValueError('expected one-dimensional interface-preserving skew space')
    vector=nullspace[0]
    denominator=S.ilcm(*(value.q for value in vector))
    integers=[int(value*denominator) for value in vector]
    common=reduce(gcd,integers)
    integers=[value//common for value in integers]
    if next(v for v in integers if v)<0: integers=[-v for v in integers]
    D=sum((value*action for value,action in zip(integers,basis)),S.zeros(12))
    Dv=sum((value*points[i] for value,i in zip(integers,pivots)),S.zeros(4))
    return {'vertices':vertices,'edges':edges,'group':group,'raw':raw,
            'basis':basis,'pivots':pivots,'boundary':boundary,'nullspace':nullspace,
            'coefficients':tuple(integers),'D':D,'Dv':Dv,'omitted':omitted}


def native_generator(classification, selected):
    selected=tuple(selected)
    if len(selected)!=11 or set(selected)!=set(classification['edges'])-{classification['omitted']}:
        raise ValueError('original eleven-arrow interface required')
    indices=tuple(classification['edges'].index(e) for e in selected)
    D=classification['D'].extract(indices,indices)
    Dv=classification['Dv']
    A=S.SparseMatrix(S.diag(S.kronecker_product(D,S.eye(11))+S.kronecker_product(S.eye(11),D),
                           S.kronecker_product(Dv,S.eye(4))+S.kronecker_product(S.eye(4),Dv)))
    return D,A


def retained_chart(fixture, transported):
    """Complete T9 value chart:137 leaves,32 middle means,32 final means.

    No data dropped. Only the consistent image represents valid native T9.
    """
    rows=transported.original
    by_label={row.label:i for i,row in enumerate(rows)}
    middle=tuple(child for family in transported.final for child in family.members)
    families=middle+transported.final
    means=S.zeros(len(families),len(rows))
    for i,family in enumerate(families):
        for leaf in fixture['leaves']((family,)):
            means[i,by_label[leaf.label]]=S.Rational(leaf.mass,family.mass)
    T=S.SparseMatrix.vstack(S.eye(len(rows)),S.SparseMatrix(means))
    L=S.SparseMatrix.hstack(S.eye(len(rows)),S.zeros(len(rows),len(families)))
    return T,L,means,middle
