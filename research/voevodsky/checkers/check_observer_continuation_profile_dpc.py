"""Compare independently defined source observers with full continuation profiles."""
from pathlib import Path
from collections import deque
import json
import hashlib
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[3]
N = ROOT / 'research/nima'
OUT = ROOT / 'research/voevodsky/results'
p = N / 'results/actual-source-evidence-coupling.json'
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, x):
    p.write_text(json.dumps(x, indent=2) + '\n')
labels = [('source', e, m) for e in range(6) for m in (0, 1)] + [('acquire',), ('deliver',), ('issue', 0), ('issue', 1)]
contract = {
    'source_sha256': sha(p),
    'histories': 'Reachable coupled states, each a sufficient state presentation of its generating execution histories.',
    'continuations': 'All finite words in the 16 declared labels; any rejected prefix gives bottom.',
    'outputs': ['typed corner', 'received validated value or absence', 'issued value or absence'],
    'Q': 'Owning current_key: typed source corner, recorder and actual assembled row signature; exported current_class.',
    'Q_plus': 'Owning enriched_key additionally retains producer, received and issued evidence; exported enriched_class.',
    'prediction': 'Within each typed corner, Q equality iff equality of every continuation profile. Q_plus tested separately.',
    'equality_scope': 'Formal row-signature equality suffices for actual analytical equality; distinct signatures alone need not establish distinct actual calibrated values.'
}
cp = OUT / 'observer-continuation-profile-contract.json'
save(cp, contract)
subprocess.run([sys.executable, str(N / 'checkers/verify_source_evidence_coupling.py')], check=True, capture_output=True, text=True)
d = json.loads(p.read_text()); states = d['states']; n = len(states)
outputs = [(0, sum(1 << e for e in s['word']), s['received'], s['issued']) for s in states]
steps = [{tuple(e): j for e, j in s['transitions']} for s in states]
def classify(keys):
    ids = {}
    return [ids.setdefault(key, len(ids)) for key in keys]
classes = classify(outputs)
rounds = 0
while True:
    new = classify([(outputs[i], tuple((a in steps[i], classes[steps[i].get(a, i)]) for a in labels)) for i in range(n)])
    rounds += 1
    if new == classes:
        break
    classes = new
# Finite deterministic partition fixed point gives equivalence for ALL words.
for i in range(n):
    for j in range(i):
        if classes[i] == classes[j]:
            assert outputs[i] == outputs[j]
            for a in labels:
                assert (a in steps[i]) == (a in steps[j])
                if a in steps[i]: assert classes[steps[i][a]] == classes[steps[j][a]]

def distinguish(i, j):
    todo = deque([(i, j, ())]); seen = set()
    while todo:
        x, y, word = todo.popleft()
        if outputs[x] != outputs[y]: return word
        if (x, y) in seen: continue
        seen.add((x, y))
        for a in labels:
            if (a in steps[x]) != (a in steps[y]): return word + (a,)
            if a in steps[x]: todo.append((steps[x][a], steps[y][a], word + (a,)))
    return None

def describe(i):
    s = states[i]
    return {'id': i, **{k: s[k] for k in ('word', 'marks', 'producer', 'received', 'issued')}, 'profile_class': classes[i]}

def analyze(field):
    lost = redundant = None
    for i in range(n):
        for j in range(i):
            if outputs[i][:2] != outputs[j][:2]: continue
            equal = states[i][field] == states[j][field]
            if equal and classes[i] != classes[j] and lost is None and outputs[i] == outputs[j]:
                w = distinguish(i, j); assert w
                lost = {'histories': [describe(i), describe(j)], 'word': w}
            if not equal and classes[i] == classes[j] and redundant is None:
                redundant = {'histories': [describe(i), describe(j)],
                             'qualification': 'Different exported formal signatures; actual numerical distinction requires independent confirmation.'}
    return {'exported_classes': len({s[field] for s in states}),
            'continuation_loss_witness': lost, 'formal_redundancy_candidate': redundant,
            'sufficient': all(states[i][field] != states[j][field] or classes[i] == classes[j] for i in range(n) for j in range(i))}
current, enriched = analyze('current_class'), analyze('enriched_class')
assert current['continuation_loss_witness'] is not None
assert not current['sufficient'] and enriched['sufficient']
assert len(set(classes)) == 62
# Prove redundancy with recorder inequality, rather than signature inequality.
sp = ROOT / 'research/voevodsky/certificates/verify_filtered_obstruction.py'
import importlib.util
spec = importlib.util.spec_from_file_location('recorder', sp)
src = importlib.util.module_from_spec(spec); spec.loader.exec_module(src)
exact_redundancy = None
for i in range(n):
    for j in range(i):
        if classes[i] != classes[j]: continue
        ri = src.record(0, tuple(states[i]['word']), tuple(states[i]['marks']))
        rj = src.record(0, tuple(states[j]['word']), tuple(states[j]['marks']))
        if ri != rj:
            exact_redundancy = {'histories': [describe(i), describe(j)],
                                'reason': 'Exact authoritative recorder polynomials differ, while full continuation profiles agree.'}
            break
    if exact_redundancy: break
assert exact_redundancy is not None
assert sha(p) == contract['source_sha256']
report = {'verdict': 'REFUTED_FOR_FROZEN_ASSEMBLED_OBSERVER',
          'contract_sha256': sha(cp), 'history_states': n, 'profile_classes': len(set(classes)),
          'partition_rounds': rounds, 'current_observer': current, 'enriched_observer': enriched,
          'exact_redundancy_witness': exact_redundancy,
          'profile_partition': classes,
          'scope': 'Actual declared finite coupled protocol. Same-observer equality implies true analytical equality in the loss witness. Redundancy is independently established by exact recorder inequality. No universal impossibility or unique-source claim.'}
save(OUT / 'observer-continuation-profile-dpc.json', report)
print(json.dumps({k: v for k, v in report.items() if k != 'profile_partition'}, indent=2))
