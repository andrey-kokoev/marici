"""Exact finite convolution/restriction candidate, not an Evans comparison theorem."""
from fractions import Fraction as Q
from itertools import permutations
import json
from pathlib import Path
from based_determinant_packet import (
    BasedPacket, matrix, identity, add, neg, mul, star, trace,
    regularizer, anomaly, eliminate,
)


def interval_packet(kernel, cuts, coupling=Q(1)):
    """Prefix compression on one retained labelled carrier; no fitted frames.

    kernel is the declared finite source operator, not its positive Gram.
    cut m retains labels 0,...,m-1. No cutoff completion is asserted.
    """
    kernel = matrix(kernel)
    n = len(kernel)
    frames = {}
    for m in cuts:
        if not isinstance(m, int) or not 0 <= m <= n:
            raise ValueError('cut outside labelled carrier')
        compressed = matrix([[coupling*kernel[i][j] if i < m and j < m else 0
                              for j in range(n)] for i in range(n)])
        frames[m] = add(identity(n), compressed)
    return BasedPacket(frames)


def main():
    # Declared discrete convolution source, phi(0)=0, phi(+/-1)=1/4.
    # This is a rational hostile, not a discretization theorem for theta.
    n = 6
    c = matrix([[Q(1, 4) if abs(i-j) == 1 else 0
                 for j in range(n)] for i in range(n)])
    packet = interval_packet(c, range(n+1))
    checks = {}
    checks['all_based_triples'] = all(
        star(packet.relative(a, b), packet.relative(b, d)) == packet.relative(a, d)
        for a in range(n+1) for b in range(n+1) for d in range(n+1))
    checks['signed_ratio_inverse'] = all(
        mul(packet.factor(a, b), packet.factor(b, a)) == identity(n)
        for a in range(n+1) for b in range(n+1))
    # Adjacent order (1,2) versus (2,1): retain the cut 1 -> 2.
    checks['ratio_face'] = (
        mul(packet.factor(0, 1), packet.factor(1, 2)) == packet.factor(0, 2))
    checks['ratio_is_detectable'] = packet.factor(1, 2) != identity(n)
    paths = []
    for word in permutations((1, 2, 3)):
        t, base = identity(n), 0
        for width in word:
            t = mul(t, packet.factor(base, base+width))
            base += width
        paths.append(t)
    checks['six_orders_same_retained_endpoint'] = all(t == paths[0] for t in paths)
    a, b, d = (packet.relative(0, 1), packet.relative(1, 3), packet.relative(3, 6))
    checks['plus_convention_anomaly'] = anomaly(a, b) == regularizer(star(a, b))-regularizer(a)-regularizer(b)
    checks['anomaly_cocycle'] = anomaly(a, b)+anomaly(star(a, b), d) == anomaly(b, d)+anomaly(a, star(b, d))
    checks['nonzero_anomaly'] = anomaly(b, d) != 0
    # Endpoint state g(j)=j: primitive increment 0 -> 1 equals 1.
    # The convolution prefix is zero at cut 1: its relative trace is 0.
    observed = packet.coordinates(0, 1)['primitive']
    checks['endpoint_trace_rival_falsified'] = observed != Q(1)
    try:
        packet.coordinates(0, 1, expected_low=(Q(1), Q(0)))
    except ValueError:
        checks['incompatible_source_current_rejected'] = True
    else:
        checks['incompatible_source_current_rejected'] = False
    # Fixed low cumulants, distinct connected channel, retained in exact det3 pairs.
    spectra = [(Q(1,2), Q(-1,2), Q(0)), (Q(4,13), Q(7,26), Q(-15,26))]
    coords = []
    for xs in spectra:
        k = matrix([[xs[i] if i == j else 0 for j in range(3)] for i in range(3)])
        coords.append(interval_packet(k, (0, 3)).coordinates(0, 3))
    checks['hostile_low_equal'] = all(coords[0][s] == coords[1][s] for s in ('primitive','square'))
    checks['hostile_connected_distinct'] = coords[0]['det3'][1] == coords[1]['det3'][1] and coords[0]['det3'][0] != coords[1]['det3'][0]
    try:
        interval_packet([[-1]], (0, 1))
    except ValueError:
        checks['singular_frame_rejected'] = True
    else:
        checks['singular_frame_rejected'] = False
    assert all(checks.values()), checks
    result = {
        'schema': 'marici.nima.interval-compression-determinant-constructor.v1',
        'strength': 'finite_rational_candidate_and_counterexample',
        'checks': checks,
        'endpoint_trace_residual': str(observed-Q(1)),
        'nonzero_anomaly': str(anomaly(b, d)),
        'source_evans_comparison_constructed': False,
        'residual': 'Prefix convolution frames do not realize arbitrary based endpoint currents; reciprocal dagger naturality and completion unproved.',
    }
    out = Path(__file__).resolve().parents[1]/'results/interval-compression-determinant-constructor.json'
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
