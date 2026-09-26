"""Mixed action-composition defect, product probes, and the even-degree tower."""
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
    out = OWNER/'results/comparison-mixed-residual.json'
    out.unlink(missing_ok=True)
    source = (OWNER/'agda/RetainedComparisonSeries.agda').read_text(encoding='utf-8')
    match = re.search(r'^swap-image-codes : .* ≡ \((\d+) , (\d+) , (\d+) , (\d+)\)$', source, re.M)
    image = tuple(map(int, match.groups()))
    p = s.Matrix(4, 4, lambda x, y: int(y == image[x]))
    eye = s.eye(4)
    r = eye-p
    a, b = s.kronecker_product(p, eye), s.kronecker_product(eye, p)
    unit = s.eye(16)
    ra, rb, rab = unit-a, unit-b, unit-a*b
    mixed = ra+rb-rab
    assert a*b == b*a
    assert mixed == ra*rb == rb*ra == s.kronecker_product(r, r)
    assert mixed != s.zeros(16)
    assert mixed.rank() == 1 and mixed*mixed == 4*mixed
    assert (mixed/4)**2 == mixed/4

    phi = s.Matrix(s.symbols('phi00 phi01 phi10 phi11'))
    psi = s.Matrix(s.symbols('psi00 psi01 psi10 psi11'))
    def action(operator, field):
        return s.expand((field.T*operator*field)[0]/2)
    s2 = action(r, phi)
    independent_product = s.kronecker_product(phi, psi)
    e4_independent = action(mixed, independent_product)
    assert s.expand(e4_independent-2*s2*action(r, psi)) == 0
    product_probe = s.kronecker_product(phi, phi)
    e4 = action(mixed, product_probe)
    delta = phi[1]-phi[2]
    assert s.expand(e4-delta**4/2) == 0
    assert s.expand(e4-2*s2*s2) == 0
    assert s.expand(action(ra, product_probe)+action(rb, product_probe)-action(rab, product_probe)-e4) == 0
    # On a purely odd probe, the simultaneous action is zero but the defect is not.
    x = s.Symbol('x')
    odd = {phi[0]: 0, phi[1]: x/2, phi[2]: -x/2, phi[3]: 0}
    assert action(rab, product_probe).subs(odd) == 0
    assert s.expand(e4.subs(odd)-x**4/2) == 0
    assert s.diff(e4.subs(odd), x, 4) == 12
    assert s.hessian(e4, phi).subs(dict.fromkeys(phi, 0)) == s.zeros(4)
    # Chain rule: residual on 16 joint coordinates is not the 4-coordinate gradient.
    jacobian = product_probe.jacobian(phi)
    gradient = s.Matrix([s.diff(e4, variable) for variable in phi])
    assert (gradient-jacobian.T*mixed*product_probe).applyfunc(s.expand) == s.zeros(4, 1)
    assert (gradient-jacobian.T*mixed*product_probe/2).applyfunc(s.expand) != s.zeros(4, 1)

    # Linearization of the source point-copy is NOT the nonlinear product probe.
    copy = s.zeros(16, 4)
    for i in range(4):
        copy[4*i+i, i] = 1
    assert copy.T*copy == eye
    assert a*b*copy == copy*p
    assert action(rab, copy*phi) == s2
    copy_mixed = action(mixed, copy*phi)
    assert s.expand(copy_mixed-(phi[1]+phi[2])**2/2) == 0
    assert s.Poly(copy_mixed, *phi).total_degree() == 2
    assert s.Poly(e4, *phi).total_degree() == 4
    joint_variables = s.Matrix(s.symbols('joint0:16'))
    assert s.hessian(action(mixed, joint_variables), joint_variables) == mixed
    assert s.Poly(action(mixed, joint_variables), *joint_variables).total_degree() == 2

    # Inclusion-exclusion of the ACTUAL independent comparison maps, not a
    # fitted polynomial. Exhaust every corner through four independent slots.
    tower = []
    for n in range(1, 5):
        states = tuple(product(range(4), repeat=n))
        amplitudes = {state: s.prod(phi[i] for i in state) for state in states}
        corners = {}
        for mask in product((0, 1), repeat=n):
            if not any(mask):
                continue
            corners[mask] = s.expand(sum(amplitudes[state]*(amplitudes[state]-amplitudes[
                tuple(image[i] if flag else i for i, flag in zip(state, mask))]) for state in states)/2)
        mixed_energy = s.expand(sum((-1)**(sum(mask)+1)*energy for mask, energy in corners.items()))
        assert s.expand(mixed_energy-delta**(2*n)/2) == 0
        tower.append({'slots': n, 'corners': len(corners), 'states': len(states),
                      'degree': s.Poly(mixed_energy, *phi).total_degree(),
                      'contrast_vertex': int(s.factorial(2*n)/2)})
    t = s.Symbol('t')
    generating_action = x*x/(2*(1-t*x*x))
    for n in range(1, 5):
        assert s.expand(s.diff(generating_action, t, n-1).subs(t, 0)/s.factorial(n-1)-x**(2*n)/2) == 0
    # A physical interaction coefficient still can be independently assigned.
    kappa = s.Symbol('kappa')
    assert s.diff(x*x/2+kappa*x**4/2, x, 4) == 12*kappa

    receipt_path = OWNER/'results/agda-ComparisonMixedResidual.json'
    receipt = json.loads(receipt_path.read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['ignore_interfaces']
    imports = {}
    def visit(module):
        path = OWNER/'agda'/(module.replace('.', '/')+'.agda')
        if not path.exists() or module in imports:
            return
        imports[module] = sha(path)
        assert imports[module] == receipt['owner_source_inventory_sha256'][path.name].lower(), module
        for dep in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)', path.read_text(encoding='utf-8'), re.M):
            visit(dep)
    visit('ComparisonMixedResidual')
    result = {
        'schema': 'marici.nima.comparison-mixed-residual.v1',
        'status': 'mixed_composition_defect_yields_quartic_under_product_probe',
        'source_swap_images': image,
        'commutator': 0, 'mixed_operator': '(I-A)(I-B)=(I-P) tensor (I-P)',
        'mixed_operator_rank': int(mixed.rank()),
        'action_defect': 'S_A+S_B-S_AB',
        'quartic_product_probe': str(s.factor(e4)),
        'quadratic_linear_copy_probe': str(s.factor(copy_mixed)),
        'independent_joint_degree': 2,
        'diagonal_product_degree': 4,
        'contrast_fourth_derivative': 12,
        'added_interaction_fourth_derivative': '12*kappa; kappa not source-selected',
        'tower_controls': tower,
        'tower_generating_action': str(generating_action),
        'hostiles': ['commuting paths do not imply additive action',
                     'simultaneous action vanishes on pure odd product but mixed defect survives',
                     'linearized source copy remains quadratic',
                     'product-probe gradient requires its Jacobian',
                     'same recipe also produces sextic and octic terms; quartic truncation not selected'],
        'assumptions': ['existing finite comparison and independent product lifts',
                        'linear pullback and finite counting pairing',
                        'factorized multiplicative probe; repeated same probe for a single-field quartic'],
        'local_formal_import_sha256': imports,
        'source_sha256': {str(path.relative_to(ROOT)): sha(path) for path in (Path(__file__), receipt_path)},
        'scope': 'Generic commutative-ring binary residual and quartic-numerator proofs; symbolic action checks and finite tower controls. No physical product-state preparation, quartic truncation, quantum prescription or coupling prediction.'
    }
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'quartic': str(s.factor(e4)),
                      'linear_copy': str(s.factor(copy_mixed)), 'fourth_derivative': 12,
                      'degrees': [row['degree'] for row in tower], 'formal_imports': len(imports)}))


if __name__ == '__main__':
    main()
