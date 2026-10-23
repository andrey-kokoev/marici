#!/usr/bin/env python3
"""Exact ideal two-arm readout using existing native matrices; no hardware claim."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/strominger/checkers'))
from electron_packet_interface import E, I, F, adj, gmm, sm, matrix_add


def gram(a):
    return gmm(adj(a), a)


def ports(a, b):
    # Two balanced splitters: field transfer to sum/difference output ports.
    return (sm(F(1, 2), matrix_add(a, b)),
            sm(F(1, 2), matrix_add(a, sm(-1, b))))


def main():
    zero = sm(0, I)
    a = gmm(E[0], E[1])
    b = gmm(E[1], E[0])
    corrected = sm(-1, b)
    checks = {}
    checks['native_routes_opposite'] = a == sm(-1, b)
    checks['native_route_unitary'] = gram(a) == I
    plus, minus = ports(a, corrected)
    checks['corrected_sum_unit_power'] = gram(plus) == I
    checks['corrected_difference_dark'] = minus == zero
    plus, minus = ports(a, b)
    checks['uncorrected_sum_dark'] = plus == zero
    checks['uncorrected_difference_unit_power'] = gram(minus) == I
    plus, minus = ports(a, zero)
    quarter = sm(F(1, 4), I)
    checks['blocked_arm_quarter_power_each_port'] = gram(plus) == quarter and gram(minus) == quarter
    plus, minus = ports(zero, zero)
    checks['no_input_or_transfer_both_dark'] = plus == zero and minus == zero
    # An equal wrong transformation fools route agreement: source checks remain necessary.
    plus, minus = ports(I, I)
    checks['common_wrong_transport_also_difference_dark'] = minus == zero and gram(plus) == I
    result = {
        'passed': all(checks.values()), 'checks': checks,
        'scope': 'Exact ideal balanced coherent interferometer identities on native logical matrices, for every input vector. No physical calibration, noise model, assembly selection, or hardware realization established.',
        'readout_boundary': 'A dark difference port alone proves neither preparation nor correct native transport. Even agreement on one input does not prove equality of operators; a spanning probe family is required.',
    }
    print(json.dumps(result, indent=2))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
