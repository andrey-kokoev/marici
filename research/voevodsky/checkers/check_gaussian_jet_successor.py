# /// script
# dependencies = ["sympy"]
# ///
"""Test a fixed information-preserving Gaussian preparation, not a fitted form."""
import json
import sys
from hashlib import sha256
from pathlib import Path
import sympy as S
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/strominger/checkers'))
from source_arrow_hamiltonian import construct
from retained_hamiltonian_observer import construct_observer
CONTRACT = 'research/conjecture_net/contracts/rh-gaussian-jet-successor-candidate.v1.json'
NOTE = 'research/voevodsky/gaussian-jet-successor-v1.md'
OUT = 'research/voevodsky/results/gaussian-jet-successor-v1.json'

def load(p): return json.loads((ROOT/p).read_text())
def sha(p): return sha256((ROOT/p).read_bytes()).hexdigest()
def require(ok,msg):
    if not ok: raise ValueError(msg)
def rows(m): return [[str(v) for v in m.row(i)] for i in range(m.rows)]

def main():
    c = load(CONTRACT); require(not any(c['boundaries'].values()),'candidate scope changed')
    by = {n['id']:n for n in load('research/conjecture_net/contracts/rh-realization-work-net.v1.json')['conjectures']}
    require(by['successor-form-candidate']['verdict']=='constructed' and by['weil-form-comparison']['verdict']=='rejected','kernel/form gate conflation')
    for key in ('successor-form-candidate','weil-form-comparison'):
        require(by[key]['candidate_contract']==CONTRACT and by[key]['outcome'] is None and by[key]['evidence']==['gaussian-jet-successor'],'registration mismatch')
    require(by['rh-cross-realization-assembly']['status']=='open' and by['rh-cross-realization-assembly']['required_verdicts']['weil-form-comparison']=='constructed','negative form promoted into assembly')
    for path in c['lineage']:
        receipt = load(path)
        for p,h in receipt['source_hashes'].items(): require(sha(p)==h,'lineage source drift: '+p)
    prior=load(c['lineage'][0]); rotor=load(c['lineage'][1])
    require(prior['conjecture_for_existing_realization']=='falsified','old rejection lost')
    native=load('research/strominger/results/source-arrow-hamiltonian-descent.json')
    source,C,edges=construct(tuple('ABCD'),native['vertex_permutation'],{'A':0,'C':1,'D':2,'B':3},S.Rational(1,2))
    w=construct_observer(source.D).witness
    K6=10*w.target.K
    require(w.P*w.E==S.eye(6) and source.K==w.P.T*K6*w.P,'active factorization')
    require(source.K*w.N==S.zeros(12) and w.P.rank()==6,'radical gate')
    # Since f0 is everywhere nonzero, linear independence reduces to that of
    # monomials. A six-point Vandermonde provides an exact finite certificate.
    V=S.Matrix([[S.Integer(i)**j for j in range(6)] for i in range(6)])
    require(V.det()!=0,'Gaussian jet dependence')
    h=S.Matrix([S.Rational(v) for v in prior['generic_bridge_witness']['coefficients']])
    v=S.zeros(12,1); v[edges.index('AD')]=1; v[edges.index('BC')]=-1
    for witness,energy in ((h,980),(v,20)):
        require(w.P*witness!=S.zeros(6,1),'stored witness still invisible')
        require((witness.T*source.K*witness)[0]/2==energy,'source energy changed')
    x0=w.E*S.eye(6)[:,0]
    require(w.P*x0==S.eye(6)[:,0],'f0 preparation mismatch')
    energy=S.simplify((x0.T*source.K*x0)[0]/2)
    lo,hi=map(S.Rational,rotor['certified_Weil_interval'])
    require(0<lo<hi<energy,'candidate not separated by stored certified test')
    # Source preparation and its norm are not recomputed from the target value.
    result=dict(schema='marici.gaussian-jet-successor.v1',passed=True,
                verdict='rejected_for_Weil_form_identity',kernel_gate='passed',
                separate_candidate_and_form_dispositions_verified=True,
                source_energy=str(energy),certified_half_Weil_interval=[str(lo),str(hi)],
                positive_gap_lower_bound=str(energy-hi),prepared_source=rows(x0),
                active_reader=rows(w.P),active_hessian=rows(K6),
                Gaussian_basis_Vandermonde_determinant=str(V.det()),
                old_hidden_and_Riemann_witnesses_seen=True,
                unchanged_source_energy=True,quadrature_rerun=False,
                preparation_natively_derived=False,all_alternative_preparations_refuted=False,
                RH_proved=False,
                source_sha256={p:sha(p) for p in [CONTRACT,NOTE,*c['lineage'],
                    'research/strominger/checkers/source_arrow_hamiltonian.py',
                    'research/strominger/checkers/retained_hamiltonian_observer.py',
                    Path(__file__).relative_to(ROOT).as_posix()]})
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('passed','verdict','kernel_gate','source_energy',
                         'certified_half_Weil_interval','positive_gap_lower_bound')},indent=2))

if __name__=='__main__': main()
