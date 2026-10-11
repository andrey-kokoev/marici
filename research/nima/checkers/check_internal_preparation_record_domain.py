"""Admission gate for the proposed internal preparation.

The prior minimal bank stores discarded contrast Qx, so Pr=0. Test that
contract, rather than treating all 24 numerical coordinates as admissible.
This is not a theorem about every possible native retained-record model.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy
import sympy as S

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    model=runpy.run_path(str(HERE/'check_internal_history_preparation.py'))
U,E,t,base=model['U'],model['E'],model['t'],model['base']
P=S.ones(12)/12
Q=S.eye(12)-P
admit=S.diag(S.eye(12),Q)
read_bank_mean=S.zeros(12).row_join(P)
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)

check('old-bank-domain-rank-23',admit.rank()==23 and admit*admit==admit)
check('baseline-in-old-domain',admit*base==base)
check('old-return-preserves-domain',U*admit==admit*U)
check('old-write-is-contrast',read_bank_mean*U*admit==S.zeros(12,24))

# Arbitrary label permutations commute with P and therefore cannot produce
# a bank mean. Adjacent transpositions generate the full permutation group.
for i in range(11):
    R=S.eye(12)
    R.row_swap(i,i+1)
    frame=S.diag(R,R)
    check('frame-preserves-domain/'+str(i),frame*admit==admit*frame)
    check('frame-fixes-empty-baseline/'+str(i),frame*base==base)

leak=S.simplify(read_bank_mean*E*base)
expected=S.ones(12,1)*2*t*t/(3+2*t*t)
check('new-preparation-leaks-bank-mean',S.simplify(leak-expected)==S.zeros(12,1))
check('only-zero-control-admitted-on-baseline',S.solve(leak[0],t)==[0])
prepared=S.simplify((E*base).subs(t,1))
check('fixture-domain-violation',admit*prepared!=prepared)
check('fixture-mean-violation',read_bank_mean*prepared==S.ones(12,1)*S.Rational(2,5))

# Projecting the proposed state back is NOT a valid silent repair: it erases
# the excluded bank mean and changes both decoded payload and budget.
repaired=admit*prepared
decoder=S.eye(12).row_join(S.eye(12))
check('projection-changes-payload',decoder*repaired==S.ones(12,1)*S.Rational(3,5))
loss=S.simplify(S.Rational(20,3)*((prepared.T*prepared)[0]-(repaired.T*repaired)[0]))
check('projection-erases-budget',loss==S.Rational(64,5))

result={
    'schema':'marici.nima.internal-preparation-record-domain.v1','status':'pass','checks':checks,
    'tested_record_contract':'minimal discarded-coordinate bank r in ker(P), initialized at zero and updated by the prior memory lift',
    'candidate_disposition':'rejected as an operation on that existing domain for every nonzero t',
    'leakage':'P r = [2t^2/(3+2t^2)] u',
    'operator_class':'original return and all simultaneous carrier/bank coordinate permutations preserve the old domain and baseline; their compositions do too',
    'silent_repair_rejected':{'t':1,'decoded_payload_after_projection':'3u/5','discarded_budget':'64/5'},
    'scope':'conditional on the inspected numerical bank contract; no prohibition on explicitly enlarged record types',
    'required_new_source_data':'an admitted storage/write operation carrying the common mode and its source/decoder correspondence; not supplied by retaining arbitrary history in the abstract',
}
(HERE.parent/'results/internal-preparation-record-domain.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact record-domain checks')
print('REJECTED under existing mean-zero-bank contract: every nonzero preparation leaves the domain.')
print('Projection back changes the decoded payload and erases budget; no silent repair is valid.')
