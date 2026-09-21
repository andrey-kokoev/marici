#!/usr/bin/env python3
"""High-precision, scaled theta Gram diagnostics for hidden-channel readout.

uv run --with mpmath python research/voevodsky/checkers/check_theta_hidden_channel_gram.py

Quadrature refinements are convergence diagnostics, not interval certificates.
The exact transport matrices are supplied by check_theta_hidden_channel_transport.py.
"""
import itertools
import json
import time
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
mp.mp.dps = 65
source = json.loads((ROOT/'research/voevodsky/results/theta-hidden-channel-transport.json').read_text())
primes = (2,3,5,7)
endpoints = sorted(2*mp.fprod(primes[j] for j in range(4) if mask & (1<<j)) for mask in range(16))
endpoints = [int(x) for x in endpoints]
intervals = list(zip(endpoints, endpoints[1:]))


def scaled_half_gammas(x):
    # Returns exp(x)*Gamma(q,x) at q=5/2,7/2,9/2.
    g = mp.sqrt(mp.pi)*mp.exp(x)*mp.erfc(mp.sqrt(x))
    power = mp.sqrt(x)
    values = {}
    for numerator in (1,3,5,7):
        g = mp.mpf(numerator)/2*g+power
        power *= x
        values[numerator+2] = g
    return values[5],values[7],values[9]


def scaled_atom_factor(i, r):
    # H_i(s)=exp(-pi*(1+r)*a_i^2)*F_i(r), r=exp(2s).
    a,b=intervals[i]
    c=mp.pi*(1+r)
    def boundary(t):
        g5,g7,g9=scaled_half_gammas(c*t)
        return (4*mp.pi**2*r*g9/c**mp.mpf('4.5')
                -6*mp.pi*(1+r)*g7/c**mp.mpf('3.5')
                +9*g5/c**mp.mpf('2.5'))
    return mp.pi**2/2*r**mp.mpf('1.25')*(boundary(a*a)-mp.exp(-c*(b*b-a*a))*boundary(b*b))


factor0 = [scaled_atom_factor(i, mp.mpf(1)) for i in range(15)]
log_h0 = [mp.log(factor0[i])-2*mp.pi*intervals[i][0]**2 for i in range(15)]


def shape_gram(order):
    nodes,weights=mp.gauss_quadrature(order,'laguerre')
    C=mp.matrix(15)
    for i in range(15):
        for j in range(i,15):
            rate=mp.pi*(intervals[i][0]**2+intervals[j][0]**2)
            value=mp.mpf(0)
            for t,w in zip(nodes,weights):
                r=1+t/rate
                fi=scaled_atom_factor(i,r)/factor0[i]
                fj=fi if i==j else scaled_atom_factor(j,r)/factor0[j]
                value += w*fi*fj/r
            C[i,j]=C[j,i]=value/(2*rate)
    return C


def rational(x):
    if '/' in x:
        a,b=x.split('/')
        return mp.mpf(a)/mp.mpf(b)
    return mp.mpf(x)

R2=mp.matrix([[rational(x) for x in row] for row in source['theta_readout_R2']])
R4=mp.matrix([[rational(x) for x in row] for row in source['theta_readout_R4']])
keys2=source['second_degree_coordinates']
keys4=source['fourth_degree_coordinates']


def diagnose(C):
    scales=[mp.sqrt(C[i,i]) for i in range(15)]
    N=mp.matrix([[C[i,j]/(scales[i]*scales[j]) for j in range(15)] for i in range(15)])
    eig=mp.eigsy(N,eigvals_only=True)
    if eig[0] <= 0:
        raise ArithmeticError('Normalized Gram lost positivity at this precision')
    Ninv=N**-1
    # Physical atom norms: exp(log_h0[i])*sqrt(C_ii).
    log_norms=[log_h0[i]+mp.log(scales[i]) for i in range(15)]
    # L=G^-1 H*: its coefficient functionals have Gram G^-1.
    dual_log_norms=[mp.log(Ninv[i,i])/2-log_norms[i] for i in range(15)]
    dual_corr=mp.matrix([[Ninv[i,j]/mp.sqrt(Ninv[i,i]*Ninv[j,j]) for j in range(15)] for i in range(15)])
    logs2=[sum(dual_log_norms[i] for i in key) for key in keys2]
    logs4=[sum(dual_log_norms[i] for i in key) for key in keys4]
    largest=max(logs2+logs4)
    def dual_tensor_gram(keys, logs):
        return mp.matrix([[mp.exp(logs[i]+logs[j]-2*largest)
                           *mp.fprod(dual_corr[a,b] for a,b in zip(ki,kj))
                           for j,kj in enumerate(keys)] for i,ki in enumerate(keys)])
    D2=dual_tensor_gram(keys2,logs2)
    D4=dual_tensor_gram(keys4,logs4)
    noise=R2*D2*R2.T+R4*D4*R4.T
    # Exact PSD inequalities: max diagonal <= lambda_max <= trace.
    lower=largest+mp.log(max(noise[i,i] for i in range(6)))/2
    upper=largest+mp.log(sum(noise[i,i] for i in range(6)))/2
    channel_logs=[(largest+mp.log(noise[i,i])/2)/mp.log(10) for i in range(6)]
    inverse_lower=-min(log_norms)/mp.log(10)
    inverse_upper=(-min(log_norms)-mp.log(eig[0])/2)/mp.log(10)
    return N, {
        'normalized_atom_gram_smallest_eigenvalue':mp.nstr(eig[0],35),
        'normalized_atom_gram_largest_eigenvalue':mp.nstr(eig[14],35),
        'normalized_atom_gram_condition_number':mp.nstr(eig[14]/eig[0],35),
        'atom_log10_L2_norms':[mp.nstr(x/mp.log(10),35) for x in log_norms],
        'dual_atom_log10_norms':[mp.nstr(x/mp.log(10),35) for x in dual_log_norms],
        'log10_full_atom_extractor_norm_bracket_numeric':[mp.nstr(inverse_lower,35),mp.nstr(inverse_upper,35)],
        'log10_parity_channel_functional_norms':[mp.nstr(x,35) for x in channel_logs],
        'log10_joint_parity_readout_norm_bracket_numeric':[mp.nstr(lower/mp.log(10),35),mp.nstr(upper/mp.log(10),35)],
        'largest_selected_product_coordinate_degree':4 if max(logs4)>=max(logs2) else 2,
        'largest_selected_four_point_coordinate':keys4[logs4.index(max(logs4))],
    }

