"""All 52 field partitions of the actual dependency-closed coupled protocol.

Rules, atomicity, bindings and outputs remain fixed. This tests changes of
ownership boundaries, not changes in scheduling or asynchronous semantics.
"""
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
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, x): p.write_text(json.dumps(x, indent=2) + '\n')
p = N / 'results/causal-interface-construction-contract.json'
c = json.loads(p.read_text())
fields, rules, labels = c['fields'], c['rules'], c['labels']
def partitions(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for part in partitions(rest):
        yield ((first,),) + part
        for i in range(len(part)):
            yield part[:i] + ((first,) + part[i],) + part[i+1:]
parts = sorted(set(partitions(tuple(fields))), key=repr)
assert len(parts) == 52
cp = OUT / 'decomposition-coherence-contract.json'
contract = {'owning_contract_sha256': sha(p), 'decompositions': parts,
 'fixed': ['operational rules', 'initial states', 'output expressions', 'source/task/run binding', 'same-snapshot atomicity'],
 'rule_ownership': 'Owner of updated field; origin-audit is owned by origin field component.',
 'prediction': 'All dependency-closed reachable carriers are isomorphic through source-coordinate comparisons, with strict composition coherence.',
 'scope': 'All partitions of the five existing fields. No hidden-field discovery, action splitting, delayed ports, or altered atomicity.'}
save(cp, contract)
subprocess.run([sys.executable, str(N / 'checkers/verify_causal_observer_interface.py')], check=True, capture_output=True, text=True)
spec = importlib.util.spec_from_file_location('expressions', N / 'checkers/construct_causal_observer_interface.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
carriers = []
for part in parts:
    owners = {f: i for i, block in enumerate(part) for f in block}
    # Recompute dependency closure before exploring this carrier.
    live = set().union(*(m.reads(x) for x in c['outputs']))
    for rule in rules.values(): live |= m.reads(rule['guard'])
    while True:
        before = set(live)
        for rule in rules.values():
            for target, expr in rule['updates'].items():
                if target in live: live |= m.reads(expr)
        if live == before: break
    assert live <= set(fields)
    blocks = tuple(tuple(f for f in block if f in live) for block in part)
    def encode(env): return tuple(tuple(env[f] for f in block) for block in blocks)
    def decode(state): return {f: v for block, values in zip(blocks, state) for f, v in zip(block, values)}
    ports = {}
    for name, rule in rules.items():
        target_fields = list(rule['updates']) or ['origin']
        actor_set = {owners[f] for f in target_fields}
        assert len(actor_set) == 1
        actor = next(iter(actor_set))
        guard = m.reads(rule['guard'])
        payload = set().union(*(m.reads(x) for x in rule['updates'].values()))
        assert guard | payload <= live
        ports[name] = {'actor': actor, 'guard': sorted(guard), 'payload': sorted(payload),
                       'remote_guard': sorted(f for f in guard if owners[f] != actor),
                       'remote_payload': sorted(f for f in payload if owners[f] != actor)}
    binding = m.digest(c['context'])
    def fetch(state, names, offered):
        if offered != binding: raise ValueError('foreign binding')
        env = decode(state)
        return {f: env[f] for f in names}
    def step(state, label):
        name, *args = label
        rule, port = rules[name], ports[name]
        env = fetch(state, port['guard'], binding)
        if not m.evaluate(rule['guard'], env, args): return False, state
        env.update(fetch(state, port['payload'], binding))
        full = decode(state)
        for target, expr in rule['updates'].items(): full[target] = m.evaluate(expr, env, args)
        return True, encode(full)
    initial = [encode(dict(zip(fields, s))) for s in c['initial_states']]
    seen = set(initial); todo = deque(initial); graph = {}
    while todo:
        state = todo.popleft(); row = []
        for label in labels:
            ok, nxt = step(state, label); row.append((ok, nxt))
            if nxt not in seen: seen.add(nxt); todo.append(nxt)
        graph[state] = row
    states = sorted(seen, key=repr); ids = {s: i for i, s in enumerate(states)}
    canonical = [tuple(decode(s)[f] for f in fields) for s in states]
    outputs = [tuple(m.evaluate(x, decode(s), []) for x in c['outputs']) for s in states]
    table = [[(ok, ids[nxt]) for ok, nxt in graph[s]] for s in states]
    try: fetch(states[0], live, 'foreign')
    except ValueError: pass
    else: raise AssertionError('foreign binding admitted')
    carriers.append({'partition': part, 'ports': ports, 'canonical_states': canonical,
                     'outputs': outputs, 'table': table, 'initial_ids': [ids[s] for s in initial]})
assert all(len(x['canonical_states']) == 70 for x in carriers)
lookup = [{s: i for i, s in enumerate(x['canonical_states'])} for x in carriers]
assert all(set(x) == set(lookup[0]) for x in lookup)
# Comparisons derived solely by source-coordinate identity, after exploration.
F = {(i, j): [lookup[j][s] for s in carriers[i]['canonical_states']]
     for i in range(52) for j in range(52)}
transition_checks = 0
for i in range(52):
    for j in range(52):
        f = F[i, j]
        assert [f[x] for x in carriers[i]['initial_ids']] == carriers[j]['initial_ids']
        for s, target in enumerate(f):
            assert carriers[i]['outputs'][s] == carriers[j]['outputs'][target]
            assert F[j, i][target] == s
            for a, (ok, nxt) in enumerate(carriers[i]['table'][s]):
                assert (ok, f[nxt]) == carriers[j]['table'][target][a]
                transition_checks += 1
triangle_checks = 0
for i in range(52):
    for j in range(52):
        for k in range(52):
            assert [F[j, k][x] for x in F[i, j]] == F[i, k]
            triangle_checks += 1
assert sha(p) == contract['owning_contract_sha256']
packet = {'contract_sha256': sha(cp), 'carriers': carriers,
          'comparisons': [{'from': i, 'to': j, 'map': f} for (i, j), f in F.items()]}
import gzip
pp = OUT / 'decomposition-coherence-carriers.json.gz'
pp.write_bytes(gzip.compress(json.dumps(packet, sort_keys=True, separators=(',', ':')).encode(), mtime=0))
report = {'passed': True, 'decompositions': 52, 'reachable_states_each': 70,
          'pair_comparisons': len(F), 'transition_checks': transition_checks,
          'strict_triangle_checks': triangle_checks,
          'contract_sha256': sha(cp), 'packet_sha256': sha(pp),
          'result': 'All independently explored carriers are strictly isomorphic under source-coordinate transport.',
          'scope': contract['scope'],
          'qualification': 'The expression semantics and atomic snapshots are shared. This certifies boundary regrouping, not automatic invariance under changes of operational semantics.'}
save(OUT / 'decomposition-coherence.json', report)
print(json.dumps(report, indent=2))
