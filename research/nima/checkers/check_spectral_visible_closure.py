"""Does retained cross-mode information feed the same-mode observation?

Controls use existing local cyclic/short-half-phase operators and the seed
symmetry, lifted to the declared tensor carrier. This is not a successor law.
Exact matrices establish all-input closure, not just a sample trajectory.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import check_record4_spectral_promotion as sp
import check_spectral_successor_many_many as rec


def main():
    words = (('AB', 'BC', 'CA'), ('BA', 'AD', 'DB'))
    cycles = tuple(sp.cycle_from_packets(tuple(sp.TwoPacket(e, e[0], e[1]) for e in word))
                   for word in words)
    # Reuse the existing short half-phase formula Q+(I-Q)/2+(C-C^T)/2.
    halves = []
    for C in cycles:
        Q = sp.scale(sp.add(sp.add(sp.I, C), sp.mm(C, C)), F(1, 3))
        S = sp.add(sp.add(Q, sp.scale(sp.sub(sp.I, Q), F(1, 2))),
                   sp.scale(sp.sub(C, sp.transpose(C)), F(1, 2)))
        assert sp.mm(S, S) == C
        assert sp.mm(sp.transpose(S), S) == sp.I
        halves.append(S)
    projectors = {(m, n): rec.kron(sp.spectral_projector(cycles[0], m)[1],
                                   sp.spectral_projector(cycles[1], n)[1])
                  for m, n in rec.KEYS}
    D = rec.matrix_sum(projectors[m, m] for m in rec.MODES)
    R = rec.matrix_sum(projectors[key] for key in rec.KEYS if key[0] != key[1])
    assert sp.zmadd(D, R) == rec.IDENTITY
    assert sp.zmm(D, R) == rec.ZERO

    def tensor(a, b):
        return rec.kron(sp.zreal(a), sp.zreal(b))

    # The graph automorphism transports left ordered slots to right ordered
    # slots and vice versa. Its action on the ordered tensor pair is the flip.
    rename = dict(zip('ABCD', 'BADC'))
    for source, target in (words, tuple(reversed(words))):
        assert tuple(rename[e[0]] + rename[e[1]] for e in source) == target
    flip = tuple(tuple(rec.ONE if row == 3 * (col % 3) + col // 3 else rec.Z
                       for col in range(9)) for row in range(9))
    assert sp.zmm(flip, flip) == rec.IDENTITY
    assert sp.zmm(flip, sp.zmm(D, flip)) == D

    controls = {
        'left-cycle': tensor(cycles[0], sp.I),
        'right-cycle': tensor(sp.I, cycles[1]),
        'both-cycles': tensor(*cycles),
        'left-short-half-phase': tensor(halves[0], sp.I),
        'right-short-half-phase': tensor(sp.I, halves[1]),
        'both-short-half-phases': tensor(*halves),
        'seed-symmetry-factor-exchange': flip,
    }
    mixed = tuple((F(i - 4, 7), F(i % 3 - 1, 5)) for i in range(9))
    observations = []
    for name, T in controls.items():
        DTR = sp.zmm(D, sp.zmm(T, R))
        RTD = sp.zmm(R, sp.zmm(T, D))
        DTD = sp.zmm(D, sp.zmm(T, D))
        RTR = sp.zmm(R, sp.zmm(T, R))
        assert DTR == RTD == rec.ZERO
        assert sp.zmm(D, T) == sp.zmm(T, D)
        assert sp.zmm(sp.dagger(T), T) == rec.IDENTITY
        assert sp.zmadd(DTD, RTR) == T
        # Full retained evolution = separate visible and hidden block evolution.
        full = rec.apply(T, mixed)
        visible_next = rec.apply(DTD, rec.apply(D, mixed))
        hidden_next = rec.apply(RTR, rec.apply(R, mixed))
        assert rec.vector_sum((visible_next, hidden_next)) == full
        assert visible_next == rec.apply(D, full)
        assert rec.norm2(visible_next) == rec.norm2(rec.apply(D, mixed))
        assert rec.norm2(hidden_next) == rec.norm2(rec.apply(R, mixed))
        observations.append({'operation': name, 'DTR_zero': True, 'RTD_zero': True,
                             'residual_fixed_pointwise': RTR == R})

    # Regression of the normal forms of the generated operation family.
    # Local S's commute, S^6=I, and flip exchanges the two local factors.
    powers = []
    for S in halves:
        current = sp.I
        side = []
        for _ in range(6):
            side.append(current)
            current = sp.mm(S, current)
        assert current == sp.I
        powers.append(side)
    assert sp.zmm(flip, sp.zmm(controls['left-short-half-phase'], flip)) == controls['right-short-half-phase']
    checked = 0
    for i, j, swapped in product(range(6), range(6), (False, True)):
        T = tensor(powers[0][i], powers[1][j])
        if swapped:
            T = sp.zmm(flip, T)
        assert sp.zmm(D, sp.zmm(T, R)) == rec.ZERO
        assert sp.zmm(R, sp.zmm(T, D)) == rec.ZERO
        checked += 1
    assert checked == 72

    # No feedback does NOT mean the hidden state is frozen.
    basis = (rec.ONE,) + (rec.Z,) * 8
    hidden = rec.apply(projectors['positive', 'common'], basis)
    evolved = rec.apply(controls['left-cycle'], hidden)
    assert rec.norm2(hidden) > 0 and evolved != hidden
    assert evolved == tuple(sp.zmul(sp.MODES['positive'], z) for z in hidden)
    assert rec.apply(D, hidden) == rec.apply(D, evolved) == (rec.Z,) * 9

    report = {
        'status': 'passed',
        'carrier': 'V_left tensor V_right, complex dimension 9',
        'reader': 'D: three same-mode components; residual R: six cross-mode components',
        'controls': observations,
        'generated_normal_forms_checked': checked,
        'hidden_phase_evolves_despite_zero_feedback': True,
        'conclusion': 'Visible coefficients close under these controls; full recovery still needs evolved or replayable residual.',
        'not_tested_as_tensor_successors': [
            'SpectralLedger.promote: record construction, not a linear map on this pair state',
            'recursive family comparison: endpoint-dependent record product, no supplied pair-state response adapter',
            'joint seed endpoint lifts: operators on six direct-sum occurrence coefficients, not the nine-dimensional tensor carrier'],
        'scope': 'Conditional control closure, not source selection of a next-rung operation or physical law',
    }
    destination = Path(__file__).resolve().parents[1] / 'results' / 'spectral-visible-closure.json'
    destination.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: DTR=RTD=0 for 7 controls and 72 generated normal forms.')
    print('PASS: visible and residual blocks evolve separately; full state is reconstructible.')
    print('PASS: a hidden cross-mode state evolves in phase while remaining invisible.')
    print('BOUNDARY: the intended successor has no supplied linear action on this tensor carrier.')
    print('Report: research/nima/results/spectral-visible-closure.json')


if __name__ == '__main__':
    main()
