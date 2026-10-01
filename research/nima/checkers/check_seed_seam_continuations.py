"""Continuation semantics of the actual seam; distinguish free and admitted paths."""
from itertools import permutations
import check_seed_seam_mixed_boundary as seam
seed=seam.seed
# Existing endpoint-matched composition works on tuples whose first two fields
# are source and target. Primitive labels remain retained as the third field.
def encoded(word): return tuple((*seed.registry[e],e) for e in word)
primitive={(encoded((label,))) for label in seed.registry}

def paths_from(vertex,depth):
    if depth==0: return {()}
    layer={p for p in primitive if p[0][0]==vertex}
    for _ in range(1,depth): layer=seed.compose(layer,primitive)
    return {tuple(e[2] for e in p) for p in layer}

x0,x1=seam.x0,seam.x1
y0,y1=seam.y0,seam.y1
assert seam.endpoints(x0)[1]==seam.endpoints(x1)[1]=='B'
counts=[]
for depth in range(7):
    suffixes=paths_from('B',depth)
    for suffix in suffixes:
        p=x0+suffix;q=x1+suffix
        assert seam.endpoints(p)[1]==seam.endpoints(q)[1]
        assert p!=q
    # Same legal suffix TYPE follows from the common terminal B. Finite
    # enumeration tests that fact; it is not a bound on all continuations.
    counts.append(len(suffixes))
    for suffix in paths_from('A',depth):
        extended={p+suffix:c for p,c in seam.rectangle.items()}
        assert len(extended)==4 and sum(extended.values())==0
        assert len({seam.endpoints(p)[1] for p in extended})==1
        for label in seed.registry:
            assert sum(c*p.count(label) for p,c in extended.items())==0
print('Free B-continuation counts at depths 0..6:',counts)

# A separate declared admission language: all A-based words using each seed
# edge exactly once. Do not replace its joint relation by Cartesian marginals.
admitted=frozenset(word for word in permutations(seed.registry)
                    if seed.registry[word[0]][0]=='A'
                    and all(seed.registry[a][1]==seed.registry[b][0]
                            for a,b in zip(word,word[1:]+word[:1])))
def allowed_after(prefix):
    return frozenset(word[len(prefix):] for word in admitted if word[:len(prefix)]==prefix)
restricted0=allowed_after(x0);restricted1=allowed_after(x1)
assert restricted0 and restricted1 and restricted0!=restricted1
joint=frozenset((prefix,suffix) for prefix in (x0,x1) for suffix in allowed_after(prefix))
assert all(prefix+suffix in admitted for prefix,suffix in joint)
assert any(prefix+suffix not in admitted for prefix in (x0,x1)
           for suffix in restricted0|restricted1)
print('PASS: unrestricted endpoint continuations cannot distinguish the two parallel forward paths.')
print('PASS: retaining full words distinguishes them, while terminal/additive readers still annihilate the extended rectangle.')
print('CONTROL: edge-once admission distinguishes continuation fibers; marginal recombination admits forbidden histories.')
print('SCOPE: composition supplies faithful path syntax; history-sensitive permissions depend on an additional admission language.')
