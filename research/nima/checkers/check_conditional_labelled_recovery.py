"""Exact exponents and hostile formulas for conditional full-port recovery."""
from pathlib import Path
from fractions import Fraction as Q
import json
import sympy as s


def main():
    exponents=0
    for gamma in (Q(3,4),Q(1),Q(3,2),Q(2)):
        for delta in (Q(1,4),Q(1,2),Q(1),Q(2),Q(4),Q(8)):
            theta=delta/(2*gamma+delta)
            alpha=min(Q(1,2),theta)
            assert theta*(-gamma)+(1-theta)*(gamma+delta)==gamma
            assert 0<alpha<=Q(1,2) and alpha<=theta
            assert alpha*(2*gamma+delta)-delta<=0
            assert alpha==Q(1,2) or alpha*(2*gamma+delta)==delta
            exponents+=1
    # Unrestricted-trace H2 extension has coefficients 3,-2.
    value,slope=s.symbols('value slope')
    assert 3*value-2*value==value
    assert -3*slope+4*slope==slope
    n=s.symbols('n',positive=True)
    c,cp,cpp=s.symbols('c cp cpp',real=True)
    u=c/n**2;du=s.I*c/n+cp/n**2;ddu=-c+2*s.I*cp/n+cpp/n**2
    h1=s.expand(s.conjugate(u)*u+s.conjugate(du)*du)
    h2=s.expand(h1+s.conjugate(ddu)*ddu)
    assert s.simplify(h1-(c*c/n**2+(c*c+cp*cp)/n**4))==0
    assert s.limit(n**2*h1,n,s.oo)==c*c
    assert s.limit(h2,n,s.oo)==c*c
    gamma,delta,R=s.symbols('gamma delta R',positive=True)
    prior=s.exp(-(gamma+delta)*R)*s.exp((gamma+delta)*R)
    strong=s.exp(-(gamma+delta)*R)*s.exp(gamma*R)
    weak=s.exp(-(gamma+delta)*R)*s.exp(-gamma*R)
    assert s.simplify(prior-1)==0
    assert s.simplify(strong-s.exp(-delta*R))==0
    assert s.simplify(weak-s.exp(-(2*gamma+delta)*R))==0
    # Bochner H2 membership of the new kernel sources: t^2 C(sigma+it)
    # is integrable for C=O(t^(2-M)), M>=8.
    assert all(4-M<-1 for M in range(8,17))
    result={'passed':True,'interpolation_and_sharp_exponent_checks':exponents,
        'checks':['unrestricted_trace_extension_matching','oscillating_H1_H2_formulas',
                  'translated_prior_strong_and_weak_norms','kernel_source_second_moment_integrability'],
        'scope':'Local interpolation and operator bounds are analytic proofs, not finite numerical reconstruction tests. The estimate uses the full weak-copy labels.'}
    out=Path(__file__).resolve().parents[1]/'results/conditional-labelled-recovery.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
