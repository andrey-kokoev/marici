"""Source-level proof DAG audit; not a primitive inference normalization."""
from pathlib import Path
import re
import json
import hashlib

ROOT = Path(__file__).resolve().parents[3]
source = ROOT / 'research/nima/agda/WolframConverse.agda'
text = source.read_text(encoding='utf-8')
names = re.findall(r'^  ((?:s|t)\d+|sh1|sh2) :', text, re.M)
bodies = {}
for name in names:
    match = re.search(r'^  ' + name + r'\b[^\n]* = ([\s\S]*?)(?=\n  \S|\n\n|\Z)', text, re.M)
    assert match, name
    bodies[name] = match.group(1)
deps = {n: sorted(set(re.findall(r'\b(?:[st]\d+|sh[12])\b', b))) for n, b in bodies.items()}

cache = {}
def closure(n, active=frozenset()):
    assert n not in active, ('cycle', n)
    if n not in cache:
        cache[n] = {n}.union(*(closure(d, active | {n}) for d in deps[n]))
    return cache[n]

# Guard against accidentally dropping the multiline bridge and hiding its cost.
assert set(deps['sh1']) == {'s2281', 's2426', 's2556'}
assert 'sh2' in closure('t3')

reconstruction = ROOT / 'research/nima/agda/WolframBooleanAlgebra.agda'
used = sorted(set(re.findall(r'\bt\d+\b', reconstruction.read_text(encoding='utf-8'))))
targets = sorted(set(used + ['t95', 't147', 't158', 's2426', 'sh1']))
result = {
    'scope': 'Named-equation dependency DAG; counts are not primitive inference counts or proof optimality.',
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'reconstruction_sha256': hashlib.sha256(reconstruction.read_bytes()).hexdigest(),
    'named_equations': len(names),
    'direct_reconstruction_dependencies': used,
    'targets': {n: {'equation': next(l.strip() for l in text.splitlines() if l.startswith('  ' + n + ' :')),
                    'ancestors_including_target': len(closure(n)),
                    'dependencies': deps[n]} for n in targets},
    'combined_ancestors': len(set().union(*(closure(n) for n in targets))),
    'unused_named_equations': sorted(set(names) - set().union(*(closure(n) for n in targets))),
    'proposed_bridge': {
        'premises': ['sh2', 's2426'],
        'named_ancestor_union': len(closure('sh2') | closure('s2426')),
        'baseline_sh1_ancestors': len(closure('sh1')),
        'warning': 'New bridge inference cost is not included; this is not a normalized proof-length win.'
    },
    'dag': deps,
}
out = ROOT / 'research/voevodsky/results/wg-ucc-audit/proof-dependencies.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in result.items() if k != 'dag'}, indent=2))
