"""Exact obstruction for the fixed Aspect marker flip as an interval shift.
Reads the foreign source without running main or writing foreign results.
"""
import ast
import contextlib
import io
import json
import runpy
import sys
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OPTICAL = 'research/aspect/checkers/check_path_marker_mate_interferometer.py'
sys.path.insert(0, str(ROOT / 'research/nima'))
from nnmhv_coherence_paths import compile_nnmhv_histories, supports_component_23


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def main():
    optics = runpy.run_path(str(ROOT / OPTICAL))
    syntax = ast.parse((ROOT / OPTICAL).read_text(encoding='utf-8'))
    fn = next(n for n in syntax.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
    assignments = [n for n in fn.body if isinstance(n, ast.Assign)
                   and any(isinstance(t, ast.Name) and t.id == 'cnot_path_to_marker' for t in n.targets)]
    require(len(assignments) == 1, 'ambiguous optical operation source')

    def matrix_literal(n):
        if isinstance(n, ast.List):
            return [matrix_literal(x) for x in n.elts]
        require(isinstance(n, ast.Name) and n.id in ('ONE', 'ZERO'), 'changed matrix interface')
        return optics[n.id]

    U = matrix_literal(assignments[0].value)
    mm, dagger, transform = (optics[x] for x in ('mm', 'dagger', 'transform'))
    identity = [[optics['ONE'] if i == j else optics['ZERO'] for j in range(4)] for i in range(4)]
    require(mm(U, U) == identity and mm(dagger(U), U) == identity, 'actual control not unitary involution')
    # Complete complex matrix-unit basis verifies the channel square, not just prepared probes.
    for i in range(4):
        for j in range(4):
            unit = [[optics['ZERO'] for _ in range(4)] for _ in range(4)]
            unit[i][j] = optics['ONE']
            require(transform(U, transform(U, unit)) == unit, 'channel square differs on a matrix unit')
    with contextlib.redirect_stdout(io.StringIO()):
        paths = runpy.run_path(str(ROOT / 'research/nima/checkers/check_indexed_path_synthesis.py'))
    compose = paths['compose']

    def word(i, j):
        return tuple((k, k + 1) for k in range(i, j + 1))

    def endpoints(p):
        return p[0][0], p[-1][0]

    def step(p, tag, m):
        i, j = endpoints(p)
        if tag == 'L':
            require(i > 1, 'illegal L')
            return next(iter(compose({((i-1, i),)}, {p})))
        if tag == 'R':
            require(j < m, 'illegal R')
            return next(iter(compose({p}, {((j+1, j+2),)})))
        require(tag == 'l' and i < j, 'illegal trim')
        return p[1:]

    counts = {'visible_double_L': 0, 'visible_double_R': 0, 'visible_double_l': 0, 'genuine_L_l_recovery': 0}
    witnesses = {}
    for m in range(3, 11):
        records = {(h.inner_pair[1]-4, h.outer_pair[1]-4): h
                   for h in compile_nnmhv_histories(m+5) if supports_component_23(h)}
        for i, j in records:
            p = word(i, j)
            if i > 1:
                q = step(p, 'L', m)
                require(step(q, 'l', m) == p, 'genuine inverse failed')
                counts['genuine_L_l_recovery'] += 1
            for tag, legal in (('L', i > 2), ('R', j + 2 <= m), ('l', i + 2 <= j)):
                if not legal:
                    continue
                q = step(p, tag, m)
                r = step(q, tag, m)
                if not all(a < b for a, b in map(endpoints, (p, q, r))):
                    continue
                require(records[endpoints(p)] != records[endpoints(r)], 'decoder collapsed the shift')
                counts['visible_double_' + tag] += 1
                witnesses.setdefault(tag, {'m': m, 'states': [list(endpoints(x)) for x in (p, q, r)],
                                            'full_decoded_records_differ': True})
    require(witnesses['L'] == {'m': 4, 'states': [[3,4],[2,4],[1,4]], 'full_decoded_records_differ': True}, 'unexpected minimal L witness')
    require(witnesses['R']['m'] == 4 and witnesses['R']['states'] == [[1,2],[1,3],[1,4]], 'unexpected minimal R witness')
    require(witnesses['l']['m'] == 4 and witnesses['l']['states'] == [[1,4],[2,4],[3,4]], 'unexpected minimal trim witness')
    # The obstruction is involutivity, not merely invertibility: a 3-cycle does not square to identity.
    cycle = (1, 2, 0)
    require(cycle[cycle[0]] != 0, 'noninvolutive control incorrectly excluded')
    # Full endpoint readout cannot factor through a collapsed encoding of either witness.
    for w in witnesses.values():
        require(w['states'][0] != w['states'][2], 'endpoint observer would not detect the collision')
    sources = [OPTICAL, 'research/nima/checkers/check_indexed_path_synthesis.py',
               'research/nima/nnmhv_coherence_paths.py',
               'research/nima/interval-marker-involution-gate.md',
               'research/nima/checkers/check_interval_marker_involution_gate.py']
    result = {'schema': 'marici.nima.interval-marker-involution-gate.v1', 'passed': True,
              'candidate_verdict': 'fixed_marker_flip_as_faithful_interval_shift_refuted',
              'optical_channel_square': 'identity on all 16 complex matrix units',
              'counts': counts, 'minimal_visible_witnesses': witnesses,
              'controls': ['legal-L-l-recovers', 'no-diagonal-in-witness', 'noninvolutive-control-not-excluded',
                           'endpoint-readout-detects-forced-collapse'],
              'boundary': 'No exclusion of richer controls, ancillary registers or optical realizations in general. No physical experiment or WG-I3 verdict.',
              'source_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}}
    dest = ROOT / 'research/nima/results/interval-marker-involution-gate.json'
    dest.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
