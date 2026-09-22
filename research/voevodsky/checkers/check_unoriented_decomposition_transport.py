"""Relational opposite and decomposition naturality on actual frozen carriers.

Opposite relations describe predecessor compatibility, not authorized reverse
execution. Acceptance/rejection labels and vertex observations are retained.
"""
from pathlib import Path
import gzip
import hashlib
import json
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'research/voevodsky/results'
subprocess.run([sys.executable, str(Path(__file__).with_name('check_decomposition_coherence.py'))], check=True, capture_output=True, text=True)
pp = OUT / 'decomposition-coherence-carriers.json.gz'
rp = OUT / 'decomposition-coherence.json'
r = json.loads(rp.read_text())
assert hashlib.sha256(pp.read_bytes()).hexdigest() == r['packet_sha256']
with gzip.open(pp, 'rt') as f: packet = json.load(f)
carriers = packet['carriers']
F = {(x['from'], x['to']): x['map'] for x in packet['comparisons']}
def transpose(rel): return frozenset((b, a) for a, b in rel)
def compose(f, g):
    # Apply f then g.
    by_source = {}
    for b, c in g: by_source.setdefault(b, set()).add(c)
    return frozenset((a, c) for a, b in f for c in by_source.get(b, ()))
relations = []
for carrier in carriers:
    # Keep separate acceptance strata: rejection remains an observable self-loop.
    relations.append({(a, accepted): frozenset((i, row[a][1]) for i, row in enumerate(carrier['table']) if row[a][0] == accepted)
                      for a in range(18) for accepted in (False, True)})
involution_checks = composition_checks = naturality_checks = 0
max_predecessors = 0
for rels in relations:
    for rel in rels.values():
        assert transpose(transpose(rel)) == rel
        involution_checks += 1
        opposite = transpose(rel)
        for i in range(70):
            max_predecessors = max(max_predecessors, sum(a == i for a, b in opposite))
    for f in rels.values():
        for g in rels.values():
            assert transpose(compose(f, g)) == compose(transpose(g), transpose(f))
            composition_checks += 1
for (i, j), mapping in F.items():
    for key, rel in relations[i].items():
        def transport(rr): return frozenset((mapping[a], mapping[b]) for a, b in rr)
        assert transport(rel) == relations[j][key]
        assert transport(transpose(rel)) == transpose(relations[j][key])
        naturality_checks += 1
    # Source-coordinate compatibility and vertex outputs travel with each end.
    for a, b in enumerate(mapping):
        assert carriers[i]['canonical_states'][a] == carriers[j]['canonical_states'][b]
        assert carriers[i]['outputs'][a] == carriers[j]['outputs'][b]
# Typed composition is associative in relations; exhaust actual generator triples
# on one carrier (other carriers are related by verified bijections).
base = list(relations[0].values())
associativity_checks = 0
for f in base:
    for g in base:
        fg = compose(f, g)
        for h in base:
            assert compose(fg, h) == compose(f, compose(g, h))
            associativity_checks += 1
report = {
    'passed': True,
    'decompositions': len(carriers),
    'states_per_carrier': 70,
    'relation_strata_per_carrier': 36,
    'double_transpose_checks': involution_checks,
    'composition_reversal_checks': composition_checks,
    'decomposition_reversal_naturality_checks': naturality_checks,
    'generator_associativity_checks_on_reference_carrier': associativity_checks,
    'maximum_reverse_successors': max_predecessors,
    'theorem': 'Relational transpose is involutive and reverses composition; every source-coordinate decomposition comparison commutes with transpose. Finite generator checks extend to all finite words by relational composition.',
    'interpretation': 'A single source-bound relation has forward and backward presentations. Backward edges express compatible predecessors, carrying the same vertex values and acceptance stratum.',
    'scope': 'Backward compatibility, not a new reverse acquisition/delivery constructor. Same frozen reachable carrier, labels, bindings, outputs and atomic semantics.',
    'packet_sha256': hashlib.sha256(pp.read_bytes()).hexdigest(),
}
(OUT / 'unoriented-decomposition-transport.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
