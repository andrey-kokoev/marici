# /// script
# dependencies = ["sympy"]
# ///
"""Native137 observation closure gate, including a factored-leg hostile."""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import runpy
import sys
import sympy as S
from source_arrow_hamiltonian import construct
from hamiltonian_descent_wg import zero
from native_t9_hamiltonian_packet import build_packet, advance_packet

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
NIMA=ROOT.parent/'nima'
OUT=ROOT/'results/native-t9-hamiltonian-gate.json'
OUT.unlink(missing_ok=True)
if str(NIMA/'checkers') not in sys.path: sys.path.insert(0,str(NIMA/'checkers'))
with redirect_stdout(io.StringIO()):
    pinned=runpy.run_path(str(NIMA/'checkers/check_pinned_T9_software_contract.py'))
    seed=runpy.run_path(str(NIMA/'checkers/check_seed_endpoint_sections.py'))
fixture=pinned['m']
transport=pinned['T9']
m=fixture['m']
source,C,edges=construct(seed['V'],seed['forward'],{'A':0,'B':3,'C':1,'D':2},S.Rational(1,2))
D=S.SparseMatrix(source.D)
vertices=seed['V']
Cv=S.SparseMatrix(4,4,lambda i,j:int(vertices[i]==seed['forward'][vertices[j]]))
Dv=Cv-Cv.T
# Explicit proposed simultaneous two-leg coefficient action. This is not
# inferred from the pinned static software transport contract.
A=S.SparseMatrix(S.diag(S.kronecker_product(D,S.eye(12))+S.kronecker_product(S.eye(12),D),
                       S.kronecker_product(Dv,S.eye(4))+S.kronecker_product(S.eye(4),Dv)))
selected=tuple(vertices[a]+vertices[b] for a,b in fixture['E'])
omitted=edges.index('AB')
indices=tuple(12*edges.index(a)+edges.index(b) for a in selected for b in selected)+tuple(range(144,160))
missing=tuple(i for i in range(160) if i not in set(indices))
R=S.SparseMatrix(137,160,{(i,j):1 for i,j in enumerate(indices)})
E=R.T
H=S.SparseMatrix(160,23,{(j,i):1 for i,j in enumerate(missing)})
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
check('pinned-contract-freshly-rerun',pinned['result']['verification_status']=='pass')
check('native-omits-counted-AB-edge',len(selected)==11 and 'AB' not in selected)
check('source-cycle-does-not-preserve-selected-11',
      {seed['forward'][e[0]]+seed['forward'][e[1]] for e in selected} != set(selected))
check('exact-native-and-hidden-layout',len(indices)==137 and len(missing)==23
      and sorted(indices+missing)==list(range(160)))
check('coordinate-left-inverse',R*E==S.eye(137))
check('candidate-coefficient-generator-skew',A.T+A==S.zeros(160))
leak=R*A*H
check('native137-is-not-autonomous',not zero(leak))
# Kernel test suffices to refute EVERY candidate B with R A=B R.
h=next(i for i in range(23) if leak[:,i]!=S.zeros(137,1))
v=H[:,h]
check('equal-native-inputs-different-native-velocities',R*v==S.zeros(137,1) and R*A*v!=S.zeros(137,1))
projection=E*R
check('compressing-generator-does-not-repair-source-intertwiner',not zero(R*A-(R*A*E)*R))
# Observe the minimal invariant LINEAR coefficient-field envelope. R already
# fixes137 coordinates, so ranks reduce to a tall matrix with only23 columns.
ranks=[137]
blocks=[]
power=R
for order in range(1,4):
    power=power*A
    blocks.append(power*H)
    ranks.append(137+S.Matrix.vstack(*blocks).rank())
check('finite-observation-envelope-closes-at160',ranks[-1]==160)

I=m['I']
X={e:m['values'][f'ax{i}'] for i,e in enumerate(selected)}
Y={e:m['values'][f'ay{i}'] for i,e in enumerate(selected)}

def completion(missing_X,missing_Y):
    legs=dict(X)
    rights=dict(Y)
    legs['AB']=missing_X
    rights['AB']=missing_Y
    matrices=[m['mul'](rights[b],legs[a]) for a in edges for b in edges]
    matrices += [row.value for row in fixture['source'][121:]]
    return S.Matrix([[v for row in matrix for v in row] for matrix in matrices])

# Both are valid factored leg preparations of the mathematical completion;
# every original native value, label, mass and reference is identical.
f1=completion(I,m['scale'](2,I))
f2=completion(m['scale'](2,I),I)
original=S.Matrix([[v for r in row.value for v in r] for row in fixture['source']])
check('both-completions-match-entire-original137-fixture',R*f1==R*f2==original)
corner=12*omitted+omitted
reference=S.Matrix(1,4,[v for r in m['values']['d'] for v in r])
check('even-missing-corner-reference-matrix-agrees',f1[corner,:]==f2[corner,:]==reference)
check('missing-leg-completions-invertible',S.Matrix(I).det()!=0 and S.Matrix(m['scale'](2,I)).det()!=0)
check('factored-leg-hostile-native-derivatives-differ',not zero(R*A*(f2-f1)))
w=S.ones(1,137)/137
check('factored-hostile-first-aggregate-derivative-cancels',zero(w*R*A*(f2-f1)))
second=S.simplify(w*R*A*A*(f2-f1))
check('same-J4-and-first-derivative-different-second-derivative',not zero(second))
# The only admitted repair here is an explicitly EXTENDED retained packet,
# not changing T9 or silently introducing contexts for missing arrows.
p1=build_packet(f1,indices,fixture,transport,'declared omitted X_AB=I,Y_AB=2I; joint coefficient completion')
p2=build_packet(f2,indices,fixture,transport,'declared omitted X_AB=2I,Y_AB=I; joint coefficient completion')
check('unchanged-native-T9-packet',p1.native==p2.native==pinned['output'])
check('unchanged-original-J4',p1.native.observe(fixture)['J4']==pinned['observed']['J4'])
check('exact23-extra-slots-retained',len(p1.hidden)==len(p2.hidden)==23 and p1.hidden!=p2.hidden)
check('complete-source-reconstruction',p1.reconstruct()==f1 and p2.reconstruct()==f2)
check('source-derivatives-recoverable-only-with-extra-packet',
      R*A*p1.reconstruct()==R*A*f1 and R*A*p2.reconstruct()==R*A*f2)
