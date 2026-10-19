# /// script
# dependencies = ["sympy"]
# ///
"""Freeze the existing native corners and matrix fixture, then test binding.

The unique linear corner interpolation is an audit control, not an authorized
source map. Only already-admissible target self-compositions are compared.
"""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/joint-parity-fixture-binding.json'
OUT.unlink(missing_ok=True)
fresh={}
def execute(name):
    path=HERE/name
    with redirect_stdout(io.StringIO()):
        data=runpy.run_path(str(path))
    fresh[name]=hashlib.sha256(path.read_bytes()).hexdigest()
    return data

native=execute('check_seed_joint_parity_response.py')
target=execute('check_endpoint_composition_gate.py')
checklist=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checklist.append(name)
check('existing-native-check-passes',native['result']['verification_status']=='pass')
check('existing-target-check-passes',target['result']['status']=='passed')
m=target['m']; rows=m['source']
selected={(i,j):rows[11*i+j] for i in range(2) for j in range(2)}
C={ij:S.Matrix(row.value) for ij,row in selected.items()}
d=S.Matrix(m['physical_reference'].value)
r=S.Matrix(target['r'])
check('unchanged-rung-reference-and-return',d==2*S.eye(2) and d*r==S.eye(2))
check('target-corners-have-distinct-record-targets',len({row.target for row in selected.values()})==4)
admissible=target['return_pairs'](tuple(selected.values()))
check('only-self-products-are-admitted-within-these-four-ports',set(admissible)=={(i,i) for i in range(4)})

# Native point (a,b) corresponds to source corner (i,j)=(1-a,1-b).
points=native['points']
images=[C[1-a,1-b] for a,b in points]
def vec(matrix): return S.Matrix(list(matrix))
fit=S.Matrix.hstack(*(vec(matrix) for matrix in images))
residual_fit=S.Matrix.hstack(*(vec(matrix-d) for matrix in images))
check('unique-linear-full-corner-fit-is-invertible',fit.det()!=0 and residual_fit.det()!=0)
for i,point in enumerate(points):
    check('exact-frozen-corner/'+str(point),fit*native['I'][:,i]==vec(images[i]))
fixture_mixed=C[1,1]-C[1,0]-C[0,1]+C[0,0]
check('mixed-record-maps-exactly',fit*native['vector']==vec(fixture_mixed))
check('residual-map-has-same-mixed-image',residual_fit*native['vector']==vec(fixture_mixed))
check('existing-nonzero-target-contrast',S.trace(fixture_mixed)==S.Rational(1,15))

# The scalar corner fit is determined by the fixed fixture, NOT by tuning
# a gain to match the native conjunction question.
scalar=S.Matrix([[S.trace(matrix-d) for matrix in images]])
check('fixed-scalar-table-derived',list(scalar)==[-S.Rational(29,15),-2,-2,-2])
check('fixed-scalar-table-formula',all(scalar[i]==-2+S.Rational(1,15)*(1-a)*(1-b)
                                    for i,(a,b) in enumerate(points)))

# Native r11 has zero parity shift. Repeating this VALID A-to-A word has
# identical finite output. At the existing target port, self-return is typed.
check('native-four-cycle-repetition-has-same-output',native['C'][1,1]==native['I'])
M=C[1,1]
repeated=M*r*M
check('typed-target-self-composition-is-not-idempotent',repeated!=M)
check('fixed-reference-scalar-also-separates-repetition',S.trace(repeated-d)!=S.trace(M-d))
check('exact-scalar-repetition-defect',S.trace(repeated-M)==-S.Rational(419,450))
# This is a failure of factorization through the finite observer, even for
# a nonlinear map agreeing on that point, not merely a poor linear fit.
self_failures=[]
for ij,value in C.items():
    source_after=native['C'][ij]**2*native['initial']
    check('native-self-product-returns-zero-parity/'+str(ij),source_after==native['initial'])
    self_value=value*r*value
    check('frozen-corner-fit-fails-typed-self-product/'+str(ij),vec(self_value)!=fit*source_after)
    self_failures.append({'corner':list(ij),'actual_target':[[str(x) for x in row] for row in self_value.tolist()]})

result={
    'schema':'marici.nima.joint-parity-fixture-binding.v1','verification_status':'pass',
    'checks':checklist,'fresh_checks_sha256':fresh,
    'linear_corner_map':[[str(x) for x in row] for row in fit.tolist()],
    'linear_corner_determinant':str(fit.det()),
    'residual_corner_determinant':str(residual_fit.det()),
    'fixed_scalar_values':list(map(str,scalar)),
    'mixed_trace':'1/15', 'typed_self_product_failures':self_failures,
    'four_cycle_repetition':{'native_finite_state':'unchanged (false,false)',
        'initial_target_residual_trace':str(S.trace(M-d)),
        'repeated_target_residual_trace':str(S.trace(repeated-d)),
        'difference':str(S.trace(repeated-M))},
    'conclusion':'Exact invertible static corner interpolation exists, but cannot bind native word concatenation to the existing target reference-return composition.',
    'scope':'Four frozen fixture slots and their already-admissible self-products. No seed-to-fixture endpoint map or identification with the whole137-row rung reader is asserted.',
    'objective_complete':False,
    'boundary':'The finer geometric state and raw histories are not excluded. Only factorization through this finite parity observer with the tested operation and reader is rejected.'}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checklist)} frozen native/fixture binding checks')
print('Exact static corner fit exists; all four typed self-compositions fail its operation square.')
print('Four-cycle repetition: fixed-reference trace defect=-419/450, despite identical parity output.')
