# /// script
# dependencies = ["sympy"]
# ///
"""Independent top-down arrow source candidate, not a native physical H12."""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S
from hamiltonian_descent_wg import generate, zero, validate
from source_arrow_hamiltonian import construct, reducing_frame

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
NIMA=ROOT.parent/'nima'
OUT=ROOT/'results/source-arrow-hamiltonian-descent.json'
OUT.unlink(missing_ok=True)
# Source construction precedes loading the bottom model. The constructor
# receives only the existing seed permutation, port labels and declared scale.
with redirect_stdout(io.StringIO()):
    seed=runpy.run_path(str(NIMA/'checkers/check_seed_endpoint_sections.py'))
labels={'A':0,'B':3,'C':1,'D':2}
source,C,edges=construct(seed['V'],seed['forward'],labels,S.Rational(1,2))
validate(source)
E=S.eye(12)[:,:4]
G4=E.T*source.G*E
P=G4.inv()*E.T*source.G
witness=generate(source,E,P,'cycle-cover orbit, existing metric-adjoint restriction')
# Only now inspect the prior bottom rotor as an independent comparison target.
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(NIMA/'checkers/check_rotor_rung4_intertwiner.py'))
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
def refuse(name,call,message):
    try: call()
    except ValueError as error: check(name,message in str(error))
    else: raise AssertionError(name)

check('fresh-seed-unique-cover',len(seed['covers'])==1)
check('all-twelve-arrow-labels-retained',len(edges)==12 and set(edges)==set(seed['full']))
check('all-original-six-seed-labels-retained',set(seed['SEED'])<=set(edges))
check('source-permutation-order-four',C**4==S.eye(12) and C**2!=S.eye(12))
check('source-generator-not-bottom-up-lift',not zero(source.D-prior['D12']))
check('source-generator-rank-six',source.D.rank()==6)
check('source-energy-rank-six',source.K.rank()==6)
check('source-Hamiltonian-equation',zero(source.D.T*source.Omega-source.K))
check('source-metric-conservation',zero(source.D.T*source.G+source.G*source.D))
check('projection-equals-prior-fixed-Gram-map',zero(P-prior['P']))
check('independently-constructed-generator-descends-to-prior-D4',zero(witness.target.D-prior['D4']))
check('declared-half-scale-recovers-prior-form',zero(witness.target.Omega-prior['Omega4']))
check('declared-half-scale-recovers-prior-energy',zero(witness.target.K-prior['Hessian4']))
check('hidden-dynamics-rank-four', (witness.N*source.D*witness.N).rank()==4)
check('hidden-energy-rank-four',(witness.N.T*source.K*witness.N).rank()==4)
check('full-retained-metric-split',zero(source.G-P.T*witness.target.G*P-witness.N.T*source.G*witness.N))
for j in range(12):
    v=S.eye(12)[:,j]
    check(f'full-source-reconstruction/{j}',zero(E*P*v+witness.N*v-v))
for power in range(7):
    check(f'continuous-series-coefficient/{power}',zero(P*source.D**power-witness.target.D**power*P))
# Even an independently constructed top generator does NOT pick absolute
# energy units. Doubling the declared form/energy leaves D unchanged.
other,_,_=construct(seed['V'],seed['forward'],labels,S.Integer(1))
other_w=generate(other,E,P,'same declared orbit; different energy normalization')
check('source-normalization-not-selected-by-dynamics',zero(other.D-source.D)
      and zero(other_w.target.K-2*witness.target.K))
refuse('nonpositive-energy-normalization-refused',
       lambda:construct(seed['V'],seed['forward'],labels,0), 'positive declared energy normalization')

# Unlike the prior zero-hidden lift, arbitrary coordinate prefixes are not
# reducing: they can cut one of the genuine hidden rotor blocks.
E11=S.eye(12)[:,:11]
P11=(E11.T*source.G*E11).inv()*E11.T*source.G
refuse('naive-first-coordinate-drop-fails',lambda:generate(source,E11,P11,'naive12->11'),
       'hidden-to-visible dynamical obstruction')
