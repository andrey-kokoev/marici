"""Exact tail transport and coordinate-distinction regressions."""
from pathlib import Path
import json
import sympy as s


def main():
    a,z,L=s.symbols('a z L',complex=True)
    density=s.symbols('f')
    G=s.symbols('Gp0 Gm0 Gp1 Gm1')
    phase_checks=0
    derivatives=[]
    for j in (0,1):
        for sig in (1,-1):
            g=G[2*j+(0 if sig==1 else 1)]
            phase=s.exp(sig*s.I*z*a)
            total=s.diff(phase,a)*g+phase*(-sig*s.I*z*g-a**j*density)
            assert s.simplify(total+a**j*phase*density)==0
            derivatives.append(s.simplify(total));phase_checks+=1
    dC=(derivatives[0]+derivatives[1])/2
    dM=(derivatives[3]-derivatives[2])/2
    expected=(s.I*a*s.sin(z*a)+L*s.cos(z*a))*density
    assert s.simplify((dM-L*dC-expected).rewrite(s.exp))==0
    B=s.symbols('B0:8')
    telescopes=0
    for n in range(1,8):
        assert s.expand(sum(B[i]-B[i+1] for i in range(n))-(B[0]-B[n]))==0
        telescopes+=1
    # Translate a product, then subtract multiply-after-translation.
    u,h=s.symbols('u h',real=True)
    chi=1+u+u**2;g=1+s.I*u+u**3
    comm=(chi*g).subs(u,u+h)-chi*g.subs(u,u+h)
    assert s.expand(comm-(chi.subs(u,u+h)-chi)*g.subs(u,u+h))==0
    # A fixed one-dimensional exponential-state fibre cannot be preserved
    # by a nonconstant feature multiplier as a scalar localization.
    assert s.diff(chi,u)!=0
    # Kernel of the residual at an imaginary spectral point.
    x,y=s.symbols('x y',positive=True)
    kernel=-s.I*x*s.sin(s.I*y*x)-L*s.cos(s.I*y*x)
    assert s.simplify(kernel-s.cosh(y*x)*(x*s.tanh(y*x)-L))==0
    result={'passed':True,'phased_tail_ode_checks':phase_checks,
            'refinement_telescoping_checks':telescopes,
            'checks':['residual_source_density','feature_translation_commutator',
                      'nonconstant_multiplier_fibre_hostile','imaginary_axis_residual_kernel'],
            'scope':'Exact algebraic regressions. Norm bounds and absence of a universal local-endpoint-jet formula are analytic proofs in the companion note.'}
    out=Path(__file__).resolve().parents[1]/'results/window-residual-tail-transport.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
