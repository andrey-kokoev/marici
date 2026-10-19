"""Exact interface test against the UNCHANGED retained path constructor."""
from contextlib import redirect_stdout
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import runpy

from seed_composition_port_summary import summarize, compose, final_occurrences

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT/'results/seed-composition-port-summary.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    prior = runpy.run_path(str(HERE/'check_actual_triangle_branch_composition.py'))
ledger = prior['ledger']
checks = []

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

formal_path=ROOT/'results/agda-SeedCompositionPortQuotient.json'
formal=json.loads(formal_path.read_text(encoding='utf-8-sig'))
check('formal-positive-path-closure-verified', formal['passed'] and formal['ignore_interfaces']
      and formal['inputs_stable_during_check'])
for name in ('SeedCompositionPortQuotient','ActualSeedEndpointTable',
             'SeedSeamPathComparisonBoundary','SeedFirstReturnActions','SeedArrivalEffects'):
    path=ROOT/'agda'/f'{name}.agda'
    check('formal-source-current/'+name,
          formal['owner_source_inventory_sha256'][path.name]==hashlib.sha256(path.read_bytes()).hexdigest())

registry = {e:(s,t,e) for e,s,t in ledger.packets}
def word(*labels):
    return tuple(registry[e] for e in labels)
def payload(labels, coefficient=F(1)):
    return ledger.retain_path_payload((word(*labels),), (coefficient,))
def product_square(left, right):
    actual = ledger.compose_payloads(left,right)
    predicted = compose(summarize(ledger,left), summarize(ledger,right))
    assert summarize(ledger,actual) == predicted
    parents,slots = ledger.deconstruct_payload(actual)
    assert parents == (left,right)
    return actual

# An actual same-arrival collision becomes observable to the old binary
# constructor: the starting port of the right operand controls admission.
left = payload(('CA',))
a = payload(('AB','BC'))
b = payload(('DB','BC'))
sa,sb = summarize(ledger,a),summarize(ledger,b)
check('same-old-final-occurrence-summary', final_occurrences(sa) == final_occurrences(sb))
check('different-starting-port-summary', sa != sb)
pa,pb = product_square(left,a),product_square(left,b)
check('same-left-context-distinguishes-products', len(pa.paths) == 1 and len(pb.paths) == 0)
check('old-summary-fails-binary-congruence',
      final_occurrences(summarize(ledger,pa)) != final_occurrences(summarize(ledger,pb)))

# Exhaustive basis-pair tests on actual existing stages. Bilinear extension
# is also tested below; the universal coefficient identity is stated in the note.
stages=[ledger.root]
for _ in range(4):
    stages.append(ledger.successor(stages[-1]))
singletons=[ledger.retain_path_payload((p,),(F(1),)) for stage in stages[:3] for p in stage.paths]
for x,y in product(singletons,repeat=2):
    product_square(x,y)
check('all-first-three-stage-basis-pairs', len(singletons) == 32)

families=[]
for stage in stages[:3]:
    n=len(stage.paths)
    for values in ((F(1),)*n,(F(0),)*n,tuple(F((-1)**i*(i+1),i+2) for i in range(n))):
        families.append(ledger.retain_payload(stage,values))
for x,y in product(families,repeat=2):
    product_square(x,y)
check('signed-zero-and-positive-family-products', len(families) == 9)

# Reuse actual source/target indexed families; keep coefficients attached to
# words rather than relying on the flattening order of a presentation.
for index,stage in enumerate(stages[:3]):
    original=families[3*index+2]
    values=dict(zip(original.paths,original.values))
    for direction in ('source','target'):
        family=ledger.family(stage,direction)
        assert ledger.deconstruct_family(family)==stage.paths
        paths=tuple(p for key,group in family.groups for p in group)
        regrouped=ledger.retain_path_payload(paths,tuple(values[p] for p in paths))
        assert summarize(ledger,regrouped)==summarize(ledger,original)
        product_square(regrouped,families[0])