runs=[]
previous=None
lastN=None
for order in (24,48,72):
    start=time.monotonic()
    C=shape_gram(order)
    N,stats=diagnose(C)
    relative_change=None if previous is None else max(abs(C[i,j]-previous[i,j])/abs(C[i,j]) for i in range(15) for j in range(15))
    stats.update({'quadrature_order':order,'max_relative_gram_change':None if relative_change is None else mp.nstr(relative_change,20),
                  'elapsed_seconds':round(time.monotonic()-start,3)})
    runs.append(stats)
    previous=C
    lastN=N
    print('order',order,'shape min eig',stats['normalized_atom_gram_smallest_eigenvalue'],
          'parity log10 norm',stats['log10_joint_parity_readout_norm_bracket_numeric'],flush=True)

# Independently compare the incomplete-gamma formula with direct v integration,
# after scaling out the huge constant exponent, for three representative atoms.
def direct_factor(i,r):
    a,b=intervals[i]
    c=mp.pi*(1+r)
    # t=a^2+z/c: integrate an exponentially localized polynomial weight.
    upper=c*(b*b-a*a)
    cap=min(upper,mp.mpf(180))
    def f(z):
        t=a*a+z/c
        return mp.pi**2/2*r**mp.mpf('1.25')*t**mp.mpf('1.5')*(2*mp.pi*t-3)*(2*mp.pi*r*t-3)*mp.exp(-z)/c
    return mp.quad(f,[0,1,5,20,cap])

formula_errors=[]
for i,r in ((0,mp.mpf('1.2')),(7,mp.mpf('1.01')),(14,mp.mpf('1.0001'))):
    exact_expression=scaled_atom_factor(i,r)
    direct=direct_factor(i,r)
    formula_errors.append(abs(exact_expression-direct)/abs(exact_expression))

convergence=mp.mpf(runs[-1]['max_relative_gram_change'])
checks={
    'scaled_formula_matches_independent_quadrature':max(formula_errors)<mp.mpf('1e-45'),
    'last_gram_refinement_relative_change_below_1e_minus_30':convergence<mp.mpf('1e-30'),
    'all_normalized_grams_positive_at_working_precision':all(mp.mpf(r['normalized_atom_gram_smallest_eigenvalue'])>0 for r in runs),
}
out={
    'schema':'marici.voevodsky.theta-hidden-channel-gram-diagnostics.v1',
    'arithmetic_precision_decimal_digits':mp.mp.dps,
    'atom_endpoints':endpoints,
    'atom_definition':'Phi_1(v)=exp(v/2)*(2*pi^2*exp(4v)-3*pi*exp(2v))*exp(-pi*exp(2v)); H_i(s)=integral_[log(a),log(b)] Phi_1(v)Phi_1(v+s)dv, s>=0',
    'quadrature':'Scaled incomplete-gamma atom evaluation and high-precision Gauss-Laguerre Gram integration',
    'runs':runs,
    'normalized_atom_gram':[[mp.nstr(lastN[i,j],55) for j in range(15)] for i in range(15)],
    'independent_formula_relative_errors':[mp.nstr(x,20) for x in formula_errors],
    'checks':checks,'passed':all(checks.values()),
    'scope':'Converged numerical diagnostics in the declared unweighted L2(ds) atom metric. No interval-arithmetic enclosure or physical noise-floor certification. Readout norm is for the specific selected-coordinate dual-atom implementation on the full direct-sum tensor observation space.',
}
p=ROOT/'research/voevodsky/results/theta-hidden-channel-gram-diagnostics.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks':checks,'passed':out['passed'],'last':runs[-1]},indent=2))
raise SystemExit(0 if out['passed'] else 1)
