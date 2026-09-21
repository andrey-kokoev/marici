#!/usr/bin/env python3
"""Exact transport of route parity channels into minimal theta coordinates."""
import importlib.util
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
source = json.loads((ROOT/'research/grothendieck/results/minimal-theta-four-point-completion.json').read_text())
words = [tuple(w) for w in source['route_order']]
Minv = s.Matrix([[s.Rational(x) for x in row] for row in source['inverse_matrix']])
M = Minv.inv()
keys2 = [tuple(k) for k in source['second_degree_coordinates']]
keys4 = [tuple(k) for k in source['fourth_degree_coordinates']]
spec = importlib.util.spec_from_file_location('theta_signature', ROOT/'research/grothendieck/theta_interval_signature.py')
theta = importlib.util.module_from_spec(spec)
spec.loader.exec_module(theta)
observations = [theta.observe_route(w) for w in words]
rebuilt = s.Matrix([[o[2].get(k,0) for o in observations] for k in keys2]
                  +[[o[4].get(k,0) for o in observations] for k in keys4])
blocks = sorted({tuple(tuple(sorted(w[j:j+2])) for j in (0,2)) for w in words})
K = s.zeros(24,6)
for i,w in enumerate(words):
    block = tuple(tuple(sorted(w[j:j+2])) for j in (0,2))
    K[i,blocks.index(block)] = (-1)**sum(w[j]>w[j+1] for j in (0,2))
P = K*K.T/4
B = K.T/2
R = B*Minv
R2, R4 = R[:,:18], R[:,18:]
Q = M[18:,:]*K
visible_four_point_prediction = -Q*R2/2
all_keys2 = sorted(set().union(*(set(o[2]) for o in observations)))
full_two_point = s.Matrix([[o[2].get(key,0) for o in observations] for key in all_keys2])

# Rigorous absolute-noise obstruction in the stated theta L2 metric.
# Machin identity and alternating arctangent bounds certify pi > 157/50.
pi_lower = 16*(s.Rational(1,5)-s.Rational(1,3*5**3))-s.Rational(4,239)
log10_upper = s.Rational(2303,1000)
exp_lower = sum(log10_upper**j/s.factorial(j) for j in range(17))
starts = (2,10,70,140)
prefactor = 2*(16*s.prod(starts))**7
exponent_lower = 2*s.Rational(157,50)*sum(a*a for a in starts)
certified_digits = 67000
certificate_checks = {
    'machin_lower_bound_exceeds_3_14': pi_lower>s.Rational(157,50),
    'exp_rational_partial_sum_exceeds_10': exp_lower>10,
    'tensor_prefactor_below_10_power_50': prefactor<10**50,
    'exponential_margin': exponent_lower>(certified_digits+50)*log10_upper,
}
transported_projector = M*P*Minv
transported_metric = Minv.T*Minv
raw_metric_error = transported_projector.T-transported_projector
c = s.Matrix([s.Rational((7*i)%11-5,i+1) for i in range(24)])
y = M*c
checks = {
    'measurement_rebuilt_from_source_events': M == rebuilt,
    'measurement_unimodular': M.det() == 1,
    'parity_basis_orthogonal': K.T*K == 4*s.eye(6),
    'two_point_kernel_is_our_parity_space': M[:18,:].rank()==18 and M[:18,:]*K==s.zeros(18,6),
    'entire_two_point_tensor_annihilates_parity': full_two_point*K==s.zeros(full_two_point.rows,6),
    'parity_readout_is_orthonormal_on_source': B*B.T==s.eye(6),
    'transported_readout_exact': R*M==B and R*y==B*c,
    'four_point_hidden_response_invertible': Q.det()!=0,
    'four_point_readout_formula': R4==2*Q.inv(),
    'route_projector_is_orthogonal': P*P==P and P.T==P,
    'measurement_projector_idempotent': transported_projector**2==transported_projector,
    'measurement_projector_self_adjoint_in_pulled_source_metric':
        transported_projector.T*transported_metric==transported_metric*transported_projector,
    'hidden_route_reconstruction': K*R*y/2==P*c,
    'visible_baseline_formula': R*y==2*Q.inv()*(y[18:,:]-visible_four_point_prediction*y[:18,:]),
    'rigorous_absolute_noise_lower_bound_certificate': all(certificate_checks.values()),
}

def rows(A):
    return [[str(x) for x in A.row(i)] for i in range(A.rows)]

out = {
    'schema':'marici.voevodsky.theta-hidden-channel-transport.v1',
    'blocks':[[list(pair) for pair in block] for block in blocks],
    'route_order':[list(w) for w in words],
    'second_degree_coordinates':keys2,'fourth_degree_coordinates':keys4,
    'parity_basis_K':rows(K),'source_projector':rows(P),
    'theta_readout_R2':rows(R2),'theta_readout_R4':rows(R4),
    'four_point_hidden_response_Q':rows(Q),
    'visible_four_point_prediction':rows(visible_four_point_prediction),
    'rigorous_noise_certificate': {
        'any_exact_linear_parity_decoder_norm_strictly_exceeds':f'10^{certified_digits}',
        'source_unit_vector':'K[:,5]/2, pair block ((2,3),(0,1))',
        'minimum_edge_starts':list(starts),
        'metric':'Direct-sum unweighted L2((0,infinity)^2) and L2((0,infinity)^4); unit source parity coordinates',
        'checks':{k:bool(v) for k,v in certificate_checks.items()},
        'analytic_inequality':'||H_[log a,log b]||_2 < (2a)^7 exp(-2*pi*a^2), for b>a>=2',
    },
    'measurement_projector':rows(transported_projector),
    'measurement_projector_is_euclidean_symmetric':raw_metric_error==s.zeros(24),
    'checks':checks,'passed':all(checks.values()),
    'formula':'b=(K^T/2)c=R2*y2+R4*y4; c_hidden=(K/2)b; y=M c',
}
p=ROOT/'research/voevodsky/results/theta-hidden-channel-transport.json'
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('parity_basis_K','source_projector','measurement_projector','route_order')},indent=2))
raise SystemExit(0 if out['passed'] else 1)
