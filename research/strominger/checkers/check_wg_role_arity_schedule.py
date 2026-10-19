"""Bounded source-bound arity schedule comparison, not a WG phase adapter.

Read the existing checker's literal arity vertices; do not replace its kernel
or claim this combinatorial test verifies analytic/type-theoretic transport.
"""
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
source = ROOT / 'research/nima/check_arity_square_duoidal_contract.py'
tree = ast.parse(source.read_text(encoding='utf-8'))
vertices = None
for node in tree.body:
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'vertices'
                                          for t in node.targets):
        vertices = ast.literal_eval(node.value)
assert vertices == [(0, 0), (0, 1), (1, 1), (1, 0)]
# Operator's previously described chronological order, not silently Gray-sorted.
operator_order = [(0, 0), (0, 1), (1, 0), (1, 1)]

def distances(order):
    return [sum(a != b for a, b in zip(order[i], order[(i+1) % 4]))
            for i in range(4)]

checks = {
    'same_four_boundary_positions': set(vertices) == set(operator_order),
    'different_chronological_orders': vertices != operator_order,
    'source_gray_cycle': distances(vertices) == [1, 1, 1, 1],
    'operator_order_uses_two_diagonals': distances(operator_order) == [1, 2, 1, 2],
}
# A square rotation/reflection preserves adjacency; it cannot turn these two
# traversals into one another while keeping the elementary-edge interpretation.
checks['not_a_square_symmetry_relabelling'] = sorted(distances(vertices)) != sorted(distances(operator_order))
assert all(checks.values())
rejected = []
for name, condition in (
    ('same_vertex_set_proves_same_schedule', vertices == operator_order),
    ('operator_diagonals_are_single_arity_flips', max(distances(operator_order)) == 1),
):
    if condition:
        raise AssertionError('hostile accepted: ' + name)
    rejected.append(name)
result = {
    'schema': 'marici.wg-role-arity-schedule.v1', 'status': 'pass',
    'source': str(source.relative_to(ROOT)), 'source_order': vertices,
    'operator_order': operator_order, 'checks': checks, 'rejected_hostiles': rejected,
    'scope': 'Finite boundary incidence only; not proof of a phase interpretation, missing filler, polynomial degree, or physical time.'
}
output = ROOT / 'research/strominger/results/wg-role-arity-schedule-v1.json'
output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
