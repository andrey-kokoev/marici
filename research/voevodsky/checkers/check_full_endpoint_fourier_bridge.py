# /// script
# dependencies = ["sympy"]
# ///
"""Full endpoint connection preserves continuous law, not discrete tick identity."""
from pathlib import Path
import hashlib,json,sys
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
NI=ROOT/'research/nima/checkers';sys.path.insert(0,str(NI))
from retained_path_successor import RetainedSuccessorLedger
from check_natural_tower_return import PACKETS,incidence
import photon_native_spatial_step as rotor


def zero(X):return S.simplify(X)==S.zeros(*X.shape)
def rows(X):return [[str(v) for v in X.row(i)] for i in range(X.rows)]

def main():
    rp=ROOT/'research/voevodsky/results/triangle-fourier-active-bridge-v1.json'
    prior=json.loads(rp.read_text());assert prior['passed']
    for p,h in prior['source_hashes'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    M=S.Matrix(incidence(PACKETS));x=S.symbols('x')
    assert S.factor(M.charpoly(x).as_expr())==(x**2-x-1)*(x**2+x+1)
    rb=S.Matrix(rotor.target_reader())*S.Matrix.hstack(S.Matrix(rotor.U),S.Matrix(rotor.W))
    pa=(rb.T*rb).inv()*rb.T;C=S.Matrix(rotor.PLANE_STEP)
    assert pa*M==C*pa
    complement=S.Matrix.hstack(*pa.nullspace())
    Q=rb.row_join(complement);Qi=Q.inv();Sfull=Qi*M*Q;K=Sfull[2:,2:]
    assert Sfull==S.diag(C,K) and K**2-K-S.eye(2)==S.zeros(2)
    assert Qi[:2,:]==pa
    A0=S.Matrix([[0,S.Rational(2,3)],[-2,0]])
    Aep0=Q*S.diag(A0,S.zeros(2))*Qi
    assert Aep0*M==M*Aep0
    F=S.zeros(4)
    for j in range(4):F[(j+1)%4,j]=1
    D=F-F.T;u=S.Matrix([1,0,-1,0]);v=F*u
    B=S.Matrix.hstack(S.sqrt(3)*u,-v)/S.sqrt(20)
    T=B.row_join(S.Matrix.hstack(S.ones(4,1),S.Matrix([1,-1,1,-1])))
    J=S.simplify(T*Qi)
    assert J.rank()==4 and zero(D*J-S.sqrt(3)*J*Aep0)
    assert zero(J*rb-B)
    # No fixed nonzero same-tick map exists even on all endpoint coordinates.
    unknown=S.symbols('j0:16');X=S.Matrix(4,4,unknown)
    equations,_=S.linear_eq_to_matrix(list(F*X-X*M),unknown)
    assert equations.rank()==16
    # Added Fourier operation in endpoint coordinates; not native extension.
    Fep=S.simplify(J.inv()*F*J)
    assert zero(Fep**4-S.eye(4)) and not zero(Fep-M)
    assert not zero(Fep*M-M*Fep)
    ledger=RetainedSuccessorLedger(PACKETS);frame=ledger.root
    weights=[S.Rational(1)]*len(frame.paths);old=None;stages=[]
    for tick in range(4):
        child=ledger.successor(frame);counts=[child.parent_slots.count(i) for i in range(len(frame.paths))]
        weights=[weights[i]/counts[i] for i in child.parent_slots];frame=child
        n=len(frame.paths);step=S.Matrix(frame.step_lift);G=S.diag(*weights)
        O=S.Matrix([[int(path[-1][1]==a) for path in frame.paths] for a in 'ABCD'])
        P=pa*O;Pfull=Qi*O
        if old is None:
            Ea=G.inv()*P.T*(P*G.inv()*P.T).inv()
            Ec=G.inv()*O.T*(O*G.inv()*O.T).inv()*complement
            Efull=Ea.row_join(Ec)
        else:
            Efull=step*old['Efull']*Sfull.inv();Ea=Efull[:,:2]
        assert Pfull*Efull==S.eye(4) and O*Ea==rb
        N=S.eye(n)-Efull*Pfull;Nold=S.eye(n)-Ea*P
        L0=Ea*A0*P
        assert O*L0==Aep0*O
        assert N*N==N and S.trace(N)==n-4
        assert Nold==Efull[:,2:]*Pfull[2:,:]+N
        assert O.rank()==4 and P.rank()==2
        if old is not None:
            assert O*step==M*old['O']
            assert Efull==step*old['Efull']*Sfull.inv()
            assert N*step==step*old['N'] and L0*step==step*old['L0']
        # Every full analytic port now comes from actual endpoint data; no new
        # independent endpoint values are appended. Continuous intertwining
        # factors through the two small identities already checked.
        stages.append({'history_dimension':n,'endpoint_rank':4,'active_rank':2,
                       'additional_endpoint_modes':2,'remaining_hidden_dimension':n-4})
        old={'Efull':Efull,'O':O,'N':N,'L0':L0}
    result={'schema':'marici.full-endpoint-fourier-bridge.v1','iteration':4,'passed':True,
      'endpoint_matrix':rows(M),'endpoint_characteristic_polynomial':str(S.factor(M.charpoly(x).as_expr())),
      'endpoint_basis':rows(Q),'complement_update':rows(K),'full_analytic_attachment':rows(J),
      'full_endpoint_continuous_generator_bridge':True,'existing_active_lift_unchanged':True,
      'missing_ports_recovered_from_retained_endpoint_data':True,'new_source_coordinates_added':False,
      'actual_stages':stages,'same_native_tick_Fourier_intertwiner_dimension':0,
      'added_Fourier_operation_commutes_with_native_tick':False,
      'full_analytic_metric_is_native_history_metric':False,
      'RH_proved':False}
    files=[Path(__file__),rp,NI/'photon_native_spatial_step.py',NI/'retained_path_successor.py',
           NI/'check_natural_tower_return.py',ROOT/'research/voevodsky/full-endpoint-fourier-bridge-v1.md']
    result['source_hashes']={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (ROOT/'research/voevodsky/results/full-endpoint-fourier-bridge-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_hashes','full_analytic_attachment')},indent=2))


if __name__=='__main__':main()