# Snapshot compatibility of the retained SOFT transport with an explicitly
# supplied coefficient variation; not an admission of this physical evolution.
shift=f1+S.Rational(1,100)*A*f1
shifted=build_packet(shift,indices,fixture,transport,'declared exact rational coefficient sample, not physical time evolution')
check('shifted-source-reconstruction',shifted.reconstruct()==shift)
old_domain={(a.label,b.label) for a in fixture['source'] for b in fixture['source'] if a.target==b.target}
new_domain={(a.label,b.label) for family in shifted.native.final for a in fixture['leaves']((family,)) for b in fixture['leaves']((family,))}
check('extended-snapshot-does-not-create-native-contexts',new_domain==old_domain and len(new_domain)==977)
try: build_packet(f1,indices,fixture,transport,'')
except ValueError: check('unprovenanced-completion-refused',True)
else: raise AssertionError('unprovenanced-completion-refused')
# Exact angular quarter, not Euler sampling. For these source rotors,
# D^3=-4D and exp(pi D/4)=I+D^2/4+D/2. Tensor exponentials commute.
Q=S.eye(12)+D*D/4+D/2
Qv=S.eye(4)+Dv*Dv/4+Dv/2
U=S.SparseMatrix(S.diag(S.kronecker_product(Q,Q),S.kronecker_product(Qv,Qv)))
check('source-quarter-polynomial-admitted',zero(D**3+4*D) and zero(Dv**3+4*Dv))
step1=advance_packet(p1,U,A,fixture,transport,'declared angular quarter t=pi/4; not a measured clock')
step2=advance_packet(p2,U,A,fixture,transport,'declared angular quarter t=pi/4; not a measured clock')
check('exact-quarter-parent-and-result-retained',step1.parent==p1 and step1.result.reconstruct()==U*f1)
check('extended-step-coefficient-budget-preserved',
      (f1.T*f1).trace()==(step1.result.reconstruct().T*step1.result.reconstruct()).trace())
check('extended-step-quadratic-energy-preserved',
      ((A*f1).T*(A*f1)).trace()==((A*step1.result.reconstruct()).T*(A*step1.result.reconstruct())).trace())
check('initial-native-T9-equality-does-not-predict-next-J4',
      step1.result.native.observe(fixture)['J4']!=step2.result.native.observe(fixture)['J4'])
try: advance_packet(p1,2*U,A,fixture,transport,'hostile gain')
except ValueError: check('gain-bearing-step-refused',True)
else: raise AssertionError('gain-bearing-step-refused')
result={
 'schema':'marici.strominger.native-t9-hamiltonian-gate.v1','verification_status':'pass','checks':checks,
 'native_Hamiltonian_descent_status':'blocked for the proposed simultaneous source-arrow/state coefficient action',
 'native_contract':'nima.T9.exact-domain.software.v1','native_contract_unchanged':True,
 'candidate_rule':'A=(D_arrow tensor I+I tensor D_arrow) direct-sum (D_state tensor I+I tensor D_state)',
 'native_slots':137,'full_joint_coefficient_slots':160,'extra_retained_slots':23,
 'leakage_rank':leak.rank(),'observation_envelope_ranks':ranks,
 'native_indices':indices,'hidden_indices':missing,'source_arrow_order':edges,
 'factored_hostile':'Same original137 Y_j X_i values and same missing-corner2I matrix; (X_AB,Y_AB)=(I,2I) versus(2I,I). Matching that matrix does not authenticate a physical reference preparation.',
 'J4_second_derivative_difference':[[str(v) for v in second]],
 'extended_packet_reconstruction':True,'extended_exact_quarter_step':True,
 'quarter_clock':'supplied angular t=pi/4, not physical time calibration',
 'coefficient_budget_and_energy_preserved':True,'complete_parent_retained':True,'extra_contexts_admitted':False,
 'physical_identification':False,'Postnikov_identification':False,
 'scope':'mathematical candidate gate and explicit coefficient-field completion; envelope rank is not physical state count or minimal preparation cost',
 'inputs_sha256':{str(p.relative_to(ROOT.parent)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                 (Path(__file__),HERE/'native_t9_hamiltonian_packet.py',HERE/'source_arrow_hamiltonian.py',
                  NIMA/'checkers/check_pinned_T9_software_contract.py',NIMA/'checkers/check_rung_transport_diagram.py')}
}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} native-T9 Hamiltonian gate checks')
print(f'Native descent BLOCKED: missing23 joint slots affect its future; envelope {ranks}.')
print('Explicit extra retained packet reconstructs source; original T9/J4/domain remain unchanged at the fixture input.')
