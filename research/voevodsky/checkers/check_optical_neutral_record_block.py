# /// script
# dependencies = ["sympy"]
# ///
"""Exact single-excitation record block, Pauli maps and retained loss flag."""
import json
from hashlib import sha256
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
DEF='research/conjecture_net/contracts/optical-neutral-record-block.v1.json'
NOTE='research/voevodsky/optical-neutral-record-block-v1.md'
OUT='research/voevodsky/results/optical-neutral-record-block-v1.json'

def main():
    checks=[]
    def check(name,ok):
        if not ok:raise ValueError(name)
        checks.append(name)
    V=S.Matrix([[0,0],[1,0],[0,1]]);I=S.eye(2)
    X=S.Matrix([[0,1],[1,0]]);Y=S.Matrix([[0,-S.I],[S.I,0]]);Z=S.diag(1,-1);n=(I-Z)/2
    N=S.diag(0,1,1);nb=S.diag(0,0,1)
    exchange=S.Matrix([[0,0,0],[0,0,1],[0,1,0]])
    H=nb-exchange/2;h=n-X/2;vac=S.diag(1,0,0)
    check('encoding-isometry',V.adjoint()*V==I and V*V.adjoint()==N)
    check('active-generator-square',H*V==V*h)
    check('inactive-generator-square',nb*V==V*n)
    check('single-excitation-invariance',H*N==N*H and H*vac==S.zeros(3))
    for name,A in [('I',I),('X',X),('Y',Y),('Z',Z),('occupation',n)]:
        B=V*A*V.adjoint()
        check(name+'/query',V.adjoint()*B*V==A and B.adjoint()==B and B*vac==S.zeros(3))
    centered=h-I/2
    check('exact-spectral-polynomial',centered**2==I/2)
    # U=e^-it/2 [c I-i sqrt(2) s centered]; c=cos(t/sqrt2), s=sin(t/sqrt2).
    c,s=S.symbols('c s',real=True)
    U=c*I-S.I*S.sqrt(2)*s*centered
    check('unitary-coefficient-law',S.simplify(U.adjoint()*U-(c*c+s*s)*I)==S.zeros(2))
    ready=S.Matrix([1,0]);rho=ready*ready.adjoint()
    p=S.simplify((U*rho*U.adjoint()*n).trace())
    check('occupation-law',p==s*s/2)
    check('no-detector-idle-substitution',h*n!=n*h and n*ready==S.zeros(2,1))
    # Complete projective readout; sum of encoded +/- effects is the occupied
    # subspace. Add vacuum flag rather than renormalize away losses.
    for name,A in [('X',X),('Y',Y),('Z',Z)]:
        plus=V*((I+A)/2)*V.adjoint();minus=V*((I-A)/2)*V.adjoint()
        check(name+'/complete-effects',plus+minus+vac==S.eye(3) and plus**2==plus and minus**2==minus)
    # Rational eta fixtures; a retained environment flag yields pure erasure.
    # Channel Kraus matrices: survival on N, jumps |vac><10|, |vac><01|,
    # and preserve original vacuum coherently within no-loss branch.
    pure=S.Matrix([1,S.I])/S.sqrt(2);encoded=V*pure*pure.adjoint()*V.adjoint()
    for eta in (S.Rational(0),S.Rational(1,2),S.Rational(1)):
        K0=vac+S.sqrt(eta)*N
        K1=S.zeros(3);K1[0,1]=S.sqrt(1-eta)
        K2=S.zeros(3);K2[0,2]=S.sqrt(1-eta)
        ks=[K0,K1,K2]
        check(f'loss/{eta}/complete',sum((k.adjoint()*k for k in ks),S.zeros(3))==S.eye(3))
        out=sum((k*encoded*k.adjoint() for k in ks),S.zeros(3))
        check(f'loss/{eta}/retained-erasure',S.simplify(out-eta*encoded-(1-eta)*vac)==S.zeros(3))
    offset=(S.sqrt(2)-1)/2
    check('positive-common-offset',S.simplify(min(h.eigenvals(),key=lambda x:float(x))+offset)==0)
    check('offset-not-global-vacuum-phase',N!=S.eye(3))
    paths=[DEF,NOTE,'research/nima/exchange-oscillator-preparation-and-measurement.md',
           'research/aspect/local-stokes-pauli-probe-provenance.md',
           'research/sontag/conditional-statistical-optical-binding-v1.md',Path(__file__).relative_to(ROOT).as_posix()]
    result=dict(schema='marici.optical-neutral-record-block-validation.v1',passed=True,checks=checks,
                primary_probability='sin(t_model/sqrt(2))^2/2 = (1-cos(sqrt(2)*t_model))/4',
                loss_is_logical_reset=False,physical_clock_calibrated=False,
                matter_projector_control_constructed=False,full_reaggregation_binding=False,physical_admission=False,
                verification_level='exact finite matrices and written standard single-excitation oscillator restriction',
                source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='source_sha256'},indent=2))
if __name__=='__main__':main()
