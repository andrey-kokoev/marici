"""Compare existing retained-table schedules; no T9 or physical law is selected.

Reuse the owning indexing/recovery and path fixtures, including their regressions.
This finite set model checks provenance; it is not a fresh Agda closure.
"""
from dataclasses import dataclass
from pathlib import Path
import contextlib
import io
import json
import runpy
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/nima/checkers'))
log = io.StringIO()
with contextlib.redirect_stdout(log):
    tower = runpy.run_path(str(ROOT / 'research/nima/checkers/check_label_from_to_fibration_tower.py'))
    paths = runpy.run_path(str(ROOT / 'research/nima/checkers/check_indexed_path_synthesis.py'))
    diagram = runpy.run_path(str(ROOT / 'research/nima/checkers/check_rung_transport_diagram.py'))

Row, indexed, unindex = (diagram[k] for k in ('Row', 'indexed', 'unindex'))
E = tuple(Row(('arrow', a, b), ('vertex', a), ('vertex', b), ((a, b),))
          for a, b in sorted(paths['edges']))

@dataclass(frozen=True)
class RetainedRow:
    field: str
    key: tuple
    parent: object

    @property
    def label(self): return self.parent.label
    @property
    def source(self): return self.parent.source
    @property
    def target(self): return self.parent.target


def total(rows, field):
    # Indexing itself is the existing owner operation, not a replacement kernel.
    family = indexed(rows, field)
    result = tuple(RetainedRow(field, key, row)
                   for key, members in family.items() for row in members)
    for r in result:
        assert r.key == getattr(r.parent, field)  # finite membership witness
    assert {r.parent for r in result} == set(rows)
    return result


def base(row):
    while isinstance(row, RetainedRow):
        row = row.parent
    return row


def phase_trace(row):
    if not isinstance(row, RetainedRow): return ()
    return phase_trace(row.parent) + (row.field,)


def require_phase(rows, expected):
    if any(phase_trace(r) != expected for r in rows):
        raise ValueError('selected-column construction history mismatch')


def profile(rows, field):
    return sorted(len(v) for v in indexed(rows, field).values())


checks = {}
checks['same_twelve_retained_arrows'] = len(E) == 12
checks['label_profile'] = profile(E, 'label') == [1] * 12
checks['source_profile'] = profile(E, 'source') == [3] * 4
checks['target_profile'] = profile(E, 'target') == [3] * 4

# Historical retained-total recurrence: label first, then source.
H11 = total(E, 'label')
H10 = total(H11, 'source')
# Later source/target triple: source first, then target, with full prior row.
D11 = total(E, 'source')
D10 = total(D11, 'target')
require_phase(H11, ('label',))
require_phase(H10, ('label', 'source'))
require_phase(D11, ('source',))
require_phase(D10, ('source', 'target'))
checks['both_schedules_recover_exact_rows'] = all(
    {base(r) for r in rows} == set(E) for rows in (H11, H10, D11, D10))
checks['first_two_successors_are_not_same_marked_construction'] = (
    set(H11) != set(D11) and set(H10) != set(D10))

# Explicit comparison by retained base label, with both construction traces kept.
comparisons = []
for left, right in ((H11, D11), (H10, D10)):
    lookup = {r.label: r for r in right}
    pairs = tuple((l, lookup[l.label]) for l in left)
    assert {l for l, r in pairs} == set(left)
    assert {r for l, r in pairs} == set(right)
    assert all(base(l) == base(r) and
               (l.label, l.source, l.target) == (r.label, r.source, r.target)
               for l, r in pairs)
    comparisons.append(pairs)
checks['explicit_field_preserving_comparisons'] = len(comparisons) == 2

# Compare the nested total with the actual later endpoint-indexing implementation.
source_view = indexed(E, 'source')
target_view = indexed(unindex(source_view), 'target')
checks['later_family_recovery'] = unindex(source_view) == unindex(target_view) == E
checks['nested_total_matches_later_target_membership'] = all(
    base(r) in target_view[r.key] for r in D10)
checks['source_and_target_not_same_marked_fibers'] = source_view != target_view

# All eight historical transitions; no inferred edges10->9 or7->6 in the grid.
current = E
schedule = []
for i in range(8):
    field = ('label', 'source', 'target')[i % 3]
    current = total(current, field)
    expected = tuple(('label', 'source', 'target')[j % 3] for j in range(i + 1))
    require_phase(current, expected)
    assert {base(r) for r in current} == set(E)
    schedule.append({'rung': 11-i, 'field': field, 'depth': i+1, 'rows': len(current)})
checks['historical_eight_transitions'] = len(schedule) == 8 and schedule[-1]['rung'] == 4
checks['no_row_count_descent'] = all(s['rows'] == 12 for s in schedule)

rejected = []
for name, rows, expected in (
    ('label_first_substituted_for_source_first', H11, ('source',)),
    ('source_outer_substituted_for_target_outer', H10, ('source', 'target')),
    ('equal_recovery_erases_phase', D10, ('label', 'source')),
    ('eight_transitions_reported_as_six', current,
     ('label', 'source', 'target', 'label', 'source', 'target')),
):
    try:
        require_phase(rows, expected)
    except ValueError:
        rejected.append(name)
    else:
        raise AssertionError('hostile accepted: ' + name)
checks['four_phase_and_count_hostiles'] = len(rejected) == 4
assert all(checks.values()), checks

sample = ('arrow', 0, 1)
def encode(row):
    if isinstance(row, RetainedRow):
        return {'field': row.field, 'key': row.key, 'parent': encode(row.parent)}
    return {'label': row.label, 'source': row.source, 'target': row.target,
            'payload': row.value}

result = {
    'schema': 'marici.wg-rung-schedule-comparison.v1',
    'status': 'pass', 'checks': checks, 'rejected_hostiles': rejected,
    'source': 'All twelve endpoint-labelled nonidentity arrows on four vertices',
    'sample_0_to_1': {name: encode(next(r for r in rows if r.label == sample))
                      for name, rows in (('historical11', H11), ('historical10', H10),
                                         ('diagram11', D11), ('diagram10', D10))},
    'historical_schedule': schedule,
    'reused_suite_output': log.getvalue().splitlines(),
    'native_promotion': 'Source inspected only; no fresh Agda compilation or T9 adapter claimed',
    'remaining_gate': 'Select the horizontal source/target table interpretation and bind actual promotion to T9',
}
out = ROOT / 'research/strominger/results/wg-rung-schedule-comparison.json'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
