"""Exact degree-three multiplication filler, including every face."""
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import json
from check_hodge_global_multiplicativity_faces import var,add,mul,scale,sub,chain


def T(y,Y,z,Z,a,b):
    return add(mul(y,add(z,scale(Z,-1))),scale(mul(Y,add(z,scale(Z,-b))),-a))


def main():
    x,X,y,Y,z,Z=[var(i) for i in range(6)]
    a,b,c=Q(2),Q(3),Q(5)
    F=add(mul(x,add(y,scale(Y,-1)),add(z,scale(Z,-1))),scale(mul(X,T(y,Y,z,Z,b,c)),-a))
    assert all((e[0]+e[1],e[2]+e[3],e[4]+e[5])==(1,1,1) for e in F)
    face=lambda axis,side:{2*axis:side,2*axis+1:1-side}  # side0=zero, side1=infinity
    expected=[scale(T(y,Y,z,Z,b,c),-a),mul(add(y,scale(Y,-1)),add(z,scale(Z,-1))),
              scale(T(x,X,z,Z,a*b,c),-1),mul(add(x,scale(X,-a)),add(z,scale(Z,-1))),
              scale(T(x,X,y,Y,a,b*c),-1),T(x,X,y,Y,a,b)]
    for k,(axis,side) in enumerate((i,j) for i in range(3) for j in (0,1)):
        assert sub(F,face(axis,side))==expected[k]
    retained=[];excluded=[]
    for axes in combinations(range(3),2):
        remaining=next(i for i in range(3) if i not in axes)
        for sides in product((0,1),repeat=2):
            values={}
            for axis,side in zip(axes,sides):values.update(face(axis,side))
            p=sub(F,values)
            # Remaining homogeneous linear equation A*u+B*v=0.
            e=[0]*6;e[2*remaining]=1;A=p.get(tuple(e),0)
            e=[0]*6;e[2*remaining+1]=1;B=p.get(tuple(e),0)
            assert A!=0 and B!=0
            root=-Q(B)/Q(A)
            (excluded if root==1 else retained).append(root)
    assert len(retained)==7 and sorted(retained)==sorted([c,b*c,b,a*b*c,a*b,a,a])
    assert len(excluded)==5
    for sides in product((0,1),repeat=3):
        values={}
        for axis,side in enumerate(sides):values.update(face(axis,side))
        p=sub(F,values)
        assert p and set(p)=={(0,)*6}
    associator={(a,b):1,(a*b,c):1,(b,c):-1,(a,b*c):-1}
    assert len(associator)==4
    boundary=[]
    for (u,v),coef in associator.items():boundary += [(v,coef),(u*v,-coef),(u,coef)]
    assert chain(*boundary)=={}
    raw=chain(('Tbc',1),('Tabc_left',-1),('Da',1),('Tabc_right',1),('Tab',-1))
    minus_A={'Tbc':1,'Tabc_left':-1,'Tabc_right':1,'Tab':-1}
    assert raw!=minus_A and {k:v for k,v in raw.items() if k!='Da'}==minus_A
    wrong=chain(('Tbc',1),('Tabc_left',1),('Da',1),('Tabc_right',1),('Tab',-1))
    assert {k:v for k,v in wrong.items() if k!='Da'}!=minus_A
    r={'passed':True,'classification':'explicit_normalized_degree_three_associator_filler',
       'faces_checked':6,'double_faces_checked':12,'triple_faces_checked':8,
       'retained_double_faces':7,'deleted_double_faces':5,
       'raw_degeneracy_retained':'Da','Hodge_proved':False,'Hodge_refuted':False,
       'residuals':['Parameter-cube degree is not algebraic codimension on the fixed sixfold.']}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-multiplication-associator-v1.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r))


if __name__=='__main__':main()
