"""Signed, non-real chain fixtures; not a sampled analytical Gram test."""
from pathlib import Path
import json
import sympy as s


def main():
    u=s.Matrix([1,s.I,1+s.I]);v=s.Matrix([[1,s.I]])
    d2=(u*v).applyfunc(s.expand);d1=s.Matrix([[1,1,-1]])
    j=s.Matrix([-s.I,1])
    assert d1*d2==s.zeros(1,2)
    assert (d2*j).applyfunc(s.expand)==s.zeros(3,1)
    J2=s.diag(1,-1);J1=s.diag(1,-1,1);J0=s.Matrix([[-1]])
    mate2=J2*d2.conjugate().T*J1
    mate1=J1*d1.conjugate().T*J0
    # T=J_2[-1]: its conjugate dual has -d1^vee, then +d2^vee.
    dual_low=-d1.conjugate().T;dual_high=d2.conjugate().T
    green_low=-mate1;green_high=mate2
    assert (dual_high*dual_low).applyfunc(s.expand)==s.zeros(2,1)
    assert (green_high*green_low).applyfunc(s.expand)==s.zeros(2,1)
    assert J1*green_low==dual_low*J0
    assert J2*green_high==dual_high*J1
    # Joint observation pulls back to the shifted source product dual.
    pullback=j.conjugate().T*J2
    assert (pullback*green_high).applyfunc(s.expand)==s.zeros(1,3)
    mu=s.Matrix([0,1]);q=s.Matrix([[1,0]])
    source_dual_d=-mu.conjugate().T
    assert source_dual_d*q.conjugate().T==s.zeros(1)
    assert source_dual_d.rank()==1
    pi=s.eye(1);Fminus=j*pi
    assert Fminus.conjugate().T*J2==pi.conjugate().T*pullback
    observer=J2*j
    assert (pullback*observer)[0]==2
    # A source-equivalent splitting remains obstructed in the local module
    # fixture: the relation acts by b -> ab, while it kills the quotient.
    action=s.Matrix([[0,0],[1,0]])
    t=s.symbols('t')
    assert action*s.Matrix([1,t])==mu
    result={'passed':True,'checks':['nonreal_joint_complex_and_cycle',
        'shifted_conjugate_dual_signs','signed_green_mate_naturality',
        'dual_and_green_square_zero','joint_pullback_chain_equation',
        'source_dual_exactness_fixture','dual_connecting_inclusion_square',
        'nonzero_paired_joint_observation','source_equivariant_splitting_hostile'],
        'scope':'Finite algebraic fixtures only. Strong-dual continuity, observer graph completeness and non-surjectivity are proved in the companion note.'}
    out=Path(__file__).resolve().parents[1]/'results/factorial-attachment-dual-square.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
