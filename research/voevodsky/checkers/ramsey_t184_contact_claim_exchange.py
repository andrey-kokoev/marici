"""Does opposite-contact exchange lift to a permutation of four claim sites?"""
from itertools import combinations, permutations
from pathlib import Path
import json

D = Path(__file__).resolve().parents[1] / 'results'
geo = json.loads((D / 'esd7_explicit_analytical_census.json').read_text())
verts = {v['id']: v['barycentric'] for v in geo['vertices']}
tets = {t['id']: set(t['vertices']) for t in geo['tetrahedra']}
central = tets['T184']
labels = sorted(central, key=lambda v: verts[v].index(1))
ports = [next(s for k, s in tets.items() if k != 'T184' and central - {v} <= s) for v in labels]
edges = list(combinations(range(4), 2))
exchange = {e: tuple(i for i, v in enumerate(labels) if v in ports[e[0]] & ports[e[1]]) for e in edges}
assert all(set(e).isdisjoint(f) and exchange[f] == e for e, f in exchange.items())

def matches(p):
    return [e for e in edges if tuple(sorted(p[i] for i in e)) == exchange[e]]

perms = list(permutations(range(4)))
best = max(len(matches(p)) for p in perms)
claim_swap = (1, 0, 3, 2)
assert best == len(matches(claim_swap)) == 4
assert all(set.intersection(*(set(exchange[e]) for e in edges if i in e)) == set() for i in range(4))
out = dict(claims=['no R-', 'no B+', 'some R+', 'some B-'], proposed=list(claim_swap), matched=matches(claim_swap), unmatched=[e for e in edges if e not in matches(claim_swap)], max_matches=best, exact_lifts=sum(len(matches(p)) == 6 for p in perms), best_permutations=[p for p in perms if len(matches(p)) == best])
(D / 'ramsey_t184_contact_claim_exchange.json').write_text(json.dumps(out, indent=2)+'\n')
print(out)
