"""Finite synthesis of labelled paths, endpoint fibers, and path composition.

Four vertices, all 12 directed nonidentity edges, retaining full edge words.
Reindexing preserves records. Pullback composition requires matching endpoints.
Repeated self-composition doubles path length; it is distinct from reindexing.
"""
from itertools import product

vertices = tuple(range(4))
edges = tuple((a,b) for a,b in product(vertices,repeat=2) if a != b)
paths1 = {(edge,) for edge in edges}


def source(p): return p[0][0]
def target(p): return p[-1][1]


def compose(left,right):
    return {p+q for p in left for q in right if target(p) == source(q)}


def fibers(paths, field):
    return {x: {p for p in paths if field(p) == x} for x in vertices}


def recover(family, field):
    for x, paths in family.items():
        assert all(field(p) == x for p in paths)
    return set().union(*family.values())


paths2 = compose(paths1,paths1)
paths4 = compose(paths2,paths2)
assert compose(compose(paths1,paths1),paths1) == compose(paths1,compose(paths1,paths1))
assert paths4 == compose(compose(compose(paths1,paths1),paths1),paths1)
for n, paths in ((1,paths1),(2,paths2),(4,paths4)):
    outgoing = fibers(paths,source)
    incoming = fibers(paths,target)
    assert recover(outgoing,source) == paths == recover(incoming,target)
    cycle = recover(fibers(recover(outgoing,source),target),target)
    assert cycle == paths
    assert len(paths) == 4*3**n
    assert all(len(p) == n for p in paths)
    assert all(len(f) == 3**n for f in outgoing.values())
    print(f'Length {n}: {len(paths)} distinct labelled paths; {3**n} per source; '
          f'{sum(source(p)==target(p) for p in paths)} closed paths.')
# Distinct histories must not collapse into their endpoint pair.
assert len({(source(p),target(p)) for p in paths2}) == 16 < len(paths2)
# A reverse traversal contributes a second edge, not a cancelled history.
assert ((0,1),(1,0)) in paths2
assert len(((0,1),(1,0))) == 2
print('Source/target reconstruction and reindexing cycles preserve all path records.')
print('Composition is associative and preserves full traversal history.')
print('Length doubling requires self-composition; reindexing alone leaves length unchanged.')
