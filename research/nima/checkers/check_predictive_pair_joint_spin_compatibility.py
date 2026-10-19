"""Frame-independent fixed-singlet compatibility of the existing spin actions.

Diagnostic for a fixed-singlet preservation policy, not selection of that policy.
For unitary doublets, projective conjugacy requires tr(U)^2/det(U) to agree.
Exhaust the proton binary tetrahedral group and every electron cycle power.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import sys

from check_predictive_pair_proton_spin_binding import main as proton_main
from check_predictive_pair_electron_spin_binding import main as electron_main

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OWNER = ROOT / 'research/voevodsky'
sys.path.insert(0, str(OWNER / 'checkers'))
from check_proton_electron_contact_binding import A, CI, I, ZERO, ONE, S2, pauli, mm, adj, add, scale, decode_matrix, outer, kron, act
from check_pentachoron_cycle_transport import power


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    with redirect_stdout(io.StringIO()):
        proton_main()
        electron_main()
    pp = HERE.parent / 'results/predictive-pair-proton-spin-binding.json'
    ep = HERE.parent / 'results/predictive-pair-electron-spin-binding.json'
    proton = json.loads(pp.read_text())
    electron = json.loads(ep.read_text())
    quaternions = set(tuple(F(sign if i == k else 0) for i in range(4))
                      for k in range(4) for sign in (-1, 1))
    quaternions.update(tuple(F(sign, 2) for sign in signs) for signs in product((-1, 1), repeat=4))
    group = tuple(add(scale(A(q[0]), I), scale(-CI, pauli(tuple(A(x) for x in q[1:]))))
                  for q in sorted(quaternions))
    def determinant(u):
        return u[0][0]*u[1][1]-u[0][1]*u[1][0]
    def invariant(u):
        trace = u[0][0]+u[1][1]
        return trace*trace / determinant(u)
    def scalar(u):
        return u[0][1] == u[1][0] == ZERO and u[0][0] == u[1][1]
    # A finite closed supergroup of every proton word suffices for the no-go;
    # no claim about a separately selected physical word language is needed.
    for i,u in enumerate(group):
        check(f'proton/unitary/{i}', mm(adj(u),u) == I)
        check(f'proton/determinant/{i}', determinant(u) == ONE)
        check(f'proton/invariant/{i}', invariant(u) in (A(0),A(1),A(4)))
        for j,v in enumerate(group):
            check(f'proton/group-closure/{i}/{j}', mm(u,v) in group)
    for row in proton['variants']:
        check('proton/all-bound-generators-contained', decode_matrix(row['logical_action']) in group)
    singlet = (ZERO, ONE/S2, -ONE/S2, ZERO)
    pi = outer(singlet)
    results = []
    comparisons = compatible = 0
    for variant in electron['variants']:
        u = decode_matrix(variant['logical_action'])
        invariants = []
        for exponent in range(10):
            v = power(u, exponent)
            check('electron/unitary-power', mm(adj(v),v) == I)
            invariants.append(invariant(v).record())
            check('electron/scalar-exactly-full-cycles', scalar(v) == (exponent % 5 == 0))
            for p in group:
                equal = invariant(p) == invariant(v)
                check('joint/only-scalar-actions-have-matching-invariants',
                      equal == (scalar(p) and scalar(v)))
                comparisons += 1
                if equal:
                    compatible += 1
                    check('joint/scalar-pair-preserves-projector', outer(act(kron(p,v),singlet)) == pi)
        results.append({'chirality': variant['chirality'], 'lift_sign': variant['lift_sign'],
                        'cycle_power_invariants': invariants})
    paths = [Path(__file__), pp, ep]
    report = {
        'schema': 'marici.nima.predictive-pair-joint-spin-compatibility.v1',
        'verification_status': 'pass', 'checks': checks,
        'proton_group_size': len(group), 'pair_comparisons': comparisons,
        'matching_pairs': compatible,
        'invariant': 'trace(U)^2 / determinant(U)', 'electron_variants': results,
        'conclusion': 'Across these source actions, frame-compatible fixed-singlet preservation '
                      'requires both local actions to be scalar. No relative spin-frame rotation '
                      'can repair a nontrivial proton/electron cycle mismatch.',
        'scope': 'All proton words in the closed binary-tetrahedral action group and all powers '
                 'of each existing electron generator. Relative frame fixed but arbitrary; '
                 'state chosen as a maximally entangled singlet in that frame. '
                 'Not a no-go for entangling interactions, evolving singlet readings, '
                 'time-dependent comparisons, or additional source operations. '
                 'No contact/mediator schedule or physical admission policy selected.',
        'input_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in paths}}
    output = HERE.parent / 'results/predictive-pair-joint-spin-compatibility.json'
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(f'PASS: {len(checks)} exact joint-spin compatibility checks')
    print(f'{comparisons} comparisons; {compatible} invariant matches, all scalar/scalar.')
    print('A fixed relative frame cannot repair nontrivial local-cycle mismatch.')
    print('Conditional fixed-singlet diagnostic, not a selected physical admission law.')


if __name__ == '__main__':
    main()
