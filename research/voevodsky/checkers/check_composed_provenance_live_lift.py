"""Frozen origin + acquisition-before-event-3 audits on the actual coupled system."""
from pathlib import Path
from collections import deque
import importlib.util
import subprocess
import sys
import json
import hashlib
ROOT = Path(__file__).resolve().parents[3]
N = ROOT / 'research/nima'
OUT = ROOT / 'research/voevodsky/results'
source_path = N / 'results/actual-source-evidence-coupling.json'
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, x):
    p.write_text(json.dumps(x, indent=2) + '\n')
spec = importlib.util.spec_from_file_location('minimization', N / 'checkers/check_compressed_observer_live_lift.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
labels = [('source', e, mark) for e in range(6) for mark in (0, 1)] + [('acquire',), ('deliver',), ('issue', 0), ('issue', 1)]
origin_labels = [('audit-origin', b) for b in (0, 1)]
acq_labels = [('audit-acquired-before-cut', b) for b in (0, 1)]
contract = {
    'source_sha256': sha(source_path),
    'base_labels': labels, 'origin_audit_labels': origin_labels, 'acquisition_audit_labels': acq_labels,
    'cut': 'first source event 3',
    'acquisition_predicate': 'An accepted acquire occurred while event 3 was absent; initializes false and thereafter persists.',
    'origin_predicate': 'Known initial prefix is [0,1]; invariant under all transitions.',
    'audit_semantics': 'Accept iff argument equals retained predicate; no state change. Rejection observable.',
    'prediction': 'The base class plus the two provenance bits lifts uniquely to the combined minimal observer; projections to individual audit observers commute.',
    'scope': 'Declared finite coupling and trusted initialization/retention. No unrestricted future audit guarantee.'
}
cp = OUT / 'composed-provenance-live-lift-contract.json'
save(cp, contract)
subprocess.run([sys.executable, str(N / 'checkers/verify_source_evidence_coupling.py')], check=True, capture_output=True, text=True)
data = json.loads(source_path.read_text()); raw = data['states']
# Lift reachable operational states with the dynamically accumulated acquisition bit.
initial = [(i, False) for i in data['initial_state_ids']]
queue = deque(initial); seen = set(initial); edges = {}
while queue:
    i, acquired = queue.popleft()
    edge_map = {tuple(a): j for a, j in raw[i]['transitions']}
    row = []
    for label in labels:
        admitted = label in edge_map
        j = edge_map.get(label, i)
        new_bit = acquired or (admitted and label == ('acquire',) and 3 not in raw[i]['word'])
        target = (j, new_bit)
        row.append((admitted, target))
        if target not in seen:
            seen.add(target); queue.append(target)
    edges[i, acquired] = row
states = sorted(seen); index = {s: k for k, s in enumerate(states)}
outputs = [(0, sum(1 << e for e in raw[i]['word']), raw[i]['received'], raw[i]['issued']) for i, _ in states]
origin = [int(raw[i]['word'][:2] == [0, 1]) for i, _ in states]
acquired = [int(b) for _, b in states]
base_table = [[(ok, index[j]) for ok, j in edges[s]] for s in states]
def table(with_origin, with_acq):
    return [row + ([(b == origin[i], i) for b in (0, 1)] if with_origin else [])
            + ([(b == acquired[i], i) for b in (0, 1)] if with_acq else [])
            for i, row in enumerate(base_table)]
tables = {'base': table(False, False), 'origin': table(True, False),
          'acquisition': table(False, True), 'combined': table(True, True)}
parts, quotients, witnesses = {}, {}, {}
for name, t in tables.items():
    parts[name], quotients[name], _ = m.partition(outputs, t)
    witnesses[name] = m.distinguishing(quotients[name])
# Determine minimal extra provenance actually needed in this instance.
base_to_acq = {}
for i, c in enumerate(parts['base']):
    base_to_acq.setdefault(c, set()).add(acquired[i])
acq_already_determined = all(len(v) == 1 for v in base_to_acq.values())
lift = {}
for i in range(len(states)):
    key = (parts['base'][i], origin[i], acquired[i])
    assert key not in lift or lift[key] == parts['combined'][i]
    lift[key] = parts['combined'][i]
projection_checks = 0
projections = {}
for name in ('base', 'origin', 'acquisition'):
    projection = {}
    for i in range(len(states)):
        child, parent = parts['combined'][i], parts[name][i]
        assert child not in projection or projection[child] == parent
        projection[child] = parent
    mapping = list(range(16))
    if name == 'origin': mapping += [16, 17]
    if name == 'acquisition': mapping += [18, 19]
    for child, q in enumerate(quotients['combined']):
        parent = projection[child]
        assert q['output'] == quotients[name][parent]['output']
        for local, global_label in enumerate(mapping):
            ok, target = q['transitions'][global_label]
            assert (ok, projection[target]) == quotients[name][parent]['transitions'][local]
            projection_checks += 1
    projections[name] = projection
all_labels = labels + origin_labels + acq_labels
step_checks = 0
for i, row in enumerate(tables['combined']):
    for label_index, (ok, j) in enumerate(row):
        label = all_labels[label_index]
        next_bit = bool(acquired[i]) or (ok and label == ('acquire',) and 3 not in raw[states[i][0]]['word'])
        assert int(next_bit) == acquired[j] and origin[i] == origin[j]
        target = lift[parts['base'][j], origin[j], acquired[j]]
        assert (ok, target) == quotients['combined'][lift[parts['base'][i], origin[i], acquired[i]]]['transitions'][label_index]
        step_checks += 1
for s in initial:
    i = index[s]
    assert acquired[i] == 0
    assert lift[parts['base'][i], origin[i], acquired[i]] == parts['combined'][i]
assert sha(source_path) == contract['source_sha256']
report = {
    'passed': True, 'contract_sha256': sha(cp), 'reachable_augmented_states': len(states),
    'minimal_state_counts': {k: len(v) for k, v in quotients.items()},
    'acquisition_bit_determined_by_base_class': acq_already_determined,
    'compatible_base_origin_acquisition_triples': len(lift),
    'projection_checks': projection_checks, 'all_label_lift_checks': step_checks,
    'partitions': parts, 'quotients': quotients, 'distinguishing_words': witnesses,
    'projections': projections, 'lift': [[*key, value] for key, value in sorted(lift.items())],
    'states': [[i, int(b)] for i, b in states],
    'scope': 'Complete finite transition proof for the frozen two audits. Acquisition provenance may already be encoded in operational continuation behavior; measured explicitly.',
}
save(OUT / 'composed-provenance-live-lift.json', report)
print(json.dumps({k: report[k] for k in ('passed', 'reachable_augmented_states', 'minimal_state_counts', 'acquisition_bit_determined_by_base_class', 'compatible_base_origin_acquisition_triples', 'projection_checks', 'all_label_lift_checks')}, indent=2))
