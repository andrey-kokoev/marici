"""Does normalized independent-product sewing select the residual resummation?"""
from itertools import product
from pathlib import Path
import hashlib
import json
import re
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
OWNER = ROOT/'research/nima'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    out = OWNER/'results/comparison-tensor-sewing.json'
    out.unlink(missing_ok=True)
    source = (OWNER/'agda/RetainedComparisonSeries.agda').read_text(encoding='utf-8')
    match = re.search(r'^swap-image-codes : .* ≡ \((\d+) , (\d+) , (\d+) , (\d+)\)$', source, re.M)
    image = tuple(map(int, match.groups()))
    p = s.Matrix(4, 4, lambda x, y: int(y == image[x]))
    phi, psi = s.Matrix(s.symbols('p0:4')), s.Matrix(s.symbols('q0:4'))
    norm = lambda v: (v.T*v)[0]
    pairing = lambda operator, v: (v.T*operator*v)[0]
    joint = s.kronecker_product(phi, psi)
    joint_operator = s.kronecker_product(p, p)
    assert s.expand(norm(joint)-norm(phi)*norm(psi)) == 0
    assert s.expand(pairing(joint_operator, joint)-pairing(p, phi)*pairing(p, psi)) == 0

    e, f, g = s.symbols('e f g')
    sew = lambda a, b: a+b-2*a*b
    assert s.expand(1-2*sew(e, f)-(1-2*e)*(1-2*f)) == 0
    assert s.expand(sew(sew(e, f), g)-sew(e, sew(f, g))) == 0
    # Derive coefficients from differentiated sewing, not a supplied log table.
    nmax = 10
    coefficients = s.symbols('a1:'+str(nmax+1))
    trial = sum(a*e**n for n, a in enumerate(coefficients, 1))
    ode = s.expand((1-2*e)*s.diff(trial, e)-1)
    solved = s.solve([ode.coeff(e, n) for n in range(nmax)], coefficients, dict=True)
    assert len(solved) == 1
    derived = [solved[0][a] for a in coefficients]
    assert derived == [s.Rational(2**(n-1), n) for n in range(1, nmax+1)]
    potential = -s.log(1-2*e)/2
    assert s.simplify((1-2*e)*s.diff(potential, e)-1) == 0
    # Full mixed functional identity through each controlled total degree.
    for cutoff in range(1, 8):
        polynomial = sum(derived[n-1]*e**n for n in range(1, cutoff+1))
        defect = s.Poly(s.expand(polynomial.subs(e, sew(e, f))-polynomial-polynomial.subs(e, f)), e, f)
        assert all(sum(monomial) > cutoff for monomial, coeff in defect.terms() if coeff != 0)
    # Exact finite polynomial truncation does NOT obey sewing.
    truncated = e+e*e
    defect4 = s.factor(truncated.subs(e, sew(e, f))-truncated-truncated.subs(e, f))
    assert s.expand(defect4-4*e*f*(e*f-e-f)) == 0
    ordinary = e/(1-2*e)
    ordinary_defect = s.factor(ordinary.subs(e, sew(e, f))-ordinary-ordinary.subs(e, f))
    assert ordinary_defect != 0
    # Highest mixed monomial obstructs every nonconstant finite polynomial.
    for degree in range(1, 9):
        leading = s.Poly(sew(e, f)**degree-e**degree-f**degree, e, f).coeff_monomial(e**degree*f**degree)
        assert leading == (-2)**degree

    # All source probes below are actual rational functions on the four values.
    field = s.Matrix([0, 2, 1, 0])
    c = pairing(p, field)/norm(field)
    energy = (1-c)/2
    assert c == s.Rational(4, 5) and energy == s.Rational(1, 10)
    c_joint = pairing(joint_operator, s.kronecker_product(field, field))/norm(s.kronecker_product(field, field))
    assert c_joint == c*c
    assert (1-c_joint)/2 == sew(energy, energy)
    assert defect4.subs({e: energy, f: energy}) == -s.Rational(19, 2500)
    assert s.expand_log(-s.log(c_joint)/2+s.log(c), force=False) == 0
    # Tensor composition is not repeated application on a single carrier.
    assert pairing(p*p, field)/norm(field) == 1
    assert c*c != 1
    # Positive/zero/negative overlaps are all admitted by the same source map.
    zero_field, negative_field = s.Matrix([0, 1, 0, 0]), s.Matrix([0, 1, -1, 0])
    assert pairing(p, zero_field) == 0 and norm(zero_field) > 0
    assert pairing(p, negative_field)/norm(negative_field) == -1
    assert s.log(s.Rational(5, 4)).is_positive is True
    # A finite additive extension at the absorbing zero would force this
    # nonzero positive action to vanish: L(0)=L(0)+L(4/5).

    x = s.Symbol('x')
    normalized_contrast_action = potential.subs(e, x*x/2)
    assert s.diff(normalized_contrast_action, x, 2).subs(x, 0) == 1
    assert s.diff(normalized_contrast_action, x, 4).subs(x, 0) == 6
    # Changing how the field is varied matters: fix the even part instead
    # of the total norm. Then the overlap is (1-x^2)/(1+x^2).
    fixed_even_action = -s.log((1-x*x)/(1+x*x))/2
    assert s.diff(fixed_even_action, x, 4).subs(x, 0) == 0
    assert s.simplify(normalized_contrast_action.subs(x*x, 2*x*x/(1+x*x))-fixed_even_action) == 0
    # Quartic approximation remainder coefficients and geometric majorant.
    expansion = s.series(normalized_contrast_action, x, 0, 14).removeO()
    assert s.expand(expansion-x*x/2-x**4/4).coeff(x, 6) == s.Rational(1, 6)

    receipt_path = OWNER/'results/agda-ComparisonTensorSewing.json'
    receipt = json.loads(receipt_path.read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['ignore_interfaces']
    imports = {}
    def visit(module):
        path = OWNER/'agda'/(module.replace('.', '/')+'.agda')
        if not path.exists() or module in imports:
            return
        imports[module] = sha(path)
        assert imports[module] == receipt['owner_source_inventory_sha256'][path.name].lower()
        for dep in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)', path.read_text(encoding='utf-8'), re.M):
            visit(dep)
    visit('ComparisonTensorSewing')
    result = {
        'schema': 'marici.nima.comparison-tensor-sewing.v1',
        'status': 'normalized_tensor_additivity_selects_formal_logarithm_conditionally',
        'normalized_energy': 'e=S_P(phi)/<phi,phi>=(1-c)/2, c=<phi,Pphi>/<phi,phi>',
        'source_sewing': 'e+f-2ef',
        'additional_readout_requirement': 'A(sew(e,f))=A(e)+A(f), A(0)=0, A_prime(0)=1; formal characteristic-zero series',
        'derived_potential': str(potential),
        'derived_coefficients': [str(a) for a in derived],
        'tower_reweighting': 'normalized n-slot mixed action / n',
        'quartic_truncation_defect': str(defect4),
        'actual_source_truncation_counterexample': '-19/2500 at e=f=1/10 from field (0,2,1,0)',
        'normalized_contrast_potential': str(normalized_contrast_action),
        'fourth_derivative_normalized_contrast': 6,
        'fourth_derivative_fixed_even_chart': 0,
        'domain': 'formal neighborhood e=0; real branch on 0<=e<1/2; zero overlap is singular; negative sign must be retained separately',
        'hostiles': ['ordinary geometric tower weights fail tensor additivity',
                     'nonconstant finite polynomial cannot obey exact sewing',
                     'tensor additivity is not sequential-comparison additivity',
                     'source admits zero overlap, prohibiting global finite nontrivial additive log',
                     'quartic coefficient depends on field chart without a kinetic identification'],
        'local_formal_import_sha256': imports,
        'source_sha256': {str(path.relative_to(ROOT)): sha(path) for path in (Path(__file__), receipt_path)},
        'scope': 'Actual source norm/overlap factorization and ring sewing identities are formal. Log uniqueness is a written formal-series argument with exact coefficient and truncation checks. Physical additivity, normalization, field chart, spacetime kinetic term and coupling are not derived.'
    }
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'coefficients': result['derived_coefficients'][:4],
                      'quartic_defect': str(defect4), 'quartic_vertex_in_normalized_chart': 6,
                      'formal_imports': len(imports)}))


if __name__ == '__main__':
    main()
