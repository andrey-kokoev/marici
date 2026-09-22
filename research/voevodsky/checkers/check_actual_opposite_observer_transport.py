"""Construct and check formal opposite of actual observer rows/actions.

Coefficient recipes remain opaque fixed scalars. This tests algebraic
transport, not admission of reversed calibration/acquisition protocols.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as Q
import copy
import hashlib
import json
import gzip

ROOT = Path(__file__).resolve().parents[3]
DIR = ROOT / 'research/nima/results'
paths = [DIR / 'actual-private-core-with-original-cubic.json',
         DIR / 'actual-retained-cubic-observer-union.json']
base, union = [json.loads(p.read_text()) for p in paths]
frames = [base] + union['frames']


def revrow(row):
    r = copy.deepcopy(row)
    a, b = row['corner_masks']
    r['corner_masks'] = [63 ^ b, 63 ^ a]
    for t in r['terms']:
        t['word'].reverse()
        t['marks'].reverse()
    return r


def revaction(action):
    a = copy.deepcopy(action)
    a['side'] = 'right' if action['side'] == 'left' else 'left'
    a['start_mask'] = 63 ^ (action['start_mask'] | (1 << action['event_index']))
    return a


def factor(text):
    return {'1': (Q(1), 0, 0), '-rho': (Q(-1), 1, 0),
            '-sigma': (Q(-1), 0, 1), 'rho*sigma': (Q(1), 1, 1)}[text]


def rowpoly(row, family):
    result = defaultdict(Q)
    for t in row['terms']:
        w, m = tuple(t['word']), tuple(t['marks'])
        if family == 'base':
            c, r, s = factor(t['coefficient'])
            result[w, m, r, s, '1'] += c
        else:
            for j, c in enumerate(t['component_coefficients']):
                atom = json.dumps([family, j, t['windows']], separators=(',', ':'))
                result[w, m, 0, 0, atom] += Q(c)
    return {k: v for k, v in result.items() if v}


def check_actions(rows, actions, family):
    polys = [rowpoly(r, family) for r in rows]
    expected = defaultdict(lambda: defaultdict(Q))
    for i, (row, poly) in enumerate(zip(rows, polys)):
        a, b = row['corner_masks']
        for (w, m, r, s, atom), c in poly.items():
            if len(w) <= 2:
                continue
            expected['left', a, w[0], m[0], i][w[1:], m[1:], r, s, atom] += c
            expected['right', b ^ (1 << w[-1]), w[-1], m[-1], i][w[:-1], m[:-1], r, s, atom] += c
    actual = defaultdict(lambda: defaultdict(Q))
    entries = 0
    for action in actions:
        side, start, event, retained = (action[k] for k in ('side', 'start_mask', 'event_index', 'retained'))
        for i, j, value in action['entries']:
            c, r, s = factor(value)
            a, b = rows[i]['corner_masks']
            assert rows[j]['corner_masks'] == ([a | (1 << event), b] if side == 'left' else [a, b ^ (1 << event)])
            for (w, m, rr, ss, atom), v in polys[j].items():
                actual[side, start, event, retained, i][w, m, r + rr, s + ss, atom] += c * v
            entries += 1
    def clean(d):
        return {k: {p: v for p, v in poly.items() if v} for k, poly in d.items() if any(poly.values())}
    assert clean(actual) == clean(expected)
    return entries

opposite = []
counts = []
for index, frame in enumerate(frames):
    family = 'base' if index == 0 else frame['family']
    rows = frame['rows']
    # Export only observer functionals; original context labels are provenance,
    # not assertions that the reversed recipe is admitted by the original protocol.
    rows = [{'corner_masks': r['corner_masks'], 'terms': r['terms']} for r in rows]
    actions = frame['actions']
    rr, aa = list(map(revrow, rows)), list(map(revaction, actions))
    assert list(map(revrow, rr)) == rows
    assert list(map(revaction, aa)) == actions
    before = check_actions(rows, actions, family)
    after = check_actions(rr, aa, family)
    assert before == after
    counts.append({'family': family, 'rows': len(rows), 'action_entries_per_orientation': before})
    opposite.append({'family': family, 'rows': rr, 'actions': aa,
                     'coefficient_semantics': 'Unchanged fixed original coefficient attached to reversed source path; protocol admission open.'})

# Reversal is an anti-involution on concatenation; exhaustive binary cut test
# lives in check_history_possibility_cut_duality.py. Here test actual row paths.
cut_checks = 0
for frame in opposite:
    for row in frame['rows']:
        for t in row['terms']:
            for k in range(len(t['word']) + 1):
                for key in ('word', 'marks'):
                    v = t[key]
                    assert (v[:k] + v[k:])[::-1] == v[k:][::-1] + v[:k][::-1]
                cut_checks += 1
# Verify reversal preserves every exported rational source-ideal generator.
presentation_path = DIR / 'actual-observer-full-finite-presentation.json.gz'
with gzip.open(presentation_path, 'rt') as stream:
    presentation = json.load(stream)
for name, digest in presentation['inputs'].items():
    assert hashlib.sha256((DIR / name).read_bytes()).hexdigest() == digest
corners = {tuple(c['corner']): c for c in presentation['source_corners']}
ideal_checks = 0
for (a, b), corner in corners.items():
    target = corners[63 ^ b, 63 ^ a]
    indices = {(tuple(w), tuple(m)): i for i, (w, m) in enumerate(target['paths'])}
    free = dict(zip(target['free_path_indices'], range(len(target['ideal_basis_columns']))))
    permutation = [indices[tuple(reversed(w)), tuple(reversed(m))] for w, m in corner['paths']]
    for raw in corner['ideal_basis_columns']:
        reversed_col = {permutation[i]: Q(v) for i, v in raw}
        rebuilt = defaultdict(Q)
        for i, v in reversed_col.items():
            if i in free:
                for j, c in target['ideal_basis_columns'][free[i]]:
                    rebuilt[j] += v * Q(c)
        assert {i: v for i, v in rebuilt.items() if v} == reversed_col
        ideal_checks += 1
outdir = ROOT / 'research/voevodsky/results'
packet = {'schema': 'formal-actual-opposite-observer-v1', 'frames': opposite,
          'inputs_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
encoded = json.dumps(packet, sort_keys=True, separators=(',', ':')).encode()
packet_path = outdir / 'formal-actual-opposite-observer.json.gz'
packet_path.write_bytes(gzip.compress(encoded, mtime=0))
report = {'passed': True, 'status': 'formal-row-and-action-transport-verified',
          'frames': counts, 'actual_path_cut_checks': cut_checks,
          'double_reversal': 'exact',
          'source_ideal_generators_reversal_checked': ideal_checks,
          'presentation_sha256': hashlib.sha256(presentation_path.read_bytes()).hexdigest(),
          'opposite_packet_sha256': hashlib.sha256(packet_path.read_bytes()).hexdigest(),
          'inputs_sha256': packet['inputs_sha256'],
          'open_gates': ['explicit ideal-power matrix transport',
                         'analytical recipe and physical/protocol admission of opposite rows',
                         'causal certificate-availability transport'],
          'scope': 'Exact raw functional and action identities with fixed opaque analytical coefficients. No complete conjecture closure.'}
(outdir / 'actual-opposite-observer-transport.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
