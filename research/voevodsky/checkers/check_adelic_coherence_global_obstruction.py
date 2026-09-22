"""Exact bounded-height local admission test; stdlib only.

Enumerate ALL nonzero reduced rationals of height <= 6. Every pair of
local constraints has a witness, but their triple intersection is empty.
No claim about transition/cycle coherence or physical clocks is tested.
"""
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
N = 6
# For reduced a/b with b>0, rational adelic height is max(|a|, b).
sources = {Q(a, b) for a in range(-N, N + 1) if a
           for b in range(1, N + 1) if gcd(abs(a), b) == 1}

def height(r):
    return max(abs(r.numerator), r.denominator)

def valuation_integer(n, p):
    n = abs(n)
    assert n > 0
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def norm(r, p):
    v = valuation_integer(r.numerator, p) - valuation_integer(r.denominator, p)
    return Q(p) ** (-v)

constraints = {
    'infinity': lambda r: Q(1, 3) <= r <= Q(1, 2),
    'p2': lambda r: norm(r, 2) == Q(2),
    'p3': lambda r: norm(r, 3) == Q(3),
}
fibers = {k: {r for r in sources if test(r)} for k, test in constraints.items()}
witnesses = {('infinity', 'p2'): Q(1, 2),
             ('infinity', 'p3'): Q(1, 3), ('p2', 'p3'): Q(1, 6)}
for (a, b), r in witnesses.items():
    assert height(r) <= N and constraints[a](r) and constraints[b](r)
    assert r in fibers[a] & fibers[b]
joint = set.intersection(*fibers.values())
assert not joint
# All rational witnesses satisfy the full product formula; primes >6
# contribute one because reduced numerator and denominator are <=6.
for r in sources:
    assert abs(r) * norm(r, 2) * norm(r, 3) * norm(r, 5) == 1
    assert max(Q(1), abs(r)) * max(Q(1), norm(r, 2)) * max(Q(1), norm(r, 3)) * max(Q(1), norm(r, 5)) == height(r)
# Independently enumerate the larger domain to certify the first admission.
extended = {Q(a, b) for a in range(-30, 31) if a
            for b in range(1, 31) if gcd(abs(a), b) == 1}
extended_joint = {r for r in extended if all(test(r) for test in constraints.values())}
assert extended_joint == {Q(11, 30), Q(13, 30)}
assert min(map(height, extended_joint)) == 30
assert norm(Q(5, 12), 2) == 4
assert not all(test(Q(5, 12)) for test in constraints.values())
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
for r in extended:
    product, adelic_height = abs(r), max(Q(1), abs(r))
    for p in primes:
        product *= norm(r, p)
        adelic_height *= max(Q(1), norm(r, p))
    assert product == 1 and adelic_height == height(r)
report = {
    'passed': True,
    'contract': 'Nonzero rational r, H(r)<=6; real interval [1/3,1/2], |r|_2=2, |r|_3=3. Other places unrestricted subject to height.',
    'source_count': len(sources),
    'pairwise_witnesses': {' & '.join(k): str(v) for k, v in witnesses.items()},
    'local_fibers': {k: [str(r) for r in sorted(v)] for k, v in fibers.items()},
    'joint_fiber': [],
    'minimum_joint_height': 30,
    'joint_fiber_at_height_30': [str(r) for r in sorted(extended_joint)],
    'extended_source_count': len(extended),
    'rejected_previous_witness': {'r': '5/12', '2_adic_norm': '4'}, 
    'checks': {'exhaustive_reduced_rational_enumeration': True,
               'pairwise_rational_witnesses': True,
               'product_formula_and_height_for_every_candidate': True,
               'empty_joint_fiber': True,
               'no_joint_witness_below_height_30': True,
               'joint_witnesses_at_height_30': True,
               'extended_product_formula_and_height': True,
               'incorrect_5_over_12_witness_rejected': True},
    'scope': 'Pairwise existential admission does not imply joint admission under a common height bound. Not a test of transition coherence, shared tact necessity, or physical realizability.',
    'supersedes': 'Earlier positivity-only checker did not establish pairwise rational realizability.'
}
out = ROOT / 'research/voevodsky/results/adelic-coherence-global-obstruction.json'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
