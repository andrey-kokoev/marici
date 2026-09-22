"""Search actual exported ideal generators for a same-observer reversal obstruction.

Reversal sends corner (a,b) to (63^b,63^a), reversing words and marks.
Checks exact ideal membership by reconstructing the reversed source in the
exported rational basis. A constant nonzero readout avoids calibration assumptions.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
NIMA = ROOT / 'research/nima/results'
path = NIMA / 'actual-observer-full-finite-presentation.json.gz'
with gzip.open(path, 'rt') as stream:
    data = json.load(stream)
for name, digest in data['inputs'].items():
    assert hashlib.sha256((NIMA / name).read_bytes()).hexdigest() == digest
corners = {tuple(c['corner']): c for c in data['source_corners']}
columns = data['G0_evaluation_columns']
exprs = [{data['coefficient_atoms'][i]: Q(v) for i, v in e} for e in data['expressions']]
found = None
checked = 0
for (a, b), corner in corners.items():
    target = corners[63 ^ b, 63 ^ a]
    target_index = {(tuple(w), tuple(m)): i for i, (w, m) in enumerate(target['paths'])}
    free = dict(zip(target['free_path_indices'], range(len(target['ideal_basis_columns']))))
    for local, raw in enumerate(corner['ideal_basis_columns']):
        gid = corner['generator_offset'] + local
        if columns[gid]:
            continue
        checked += 1
        reversed_source = {}
        for i, v in raw:
            w, m = corner['paths'][i]
            reversed_source[target_index[tuple(reversed(w)), tuple(reversed(m))]] = Q(v)
        coordinates = {free[i]: v for i, v in reversed_source.items() if i in free}
        rebuilt = defaultdict(Q)
        for i, v in coordinates.items():
            for j, c in target['ideal_basis_columns'][i]:
                rebuilt[j] += v * Q(c)
        assert {i: v for i, v in rebuilt.items() if v} == reversed_source
        values = defaultdict(lambda: defaultdict(Q))
        for i, v in coordinates.items():
            for row, expression in columns[target['generator_offset'] + i]:
                for atom, c in exprs[expression].items():
                    values[row][atom] += v * c
        constants = []
        for row, poly in values.items():
            poly = {atom: c for atom, c in poly.items() if c}
            if set(poly) == {'1'}:
                constants.append((row, poly['1']))
        if constants:
            row, value = sorted(constants)[0]
            found = {
                'source_generator': gid, 'source_corner': [a, b],
                'source_terms': [{'word': corner['paths'][i][0], 'marks': corner['paths'][i][1],
                                  'coefficient': str(Q(v))} for i, v in raw],
                'reversed_corner': target['corner'],
                'reversed_source_coordinates': [[target['generator_offset'] + i, str(v)] for i, v in sorted(coordinates.items())],
                'original_observer_column': [], 'reversed_nonzero_row': row,
                'reversed_exact_value': str(value),
            }
            break
    if found:
        break
if found:
    # Independently bind the nonzero readout to its owning raw coefficient row.
    base = json.loads((NIMA / 'actual-private-core-with-original-cubic.json').read_text())
    raw_row = base['rows'][found['reversed_nonzero_row']]
    assert raw_row['corner_masks'] == found['reversed_corner']
    source = {(tuple(reversed(t['word'])), tuple(reversed(t['marks']))): Q(t['coefficient'])
              for t in found['source_terms']}
    assert all(t['coefficient'] == '1' for t in raw_row['terms'])
    direct_value = sum((source.get((tuple(t['word']), tuple(t['marks'])), Q(0))
                        for t in raw_row['terms']), Q(0))
    assert direct_value == Q(found['reversed_exact_value'])
    found['owning_raw_row_independently_checked'] = True
report = {
    'schema': 'actual-observer-reversal-descent-test-v1',
    'presentation_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
    'input_digests_verified': True,
    'hidden_generators_checked': checked,
    'status': 'same-observer-reversal-obstructed' if found else 'search-inconclusive',
    'witness': found,
    'scope': 'Actual exported ideal aggregate and complement-corner word/mark reversal. Source ideal elements are linear relations, not individually admitted physical histories. Opposite-observer transport remains a separate contract.',
}
out = ROOT / 'research/voevodsky/results/actual-observer-reversal-descent.json'
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
