"""Partial source binding: electron requests to existing five-cell spin transport.

No proton-spin request map or relative-position dynamics is supplied here.
Owner stores are read/hash-checked, never rewritten. Exact embedding covariance
and the induced logical action are freshly verified for all four variants.
"""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import sys

from check_actual_pair_phase_rung_bridge import main as build
from predictive_pair_quotient import PredictivePairQuotient

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OWNER = ROOT / 'research/voevodsky'
sys.path.insert(0, str(OWNER / 'checkers'))
from check_proton_electron_contact_binding import (
    A, ZERO, ONE, S2, I, decode_matrix, mm, adj, scale, outer, kron, act)
from check_pentachoron_cycle_transport import power


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    store = OWNER / 'results/pentachoron_cycle_transport.json'
    raw = store.read_bytes()
    data = json.loads(raw)
    check('owner/verified-store', data['verification_passed'])
    for name, digest in data['source_hashes'].items():
        check('owner/source-pin/' + name,
              hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest)
    with redirect_stdout(io.StringIO()):
        binding = build()
    q = PredictivePairQuotient(binding)
    electron = tuple(a for a in q.actions if a[0] == 'electron')
    check('binding/five-electron-requests', len(electron) == 5)
    # Pair adapter labels the source origin A; the spin backend labels it E.
    # Both use the same affine generator. This cyclic relabelling is explicit.
    label_map = dict(zip('ABCDE', 'EABCD'))
    check('binding/cycle-label-dictionary', all(
        (ord(label_map[a[3]]) - ord(label_map[a[2]])) % 5 == 1 for a in electron))
    path = ()
    endpoint = ('A', 'E')
    for name in ('EA', 'AB', 'BC', 'CD', 'DE'):
        edge = next(edge for (edge,) in q.bridge['frame']
                    if edge[0] == endpoint and edge[2][0] == 'electron'
                    and ''.join(edge[2][2:]) == name)
        path += (edge,)
        endpoint = edge[1]
    check('geometric/full-cycle-forgotten', q.project(path) == q.project(path + path))
    singlet = (ZERO, ONE / S2, -ONE / S2, ZERO)
    pi = outer(singlet)
    variants = []
    for row in data['chirality_results']:
        spin = decode_matrix(row['spin_lift'])
        for sign, key in ((1, 'attachment_encoding'), (-1, 'opposite_lift_attachment_encoding')):
            tag = f'{row["chirality"]}/{sign}'
            s = scale(A(sign), spin)
            encoding = row['conditional_cycle_defect_extension'][key]
            cell = decode_matrix(encoding['cell_isometry'])
            face = decode_matrix(encoding['face_isometry'])
            order = tuple(map(tuple, encoding['face_order']))
            check('embedding/isometries/' + tag, mm(adj(cell), cell) == I and mm(adj(face), face) == I)
            t = tuple(tuple(s[i % 2][j % 2] if i // 2 == (j // 2 + 1) % 5 else ZERO
                            for j in range(10)) for i in range(10))
            logical = mm(adj(cell), mm(t, cell))
            check('binding/logical-unitary/' + tag, mm(adj(logical), logical) == I)
            check('binding/cell-intertwiner/' + tag, mm(t, cell) == mm(cell, logical))
            moved_face = []
            for c, d in order:
                previous = order.index(((c - 1) % 5, (d - 1) % 5))
                moved_face.extend(mm(s, face[2 * previous:2 * previous + 2]))
            check('binding/face-intertwiner/' + tag, tuple(moved_face) == mm(face, logical))
            expected = scale(A(-sign), I)
            check('binding/fifth-power/' + tag, power(logical, 5) == expected)
            for action in electron:
                # All five moving correspondences reference the same source generator.
                check('binding/request-action/' + tag + '/' + repr(action),
                      mm(t, cell) == mm(cell, logical))
            pair_action = kron(I, logical)
            next_singlet = act(pair_action, singlet)
            check('interaction/electron-step-changes-singlet-projector/' + tag,
                  outer(next_singlet) != pi)
            returned = act(kron(I, power(logical, 5)), singlet)
            check('interaction/fifth-step-restores-projector/' + tag, outer(returned) == pi)
            check('interaction/amplitude-return-sign/' + tag,
                  returned == tuple(A(-sign) * x for x in singlet))
            for policy in ('inherited', 'common'):
                retained = q.retain(path, policy)
                recovered = q.restore(retained)
                count = sum(edge[2][0] == 'electron' for edge in recovered)
                check('transport/electron-count-and-spin-action/' + policy + '/' + tag,
                      count == 5 and power(logical, count) == expected)
            variants.append({'chirality': row['chirality'], 'lift_sign': sign,
                             'logical_action': [[z.record() for z in r] for r in logical],
                             'fifth_power': '-I' if sign == 1 else '+I',
                             'single_step_preserves_singlet_projector': False,
                             'five_steps_preserve_singlet_projector': True})
    check('owner/store-unchanged', store.read_bytes() == raw)
    inputs = [Path(__file__), store, OWNER / 'inputs/relative-electron.json',
              OWNER / 'checkers/check_pentachoron_cycle_transport.py',
              OWNER / 'checkers/check_proton_electron_contact_binding.py',
              HERE.parent / 'results/actual-pair-phase-rung-bridge.json']
    report = {'schema': 'marici.nima.predictive-pair-electron-spin-binding.v1',
              'verification_status': 'pass', 'binding_status': 'partial-electron-only',
              'checks': checks, 'label_map_pair_to_spin_backend': label_map,
              'variants': variants,
              'unbound': ['proton request spin action', 'relative-position/contact update',
                          'physical choice of chirality/lift', 'initial logical pair preparation',
                          'policy turning contact operator into transition admission'],
              'scope': 'Fresh cell/face intertwiners from hash-pinned existing encodings; '
                       'not a rerun of their full producer or the contact energy calculation. '
                       'Pair I tensor U is electron-only; no proton dynamics inferred. '
                       'A global minus sign distinguishes vectors, not their projectors.',
              'input_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in inputs}}
    output = HERE.parent / 'results/predictive-pair-electron-spin-binding.json'
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(f'PASS: {len(checks)} exact electron-spin binding checks')
    print('All four variants intertwine the source step on cell and face encodings.')
    print('One electron step changes the singlet projector; five restore it.')
    print('Partial binding only: proton spin/contact operations remain unsupplied.')


if __name__ == '__main__':
    main()
