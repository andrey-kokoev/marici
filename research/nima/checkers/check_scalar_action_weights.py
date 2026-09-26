"""Action differentiation -> tree weights; audit what the source does NOT select.
Run with: uv run --with sympy python research/nima/checkers/check_scalar_action_weights.py
"""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json
import re
import sys
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
OWNER = ROOT / 'research/nima'
sys.path.insert(0, str(OWNER / 'amplitudes'))
import native_scalar_fibers as reference


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def zero(value):
    assert s.expand(value) == 0, value


def read_source():
    text = (OWNER / 'agda/ScalarSixFixture.agda').read_text(encoding='utf-8')
    def integer(kind, value):
        return int(value) if kind == 'pos' else -int(value)-1
    ps = []
    for label in range(6):
        line = re.search(rf'^momenta l{label} = (.+)$', text, re.M).group(1)
        ps.append(tuple(integer(k, n) for k, n in re.findall(r'\((pos|negsuc) (\d+)\)', line)))
    values = {}
    for name in ('couplingNumerator', 'couplingDenominator', 'exportedNumerator', 'exportedDenominator'):
        match = re.search(rf'^{name} = \((pos|negsuc) (\d+)\)', text, re.M)
        values[name] = integer(*match.groups())
    return ps, values


def main():
    out = OWNER / 'results/scalar-action-weights.json'
    out.unlink(missing_ok=True)
    phi, z, mass2, g = s.symbols('phi Z mass_squared lambda')
    derivatives = s.symbols('d0:4')
    momenta = s.symbols('q0:4')
    metric = (1, -1, -1, -1)
    lagrangian = z * sum(sign*x*x for sign, x in zip(metric, derivatives))/2 - mass2*phi**2/2 - g*phi**4/s.factorial(4)
    kinetic_hessian = s.hessian(lagrangian, derivatives)
    kernel = s.expand((s.Matrix(momenta).T * kinetic_hessian * s.Matrix(momenta))[0]
                      + s.diff(lagrangian, phi, 2).subs(phi, 0))
    q2 = sum(sign*x*x for sign, x in zip(metric, momenta))
    zero(kernel - (z*q2 - mass2))
    fourth = s.diff(lagrangian, phi, 4)
    zero(fourth + g)
    vertex = s.I * fourth
    # Formal Gaussian integration-by-parts identity. Vanishing boundary term,
    # the phase exp(iS), and a Green prescription are physical assumptions.
    x, k, covariance = s.symbols('x K G')
    ibp_polynomial = s.expand(s.diff(x*s.exp(s.I*k*x*x/2), x) / s.exp(s.I*k*x*x/2))
    zero(ibp_polynomial - (1+s.I*k*x*x))
    gaussian_identity = ibp_polynomial.subs(x*x, covariance)
    propagator = s.solve(gaussian_identity, covariance)[0]
    zero(k*propagator - s.I)
    term = s.simplify(vertex**2 * propagator / s.I)
    zero(term + g*g/k)
    phase_checks = []
    for vertices in range(1, 13):
        edges = vertices-1
        phase = s.simplify((-s.I)**vertices * s.I**edges / s.I)
        assert phase == -1
        phase_checks.append({'vertices': vertices, 'internal_edges': edges, 'stripped_phase': str(phase)})

    # Freeze the common physical restrictions independently of any readout.
    # These restrictions do not choose the remaining dimensionless coupling.
    zero(lagrangian.subs({phi: -phi, **{v: -v for v in derivatives}}, simultaneous=True) - lagrangian)
    invariant, scale, contact = s.symbols('s scale contact')
    canonical_kernel = kernel.subs({z: 1, mass2: 0})
    zero(canonical_kernel-q2)
    spectral_kernel = kernel.subs({momenta[1]: 0, momenta[2]: 0, momenta[3]: 0}).subs(momenta[0]**2, invariant)
    zero(spectral_kernel-(z*invariant-mass2))
    assert s.diff(spectral_kernel, invariant).subs(z, 1) == 1  # derived kinetic normalization
    residue = s.limit(invariant * term.subs(k, invariant), invariant, 0)
    zero(residue - (-(fourth*fourth)))
    zero(s.limit(invariant * (term.subs(k, invariant)+contact), invariant, 0)-residue)
    # An extra contact is outside the frozen pure-quartic grammar; it only
    # shows why pole residues alone cannot select that grammar.
    scaling_factorization = []
    for n in range(6, 22, 2):
        for left in range(4, n, 2):
            right = n+2-left
            if right < 4:
                continue
            assert n//2-1 == (left//2-1)+(right//2-1)
            scaling_factorization.append((n, left, right))

    ps, source = read_source()
    ps_fraction = tuple(tuple(Fraction(v) for v in p) for p in ps)
    reference.check_boundary(ps_fraction)
    source_coupling = s.Rational(source['couplingNumerator'], source['couplingDenominator'])
    declared_models = (source_coupling, 2*source_coupling)
    models = []
    unweighted_signatures = []
    for coupling in declared_models:
        assert coupling > 0
        terms = []
        compared = {}
        signature = []
        for i, j in combinations(range(1, 6), 2):
            labels = (0, i, j)
            complement = tuple(a for a in range(6) if a not in labels)
            momentum = tuple(sum(ps[a][mu] for a in labels) for mu in range(4))
            denominator = canonical_kernel.subs(dict(zip(momenta, momentum)))
            if denominator == 0:
                raise ValueError('internal pole: no rational propagator admitted')
            contribution = s.factor(term.subs({g: coupling, k: denominator}))
            # Calculation above never calls a reference amplitude or local weight.
            split = (labels, complement)
            compared[split] = Fraction(int(s.numer(contribution)), int(s.denom(contribution)))
            signature.append((split, momentum, int(denominator)))
            terms.append({'split': split, 'kernel': str(denominator), 'weight': str(contribution)})
        ref = dict(reference.contributions(reference.construct(ps_fraction, Fraction(str(coupling)))))
        assert compared == ref
        amplitude = s.factor(sum(s.Rational(w.numerator, w.denominator) for w in compared.values()))
        models.append({'coupling': str(coupling), 'four_point': str(fourth.subs(g, coupling)),
                       'six_point': str(amplitude), 'terms': terms,
                       'quadratic_kernel': str(canonical_kernel), 'kinetic_normalization': '1',
                       'even_field_parity': True, 'local_polynomial_quartic_interaction': True})
        unweighted_signatures.append(signature)
    assert unweighted_signatures[0] == unweighted_signatures[1]
    assert models[0]['six_point'] == str(s.Rational(source['exportedNumerator'], source['exportedDenominator']))
    assert models[0]['four_point'] != models[1]['four_point']
    assert models[0]['six_point'] != models[1]['six_point']
    action_difference = s.expand(lagrangian.subs(g, declared_models[1])-lagrangian.subs(g, declared_models[0]))
    assert action_difference != 0  # never claim these are the same marked source

    hostile_expressions = {
        'omitted_vertex_factorial_residual': s.diff(-g*phi**4, phi, 4)-fourth,
        'kernel_instead_of_inverse_residual': s.expand(k*(s.I*k)-s.I),
        'wrong_stripped_tree_sign_residual': s.simplify(-term-term),
        'unfixed_contact_changes_value_but_not_residue': contact,
    }
    assert all(value != 0 for value in hostile_expressions.values())
    hostiles = {key: str(value) for key, value in hostile_expressions.items()}
    formal_path = OWNER / 'results/agda-ScalarActionWeights.json'
    formal = json.loads(formal_path.read_text(encoding='utf-8-sig'))
    assert formal['passed'] and formal['ignore_interfaces']
    checked = {}
    def visit(name):
        path = OWNER / 'agda' / (name.replace('.', '/') + '.agda')
        if not path.is_file() or name in checked:
            return
        checked[name] = digest(path)
        assert checked[name] == formal['owner_source_inventory_sha256'][path.name].lower(), name
        for dep in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)', path.read_text(encoding='utf-8'), re.M):
            visit(dep)
    visit('ScalarActionWeights')
    result = {
        'schema': 'marici.nima.scalar-action-weights.v1',
        'status': 'conditional_derivation_with_coupling_nonuniqueness',
        'lagrangian': str(lagrangian), 'derived_hessian': str(kernel),
        'derived_fourth_variation': str(fourth), 'gaussian_ibp_identity': str(gaussian_identity),
        'derived_propagator_away_from_poles': str(propagator), 'derived_six_point_term': str(term),
        'models': models, 'same_unweighted_kinematic_incidence': True,
        'same_complete_marked_source': False, 'action_difference': str(action_difference),
        'phase_controls': phase_checks, 'factorization_scaling_arity_controls': scaling_factorization,
        'hostiles': hostiles, 'formal_local_import_sha256': checked,
        'source_sha256': {str(p.relative_to(ROOT)): digest(p) for p in
            (Path(__file__), Path(reference.__file__), formal_path, OWNER/'agda/ScalarSixFixture.agda')},
        'remaining_inputs': ['Lorentz metric and local scalar action class', 'masslessness and kinetic normalization',
                             'coupling value', 'exp(iS) and Gaussian/Wick pairing with boundary prescription',
                             'external kinematics', 'geometric component hypothesis'],
        'scope': 'Formal polynomial derivatives, general nonzero-integer inverse proof, ten formal channel comparisons and native coupling counterexample. Symbolic action/phase audit and finite fixture checks. Not a derivation of physical selection from bare fibration or a construction of a continuum path integral.'
    }
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'models': [{k: m[k] for k in ('coupling', 'four_point', 'six_point')} for m in models],
                      'formal_imports': len(checked), 'hostiles': hostiles}))


if __name__ == '__main__':
    main()
