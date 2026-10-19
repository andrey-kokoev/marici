"""Exact weak-gradient/core controls; finite circles are not SU2 eigenfunctions."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_probe_quasilocal import report as predecessor_report
from check_yang_mills_probe_pressure import require

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-gradient-core.v1.json'
NOTE = BASE+'yang-mills-probe-gradient-core-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_gradient_core.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-gradient-core-v1.json')


def add(f, g):
    return {j: f.get(j, F(0))+g.get(j, F(0)) for j in f.keys() | g.keys()}


def scale(f, c):
    return {j: c*x for j, x in f.items()}


def mul(f, g):
    out = {}
    for j, x in f.items():
        for k, y in g.items():
            out[j+k] = out.get(j+k, F(0))+x*y
    return out


def derivative(f):
    # D=z*d/dz; the real circle derivative is i*D.
    return {j: j*x for j, x in f.items()}


def inner(f, g):
    # All Fourier coefficients in these tests are real rationals, although
    # the tested Laurent functions need not be real-valued.
    return sum((x*g.get(j, F(0)) for j, x in f.items()), F(0))


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(contract['batch_iteration'] == 9 and contract['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in contract['boundary'].values()) and not contract['parent_net']['discharges_parent'], 'scope')
    require(contract['subnet']['parent_outcome'] is None and contract['subnet']['ready_frontier'] == ['small-probe-gradient-transport'], 'gradient-transport frontier')
    parent = json.loads((ROOT/contract['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == contract['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-quasilocal-v1.json')).read_text()), 'fresh quasilocal receipt')
    fourier_packets = 0
    for epsilon, kappa, j, k in product([F(0), F(1, 64), F(1, 32), F(1, 16)], [F(1, 2), F(1), F(2)], [-1, 0, 1, 2], [-1, 0, 1, 2]):
        psi = {-1: epsilon/2, 0: F(1), 1: epsilon/2}
        dp = derivative(psi)
        ddp = derivative(dp)
        normalizer = inner(psi, psi)
        f, g = {j: F(1)}, {k: F(1)}
        df, dg = derivative(f), derivative(g)
        require(normalizer == 1+epsilon**2/2 and 1-epsilon > 0, 'positive actual multiplier and probability normalizer')
        require(kappa*epsilon/(1-epsilon) <= kappa/15 < kappa/8, 'continuous-circle norm-small potential')
        # <g,Df>_weighted=<Dg+2(Dpsi/psi)g,f>_weighted;
        # this is weak integration by parts for X=iD, with conjugation.
        left_ibp = inner(mul(psi, g), mul(psi, df))
        right_ibp = inner(add(mul(psi, dg), scale(mul(dp, g), 2)), mul(psi, f))
        require(left_ibp == right_ibp, 'actual weak logarithmic derivative, including mixed terms')
        source_energy = kappa*inner(derivative(mul(psi, f)), derivative(mul(psi, g)))
        potential_energy = -kappa*inner(mul(psi, f), mul(ddp, g))
        gradient_energy = kappa*inner(mul(psi, df), mul(psi, dg))
        require((source_energy+potential_energy)/normalizer == gradient_energy/normalizer, 'ground-state weak eigenfunction cancellation and normalized weighted form')
        fourier_packets += 1
    epsilon = F(1, 16)
    psi = {-1: epsilon/2, 0: F(1), 1: epsilon/2}
    f, one = {-1: F(1, 2), 1: F(1, 2)}, {0: F(1)}
    normalizer = inner(psi, psi)
    af = derivative(derivative(f))
    naive = inner(mul(psi, f), mul(psi, af))/normalizer
    actual = inner(mul(psi, derivative(f)), mul(psi, derivative(f)))/normalizer
    drift_defect = naive-actual
    symmetry_defect = (inner(mul(psi, one), mul(psi, af))-inner(mul(psi, derivative(derivative(one))), mul(psi, f)))/normalizer
    require(drift_defect == F(1, 1026), 'omitting weak drift hostile energy')
    require(symmetry_defect == F(32, 513), 'original A is not symmetric in the tilted space')
    range_packets = young_packets = 0
    for R, kappa, gradient_u in product([F(0), F(1, 128), F(9, 128), F(575, 4096)], [F(1, 2), F(1), F(2)], [F(0), F(1)]):
        m = kappa*(F(1, 2)-3*R)
        L = gradient_u/m
        alpha = kappa*(1+4*L**2)
        norm_bound_squared = kappa*L**2/alpha
        require(alpha > 0 and norm_bound_squared < F(1, 4), 'Neumann full range with inverse factor at most2')
        for spectral_lambda in [F(0), m, alpha, 4*alpha]:
            require(4*kappa*L**2*spectral_lambda/(alpha+spectral_lambda)**2 <= norm_bound_squared, 'actual spectral resolvent envelope')
        for eta, u, v in product([F(1, 4), F(1, 2), F(3, 4)], [F(0), F(1), F(4)], [F(0), F(1), F(4)]):
            rhs = eta*u+kappa*L**2*v/eta
            require(rhs**2-4*kappa*L**2*u*v == (eta*u-kappa*L**2*v/eta)**2 >= 0, 'relative bound0 and graph-norm equivalence')
            young_packets += 1
        range_packets += 1
    cusp_cuts = []
    for n in [2, 4, 8, 9, 16, 32]:
        cutoff = F(1, n*n)
        exponent = F(1, 4)
        integral_coefficient = exponent**2/(1-2*exponent)
        energy = integral_coefficient*(n-1)
        require(cutoff*n*n == 1 and energy > 0 and energy == F(n-1, 8), 'exact localized cusp derivative energy')
        cusp_cuts.append({'n': n, 'cutoff': str(cutoff), 'energy': str(energy)})
    require(next(c['energy'] for c in cusp_cuts if c['n'] == 9) == '1', 'bounded-positive multiplier hostile')
    require((fourier_packets, range_packets, young_packets) == (192, 24, 648), 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, contract['parent_net']['path']]
    for name in ['probe-quasilocal', 'probe-doob', 'thermodynamic-form', 'propagator-comparison']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md', BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-gradient-core.result.v1', 'passed': True,
            'strength': 'written actual tilted closed form, L2 cylinder operator core and weak logarithmic drift; independent analytic review open',
            'continuous_circle_fourier_packets': fourier_packets, 'source_range_graph_envelopes': range_packets, 'young_scalar_subtests': young_packets,
            'missing_weak_drift_energy_defect': str(drift_defect), 'wrong_measure_original_generator_symmetry_defect': str(symmetry_defect),
            'bounded_positive_multiplier_cusp_cuts': cusp_cuts, 'cusp_energy_growth_law': '(N-1)/8, unbounded',
            'gradient_norm_transport_proved': False, 'classical_smooth_log_drift_proved': False,
            'C_X_generator_cylinder_core_proved': False, 'independent_analytic_review': False, 'continuum_Yang_Mills': False,
            'ready_frontier': contract['subnet']['ready_frontier'], 'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'continuous_circle_fourier_packets', 'source_range_graph_envelopes',
                     'young_scalar_subtests', 'missing_weak_drift_energy_defect', 'wrong_measure_original_generator_symmetry_defect']}, indent=2))
