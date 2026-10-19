# /// script
# dependencies = ["sympy"]
# ///
"""Check full cyclic transport, not just skew-generator transport, at each rung."""
from pathlib import Path
import hashlib,json,sys
import sympy as S
ROOT=Path(__file__).resolve().parents[3]
ST=ROOT/'research/strominger'
sys.path.insert(0,str(ST/'checkers'))
from source_arrow_hamiltonian import construct,reducing_frame
from hamiltonian_descent_wg import state,generate


def rows(M):return [[str(v) for v in M.row(i)] for i in range(M.rows)]

def main():
    receipt_path=ROOT/'research/voevodsky/results/carrier-fourier-orbit-bridge-v1.json'
    receipt=json.loads(receipt_path.read_text());assert receipt['passed']
    for p,h in receipt['source_hashes'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    srcpath=ST/'results/source-arrow-hamiltonian-descent.json'
    old=json.loads(srcpath.read_text())
    source,C,edges=construct(tuple('ABCD'),old['vertex_permutation'],{'A':0,'C':1,'D':2,'B':3},S.Rational(1,2))
    E=S.eye(12)[:,:4];P=(E.T*source.G*E).inv()*E.T*source.G;N=S.eye(12)-E*P
    framed,B,pairs,nzeros=reducing_frame(source,E,P)
    assert pairs==2 and nzeros==4
    schedule=(12,11,10,9,8,6,4)
    # Evaluate each original prefix directly in the source: even after one
    # failed step we do not invent a descended intermediate permutation.
    original=[]
    for m in schedule[1:]:
        Em=B[:,:m];Pm=(Em.T*source.G*Em).inv()*Em.T*source.G;Nm=S.eye(12)-Em*Pm
        defect=Pm*C*Nm
        rec={'source_dimension':12,'prefix_dimension':m,'full_tick_leakage_rank':defect.rank(),
             'generator_leakage_rank':(Pm*source.D*Nm).rank()}
        if defect!=S.zeros(m,12):
            j=next(j for j in range(12) if defect[:,j]!=S.zeros(m,1))
            h=Nm[:,j]
            assert Pm*h==S.zeros(m,1) and Pm*C*h!=S.zeros(m,1)
            rec.update({'hidden_input':rows(h),'visible_tick_output':rows(Pm*C*h)})
        original.append(rec)
    # Split hidden stationary space by the FULL source character projectors.
    Qplus=(S.eye(12)+C+C**2+C**3)/4
    Qminus=(S.eye(12)-C+C**2-C**3)/4
    plus=(Qplus*N).columnspace();minus=(Qminus*N).columnspace()
    assert len(plus)==len(minus)==2
    Bfix=S.Matrix.hstack(B[:,:8],*plus,*minus)
    assert Bfix.rank()==12 and Bfix[:,:4]==E
    assert all(C*v==v for v in plus) and all(C*v==-v for v in minus)
    current=state(Bfix.T*source.G*Bfix,Bfix.inv()*source.D*Bfix,
                  Bfix.T*source.Omega*Bfix,Bfix.T*source.K*Bfix,
                  source.provenance+('hidden stationary parity-resolved frame',))
    Ccur=Bfix.inv()*C*Bfix;total=Bfix.inv();steps=[]
    for n,m in zip(schedule,schedule[1:]):
        Ee=S.eye(n)[:,:m];Pe=(Ee.T*current.G*Ee).inv()*Ee.T*current.G
        step=generate(current,Ee,Pe,f'parity-resolved full-cycle descent {n}->{m}')
        Ce=Pe*Ccur*Ee
        assert Pe*Ccur*step.N==S.zeros(m,n)
        assert Pe*Ccur==Ce*Pe and Ccur*Ee==Ee*Ce
        assert step.N*Ccur==Ccur*step.N
        assert Ce**4==S.eye(m) and Ce.T*step.target.G*Ce==step.target.G
        assert Ccur.T*current.K*Ccur==current.K
        assert Ccur.T*current.Omega*Ccur==current.Omega
        # Both visible and hidden coordinates retain exact reconstruction.
        assert Ee*Pe+step.N==S.eye(n)
        total=Pe*total
        assert total*C==Ce*total and total*source.D==step.target.D*total
        steps.append({'from':n,'to':m,'full_tick_intertwining':True,
                      'generator_form_energy_gate':True,'hidden_reconstruction':True})
        current=step.target;Ccur=Ce
    assert total==P and Ccur==P*C*E
    assert current.D==P*source.D*E and current.K==E.T*source.K*E
    # Preserve iteration1 analytic attachment, with no new analytic seed choice.
    J=S.zeros(4);port={'AD':0,'DB':1,'BC':2,'CA':3}
    for j,e in enumerate(edges[:4]):J[port[e],j]=1
    F=S.zeros(4)
    for j in range(4):F[(j+1)%4,j]=1
    assert J*total*C==F*J*total
    result={'schema':'marici.fourier-six-step-descent.v1','iteration':3,'passed':True,
      'original_prefix_audit':original,
      'original_frame_full_cycle_all_prefixes_pass':all(r['full_tick_leakage_rank']==0 for r in original),
      'stationary_hidden_character_dimensions':{'plus_one':2,'minus_one':2},
      'parity_resolved_frame':rows(Bfix),'schedule':list(schedule),'verified_steps':steps,
      'composite_equals_original_direct_P':True,'full_Fourier_orbit_attachment_preserved':True,
      'declared_frame_change_not_physical_preparation':True,
      'native_history_tick_equals_Fourier_tick':False,'RH_proved':False}
    files=[Path(__file__),receipt_path,srcpath,ST/'checkers/source_arrow_hamiltonian.py',
           ST/'checkers/hamiltonian_descent_wg.py',ROOT/'research/voevodsky/fourier-six-step-descent-v1.md']
    result['source_hashes']={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (ROOT/'research/voevodsky/results/fourier-six-step-descent-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_hashes','parity_resolved_frame','original_prefix_audit')},indent=2))
    print('Original prefix leakage:',[(r['prefix_dimension'],r['full_tick_leakage_rank']) for r in original])


if __name__=='__main__':main()
