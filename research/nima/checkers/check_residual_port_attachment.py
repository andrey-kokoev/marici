"""Residual-coordinate form identity and actual balanced products."""
from pathlib import Path
from collections import defaultdict
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('descent',HERE/'check_seven_event_factorization_descent.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)


def equal(a,b):assert (a-b).applyfunc(s.expand)==s.zeros(a.rows,a.cols)


def joint(left,right):
    out=defaultdict(int)
    for (x,y,u,k,v),a in left.items():
        for (xx,yy,uu,kk,vv),b in right.items():
            out[((('e',x,y,k),('e',xx,yy,kk)),(u,v+uu,vv))]+=a*b
    return f.clean(out)


def main():
    A=s.Matrix([[1+s.I,2],[-s.I,3-s.I]])
    I=s.eye(2);Z=s.zeros(2)
    swap=Z.row_join(I).col_join(I.row_join(Z))
    forward=I.row_join(Z).col_join((-A).row_join(I))
    inverse=I.row_join(Z).col_join(A.row_join(I))
    enlarged=(A+A.conjugate().T).row_join(I).col_join(I.row_join(Z))
    equal(forward*inverse,s.eye(4))
    equal(inverse.conjugate().T*swap*inverse,enlarged)
    equal(forward.conjugate().T*enlarged*forward,swap)
    two=s.kronecker_product(forward,forward)
    equal(two.conjugate().T*s.kronecker_product(enlarged,enlarged)*two,
          s.kronecker_product(swap,swap))
    # Refinement is linear on the same full port state, not a reset.
    a=s.Matrix([1,s.I,2,3]);b=s.Matrix([2,1-s.I,0,s.I]);c=s.Matrix([0,1,2*s.I,1])
    equal(forward*a+forward*(b+c)-forward*(a+b)-forward*c,s.zeros(4,1))
    balanced=0
    for left_kind in (0,1):
        for right_kind in (0,1):
            for keep in (0,1):
                left=f.relation((0,1),left_kind)
                middle={((2,),(keep,)):1}
                right=f.relation((3,4),right_kind)
                lm=f.multiply(left,middle);mr=f.multiply(middle,right)
                before=joint(f.derivative(0,lm),f.derivative(7,right))
                after=joint(f.derivative(0,left),f.derivative(3,mr))
                assert before==after and before
                assert not f.balanced_boundary(before)
                assert f.multiply(lm,right)==f.multiply(left,mr)
                balanced+=1
    result={'passed':True,'checks':['nonreal_triangular_inverse','forced_residual_form',
        'one_slot_pairing_reconstruction','two_slot_tensor_pairing_reconstruction',
        'chamber_refinement_without_reset'],
        'actual_nonminimal_balancing_checks':balanced,
        'scope':'Finite algebraic fixtures, not a sampled arithmetic operator. Compact-spectral bounds and completed descent are proved in the companion note.'}
    out=HERE.parent/'results/residual-port-attachment.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
