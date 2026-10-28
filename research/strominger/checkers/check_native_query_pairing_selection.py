"""Exact pairing counterexample and conditional uniform-measure repair.

Independent finite replay of the documented native query; not a rerun of its
Agda binding or an apparatus/physical authority proof.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
source = BASE / 'contracts/task-relative-memory-selection.v1.json'
edges = json.loads(source.read_text())['source']['edges']
idx = {v: i for i, v in enumerate('ABCD')}
identity = tuple(range(4))
def compose(g,h): return tuple(g[h[i]] for i in range(4))
def inverse(g): return tuple(g.index(i) for i in range(4))
generators = [(1,2,0,3),(3,0,2,1)]
seen = {identity}; todo = [identity]
for g in todo:
    for h in generators:
        k = compose(g,h)
        if k not in seen: seen.add(k); todo.append(k)
group = sorted(seen)
assert len(group) == 12
features = {name: tuple(F(g[idx[a]] == idx[b]) for g in group)
            for name,a,b in edges}
checks = []
def check(name, value):
    if not value: raise AssertionError(name)
    checks.append(name)
def dot(x,y,metric): return sum((a*b*d for a,b,d in zip(x,y,metric)), F(0))

results = []
for d in (1,2):
    # The double-transposition conjugacy class gets weight d. All others 1.
    weights = tuple(F(d if g != identity and compose(g,g) == identity else 1)
                    for g in group)
    for h in permutations(range(4)):
        for g,w in zip(group,weights):
            conjugate = compose(compose(h,g),inverse(h))
            check(f'conjugation-invariance/{d}/{h}/{g}', weights[group.index(conjugate)] == w)
    norms = {e:dot(f,f,weights) for e,f in features.items()}
    check(f'equal-feature-norms/{d}', set(norms.values()) == {F(d+2)})
    # Equivalent to normalizing each feature; common scalar is put in metric.
    metric_q = tuple(w/F(d+2) for w in weights)
    metric = metric_q + (F(1),)*6
    names = list(features)
    def event(state,e):
        q,r = state[:12],list(state[12:]); f = features[e]; j=names.index(e)
        observed = dot(f,q,metric_q); delta=r[j]-observed
        r[j]=observed
        return tuple(qi+fi*delta for qi,fi in zip(q,f))+tuple(r)
    basis = [tuple(F(i==j) for i in range(18)) for j in range(18)]
    for e in names:
        columns = [event(b,e) for b in basis]
        check(f'involution/{d}/{e}', all(event(c,e)==b for c,b in zip(columns,basis)))
        check(f'whole-domain-isometry/{d}/{e}', all(
            dot(columns[i],columns[j],metric)==(metric[i] if i==j else 0)
            for i in range(18) for j in range(18)))
    initial = tuple([F(0)]*12+[F(e=='AB') for e in names])
    first = event(initial,'AB'); final = event(first,'BA')
    check(f'common-first-state/{d}', first == features['AB']+(F(0),)*6)
    response = final[12+names.index('BA')]
    check(f'predicted-response/{d}', response==F(d,d+2))
    check(f'common-prepared-budget/{d}', dot(initial,initial,metric)==1)
    # Exact criterion for left invariance; the repair supplies this stronger law.
    left_invariant = all(weights[group.index(compose(h,g))]==weights[group.index(g)]
                         for h in group for g in group)
    check(f'left-invariance-separates/{d}', left_invariant==(d==1))
    gram = [[str(dot(features[e],features[f],metric_q)) for f in names] for e in names]
    results.append({'double_transposition_weight':d,'other_weights':1,
                    'AB_BA_record':str(response),'left_invariant':left_invariant,
                    'normalized_gram':gram})
check('same-query-different-continuation',results[0]['AB_BA_record']!=results[1]['AB_BA_record'])
# Left multiplication carries the identity to EVERY group element. Hence a
# left-invariant positive weight is constant; unit total mass fixes it to 1/12.
check('left-action-transitive', {compose(h,identity) for h in group}==set(group))
paths = [Path(__file__).resolve(),source,
         ROOT/'research/nima/agda/NativeSeedTransitionProbe.agda',
         ROOT/'research/nima/native-seed-transition-probe.md',
         BASE/'native-query-pairing-selection-repair-v1.md']
report = {'status':'pass','checks':len(checks),'group_size':len(group),'edge_order':list(features),
          'models':results,'conjecture':'refuted: native query plus conjugation symmetry does not select the pairing or response',
          'repair':'left-translation invariant measure selects the normalized Gram; locality, real linear isometry, matched-state fixing and nonidentity select exchange',
          'scope':'Exact finite algebra; arbitrary-word uniqueness is the written induction from identical selected event maps. No new Agda or physical selection theorem.',
          'sha256':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
out=BASE/'results/native-query-pairing-selection/verification.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'pass','checks':len(checks),'responses':[r['AB_BA_record'] for r in results],
                  'repair':'conditional; left invariance is additional authority'}))
