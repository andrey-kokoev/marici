"""One-clock elementary-gap/contact adapter; exact rational controls.

The elementary Hamiltonian is E_star*(I-N_e), restricted to one bright/dark
pair. Its gap, not its coherent-sector rest offset, defines E_star=1.
New input: use the same projector-generator coefficient for internal exchange.
No measured masses enter this test.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1]


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def mv(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def bracket(rows):
    # H=K+P_exchange+P_aux. Below its first positive native pole,
    # Schur elimination gives R(-y)+2+1/(1-y)=0.
    def residual(y):
        return sum(w/(e-y) for e, w in rows)+2+1/(1-y)
    edge = min([F(1)]+[e for e, _ in rows if e>0])
    lo = edge / 2**100
    hi = edge / 2
    assert residual(lo)<0
    while residual(hi)<=0:
        hi = (hi+edge)/2
    for _ in range(100):
        mid = (lo+hi)/2
        if residual(mid)<0:
            lo = mid
        else:
            hi = mid
    assert residual(lo)<0<=residual(hi)
    return lo, hi


def main():
    source_path = BASE/'results/common_contact_dressing.json'
    raw = source_path.read_bytes()
    source = json.loads(raw)
    assert source['verification_passed']
    spectra = {s: [(F(e), F(w)) for e, w in
                  zip(source[s+'_poles'], source[s+'_weights']) if F(w)]
               for s in ('proton', 'belt')}
    controls = {}
    intervals = {}
    for species, rows in spectra.items():
        assert sum(w for _, w in rows)==1
        assert rows[0][0]==0 and rows[0][1]>0
        weights = [w for _, w in rows]
        metric = [F(1)]+weights
        n = len(metric)
        # P_exchange=(|aux>-|w>)(<aux|-<w|)/2, metric-normalized.
        p = [[F(0) for _ in range(n)] for _ in range(n)]
        p[0][0] = F(1, 2)
        for j, w in enumerate(weights, 1):
            p[0][j] = -w/2
            p[j][0] = -F(1, 2)
            for k, wk in enumerate(weights, 1):
                p[j][k] = wk/2
        assert mm(p, p)==p
        assert sum(p[i][i] for i in range(n))==1
        for i in range(n):
            for j in range(n):
                assert metric[i]*p[i][j]==metric[j]*p[j][i]
        h = [row[:] for row in p]
        for j, (e, _) in enumerate(rows, 1):
            h[j][j] += e
        # Exact kernel: original zero mode plus its matched aux amplitude.
        zero = [weights[0], F(1)]+[F(0)]*(n-2)
        assert mv(h, zero)==[0]*n
        # H is a sum of positive operators, hence this is a ground state.
        # Internal occupation is the next single-clock operation.
        h_occupied = [row[:] for row in h]
        h_occupied[0][0] += 1
        assert mv(h_occupied, zero)!=[0]*n
        intervals[species] = bracket(rows)
        # Tensor I_2 preserves both logical spins. All sector labels are
        # constant on each block, so every exchange commutes with Q and B.
        controls[species] = {
            'bright_dimension_before_spin': n,
            'exchange_projector_exact': True,
            'weighted_hermiticity_exact': True,
            'exchange_only_ground_energy': '0',
            'zero_mode_coordinates': list(map(str, zero)),
            'exchange_plus_occupation_ground_interval': list(map(str, intervals[species])),
            'exchange_plus_occupation_ground_energy': float(sum(intervals[species])/2),
        }
    plo, phi = intervals['proton']
    blo, bhi = intervals['belt']
    assert plo>bhi
    # Native dark spectators are unchanged. Prior full carrier spectra put
    # proton positive modes >=1/2 and belt positive modes >0.172938631059.
    assert phi<F(1, 2)
    assert bhi<F(172938631059, 10**12)
    difference = (blo-phi, bhi-plo)
    report = {
        'verification_passed': True,
        'source_sha256': sha256(raw).hexdigest(),
        'elementary_gap_definition': 'E_star*(I-N_e): coherent doublet 0, dark gap E_star; choose E_star=1.',
        'elementary_rest_offset_selected': False,
        'shared_rule': 'Each admitted involution contributes E_star*(I-F)/2; no species-specific coefficients.',
        'internal_exchange': 'F swaps aux with normalized w and fixes dark contact directions.',
        'spin_adapter': 'Every carrier/internal-channel operator is tensored with I_2.',
        'sector_labels': {'proton': {'Q': 1, 'B': 1}, 'belt': {'Q': 0, 'B': 1}},
        'species_conversion': False,
        'controls': controls,
        'exchange_only_splitting': '0',
        'exchange_plus_occupation_belt_minus_proton_interval': list(map(str, difference)),
        'exchange_plus_occupation_belt_minus_proton': float(sum(difference)/2),
        'exchange_plus_occupation_ordering': 'proton above belt, opposite to the prior exchange-only off-diagonal model',
        'reason': 'A full involution generator includes the carrier contact self-term |w><w|/2.',
        'measured_mass_inputs': [],
        'next_gate': 'Source an interaction whose complete diagonal and exchange terms retain the desired ordering; do not drop the contact self-term to identify g with the elementary clock.',
    }
    out = BASE/'results/elementary_gap_contact_bridge.json'
    out.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__=='__main__':
    main()
