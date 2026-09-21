"""Source-polarity dagger: exact sewing signs and a compact-source regression."""
from pathlib import Path
import json
import sympy as sp
import mpmath as mp

ROOT=Path(__file__).resolve().parents[3]


def main():
    I=sp.I
    C=sp.Matrix([[0,0,-1,1],[0,0,-1,1],[-1,-1,0,0],[1,1,0,0]])/2
    P=sp.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])
    S=I*sp.Matrix([[-1,1,1,1],[-1,1,-1,-1]])/2
    phase=sp.diag(I,-I,I,-I)
    B=S*phase
    sheet=sp.Matrix([[0,1],[1,0]])
    J=sp.diag(1,-1)
    W=sp.Matrix([[0,1],[-1,0]])
    assert P.T*P==sp.eye(4) and P*P==sp.eye(4)
    assert P.T*C*P==-C
    assert B*P==sheet*B
    assert sheet.T*J*sheet==-J
    assert sheet.T*W*sheet==-W
    # Independent complex vectors ensure this tests the full polarization.
    hw=sp.Matrix([1+I,2-I,-1+2*I,3])
    hz=sp.Matrix([2,-I,1+I,-2+I])
    z=sp.Rational(1,3)+2*I
    w=-sp.Rational(1,4)+I
    upper=(hw.conjugate().T*C*hz)[0]/(-I*(z-sp.conjugate(w)))
    hm_w,hm_z=P*hw.conjugate(),P*hz.conjugate()
    # Lower-half-plane feature has Gram 1/[+i(z-conj(w))].
    lower=(hm_w.conjugate().T*(-C)*hm_z)[0]/(I*(sp.conjugate(z)-w))
    wrong=(hm_w.conjugate().T*C*hm_z)[0]/(I*(sp.conjugate(z)-w))
    assert sp.simplify(lower-sp.conjugate(upper))==0
    assert upper!=0 and sp.simplify(wrong+sp.conjugate(upper))==0

    mp.mp.dps=35
    intervals=((mp.mpf(0),mp.mpf(1)),(mp.mpf(1),mp.mpf(2)))
    coefficients=(mp.mpc(1,2),mp.mpc(-2,1))
    signs=(1,-1,1,-1)
    moments=(0,0,1,1)
    swap=(1,0,3,2)
    spectral=mp.mpc('.3','1.2')
    def tail(coefs,k,z,x):
        a=signs[k]*1j*z-1
        if moments[k]==0:
            primitive=lambda t:mp.exp(a*t)/a
        else:
            primitive=lambda t:mp.exp(a*t)*(t/a-1/a**2)
        answer=mp.mpc(0)
        for coef,(left,right) in zip(coefs,intervals):
            if x<right:
                answer+=coef*mp.exp(-signs[k]*1j*z*x)*(primitive(right)-primitive(max(left,x)))
        return answer
    errors=[]
    for x in (mp.mpf(0),mp.mpf('.5'),mp.mpf('1.5'),mp.mpf(3)):
        for k in range(4):
            lhs=tail(tuple(mp.conj(c) for c in coefficients),k,mp.conj(spectral),x)
            rhs=mp.conj(tail(coefficients,swap[k],spectral,x))
            errors.append(abs(lhs-rhs))
    assert max(errors)<mp.mpf('1e-28')
    # Word reversal changes left creation into right creation, not deletion.
    for n in range(5):
        word=tuple(range(n))
        letter=9
        assert tuple(reversed((letter,)+word))==tuple(reversed(word))+(letter,)
        assert tuple(reversed(tuple(reversed(word))))==word
    result={
        'schema':'marici.voevodsky.clark-history-polarity-dagger.v1',
        'passed':True,
        'exact_checks':['P^T C P=-C','B P=sheet_swap B','sheet swap reverses signature and Wronskian',
                        'oriented full kernels conjugate','wrong lower signature has opposite sign',
                        'word reversal exchanges left and right creation'],
        'tail_fixture':'exp(-x) on two shells, with independent complex coefficients',
        'maximum_tail_conjugation_error':mp.nstr(max(errors),8),
        'scope':'Tail-polarity conjugation and tensor-order reversal. No identification with spatial reciprocal reflection, arithmetic inverse, or one fixed-metric unitary action.',
    }
    out=ROOT/'research/voevodsky/results/clark-history-polarity-dagger.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
