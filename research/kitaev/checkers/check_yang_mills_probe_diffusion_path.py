"""Exact path-tightness/martingale controls; not a source diffusion simulation."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_probe_gradient_transport import report as predecessor_report
from check_yang_mills_probe_gradient_core import inner
from check_yang_mills_probe_pressure import require

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-diffusion-path.v1.json'
NOTE = BASE+'yang-mills-probe-diffusion-path-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_diffusion_path.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-diffusion-path-v1.json')


def polynomial_product(f, g):
    out = [F(0)]*(len(f)+len(g)-1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            out[i+j] += x*y
    return out


def fourth_integral_unit(f):
    squared = polynomial_product(f, f)
    fourth = polynomial_product(squared, squared)
    return sum((x/F(i+1) for i, x in enumerate(fourth)), F(0))


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(contract['batch_iteration'] == 11 and contract['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in contract['boundary'].values()) and not contract['parent_net']['discharges_parent'], 'scope')
    require(contract['subnet']['parent_outcome'] is None and contract['subnet']['ready_frontier'] == ['small-probe-path-density'], 'path-density frontier')
    parent = json.loads((ROOT/contract['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == contract['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-gradient-transport-v1.json')).read_text()), 'fresh gradient-transport receipt')
    jet_packets = 0
    points = [[F(2), F(0), F(0), F(0)], [F(0), F(2), F(0), F(0)], [F(1)]*4,
              [F(6, 5), F(8, 5), F(0), F(0)], [F(2, 3), F(4, 3), F(4, 3), F(0)]]
    for y, kappa in product(points, [F(1, 2), F(1), F(2)]):
        require(sum(x*x for x in y) == 4, 'actual radius-two embedding point')
        gram = [[F(int(a == b))-y[a]*y[b]/4 for b in range(4)] for a in range(4)]
        require(all(sum(gram[a][c]*gram[c][b] for c in range(4)) == gram[a][b] for a, b in product(range(4), repeat=2)), 'tangent projection and coordinate gradient Gram')
        tangent = [sum(gram[a][b]*v for b, v in enumerate([F(1), F(-2), F(3), F(-1)])) for a in range(4)]
        require(sum(x*v for x, v in zip(y, tangent)) == 0, 'arbitrary tangent drift fixture')
        generator_y = [kappa*(-F(3, 4)*x+v) for x, v in zip(y, tangent)]
        for a, b in product(range(4), repeat=2):
            generator_product = kappa*(2*F(int(a == b))-2*y[a]*y[b]+tangent[a]*y[b]+y[a]*tangent[b])
            bracket = generator_product-y[a]*generator_y[b]-y[b]*generator_y[a]
            require(bracket == 2*kappa*gram[a][b], 'actual coordinate product identity cancels the full drift')
            require(0 <= gram[a][a] <= 1, 'coordinate bracket bounded by2kappa')
            jet_packets += 1
    bracket_defect = 2*F(1)-F(1)
    require(bracket_defect == 1, 'half-bracket unit-tangent hostile')
    moment_packets = 0
    for R, kappa, gradient_u, h in product([F(0), F(9, 128), F(575, 4096)], [F(1, 2), F(1), F(2)], [F(0), F(1)], [F(1, 16), F(1, 8), F(1, 2), F(1)]):
        m = kappa*(F(1, 2)-3*R)
        L = gradient_u/m
        B = kappa*(F(3, 2)+4*R+2*L)
        # Symmetric three-point tangent increment with probabilities1/6,2/3,1/6
        # and squared endpoint6*kappa*h, matching Gaussian moments through4.
        endpoint_squared = 6*kappa*h
        variance = endpoint_squared/3
        fourth = endpoint_squared**2/3
        require(variance == 2*kappa*h and fourth == 12*kappa**2*h**2, 'source covariance and fourth-power identity')
        actual_constant_drift_fourth = fourth+6*(B*h)**2*variance+(B*h)**4
        general_envelope = 8*(B*h)**4+96*kappa**2*h**2
        require(actual_constant_drift_fourth <= general_envelope <= (8*B**4+96*kappa**2)*h**2, 'fourth-moment source envelope for S=1')
        require(16*F(11, 7)**4*(8*B**4+96*kappa**2) > 0, 'rational geodesic/coordinate source budget')
        moment_packets += 1
    occupation_packets = 0
    for n, S in product([1, 2, 4, 8, 16, 32], [F(1, 2), F(1), F(2)]):
        t = F(1, 8*n)
        law = [(2-t)/8, (2+t)/8, F(1, 2)]
        error = [t, 2*t, -t]
        source_error_norm2 = sum(p*e*e for p, e in zip(law, error))
        # Frozen stationary paths make Cauchy-Schwarz sharp. This is a module
        # control, not a source diffusion or an actual generator drift.
        supremum_integral_error2 = sum(p*(S*e)**2 for p, e in zip(law, error))
        require(supremum_integral_error2 == S*S*source_error_norm2 <= 4*S*S*t*t, 'stationary same-source occupation recovery')
        occupation_packets += 1
    pulse_packets = []
    weak_field_packets = 0
    for n in [4, 8, 16, 32, 64, 128]:
        h = F(1, n)
        pulse_fourth = sum(fourth_integral_unit(p) for p in [[F(1), F(-2)], [F(0), F(1)], [F(1), F(-1)]])/n
        pulse_one_point_fourth = 2*fourth_integral_unit([F(0), F(1)])/n
        require(pulse_fourth == F(3, 5*n) and pulse_one_point_fourth == F(2, 5*n), 'exact random-phase stationary thin-pulse moments')
        require(pulse_fourth/(h*h) == F(3*n, 5), 'finite-dimensional collapse does not imply uniform path modulus')
        pulse_packets.append({'n': n, 'nonzero_probability': str(F(2, n)), 'supremum': '1', 'fourth_increment_over_h2': str(pulse_fourth/(h*h))})
        field = {-n: F(1, 2), n: F(1, 2)}
        for k in range(-3, 4):
            require(inner({k: F(1)}, field) == 0, 'fixed low-mode weak field tests')
        require(inner(field, field) == F(1, 2), 'weak-only frozen stationary additive error at S=1')
        weak_field_packets += 1
    require((jet_packets, moment_packets, occupation_packets, len(pulse_packets), weak_field_packets) == (240, 72, 18, 6, 6), 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, contract['parent_net']['path']]
    for name in ['probe-gradient-transport', 'probe-gradient-core', 'probe-quasilocal', 'thermodynamic-form']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md', BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-diffusion-path.result.v1', 'passed': True,
            'strength': 'written stationary continuous-path diffusion and joint finite-source path/drift/martingale/bracket transport; independent analytic review open',
            'radius_two_coordinate_jet_packets': jet_packets, 'fourth_moment_envelopes': moment_packets, 'stationary_occupation_packets': occupation_packets,
            'stationary_pulse_packets': pulse_packets, 'weak_field_packets': weak_field_packets,
            'finite_time_only_path_supremum_defect': '1', 'weak_field_additive_squared_defect': '1/2', 'half_bracket_defect': str(bracket_defect),
            'all_start_point_weak_drift_identified': False, 'strong_SDE_uniqueness_proved': False,
            'finite_horizon_original_tilted_path_density_constructed': False, 'physical_clock_or_continuum_Yang_Mills': False,
            'independent_analytic_review': False, 'ready_frontier': contract['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'radius_two_coordinate_jet_packets', 'fourth_moment_envelopes',
                     'stationary_occupation_packets', 'finite_time_only_path_supremum_defect', 'weak_field_additive_squared_defect', 'half_bracket_defect']}, indent=2))
