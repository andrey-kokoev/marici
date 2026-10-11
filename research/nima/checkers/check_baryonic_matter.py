"""Finite natural-S4 character and permutation-operator Gram diagnostic.

The old SM matter assignment is withdrawn. See ../s4-gram-action-comparison.md
and the earlier ../weak-doublet-singlet-weight-and-s4-representation-audit.md.
Original bytes are in ../quarantine/20261007-s4-evidence/checkers/.
No physical gauge group, matter multiplicity or masses are derived here.
"""
from itertools import permutations
from pathlib import Path
import json
from fractions import Fraction as F

ROOT = Path(__file__).resolve().parents[1]
pts = list(range(4))
s4 = list(permutations(pts))
char_table = {
    'Triv':  [1, 1, 1, 1, 1],
    'Sign':  [1, -1, 1, 1, -1],
    'Std2':  [2, 0, 2, -1, 0],
    'Std3a': [3, 1, -1, 0, -1],
    'Std3b': [3, -1, -1, 0, 1],
}
class_sizes = [1, 6, 3, 8, 6]


def cycle_index(p):
    visited = [False] * 4
    cyc = []
    for i in range(4):
        if not visited[i]:
            length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = p[j]
                length += 1
            cyc.append(length)
    return tuple(cyc.count(k) for k in range(1, 5))


def conj_class(p):
    return [(4, 0, 0, 0), (2, 1, 0, 0), (0, 2, 0, 0),
            (1, 0, 1, 0), (0, 0, 0, 1)].index(cycle_index(p))


# Preserve the original full matrix construction, including composition order.
# Its entries are Hilbert-Schmidt overlaps of natural permutation matrices;
# indexing by 24 group elements does not make it a nondegenerate regular Gram.
G = [[0]*24 for _ in range(24)]
for i in range(24):
    for j in range(24):
        inv_i = tuple(s4[i].index(k) for k in range(4))
        comp = tuple(s4[j][inv_i[k]] for k in range(4))
        G[i][j] = sum(1 for k in range(4) if comp[k] == k)

natural_character = [sum(p[k] == k for k in range(4)) for p in s4]
natural_multiplicities = {
    name: sum(F(natural_character[i]*chi[conj_class(p)], 24)
              for i, p in enumerate(s4)) for name, chi in char_table.items()}
assert natural_multiplicities == {'Triv': 1, 'Sign': 0, 'Std2': 0, 'Std3a': 1, 'Std3b': 0}
assert [sum(conj_class(p) == j for p in s4) for j in range(5)] == class_sizes
for name, chi in char_table.items():
    for other, psi in char_table.items():
        assert sum(F(n* x*y, 24) for n, x, y in zip(class_sizes, chi, psi)) == (name == other)

result = {
    'schema': 'marici.nima.baryonic-matter-bridge.v2',
    'status': 'finite_representation_only',
    'classification': 'natural_S4_is_trivial_plus_standard_three_dimensional',
    'natural_multiplicities': {k: int(v) for k, v in natural_multiplicities.items()},
    'operator_gram_shape': [24, 24],
    'comparison_packet': 's4-gram-action-comparison.md',
    'stronger_existing_construction': 'weak-doublet-singlet-weight-and-s4-representation-audit.md',
    'not_established': 'Physical SM gauge group, matter, generations, masses or selected charges.'}

if __name__ == '__main__':
    (ROOT/'results/baryonic-matter-bridge.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
