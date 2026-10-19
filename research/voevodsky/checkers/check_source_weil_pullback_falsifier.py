# /// script
# dependencies = ["sympy"]
# ///
"""Falsify full positive-form pullback through the actual constructed maps.
Exit zero means controls verified, NOT that the conjectured equality survived.
"""
from pathlib import Path
import hashlib,json,sys
import sympy as S
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
ST=ROOT/'research/strominger';sys.path.insert(0,str(ST/'checkers'))
from source_arrow_hamiltonian import construct


def main():
    bp=BASE/'results/carrier-fourier-orbit-bridge-v1.json'
    br=json.loads(bp.read_text());assert br['passed']
    for p,h in br['source_hashes'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    sp=ST/'results/source-arrow-hamiltonian-descent.json';sr=json.loads(sp.read_text())
    source,C,edges=construct(tuple('ABCD'),sr['vertex_permutation'],{'A':0,'C':1,'D':2,'B':3},S.Rational(1,2))
    E=S.eye(12)[:,:4];P=(E.T*source.G*E).inv()*E.T*source.G
    R=S.Matrix(br['projection_then_attachment']);r=S.ones(1,4)*R
    h=S.zeros(12,1)
    for i in range(4):h[i]=-1
    h[edges.index('AB')]=14
    assert P*h==S.zeros(4,1) and R*h==S.zeros(4,1)
    qg=(h.T*source.G*h)[0];qh=(h.T*source.K*h)[0]/2
    assert qg==2100 and qh==980
    v=S.zeros(12,1);v[edges.index('AD')]=1;v[edges.index('BC')]=-1
    assert r*v==S.zeros(1,1) and P*v!=S.zeros(4,1)
    assert (v.T*source.G*v)[0]==20 and (v.T*source.K*v)[0]/2==20
    # Actual quadratic descent obstruction: invisible directions not radical.
    N=S.eye(12)-E*P
    assert (N.T*source.G*N).rank()==8
    assert (N.T*source.K*N).rank()==4
    G4=E.T*source.G*E
    assert source.G==P.T*G4*P+N.T*source.G*N
    assert source.K==P.T*(E.T*source.K*E)*P+N.T*source.K*N
    # Rescue by declaring invisible directions zero changes the source form.
    visible_form=P.T*G4*P
    assert visible_form!=source.G and (h.T*visible_form*h)[0]==0
    result={'schema':'marici.source-weil-pullback-falsifier.v1','passed':True,
      'claim_under_test':'Existing positive source metric or Hamiltonian equals Weil pullback through the constructed analytic maps on all source states',
      'conjecture_for_existing_realization':'falsified',
      'generic_bridge_witness':{'arrow_order':list(edges),'coefficients':[str(x) for x in h],
        'analytic_image':'0','source_metric_square':str(qg),'source_Hamiltonian':str(qh),'Weil_of_zero':0},
      'riemann_specialization_witness':{'state':'e_AD-e_BC','analytic_image':'0',
        'source_metric_square':20,'source_Hamiltonian':20,'Weil_of_zero':0},
      'hidden_metric_rank':8,'hidden_energy_rank':4,
      'retention_recovers_source_but_does_not_make_Weil_readout_detect_hidden_energy':True,
      'quotient_visible_form_equals_original_source_form':False,
      'any_linear_test_preparation_after_current_analytic_map_repairs_kernel':False,
      'all_alternative_source_realizations_ruled_out':False,
      'unfixed_existential_conjecture_settled':False,
      'scope':'Exact kernel obstruction. No computation or sign claim about the Weil form on a nonzero test is needed.'}
    files=[Path(__file__),bp,sp,ST/'checkers/source_arrow_hamiltonian.py',
           ST/'checkers/hamiltonian_descent_wg.py',BASE/'source-weil-pullback-falsifier-v1.md']
    result['source_hashes']={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (BASE/'results/source-weil-pullback-falsifier-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_hashes'},indent=2))


if __name__=='__main__':main()
