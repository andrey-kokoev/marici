"""Explicit residual observer and the finite source-equivariance hostile."""
from pathlib import Path
from collections import defaultdict
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('descent',HERE/'check_seven_event_factorization_descent.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)


def main():
    X1,X2,mu,delta,y,weight=s.symbols('X1 X2 mu delta y weight',positive=True)
    L=s.symbols('L',real=True)
    form=s.Matrix([[2*L,1],[1,0]])/(2*y)
    observer=s.Matrix([1,-2*L])
    def port(X,m):return s.sqrt(2)*X*s.Matrix([1,m-L])
    first=(port(X1,mu).conjugate().T*form*observer)[0]
    second=(port(X2,mu+delta).conjugate().T*form*observer)[0]
    value=s.simplify(weight*(second/X2-first/X1))
    assert s.simplify(value-weight*s.sqrt(2)*delta/(2*y))==0
    assert s.simplify(first-s.sqrt(2)*X1*(mu-L)/(2*y))==0
    assert s.simplify(second-s.sqrt(2)*X2*(mu+delta-L)/(2*y))==0
    # Real arithmetic multipliers of either sign give the same detector.
    for ell in (-3,0,7):assert s.simplify(value.subs(L,ell)-value)==0
    a=f.relation((0,1),1);c=f.relation((2,3),0)
    source=f.multiply(a,c)
    assert len(source)==8 and sum(abs(v) for v in source.values())==8
    da=f.derivative(0,a);dc=f.derivative(3,c)
    joint=defaultdict(int)
    for (x,xx,u,k,v),alpha in da.items():
        for (z,zz,uu,kk,vv),beta in dc.items():
            joint[((('e',x,xx,k),('e',z,zz,kk)),(u,v+uu,vv))]+=alpha*beta
    joint=f.clean(joint)
    sectors=[((('e',0,1,1),('e',3,7,0)),((),(),())),
             ((('e',1,3,1),('e',3,7,0)),((),(),()))]
    assert all(joint[key]==1 for key in sectors)
    assert not f.balanced_boundary(joint)
    # On span(c,ac), the left relation action is c -> ac -> 0.
    action=s.Matrix([[0,0],[1,0]]);inclusion=s.Matrix([0,1])
    h0,h1=s.symbols('h0 h1')
    H=s.Matrix([[h0,h1]])
    assert H*action==s.Matrix([[h1,0]])
    assert H*inclusion==s.Matrix([[h1]])
    assert s.solve([h1,h1-value],[h1],dict=True)==[]
    result={'passed':True,'checks':['explicit_residual_isolating_observer',
        'positive_two_window_difference','arithmetic_multiplier_cancels',
        'eight_term_actual_source_product','two_selected_balanced_sectors',
        'actual_joint_cycle','source_equivariant_nullhomotopy_obstruction'],
        'scope':'No numerical theta values or scalar-cohomology inference. Positivity of the actual window-mean gap and nonzero localization follow from the companion proof.'}
    out=HERE.parent/'results/residual-attachment-nonzero.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
