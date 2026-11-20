"""Test barycentric permutations on actual cells; test scalar signed packets, separately from the cell test."""
from itertools import permutations, combinations, product
from pathlib import Path
import json
D = Path(__file__).resolve().parents[1]/'results'
g = json.loads((D/'esd7_explicit_analytical_census.json').read_text())
v = {r['id']:tuple(r['barycentric']) for r in g['vertices']}
t = {r['id']:frozenset(v[i] for i in r['vertices']) for r in g['tetrahedra']}
c = t['T184']; block = {s for s in t.values() if len(s & c)>=3}
assert len(block)==5
P = list(permutations(range(4)))
def sym(sites):
    return [p for p in P if all(frozenset(tuple(x[i] for i in p) for x in cell) in sites for cell in sites)]
G = sym(block); assert sym({c})==P and len(G)==8 and G==sym(set(t.values()))
E = list(combinations(range(4),2)); C = {e:tuple(i for i in range(4) if i not in e) for e in E}; S=(1,0,3,2)
def act(p,e): return tuple(sorted(p[i] for i in e))
orbits=sorted({tuple(sorted({act(p,e) for p in G})) for e in E}); allowed=[]; signed=[]
for x in product((-1,0,1),repeat=6):
    m=dict(zip(E,x)); n=sum(bool(a) for a in x)
    if all(m[C[e]]==-m[e] for e in E):
        allowed.append(n)
        if all(m[act(S,e)]==-m[e] for e in E):signed.append(n)
assert sorted(set(allowed))==[0,2,4,6] and sorted(set(signed))==[0,2,4]
out=dict(block_and_global_coordinate_symmetries=G, contact_orbits=orbits, claim_swap_preserves_cells=S in G, supports_with_opposition=sorted(set(allowed)),supports_with_both_sign_rules=sorted(set(signed)), scalar_forced_zero=[e for e in E if act(S,e)==e]);print(out);(D/'ramsey_t184_signed_contact_extension.json').write_text(json.dumps(out,indent=2)+'\n')
