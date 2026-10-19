"""A rational Weil projector, not a proved all-cycle Hodge obstruction."""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from math import comb
from pathlib import Path
import json
from check_hodge_literature_boundary_audit import combine, weil_forms, wedge
from check_hodge_explicit_sixfold_candidate import full_pullback, report as candidate_report

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / 'research/conjecture_net/contracts/hodge-weil-projector.v1.json'
NOTE = ROOT / 'research/voevodsky/hodge-weil-projector-v1.md'
OUT = ROOT / 'research/voevodsky/results/hodge-weil-projector-v1.json'
MODULI = ((15625,234,1), (15625,70,1), (15625,-150,1), (-125,1))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def trim(p):
    p = list(map(Q, p))
    while p and not p[-1]:
        p.pop()
    return p


def pmul(a, b):
    out = [Q(0)] * (len(a)+len(b)-1) if a and b else []
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def padd(a, b, sign=1):
    out = [Q(0)]*max(len(a),len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += sign*x
    return trim(out)


def remainder(a, b):
    a, b = trim(a), trim(b)
    require(bool(b), 'zero modulus')
    while len(a) >= len(b):
        scale, shift = a[-1]/b[-1], len(a)-len(b)
        for i, x in enumerate(b):
            a[shift+i] -= scale*x
        a = trim(a)
    return a


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def cpow(a, n):
    out = (Q(1),Q(0))
    for _ in range(n):
        out = cmul(out,a)
    return out


def peval(p, z):
    out = (Q(0),Q(0))
    for x in reversed(p):
        out = cmul(out,z)
        out = out[0]+x,out[1]
    return out


def projection_polynomial():
    m0,m1,m2,m3 = MODULI
    q = pmul(pmul(m1,m2),m3)
    c,d = remainder(q,m0)
    denominator = c*(c-234*d)+15625*d*d
    s = [(c-234*d)/denominator, -d/denominator]
    p = pmul(s,q)
    require(remainder(p,m0) == [Q(1)] and all(not remainder(p,m) for m in (m1,m2,m3)), 'CRT projector')
    return p,q,s


def f_matrix(real=2, imaginary=1):
    f = [[Q(0)]*12 for _ in range(12)]
    for j in range(6):
        f[2*j][2*j], f[2*j+1][2*j+1] = real,real
        f[2*j][2*j+1], f[2*j+1][2*j] = -imaginary,imaginary
    return f


def apply_polynomial(p, form):
    out = {}
    for coefficient in reversed(p):
        out = full_pullback(f_matrix(),out)
        out = combine(out,{s: coefficient*v for s,v in form.items()})
    return {s:v for s,v in out.items() if v}


def witness_coefficients(a,b):
    a,b = Q(a),Q(b)
    require(bool(a or b), 'zero Weil witness')
    return (44*a+117*b)/(44*(a*a+b*b)), b/(44*(a*a+b*b))


@lru_cache(maxsize=1)
def exact_core():
    # Fixed rational computations only; mutable source reads remain uncached.
    p,q,s = projection_polynomial()
    minimal = [Q(1)]
    for m in MODULI:
        minimal = pmul(minimal,m)
    require(not remainder(padd(pmul(p,p),p,-1),minimal), 'idempotence modulo minimal polynomial')
    multiplicities, values = [], []
    for a in range(7):
        value = cmul(cpow((Q(2),Q(1)),a),cpow((Q(2),Q(-1)),6-a))
        values.append(value)
        multiplicities.append(comb(6,a)**2)
        require(peval(p,value) == (Q(int(a in (0,6))),Q(0)), 'separated characters')
    require(len(set(values)) == 7 and sum(multiplicities) == 924, 'full exterior spectrum')
    require(sum(n for a,n in enumerate(multiplicities) if peval(p,values[a])[0]) == 2, 'projector rank')
    real,imaginary = weil_forms(6)
    require(full_pullback(f_matrix(),real) == combine({s:-117*v for s,v in real.items()},{s:-44*v for s,v in imaginary.items()}), 'F on R')
    require(full_pullback(f_matrix(),imaginary) == combine({s:44*v for s,v in real.items()},{s:-117*v for s,v in imaginary.items()}), 'F on I')
    require(apply_polynomial(p,real) == real and apply_polynomial(p,imaginary) == imaginary, 'fixed Weil generators')
    E = {(2*j,2*j+1):d for j,d in enumerate((1,1,1,-1,-1,-3))}
    cube = wedge(wedge(E,E),E)
    require(full_pullback(f_matrix(),cube) == {s:125*v for s,v in cube.items()} and not apply_polynomial(p,cube), 'divisor cube killed')
    # Full H^6 hostile: (1+i) cannot distinguish endpoints from a=2,4.
    coarse_rank = sum(n for a,n in enumerate(multiplicities) if a % 2 == 0)
    for a in range(7):
        eigenvalue = cmul(cpow((Q(1),Q(1)),a),cpow((Q(1),Q(-1)),6-a))
        require(peval([Q(1,2),0,Q(-1,128)],eigenvalue) == (Q(int(a % 2 == 0)),Q(0)), 'coarse aliasing formula')
    require(coarse_rank == 452, 'coarse character rank')
    # Rational witnesses with negative coefficients and denominators included.
    samples = [(Q(a,3),Q(b,5)) for a in range(-3,4) for b in range(-3,4) if a or b]
    for a,b in samples:
        c,d = witness_coefficients(a,b)
        require(c*a+d*(-117*a+44*b) == 1 and c*b+d*(-44*a-117*b) == 0, 'Weil witness conversion')
        require(-44*(a*a+b*b) != 0, 'irreducible rational Weil plane')
    # Special fiber: R is an explicit polynomial in rational divisor classes.
    r,im = {():Q(1)},{}
    for j in range(3):
        a,b = 2*j,2*(j+3)
        rj,sj = {(a,b):1,(a+1,b+1):-1},{(a,b+1):1,(a+1,b):1}
        r,im = combine(wedge(r,rj),wedge(im,sj),-1),combine(wedge(r,sj),wedge(im,rj))
    special_R = {s:-v for s,v in r.items()}
    require(special_R == real and apply_polynomial(p,special_R) == real, 'uniform annihilation counterexample')
    return {'polynomial_coefficients_ascending':[str(x) for x in p],
            'factor_q_coefficients_ascending':[str(x) for x in q],
            'inverse_linear_coefficients_ascending':[str(x) for x in s],
            'H6_dimension':924,'rational_projector_rank':2,'coarse_1_plus_i_projector_rank':coarse_rank,
            'character_multiplicities':multiplicities,'witness_conversion_control_count':len(samples)}


def validate_projector(c):
    require(c['schema'] == 'marici.hodge-weil-projector.v1' and
            c['candidate_id'] == 'marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1','projector source identity')
    require(c['resolved_nodes'] == {
        'obstruction-construction':'explicit_candidate_weil_isotypic_projector_without_annihilation',
        'cohomology-descent':'functorial_cohomology_projector_independent_of_presentations',
        'rational-survival':'nonzero_rational_rank_two_projector_target',
        'candidate-obstruction-nonzero':'fixed_alpha_is_fixed_by_candidate_projector'}, 'projector node bindings')
    d = c['definition']
    require(d['endomorphism'] == 'f=2+i on the fixed polarized Q(i)-abelian sixfold' and
            tuple(tuple(d[k]) for k in ('m0','m1','m2','m3')) == MODULI and
            d['coefficient_order'] == 'ascending_powers' and
            d['factored_numerator_linear'] == [-10391779,-68381] and
            d['common_denominator'] == 930187500000000000 and
            d['all_cycle_quotient_used'] is False,'projector formula or circularity')
    require(c['admitted_operations'] == ['rational_linear_combinations_of_cohomology_pullbacks',
            'flat_pullback_CH3_Q_by_the_explicit_finite_etale_isogenies_f_to_power_k'],'untyped pullback extension')
    policy = c['algebraic_cycle_policy']
    require(policy['preserves_algebraic_cycle_classes'] is True and
            policy['Chow_idempotence_claimed'] is False and
            policy['annihilates_divisor_products_on_selected_X'] is True and
            policy['annihilates_all_algebraic_cycles_on_selected_X'] is False,'cycle preservation promoted to annihilation')
    require(c['rejected_uniform_claim']['id'] == 'uniform-weil-projector-annihilation' and
            c['rejected_uniform_claim']['verdict'] == 'rejected','uniform rejection lost')
    require(len(c['boundary']) == 8 and all(v is False for v in c['boundary'].values()),'projector promoted to Hodge verdict')


def report():
    c = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_projector(c)
    candidate = json.loads((ROOT/c['candidate_receipt']).read_text(encoding='utf-8'))
    require(candidate == candidate_report() and candidate['candidate_id'] == c['candidate_id'],'candidate binding stale')
    core = exact_core()
    require(core['inverse_linear_coefficients_ascending'] ==
            [str(Q(x,c['definition']['common_denominator'])) for x in c['definition']['factored_numerator_linear']],
            'displayed projector coefficients')
    checks = dict.fromkeys([
        'exact_seven_character_spectrum_and_rank_two_CRT_idempotent',
        'candidate_alpha_and_other_weil_generator_fixed_exactly',
        'divisor_cube_annihilated_without_all_cycle_claim',
        'coarse_1_plus_i_projector_rejected_by_rank_452_hostile',
        'rational_denominators_and_negative_witness_coefficients_verified',
        'nonzero_weil_witness_converts_to_fixed_alpha_in_48_rational_controls',
        'special_fiber_algebraic_weil_class_refutes_uniform_annihilation',
        'cycle_preserving_correspondence_not_claimed_chow_idempotent_or_annihilator',
        'same_selected_candidate_and_prior_membership_proofs_retained',
    ],True)
    sources = {p.relative_to(ROOT).as_posix() for p in (CONTRACT,NOTE,Path(__file__).resolve())} | {
        c['candidate_contract'],c['candidate_receipt'],
        'research/voevodsky/checkers/check_hodge_explicit_sixfold_candidate.py',
        'research/voevodsky/checkers/check_hodge_literature_boundary_audit.py'}
    return {'schema':'marici.hodge-weil-projector-result.v1','passed':True,'checks':checks,
            'candidate_id':c['candidate_id'],'resolved_nodes':c['resolved_nodes'], **core,
            'verification_level':'Written spectral/descent and cycle-functoriality proofs, exact polynomial/exterior controls; not proof-assistant formalization or all-cycle annihilation.',
            'candidate_map_constructed':True,'cohomology_descent_proved':True,'rational_survival_proved':True,
            'candidate_value':'O(alpha)=alpha','candidate_value_nonzero_proved':True,
            'preserves_algebraic_cycle_classes':True,'uniform_annihilation_candidate_verdict':'rejected',
            'all_cycle_annihilation_equivalent_to_alpha_nonalgebraicity':True,
            'validated_hodge_obstruction':False,'all_cycle_annihilation_proved':False,
            'alpha_nonalgebraic_proved':False,'algebraic_representative_of_alpha_constructed':False,
            'Hodge_proved':False,'Hodge_refuted':False,
            'source_sha256':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'source_sha256'},indent=2))
