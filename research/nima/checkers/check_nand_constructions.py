"""NAND constructor audit. Exact finite sets, Boolean algebras, and a Heyting hostile.
Obligations: forward realization, route compatibility, readout descent.
Conjecture: input-indexed Pi into Empty constructs NAND on decidable truth types;
fixed covariant E/P assembly and coherence rearrangement alone do not.
"""
from itertools import product
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parents[1]

def functions(domain, codomain):
    return tuple(product(codomain, repeat=len(domain)))

def nand(a, b):
    return not (a and b)

def wolfram(op, a, b, c):
    return op(op(op(a, b), c), op(a, op(op(a, c), a)))

rows = []
finite_route_cases = 0
choice_collapse = None
for na, nb in product(range(4), repeat=2):
    A, B = tuple(range(na)), tuple(range(nb))
    AB = tuple(product(A, B))
    direct = functions(AB, ())
    curried = functions(A, functions(B, ()))
    def curry(f):
        return tuple(tuple(f[AB.index((a, b))] for b in B) for a in A)
    def uncurry(g):
        return tuple(g[A.index(a)][B.index(b)] for a, b in AB)
    assert {curry(f) for f in direct} == set(curried)
    assert all(uncurry(curry(f)) == f for f in direct)
    assert all(curry(uncurry(g)) == g for g in curried)
    assert bool(direct) == nand(bool(A), bool(B))
    tagged_refutations = [('left', f) for f in functions(A, ())] + [('right', g) for g in functions(B, ())]
    assert bool(tagged_refutations) == bool(direct)
    if na == nb == 0:
        assert len(tagged_refutations) == 2 and len(direct) == 1
        choice_collapse = {'sum_of_refutations': 2, 'joint_refutation': 1,
                           'interpretation': 'same inhabitation, different retained witness spaces'}
    if na <= 1 and nb <= 1:
        rows.append({'a': na, 'b': nb, 'direct': len(direct), 'curried': len(curried),
                     'sum_of_refutations': len(tagged_refutations)})
    finite_route_cases += 1

bits = (False, True)
assert all(wolfram(nand, a, b, c) == c for a, b, c in product(bits, repeat=3))
assert all(nand(a, a) == (not a) for a in bits)
assert all(nand(nand(a, b), nand(a, b)) == (a and b) for a, b in product(bits, repeat=2))
assert all(nand(nand(a, a), nand(b, b)) == (a or b) for a, b in product(bits, repeat=2))

# Geometric route: a DECLARED forbidden corner, not supplied by commutation.
corners = tuple(product((0, 1), repeat=2))
allowed = set(corners) - {(1, 1)}
fibres = {corner: tuple(v for v in allowed if v == corner) for corner in corners}
assert all(bool(fibres[(a, b)]) == nand(a, b) for a, b in corners)
rotated = {(1-b, a) for a, b in allowed}
assert rotated != allowed
alternate_markings = [{'forbidden': list(forbidden),
                      'truth_table': [int(c != forbidden) for c in corners]}
                     for forbidden in corners]
assert len({tuple(m['truth_table']) for m in alternate_markings}) == 4

# Powerset route: complement relative to an explicit universe, intersection
# constructed as the shared-membership pullback. Test the identity pointwise.
U = frozenset(range(3))
subsets = tuple(frozenset(i for i in U if mask & (1 << i)) for mask in range(8))
set_nand = lambda A, B: U - (A & B)
assert all(wolfram(set_nand, A, B, C) == C for A, B, C in product(subsets, repeat=3))
assert all((i in set_nand(A, B)) == nand(i in A, i in B)
           for A, B in product(subsets, repeat=2) for i in U)

# Exact two-input Boolean function closure. Four bits encode 00,01,10,11.
def closure(initial, operations):
    found = set(initial)
    while True:
        expanded = found | {op(a, b) for op in operations for a, b in product(found, repeat=2)}
        if expanded == found:
            return found
        found = expanded
positive = closure({0, 15, 12, 10}, [lambda a, b: a & b, lambda a, b: a | b])
assert positive == {0, 8, 10, 12, 14, 15} and 7 not in positive
nand_generated = closure({12, 10}, [lambda a, b: (~(a & b)) & 15])
assert len(nand_generated) == 16

# Intuitionistic negative control: upward-closed sets of the chain 0<1.
# The middle proposition exists in this Heyting algebra but is not decidable.
worlds = frozenset({0, 1})
opens = (frozenset(), frozenset({1}), worlds)
def intuitionistic_not(A):
    return frozenset(w for w in worlds if not any(v >= w and v in A for v in worlds))
heyting_nand = lambda A, B: intuitionistic_not(A & B)
failures = [(A, B, C, wolfram(heyting_nand, A, B, C))
            for A, B, C in product(opens, repeat=3)
            if wolfram(heyting_nand, A, B, C) != C]
assert failures
A, B, C, actual = failures[0]
assert C != intuitionistic_not(intuitionistic_not(C))

files = [Path(__file__), BASE/'agda/NandConstructions.agda']
packet = {
    'status': 'nand-constructed-with-explicit-empty-target-or-complement',
    'obligations': ['forward realization', 'route/coherencer compatibility', 'readout descent'],
    'boolean_rows': rows, 'finite_function_space_route_cases': finite_route_cases,
    'wolfram_boolean_cases': 8, 'powerset_identity_cases': 512,
    'retained_choice_hostile': choice_collapse,
    'marked_corner_alternatives': alternate_markings,
    'unmarked_square_does_not_select_forbidden_corner': True,
    'positive_EP_boolean_function_count': len(positive),
    'positive_EP_contains_NAND': False, 'NAND_generated_function_count': len(nand_generated),
    'heyting_counterexample': {'a': sorted(A), 'b': sorted(B), 'c': sorted(C), 'left_side': sorted(actual)},
    'scope': 'Exact finite semantic models. Arbitrary fixed-covariant E/P terms are monotone by induction; variable input-indexed Pi into Empty introduces contravariance. No global Choice or Booleanity theorem for all types.',
    'sha256': {str(p.relative_to(BASE)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
}
(BASE/'results/nand-constructions.json').write_text(json.dumps(packet, indent=2)+'\n', encoding='utf-8')
print('NAND routes pass. Positive E/P shadow: 6 functions, NAND absent. Joint refutation: NAND; tagged alternatives retain extra witnesses. Heyting hostile found.')
