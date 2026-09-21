"""Exact port algebra and actual diamond/product observation sectors."""
from pathlib import Path
from collections import defaultdict
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('descent',HERE/'check_seven_event_factorization_descent.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)


def main():
    F,Fp,G,Gp,L,Lbar=s.symbols('F Fp G Gp L Lbar')
    # F,Fp denote conjugate left-port values, independent symbolic variables.
    numerator=s.expand((F-s.I*Fp)*(G+s.I*Gp)-(F+s.I*Fp)*(G-s.I*Gp))
    assert s.expand(numerator-2*s.I*(F*Gp-Fp*G))==0
    arithmetic=2*F*G*(L+Lbar)
    residual=2*(F*(s.I*Gp-L*G)+(-s.I*Fp-Lbar*F)*G)
    assert s.expand(numerator-arithmetic-residual)==0
    X,mu,ell,y=s.symbols('X mu ell y',positive=True)
    diagonal=s.expand((numerator-arithmetic).subs({F:X,G:X,Fp:s.I*mu*X,Gp:-s.I*mu*X,L:ell,Lbar:ell})/(2*y))
    assert s.simplify(diagonal-2*X**2*(mu-ell)/y)==0
    x=s.symbols('x',positive=True)
    h=x*s.tanh(y*x)
    assert s.simplify(s.diff(h,x)-(s.tanh(y*x)+x*y/s.cosh(y*x)**2))==0
    A,B,C,Ap,Bp,Cp=s.symbols('A B C Ap Bp Cp')
    windows=[(A,Ap),(B+C,Bp+Cp),(A+B,Ap+Bp),(C,Cp)]
    signs=(1,1,-1,-1)
    assert s.expand(sum(sign*value for sign,(value,deriv) in zip(signs,windows)))==0
    assert s.expand(sum(sign*(s.I*deriv-L*value) for sign,(value,deriv) in zip(signs,windows)))==0
    # Singly retained diamond: both successive edge-feature sectors survive.
    a=f.relation((0,1),1);c=f.relation((2,3),0)
    da=f.derivative(0,a);dc=f.derivative(3,c)
    assert not f.boundary(da) and not f.boundary(dc)
    assert da[0,1,(),1,()]==1 and da[1,3,(),1,()]==1
    assert dc[3,7,(),0,()]==1
    joint=defaultdict(int)
    for (u,v,p,k,q),alpha in da.items():
        for (uu,vv,pp,kk,qq),beta in dc.items():
            key=((('e',u,v,k),('e',uu,vv,kk)),(p,q+pp,qq))
            joint[key]+=alpha*beta
    joint=f.clean(joint)
    for edge in ((0,1),(1,3)):
        key=((('e',*edge,1),('e',3,7,0)),((),(),()))
        assert joint[key]==1
    assert not f.balanced_boundary(joint)
    source=f.multiply(a,c)
    assert sum(abs(v) for v in source.values())==8
    result={'passed':True,'checks':['two_sheet_moment_identity','exact_arithmetic_residual',
        'imaginary_axis_diagonal_defect','strictly_increasing_window_mean_integrand',
        'diamond_additivity_and_residual_additivity','two_actual_retained_edge_sectors',
        'actual_two_seam_product_sectors_and_cycle'],
        'scope':'No numerical Clark samples. Strict separation of the two positive window means is proved analytically in the companion note. No unprojected total self-pairing defect is inferred from a single sector.'}
    out=HERE.parent/'results/window-arithmetic-attachment-defect.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