check('both-existing-indexed-presentations-preserve-summary-square', True)

primitive=[payload((e,)) for e in registry]
for x,y,z in product(primitive,repeat=3):
    sx,sy,sz=(summarize(ledger,p) for p in (x,y,z))
    assert compose(compose(sx,sy),sz) == compose(sx,compose(sy,sz))
    xy_z=ledger.compose_payloads(ledger.compose_payloads(x,y),z)
    x_yz=ledger.compose_payloads(x,ledger.compose_payloads(y,z))
    assert xy_z.paths == x_yz.paths and xy_z.values == x_yz.values
    assert summarize(ledger,xy_z) == compose(compose(sx,sy),sz)
check('associative-on-all-primitive-triples', True)

# Structural support and coefficients are distinct: cancellations must not
# turn admitted ports into absent ports.
# Find distinct actual words with the same starting/final port.
groups={}
for p in stages[3].paths:
    groups.setdefault((p[0][0],p[-1][2]),[]).append(p)
pair=next(paths[:2] for paths in groups.values() if len(paths)>1)
zero_support=ledger.retain_path_payload(tuple(pair),(F(1),F(-1)))
szero=summarize(ledger,zero_support)
check('cancellation-retains-admitted-port', len(szero.entries)==1 and szero.entries[0][2]==0)
product_square(zero_support,families[0])
empty_summary=summarize(ledger,pb)
check('empty-domain-not-zero-valued-domain', empty_summary.entries==() and szero.entries!=())

# The summary does not pretend to recover full paths.
once=payload(('AB','BC','CA'))
twice=payload(('AB','BC','CA','AB','BC','CA'))
check('retained-history-still-finer', once.paths != twice.paths and summarize(ledger,once)==summarize(ledger,twice))
all_ports={(s,e) for stage in stages for s,e,v in summarize(ledger,ledger.retain_payload(stage,(F(1),)*len(stage.paths))).entries}
vertices={s for e,s,t in ledger.packets}|{t for e,s,t in ledger.packets}
check('all24-source-final-ports-reachable', all_ports==set(product(vertices,registry)))

result={
    'schema':'marici.nima.seed-composition-port-summary.v1','verification_status':'pass',
    'checks':checks, 'fresh_prior_checks':len(prior['checks']),
    'formal_receipt_sha256':hashlib.sha256(formal_path.read_bytes()).hexdigest(),
    'formal_scope':'All positive typed paths, binary congruence, and all typed prefix/suffix arrival contexts; not finite coefficient summation.',
    'basis_pairs_tested':len(singletons)**2, 'family_pairs_tested':len(families)**2,
    'primitive_triples_tested':len(primitive)**3,
    'stage_word_counts':[len(s.paths) for s in stages], 'reachable_port_count':len(all_ports),
    'hostile':{'left':['CA'],'right_a':['AB','BC'],'right_b':['DB','BC'],
               'same_old_final_occurrence':'BC','left_products_sizes':[len(pa.paths),len(pb.paths)]},
    'summary':'Starting vertex plus final occurrence, with summed rational coefficients AND admitted coarse support.',
    'operation':'Homomorphic observation of existing chronological endpoint-compatible compose_payloads; not a replacement constructor.',
    'scope':'Positive homogeneous retained path families, arbitrary exact rational coefficients; no zero-length identity paths in the ledger payload interface.',
    'not_claimed':['full-history or operand recovery from summary','physical transition/normalization selection','identification with intended T9 or J4','a universal minimum-state theorem'],
    'sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
              (Path(__file__),HERE/'seed_composition_port_summary.py',HERE/'retained_path_successor.py',HERE/'check_actual_triangle_branch_composition.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} composition-summary checks; {len(singletons)**2} basis pairs, {len(families)**2} family pairs,216 triples')
print('Binary composition requires the starting port; the source/final summary closes exactly with support retained.')
