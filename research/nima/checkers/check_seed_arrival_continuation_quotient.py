"""Bind the formal arrival quotient's ports to the existing path successor."""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import re
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT/'results/seed-arrival-continuation-quotient.json'
OUT.unlink(missing_ok=True)
module = ROOT/'agda/SeedArrivalContinuationQuotient.agda'
receipt_path = ROOT/'results/agda-SeedArrivalContinuationQuotient.json'
receipt = json.loads(receipt_path.read_text(encoding='utf-8-sig'))
assert receipt['passed'] and receipt['ignore_interfaces'] and receipt['inputs_stable_during_check']
assert receipt['source_sha256'] == hashlib.sha256(module.read_bytes()).hexdigest()
checks = []

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

seed = ROOT/'agda/ActualSeedEndpointTable.agda'
text = seed.read_text(encoding='utf-8')
sources = dict(re.findall(r'^source (AB|BC|CA|AD|DB|BA) = ([ABCD])$', text, re.M))
targets = dict(re.findall(r'^target (AB|BC|CA|AD|DB|BA) = ([ABCD])$', text, re.M))
check('formal-table-has-exact-six-occurrences', set(sources) == set(targets) == {'AB','BC','CA','AD','DB','BA'})
with redirect_stdout(io.StringIO()):
    prior = runpy.run_path(str(HERE/'check_actual_triangle_branch_composition.py'))
check('same-existing-successor-endpoint-registry', prior['registry'] == {e:(sources[e],targets[e]) for e in sources})
transitions = {(e,f) for e in sources for f in sources if targets[e] == sources[f]}
check('six-state-ten-transition-domain', len(sources) == 6 and len(transitions) == 10)
check('exact-existing-successor-support', transitions == set(prior['words']))
role_support = {name:set(map(tuple, row['words'])) for name,row in prior['report'].items()}
check('existing-role-products-cover-transitions', set.union(*role_support.values()) == transitions)
check('existing-role-products-disjoint', sum(map(len,role_support.values())) == len(transitions))
# Binding receipts do not rely only on a top-level source hash.
for name in ('ActualSeedEndpointTable','SeedFirstReturnActions','SeedArrivalEffects',
             'SeedTriangleJointContext','SeedJointQuestionReadout'):
    path = ROOT/'agda'/f'{name}.agda'
    check('formal-input-inventory/'+name,
          receipt['owner_source_inventory_sha256'][path.name] == hashlib.sha256(path.read_bytes()).hexdigest())
result = {
    'schema':'marici.nima.seed-arrival-continuation-quotient.v1',
    'verification_status':'pass', 'checks':checks,
    'states':list(sources), 'transitions':sorted(map(list,transitions)),
    'role_support_sizes':{name:len(support) for name,support in role_support.items()},
    'formal_receipt_sha256':hashlib.sha256(receipt_path.read_bytes()).hexdigest(),
    'fresh_existing_successor_checks':len(prior['checks']),
    'theorem':'Current arrival equality iff equal arrival after every typed finite continuation, with empty continuation included.',
    'operation':'Existing arrive update; append a primitive occurrence at its actual matching endpoint.',
    'scope':'Exact contextual quotient for arrival-only observations, not recovery of histories, role correlations, or physical state.',
    'rung_binding':'Not identified with intended T9 or matrix J4; transition support agrees with the existing endpoint-compatible successor.'}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} port-binding checks; existing {len(prior["checks"])} successor checks rerun')
print('Six arrival states and ten transitions; all-future equivalence supplied by the fresh Agda theorem.')