framed,B,pairs,zeros=reducing_frame(source,E,P)
validate(framed)
check('hidden-frame-four-stationary-two-rotor-pairs',pairs==2 and zeros==4)
check('frame-keeps-visible-carrier-arrow-columns',B[:,:4]==E)
check('frame-retains-all-original-coordinates',B.rank()==12)
# Six admitted drops: four stationary directions, then two whole rotor pairs.
schedule=(12,11,10,9,8,6,4)
current=framed
T=B.inv() # relates current framed coefficients to original source coordinates
for n,m in zip(schedule,schedule[1:]):
    stepE=S.eye(n)[:,:m]
    stepP=(stepE.T*current.G*stepE).inv()*stepE.T*current.G
    step=generate(current,stepE,stepP,f'reducing modes{n}->{m}')
    check(f'six-step-intertwiner/{n}->{m}',zero(stepP*current.D-step.target.D*stepP))
    T=stepP*T
    current=step.target
check('six-step-projection-is-direct-projection',zero(T-P))
check('six-step-generator-is-direct-generator',zero(current.D-witness.target.D))
check('six-step-energy-is-direct-energy',zero(current.K-witness.target.K))
check('six-step-form-is-direct-form',zero(current.Omega-witness.target.Omega))
# Skew extraction realizes only active sectors, not the complete source tick.
active=-source.D**2/4
minus=(S.eye(12)-C+C**2-C**3)/4
quarter=S.eye(12)-active+source.D/2
check('alternating-source-sector-retained',minus.rank()==3)
check('rotor-does-not-realize-full-permutation',zero(quarter-C-2*minus) and C.det()==-1)
check('induced-arrow-action-not-an-automorphism-of-six-edge-seed',
      {seed['forward'][e[0]]+seed['forward'][e[1]] for e in seed['SEED']}!=set(seed['SEED']))
result={
 'schema':'marici.strominger.source-arrow-hamiltonian-descent.v1','status':'pass','checks':checks,
 'source_construction':'Independent D12=C12-C12^T, induced vertex-cycle action on all twelve directed carrier-arrow labels',
 'source_rules_supplied':['existing unique seed cycle-cover objective','induced S4 action on twelve arrows',
                          'historical four-port labeling','fixed stabilizer-probe Gram10I+J',
                          'skew-part angular flow rule','Omega=alpha G D; alpha=1/2 for prior energy convention'],
 'arrow_order':edges,'vertex_permutation':seed['forward'],'source_generator':[[str(v) for v in source.D.row(i)] for i in range(12)],
 'source_energy_rank':6,'visible_energy_rank':2,'hidden_energy_rank':4,
 'target_matches_prior_D4':True,'target_matches_prior_energy_at_declared_scale':True,
 'six_step_schedule':schedule,'six_step_frame':[[str(v) for v in B.row(i)] for i in range(12)],
 'naive_coordinate_descent':'fails12->11 because hidden rotor is cut',
 'continuous_intertwining':'P exp(t D12)=exp(t D4) P for all real t in supplied common angular parameter',
 'native_137_record_T9_identification':False,'physical_Hamiltonian_selection':False,'Postnikov_identification':False,
 'full_source_permutation_realized_by_rotor':False,
 'scope':'independent top-down mathematical carrier candidate, not source-selected physical H12 or native six-edge successor',
 'input_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                (Path(__file__),HERE/'source_arrow_hamiltonian.py',HERE/'hamiltonian_descent_wg.py',
                 NIMA/'checkers/check_seed_endpoint_sections.py',NIMA/'checkers/check_rotor_rung4_intertwiner.py')}
}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} independent source-arrow Hamiltonian descent checks')
print('Top-down angular generator reaches prior D4; nonzero hidden energy/dynamics retained.')
print('Six reducing-mode WG steps pass; naive coordinate drop fails. Native/physical/Postnikov identification remains open.')
