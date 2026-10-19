# /// script
# dependencies = ["sympy"]
# ///
"""Apply the existing Strominger observer to the same twelve-arrow candidate.
No source-owner result files are written. Energy normalization is derived.
"""
from pathlib import Path
import hashlib,json,sys
import sympy as S
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/voevodsky'
ST=ROOT/'research/strominger';sys.path.insert(0,str(ST/'checkers'))
from source_arrow_hamiltonian import construct
from retained_hamiltonian_observer import construct_observer


def main():
    prior_path=BASE/'results/source-weil-pullback-falsifier-v1.json'
    prior=json.loads(prior_path.read_text());assert prior['conjecture_for_existing_realization']=='falsified'
    for p,h in prior['source_hashes'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    receipt_path=ST/'results/source-arrow-hamiltonian-descent.json'
    receipt=json.loads(receipt_path.read_text())
    source,C,edges=construct(tuple('ABCD'),receipt['vertex_permutation'],
                            {'A':0,'C':1,'D':2,'B':3},S.Rational(1,2))
    observer=construct_observer(source.D);w=observer.witness
    # Native G=10I+J, and JD=0. Scale is forced by the source, not fitted.
    assert source.G*source.D==10*source.D
    assert source.K==10*w.source.K and source.Omega==10*w.source.Omega
    Kactive=10*w.target.K
    assert source.K==w.P.T*Kactive*w.P
    assert w.P.rows==source.K.rank()==6
    assert w.N.rank()==6 and source.K*w.N==S.zeros(12)
    assert source.D*w.N==S.zeros(12)
    assert w.N.T*source.G*w.N!=S.zeros(12) # energy radical is not norm radical
    for j in range(12):
        observation=observer.observe(S.eye(12)[:,j],'source basis control')
        assert observer.reconstruct(observation)==S.eye(12)[:,j]
        assert 10*observation.energy==(observation.source.T*source.K*observation.source)[0]/2
    h=S.Matrix([S.Rational(x) for x in prior['generic_bridge_witness']['coefficients']])
    oh=observer.observe(h,'previous analytic-kernel counterexample')
    assert oh.active!=S.zeros(6,1) and 10*oh.energy==980
    assert observer.reconstruct(oh)==h
    v=S.zeros(12,1);v[edges.index('AD')]=1;v[edges.index('BC')]=-1
    ov=observer.observe(v,'previous Riemann-specialization counterexample')
    assert ov.active!=S.zeros(6,1) and 10*ov.energy==20
    # Full source tick also descends, preserving the inherited energy.
    Cactive=w.P*C*w.E
    assert w.P*C==Cactive*w.P and Cactive**4==S.eye(6)
    assert Cactive.T*Kactive*Cactive==Kactive
    result={'schema':'marici.recovered-source-energy-observer.v1','passed':True,
      'prior_constructor':'research/strominger/checkers/retained_hamiltonian_observer.py',
      'source_dimension':12,'minimum_linear_energy_reader_dimension':6,
      'retained_zero_energy_dimension':6,'source_energy_scale_relative_to_generic_observer':10,
      'counterexample_energy_recovered':980,'riemann_counterexample_energy_recovered':20,
      'original_energy_not_redefined':True,'source_tick_intertwining':True,
      'all_twelve_source_basis_states_reconstructed':True,
      'source_positive_norm_descends_to_six_active_coordinates':False,
      'energy_reader_is_a_Weil_test_map':False,'previous_four_port_pullback_falsification_reversed':False,
      'scope':'Existing source energy observer repairs coefficient information loss, not arithmetic form identification.'}
    files=[Path(__file__),prior_path,receipt_path,ST/'checkers/retained_hamiltonian_observer.py',
           ST/'checkers/source_arrow_hamiltonian.py',ST/'checkers/hamiltonian_descent_wg.py',
           BASE/'bounded-search-energy-descent-repair-v1.md']
    result['source_hashes']={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (BASE/'results/recovered-source-energy-observer-v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_hashes'},indent=2))


if __name__=='__main__':main()
