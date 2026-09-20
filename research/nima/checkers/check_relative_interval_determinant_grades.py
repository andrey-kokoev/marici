"""Relative trace-power grades from source compression, exact rational tests."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from based_determinant_packet import matrix, identity, add, neg, mul, trace, regularizer, anomaly, eliminate
from check_interval_compression_determinant_constructor import interval_packet


def power(a, k):
    result = identity(len(a))
    for _ in range(k):
        result = mul(result, a)
    return result


def relative_grades(packet, source, target):
    """Oriented pair of retained operators, not powers of their difference.

    det3 pair means rational_prefactor * exp(rational_exponent).
    No scalar evaluation or identification with endpoint currents is assumed.
    """
    fs, ft = packet.frames[source], packet.frames[target]
    a, b = add(fs, neg(identity(len(fs)))), add(ft, neg(identity(len(ft))))
    j1 = trace(b)-trace(a)
    j2 = (trace(mul(b,b))-trace(mul(a,a)))/2
    return {
        'primitive': j1,
        'square': j2,
        'det3_ratio': (eliminate(ft)[0]/eliminate(fs)[0], -j1+j2),
        'correction_to_relative_K': regularizer(b)-regularizer(a)-regularizer(packet.relative(source,target)),
        'log_cubic_coefficient': (trace(power(b,3))-trace(power(a,3)))/3,
    }


def main():
    n = 6
    # Source has oriented nearest-neighbour loops and nonzero diagonal.
    c = matrix([[Q(1,5) if i == j else Q(1,4) if abs(i-j)==1 else 0
                 for j in range(n)] for i in range(n)])
    p = interval_packet(c, range(n+1))
    coords = {(a,b): relative_grades(p,a,b) for a,b in product(range(n+1),repeat=2)}
    checks = {}
    checks['low_grades_add_on_all_triples'] = all(
        coords[a,b][k]+coords[b,d][k] == coords[a,d][k]
        for a,b,d in product(range(n+1),repeat=3) for k in ('primitive','square','log_cubic_coefficient'))
    checks['det3_ratios_compose'] = all(
        (coords[a,b]['det3_ratio'][0]*coords[b,d]['det3_ratio'][0],
         coords[a,b]['det3_ratio'][1]+coords[b,d]['det3_ratio'][1]) == coords[a,d]['det3_ratio']
        for a,b,d in product(range(n+1),repeat=3))
    checks['signed_face_grades_reverse'] = all(
        coords[a,b][k] == -coords[b,a][k]
        for a,b in coords for k in ('primitive','square','log_cubic_coefficient'))
    checks['anomaly_supplies_frame_correction'] = all(
        coords[a,b]['correction_to_relative_K'] == anomaly(
            add(p.frames[a],neg(identity(n))),p.relative(a,b)) for a,b in coords)
    checks['corrected_det3_equals_relative_line'] = all(
        p.coordinates(a,b)['det3'][1]+coords[a,b]['correction_to_relative_K'] == coords[a,b]['det3_ratio'][1]
        and p.coordinates(a,b)['det3'][0] == coords[a,b]['det3_ratio'][0] for a,b in coords)
    checks['correction_is_not_identically_zero'] = any(x['correction_to_relative_K'] for x in coords.values())
    forward, reverse = p.coordinates(1,2)['square'], p.coordinates(2,1)['square']
    checks['square_of_relative_K_fails_orientation'] = forward+reverse != 0
    # Cut 1 -> 2 contains a new diagonal contribution and a cross-boundary loop.
    expected_cross_loop = Q(1,16)
    new_diagonal_square = Q(1,50)
    checks['cross_boundary_square_loop_retained'] = coords[1,2]['square']-new_diagonal_square == expected_cross_loop
    checks['cubic_loop_retained'] = coords[1,2]['log_cubic_coefficient'] != Q(1,375)
    # Endpoint g(j)=j is still independent of the declared matrix.
    checks['endpoint_identification_still_fails'] = coords[0,1]['primitive'] != 1
    assert all(checks.values()), checks
    result = {
        'schema':'marici.nima.relative-interval-determinant-grades.v1',
        'strength':'finite_relative_determinant_identity_and_hostiles',
        'checks':checks,
        'oriented_square_residual_for_relative_K':str(forward+reverse),
        'relative_square_cut_1_to_2':str(coords[1,2]['square']),
        'cross_boundary_square_loop':str(expected_cross_loop),
        'endpoint_primitive_residual':str(coords[0,1]['primitive']-1),
        'source_endpoint_comparison':False,
        'completion_and_reciprocal_dagger':'not established',
    }
    out = Path(__file__).resolve().parents[1]/'results/relative-interval-determinant-grades.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
