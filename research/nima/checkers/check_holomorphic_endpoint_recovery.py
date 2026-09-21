"""Reduced-output recovery; distinct from retaining the weak residual label."""
from pathlib import Path
import json
import sympy as s


def main():
    z=s.symbols('z');h=s.Function('h')(z);L=s.Function('L')(z)
    sz=s.Rational(1,2)-s.I*z
    amplitude=sz*h
    moment=s.I*s.diff(amplitude,z)
    assert s.simplify(moment-(h+s.I*sz*s.diff(h,z)))==0
    residual=moment-L*amplitude
    assert s.simplify(residual-((1-L*sz)*h+s.I*sz*s.diff(h,z)))==0
    assert s.cancel(amplitude/sz-h)==0
    # Actual-window signed combination: even trace zero, moment nonzero.
    X1,X2,mu,gap=s.symbols('X1 X2 mu gap',positive=True)
    even=X2/X2-X1/X1
    mom=X2*(mu+gap)/X2-X1*mu/X1
    assert even==0 and s.simplify(mom-gap)==0
    assert s.simplify(mom-L*even-gap)==0
    # Slotwise reconstruction works on entangled polynomial amplitudes too.
    z1,z2=s.symbols('z1 z2')
    s1=s.Rational(1,2)-s.I*z1;s2=s.Rational(1,2)-s.I*z2
    H=1+z1**2*z2+s.I*z1*z2**2
    L1=s.Function('L1')(z1);L2=s.Function('L2')(z2)
    def residual1(f):return (1-L1*s1)*f+s.I*s1*s.diff(f,z1)
    def residual2(f):return (1-L2*s2)*f+s.I*s2*s.diff(f,z2)
    assert s.expand(residual1(residual2(H))-residual2(residual1(H)))==0
    assert s.expand(residual1(s2*H)-s2*residual1(H))==0
    assert s.expand(residual2(s1*H)-s1*residual2(H))==0
    assert s.cancel((s1*s2*H)/(s1*s2)-H)==0
    result={'passed':True,'checks':['endpoint_amplitude_recovery','moment_differentiation',
        'residual_reconstruction','actual_window_pointwise_hostile',
        'independent_slot_residual_operators_commute','tensor_endpoint_recovery'],
        'scope':'Recovery after discarding the weak residual output requires a holomorphic family. This does not contradict the five-label pointwise prepared-sector equivalence.'}
    out=Path(__file__).resolve().parents[1]/'results/holomorphic-endpoint-recovery.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
