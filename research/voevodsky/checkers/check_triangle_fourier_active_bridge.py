# /// script
# dependencies = ["sympy"]
# ///
"""Reuse actual retained history extension; distinguish order-three/four ticks."""
from pathlib import Path
import hashlib,json,sys
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
NI=ROOT/'research/nima/checkers'
sys.path.insert(0,str(NI))
from retained_path_successor import RetainedSuccessorLedger
import photon_native_spatial_step as rotor
from check_natural_tower_return import PACKETS


def zero(M):return S.simplify(M)==S.zeros(*M.shape)

def main():
    prior=ROOT/'research/voevodsky/results/carrier-fourier-orbit-bridge-v1.json'
    receipt=json.loads(prior.read_text());assert receipt['passed']
    for p,h in receipt['source_hashes'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    F=S.zeros(4)
    for j in range(4):F[(j+1)%4,j]=1
    D=F-F.T;G=10*S.eye(4)+S.ones(4)
    u=S.Matrix([1,0,-1,0]);v=F*u
    B=S.Matrix.hstack(S.sqrt(3)*u,-v)/S.sqrt(20)
    A=S.Matrix([[0,2/S.sqrt(3)],[-2*S.sqrt(3),0]])
    H=S.diag(3,1);C=S.Matrix(rotor.PLANE_STEP)
    assert zero(D*B-B*A) and zero(B.T*G*B-H)
    assert C**3==S.eye(2) and C!=S.eye(2)
    assert C==-S.eye(2)/2+S.sqrt(3)*A/4
    assert not zero(F*B-B*C)
    assert zero((F**2+S.eye(4))*B)
    # No nonzero same-tick intertwiner, even without injectivity.
    symbols=S.symbols('x0:8');X=S.Matrix(4,2,symbols)
    equations,_=S.linear_eq_to_matrix(list(F*X-X*C),symbols)
    assert equations.rank()==8
    stationary=S.Matrix.hstack(S.ones(4,1),S.Matrix([1,-1,1,-1]))
    assert S.Matrix.hstack(B,stationary).rank()==4 and D*stationary==S.zeros(4,2)
    assert F*stationary==stationary*S.diag(1,-1)
    # Actual native history data and the previously declared reader/section policy.
    rb=S.Matrix(rotor.target_reader())*S.Matrix.hstack(S.Matrix(rotor.U),S.Matrix(rotor.W))
    rbplus=(rb.T*rb).inv()*rb.T
    ledger=RetainedSuccessorLedger(PACKETS);frame=ledger.root
    weights=[S.Rational(1)]*len(frame.paths);old=None;stages=[]
    for tick in range(4):
        child=ledger.successor(frame)
        counts=[child.parent_slots.count(i) for i in range(len(frame.paths))]
        weights=[weights[i]/counts[i] for i in child.parent_slots];frame=child
        T=S.Matrix(frame.step_lift);n=len(frame.paths);metric=S.diag(*weights)
        O=S.Matrix([[int(path[-1][1]==a) for path in frame.paths] for a in 'ABCD'])
        P=rbplus*O
        E=metric.inv()*P.T*(P*metric.inv()*P.T).inv() if old is None else T*old['E']*C.inv()
        # Factor out sqrt(3) before large history products. The remaining
        # matrices are rational; check the analytic/metric squares by their
        # exact small factors instead of expanding radical n-by-n Grams.
        A0=S.simplify(A/S.sqrt(3))
        N=S.eye(n)-E*P;L0=E*A0*P;R=S.simplify(B*P)
        assert P*E==S.eye(2) and P*L0==A0*P
        assert zero(D*B-B*A) and zero(B.T*G*B-H)
        if old is not None:
            assert P*T==C*old['P'] and L0*T==T*old['L0']
            assert N*T==T*old['N']
            # Native continuation is angle pi/3, not the Fourier quarter-step.
            Uthird=-S.eye(4)/2+S.sqrt(3)*D/4
            assert zero(R*T-Uthird*old['R'])
            assert not zero(R*T-F*old['R'])
        stages.append({'word_length':tick+2,'history_dimension':n,'analytic_reader_rank':R.rank(),
                       'hidden_dimension':n-2,'generator_square':True})
        assert N*N==N and S.trace(N)==n-2
        old={'P':P,'E':E,'N':N,'L0':L0,'R':R}
    result={'schema':'marici.triangle-fourier-active-bridge.v1','iteration':2,'passed':True,
      'active_adapter':[[str(x) for x in B.row(i)] for i in range(4)],
      'continuous_generator_and_declared_metric_match':True,
      'native_tick_order':3,'Fourier_tick_order':4,'same_tick_intertwiner_dimension':0,
      'native_tick_angle':'pi/3','Fourier_active_tick_angle':'pi/4',
      'actual_history_stages':stages,'remaining_Fourier_characters':['1','-1'],
      'stationary_ports_supplied_by_rank_two_history_reader':False,
      'analytic_gamma_identity':'Prior Mellin-Fourier identity composes on the active image',
      'analytic_Hilbert_metric_identification':False,'RH_proved':False}
    files=[Path(__file__),prior,NI/'photon_native_spatial_step.py',NI/'retained_path_successor.py',
           NI/'check_triangle_coherent_generator_transport.py',
           ROOT/'research/voevodsky/triangle-fourier-active-bridge-v1.md']
    result['source_hashes']={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (ROOT/'research/voevodsky/results/triangle-fourier-active-bridge-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_hashes'},indent=2))


if __name__=='__main__':main()
