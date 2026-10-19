# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Compare the universal native port gate with the existing response fixture.

No seed-to-matrix map is constructed. This records the obligation on a proposed
binding preserving the fixture's nonzero mixed response and the gate's premises.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import hashlib
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/seed-port-response-descent-gate.json'
OUT.unlink(missing_ok=True)
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)

formal_path=ROOT/'results/agda-SeedPortResponseDescentGate.json'
formal=json.loads(formal_path.read_text(encoding='utf-8-sig'))
check('fresh-formal-gate-valid',formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check'])
for name in ('SeedPortResponseDescentGate','SeedCompositionPortQuotient','SeedFirstReturnActions','ActualSeedEndpointTable'):
    path=ROOT/'agda'/f'{name}.agda'
    check('formal-source-current/'+name,formal['owner_source_inventory_sha256'][path.name]==hashlib.sha256(path.read_bytes()).hexdigest())
with redirect_stdout(io.StringIO()):
    experiment=runpy.run_path(str(HERE/'check_source_exchange_end_to_end.py'))
check('existing-instrument-chain-passes',experiment['result']['status']=='passed')
native=experiment['native']
values=native['values'];add,scale,mul=native['add'],native['scale'],native['mul']
def minus(a,b): return add(a,scale(-1,b))
def trace(a): return a[0][0]+a[1][1]
def determinant(a): return a[0][0]*a[1][1]-a[0][1]*a[1][0]
X=[values[f'ax{i}'] for i in range(2)]
Y=[values[f'ay{j}'] for j in range(2)]
check('existing-four-leg-values-invertible',all(determinant(a)==1 for a in X+Y))
C={(i,j):mul(Y[j],X[i]) for i in range(2) for j in range(2)}
mixed=add(minus(C[1,1],C[1,0]),minus(C[0,0],C[0,1]))
check('existing-mixed-factorization',mixed==mul(minus(Y[1],Y[0]),minus(X[1],X[0])))
check('nonzero-existing-mixed-trace',trace(mixed)==F(1,15))
residual={ij:minus(a,values['d']) for ij,a in C.items()}
check('fixed-reference-does-not-remove-mixed-response',
      add(minus(residual[1,1],residual[1,0]),minus(residual[0,0],residual[0,1]))==mixed)
raw=experiment['raw']
# Existing arrow block is ordered (i,j) with j the fast index.
check('actual-instrument-preparation-has-same-contrast',raw[12]-raw[11]-raw[1]+raw[0]==trace(mixed))
check('declared-gain-keeps-contrast-nonzero',experiment['gamma']*trace(mixed)==F(1,60))
result={
    'schema':'marici.nima.seed-port-response-descent-gate.v1','verification_status':'pass',
    'checks':checks,'formal_receipt_sha256':hashlib.sha256(formal_path.read_bytes()).hexdigest(),
    'fresh_instrument_support':experiment['result']['fresh_support_checks'],
    'fixture_mixed_matrix':[[str(x) for x in row] for row in mixed],
    'fixture_mixed_trace':str(trace(mixed)),
    'fixture_prepared_X_contrast':str(experiment['gamma']*trace(mixed)),
    'native_theorem':'Injective primitive effect actions plus full-effect factorization through typed source/final ports force all positive parallel path effects to agree.',
    'conditional_binding_obligation':'A binding preserving this nonzero fixture rectangle cannot also identify its full reversible effects with that arrival-port quotient. It must retain a finer effect state, use a noninjective effect law, or change the target response contract explicitly.',
    'scope':'No seed-to-matrix role map is supplied. The obstruction is not asserted for arbitrary scalar readouts of a hidden reversible state, noninjective effects, or unquotiented retained histories.',
    'objective_complete':False}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} native/fixture response-gate checks')
print('Existing mixed trace=1/15; declared preparation contrast=1/60.')
print('Full reversible mixed effects require more than the arrival-port quotient under the proved premises.')
