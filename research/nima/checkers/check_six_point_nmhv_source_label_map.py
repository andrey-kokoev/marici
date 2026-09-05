from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FIXTURE = json.loads((ROOT / 'research/nima/six-point-nmhv-triangulation-fixture.json').read_text(encoding='utf-8'))
RESULT = ROOT / 'research/nima/results/six-point-nmhv-source-label-map.json'


def canonical_cyclic_tuple(values):
    rotations = [tuple(values[i:] + values[:i]) for i in range(len(values))]
    return min(rotations)


def source_triangulation(n=6):
    cells = []
    for i in range(2, n):
        for j in range(i + 2, n):
            values = [1, i, i + 1, j, j + 1]
            if len(set(values)) == 5:
                cells.append(tuple(values))
    return cells


def shift(cell):
    return tuple(1 if value == 6 else value + 1 for value in cell)


def normalized(cell):
    return tuple(sorted(cell))


def main():
    left = sorted(map(tuple, FIXTURE['triangulations']['left']))
    right = sorted(map(tuple, FIXTURE['triangulations']['right']))
    generated = sorted(normalized(cell) for cell in source_triangulation())
    shifted = sorted(normalized(shift(cell)) for cell in source_triangulation())
    checks = {
        'source_sum_generates_left_labels': generated == left,
        'cyclic_shift_generates_right_labels': shifted == right,
        'three_terms_each': len(generated) == len(shifted) == 3,
    }
    out = {
        'schema': 'marici.nima.six_point_nmhv_source_label_map.result.v1',
        'status': 'passed' if all(checks.values()) else 'failed',
        'checks': checks,
        'source_formula': '(1,i,i+1,j,j+1) with nondegenerate n=6 labels',
        'generated_left': [''.join(map(str,c)) for c in generated],
        'cyclically_shifted_right': [''.join(map(str,c)) for c in shifted],
        'source_locator': '1312.2007/amplituhedron.tex lines 507-520',
        'claim_boundary': 'This derives the local labels from the source textual triangulation formula and one cyclic relabelling. It does not identify the figure permutation labels in 1212.5605 independently.'
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
    if out['status'] != 'passed': raise SystemExit(1)


if __name__ == '__main__': main()
