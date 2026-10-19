# /// script
# dependencies = ["sympy"]
# ///
"""Conditional matrix representation of full seed paths, not parity records.

All coefficients are constrained by the frozen target fixture. Internal frames
are explicit gauge choices; signed words are geometric paths, not newly
admitted directed execution events. Record-port binding remains separate.
"""
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/geometric-fixture-representation.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_joint_parity_fixture_binding.py'))
C,d,r=prior['C'],prior['d'],prior['r']
m=prior['m']; native=prior['native']
sources,targets=native['sources'],native['targets']
I=S.eye(2)
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
formal_path=ROOT/'results/agda-SeedGeometricResponseInterpretation.json'
formal=json.loads(formal_path.read_text(encoding='utf-8-sig'))
check('generic-native-interpretation-theorem-current',formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check'])
for name in ('SeedGeometricResponseInterpretation','SeedGeometricResponseState','SeedTetrahedronBridge','ActualSeedEndpointTable'):
    path=ROOT/'agda'/f'{name}.agda'
    check('formal-source-current/'+name,formal['owner_source_inventory_sha256'][path.name]==hashlib.sha256(path.read_bytes()).hexdigest())

# Normalize the existing reference-return algebra, NOT its physical reference.
# Phi(p)=d*rho(p) gives Phi(pq)=Phi(q)*r*Phi(p) for chronological p,q.
K={ij:r*value for ij,value in C.items()}
check('fourth-corner-compatibility',K[1,1]==K[0,1]*K[0,0].inv()*K[1,0])
X=K[0,0].inv()*K[1,0]
Y=K[0,1]*K[0,0].inv()
canonical={'AB':I,'AD':I,'BC':I,'BA':K[0,0],'DB':X,'CA':K[0,1]}
check('all-six-primitive-matrices-invertible',set(canonical)==set(sources) and all(a.det()!=0 for a in canonical.values()))

def signed(word): return tuple((e,1) for e in word)
def inverse(word): return tuple((e,-sign) for e,sign in reversed(word))
def evaluate(word,assignment=canonical):
    at='A';value=I
    for e,sign in word:
        s,t=(sources[e],targets[e]) if sign==1 else (targets[e],sources[e])
        if at!=s: raise AssertionError('Noncomposable geometric word')
        at=t
        matrix=assignment[e] if sign==1 else assignment[e].inv()
        value=matrix*value
    return at,value

def phi(word,assignment=canonical):
    end,value=evaluate(word,assignment)
    if end!='A': raise AssertionError('Expected a based loop')
    return d*value

loops={ij:signed(native['legs'][f'x{ij[0]}']+native['legs'][f'y{ij[1]}']) for ij in C}
check('empty-geometric-loop-maps-to-fixed-reference',phi(())==d)
check('BA-not-identified-with-inverse-AB',canonical['BA']!=canonical['AB'].inv())
for ij,word in loops.items():
    check('frozen-corner-exact/'+str(ij),phi(word)==C[ij])
    check('geometric-inverse-returns-reference/'+str(ij),phi(word+inverse(word))==d)
    for n in range(1,6):
        target=C[ij]
        for _ in range(n-1): target=C[ij]*r*target
        check('admitted-self-composition/'+str(ij)+'/'+str(n),phi(word*n)==target)
check('four-cycle-parity-collision-resolved',phi(loops[1,1]*2)!=phi(loops[1,1]))
check('same-original-repetition-defect',S.trace(phi(loops[1,1]*2)-phi(loops[1,1]))==-S.Rational(419,450))

# All invertible solutions of the four corner equations have the following
# form; the deduction is given in the note. Verify internal-frame freedom.
def assignment(P,Q,R):
    return {'AB':P,'AD':Q,'BC':R,'BA':K[0,0]*P.inv(),
            'DB':P*X*Q.inv(),'CA':K[0,1]*P.inv()*R.inv()}
frame_trials=[(I,I,I),(S.Matrix([[2,1],[1,1]]),S.Matrix([[1,2],[0,1]]),S.Matrix([[1,0],[3,1]])),
              (S.diag(2,3),S.Matrix([[0,-1],[1,0]]),S.Matrix([[1,1],[1,2]]))]
for n,(P,Q,R) in enumerate(frame_trials):
    chosen=assignment(P,Q,R)
    frames={'A':I,'B':P,'D':Q,'C':R*P}
    check('internal-frame-equations/'+str(n),all(chosen[e]==frames[targets[e]]*canonical[e]*frames[sources[e]].inv() for e in canonical))
    check('all-corners-frame-independent/'+str(n),all(phi(word,chosen)==C[ij] for ij,word in loops.items()))
    for left,right in product(loops.values(),repeat=2):
        check('based-concatenation-frame-independent/'+str(n)+'/'+str(left+right),phi(left+right,chosen)==phi(left+right))

# Reconstruct ALL137 numerical values using signed geometric loop generators.
# Inverses are mathematical geometric paths, not primitive seed occurrences.
base=loops[0,0]
xword=loops[1,0]+inverse(base)
yword=inverse(base)+loops[0,1]
check('geometric-generator-X',evaluate(xword)[1]==X)
check('geometric-generator-Y',evaluate(yword)[1]==Y)
check('inherited-unipotent-generators',(X-I)**2==S.zeros(2) and (Y-I)**2==S.zeros(2))
check('existing-reference-holonomy',evaluate(base)[1]==r)
representatives=[]
slot=0
for tag,size in (('a',11),('s',4)):
    for i,j in product(range(size),repeat=2):
        word=base+xword*i+yword*j
        actual=S.Matrix(m['source'][slot].value)
        check('existing-fixture-value/'+tag+str((i,j)),phi(word)==actual==Y**j*X**i)
        representatives.append({'label':list(m['source'][slot].label),'tag':tag,'i':i,'j':j,'word':word})
        slot+=1
check('all137-labelled-values-retained',slot==137 and len({tuple(p['label']) for p in representatives})==137)
check('numeric-duplicates-do-not-derive-state-branch',len({p['word'] for p in representatives})==121)
# Existing aggregate, with its original membership measure and reference.
mean=sum((phi(p['word']) for p in representatives),S.zeros(2))/137-d
old=S.Matrix(m['read_at_four'](m['right4']))
check('unchanged137-member-J4-reproduced',mean==old)

result={
    'schema':'marici.nima.geometric-fixture-representation.v1','verification_status':'pass',
    'checks':checks,'formal_receipt_sha256':hashlib.sha256(formal_path.read_bytes()).hexdigest(),
    'canonical_edge_matrices':{e:[[str(v) for v in row] for row in a.tolist()] for e,a in canonical.items()},
    'edge_determinants':{e:str(a.det()) for e,a in canonical.items()},
    'reference':'unchanged d=2I; normalized loop representation rho; response Phi=d*rho',
    'general_solution':'AB=P; AD=Q; BC=R; BA=K00 P^-1; DB=P K00^-1 K10 Q^-1; CA=K01 P^-1 R^-1, with P,Q,R invertible.',
    'frame_interpretation':'Internal frames gA=I,gB=P,gD=Q,gC=R P; all based loop responses are invariant.',
    'generating_geometric_words':{'base':base,'X':xword,'Y':yword},
    'numeric_fixture_rows_reproduced':137,'distinct_geometric_representatives':121,
    'J4':[[str(v) for v in row] for row in mean.tolist()],
    'conditional_value_representation_complete':True,'source_selected_rung_descent_complete':False,
    'scope':'Exact representation of the supplied numerical values and reference-return value law. Native theorem is generic; no Agda matrix instance or physical calibration is claimed.',
    'open_gates':['Matrix assignments are imposed by the frozen target, not selected by the bare seed.',
                  'Signed geometric inverses are not admitted directed execution events.',
                  'The137 labels, two branches, family sizes and equal weights are supplied target structure.',
                  'Record endpoints still differ: off-diagonal target products are not automatically admitted.',
                  'No identification of this representation with the intended T9 promotion or physical instruments.'],
    'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HERE/'check_joint_parity_fixture_binding.py',HERE/'check_shared_leg_dg_realization.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} conditional geometric/fixture representation checks')
print('All137 matrix values and unchanged J4 reproduced; typed self-composition and repetition now agree.')
print('Three internal GL2 frames remain; numerical calibration, record endpoints and T9 selection are not derived.')
