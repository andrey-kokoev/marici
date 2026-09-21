"""Labelled test/dual algebra and genuine two-slot balancing checks."""
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
    beta=s.Matrix([1+s.I,2-s.I]);swap=s.Matrix([[0,1],[1,0]])
    endpoint=(beta.conjugate().T*swap*beta)[0].expand()
    L=s.Integer(3);B=2*L-endpoint;leak=2+s.I
    E=s.Matrix([[1,0],[0,0],[beta[0],0],[beta[1],0],[1,0],[0,1]])
    R=s.Matrix([[B,0],[-leak,0],[beta[1],0],[beta[0],0],[0,1],[1,0]])
    form=s.Matrix([[2*L,1],[1,0]])
    equal(E.conjugate().T*R,form)
    negative_test=s.Matrix([[0,1,0,0,0,0]])
    equal(negative_test*R,s.Matrix([[-leak,0]]))
    perturb=s.zeros(6,2);perturb[0,0]=s.Rational(1,7);perturb[1,0]=s.I/5
    RP=R+perturb
    equal(E.conjugate().T*(RP-R),s.Matrix([[s.Rational(1,7),0],[0,0]]))
    E2=s.kronecker_product(E,E);R2=s.kronecker_product(R,R)
    equal(E2.conjugate().T*R2,s.kronecker_product(form,form))
    equal(R2-s.kronecker_product(RP,RP),
          s.kronecker_product(R-RP,R)+s.kronecker_product(RP,R-RP))
    equal(s.kronecker_product(negative_test,negative_test)*R2,
          s.kronecker_product(negative_test*R,negative_test*R))
    N=s.symbols('N',positive=True);sigma=s.symbols('sigma',positive=True)
    tail=N**(1-sigma)*(s.log(N)/(sigma-1)+1/(sigma-1)**2)
    assert s.simplify(s.diff(tail,N)+s.log(N)*N**(-sigma))==0
    cases=0
    for left_kind in (0,1):
        for right_kind in (0,1):
            for keep in (0,1):
                if left_kind+right_kind+keep>2:continue
                a=f.relation((0,1),left_kind);c=f.relation((3,4),right_kind)
                e={((2,),(keep,)):1}
                before=joint(f.derivative(0,f.multiply(a,e)),f.derivative(7,c))
                after=joint(f.derivative(0,a),f.derivative(3,f.multiply(e,c)))
                assert before==after and before
                assert not f.balanced_boundary(before)
                cases+=1
    result={'passed':True,'checks':['signed_compression_endpoint_residual_pairing',
        'negative_side_test_detects_leakage','source_graph_does_not_test_leakage',
        'two_slot_pairing','response_tensor_telescoping','double_leakage_label_retained',
        'prime_cutoff_integral_majorant'],
        'actual_at_most_two_feature_balancing_checks':cases,
        'scope':'Two retained slots, not arbitrary feature count. Response topology is weighted test/dual, never unweighted L2.'}
    out=HERE.parent/'results/two-slot-rigged-response.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
