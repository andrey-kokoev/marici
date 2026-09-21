"""Prescribed signed creation mates and observer weight ratios."""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import json
import sympy as s


def equal(a,b):assert (a-b).applyfunc(s.expand)==s.zeros(a.rows,a.cols)


def tensor_power(a,n):
    out=s.eye(1)
    for _ in range(n):out=s.kronecker_product(out,a)
    return out


def main():
    J=s.diag(1,-1)
    g=s.Matrix([1+s.I,2-s.I]);h=s.Matrix([s.I,1-2*s.I])
    fixtures=0
    for tau in (s.Rational(1,2),s.Integer(2)):
        for m in range(3):
            identity=s.eye(2**m)
            gram=tau**(2*m)*tensor_power(J,m)
            next_gram=tau**(2*(m+1))*tensor_power(J,m+1)
            left=s.kronecker_product(g,identity)
            right=s.kronecker_product(identity,g)
            lm=gram.inv()*left.conjugate().T*next_gram
            rm=gram.inv()*right.conjugate().T*next_gram
            equal(lm,tau**2*s.kronecker_product(g.conjugate().T*J,identity))
            equal(rm,tau**2*s.kronecker_product(identity,g.conjugate().T*J))
            equal(gram*lm,left.conjugate().T*next_gram)
            equal(gram*rm,right.conjugate().T*next_gram)
            # Compose two left creations, then compare the reversed mates.
            second=s.kronecker_product(h,s.eye(2**(m+1)))
            final_gram=tau**(2*(m+2))*tensor_power(J,m+2)
            second_mate=next_gram.inv()*second.conjugate().T*final_gram
            joint_mate=gram.inv()*(second*left).conjugate().T*final_gram
            equal(joint_mate,lm*second_mate)
            fixtures+=1
    ratios=0
    for n,l,m,d,R,b in product(range(5),range(4),range(5),range(4),(1,2,3),(1,2,3)):
        if d>l:continue
        assert Q(R**(n+l)*b**(m+d),R**n*b**m)==R**l*b**d
        if n>=l and m>=d:
            ratio=Q(R**(n-l)*b**(m-d),R**n*b**m)
            assert ratio==Q(1,R**l*b**d) and ratio<=1
        ratios+=1
    result={'passed':True,'signed_homogeneous_creation_mate_fixtures':fixtures,
            'endpoint_feature_weight_ratio_checks':ratios,
            'scope':'Fixed word outer actions, not differential incidence sums or arbitrary word splitting. Completed continuity is proved in the companion note.'}
    out=Path(__file__).resolve().parents[1]/'results/observer-source-actions.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
