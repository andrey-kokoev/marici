"""Counting-metric kinetic readout and coordinate-invariant tree four-point test."""
from itertools import permutations
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
    out = OWNER/'results/comparison-kinetic-readout.json'
    out.unlink(missing_ok=True)
    source = (OWNER/'agda/RetainedComparisonSeries.agda').read_text(encoding='utf-8')
    match = re.search(r'^swap-image-codes : .* ≡ \((\d+) , (\d+) , (\d+) , (\d+)\)$', source, re.M)
    image = tuple(map(int, match.groups()))
    p = s.Matrix(4, 4, lambda i, j: int(j == image[i]))
    anchor = s.Matrix([1, 0, 0, 0])
    odd = s.Matrix([0, 1, -1, 0])/s.sqrt(2)
    assert p*anchor == anchor and p*odd == -odd
    assert (s.eye(4)-p).rank() == 1 and (anchor.T*odd)[0] == 0
    theta, u, z, epsilon, eta = s.symbols('theta u z epsilon eta', real=True)
    F, U = s.symbols('F U', positive=True)
    v = s.Symbol('v', real=True)
    curves = {
        'angle': (theta, s.cos(theta)*anchor+s.sin(theta)*odd),
        'fixed_even_ratio': (u, (anchor+u*odd)/s.sqrt(1+u*u)),
        'unit_odd_component': (z, s.sqrt(1-z*z)*anchor+z*odd),
    }
    expected_metric = [1, 1/(1+u*u)**2, 1/(1-z*z)]
    expected_overlap = [s.cos(2*theta), (1-u*u)/(1+u*u), 1-2*z*z]
    rows = []
    for (name, (coordinate, curve)), metric_expected, c_expected in zip(curves.items(), expected_metric, expected_overlap):
        assert s.simplify(s.trigsimp((curve.T*curve)[0]-1)) == 0
        c = s.trigsimp((curve.T*p*curve)[0])
        metric = s.trigsimp((curve.diff(coordinate).T*curve.diff(coordinate))[0])
        assert s.simplify(c-c_expected) == 0
        assert s.simplify(metric-metric_expected) == 0
        potential = -U*s.log(c)/2
        potential_v = s.series(potential.subs(coordinate, v/F), v, 0, 5).removeO().expand()
        metric_v = s.series(metric.subs(coordinate, v/F), v, 0, 3).removeO().expand()
        m2 = s.diff(potential_v, v, 2).subs(v, 0)
        lambda_potential = s.diff(potential_v, v, 4).subs(v, 0)
        derivative_coefficient = metric_v.coeff(v, 2)/2
        assert s.simplify(m2-2*U/F**2) == 0
        effective = s.simplify(lambda_potential-8*derivative_coefficient*m2)
        assert s.simplify(effective-16*U/F**4) == 0
        rows.append({'chart': name, 'metric': str(metric), 'overlap': str(c),
                     'potential_fourth_derivative': str(lambda_potential),
                     'derivative_vertex_coefficient': str(derivative_coefficient),
                     'on_shell_quartic': str(effective)})
    assert [row['potential_fourth_derivative'] for row in rows] == ['16*U/F**4', '0', '24*U/F**4']

    # Same normalized-overlap readout between neighboring probes supplies metric.
    curve = curves['angle'][1]
    neighbor_overlap = s.trigsimp((curve.T*curve.subs(theta, theta+epsilon))[0])
    assert s.trigsimp(neighbor_overlap-s.cos(epsilon)) == 0
    neighbor_cost = -s.log(neighbor_overlap)/2
    assert s.simplify(2*s.diff(neighbor_cost, epsilon, 2).subs(epsilon, 0)) == 1
    product_cost = -s.log(s.cos(epsilon)*s.cos(eta))/2
    product_metric = (2*s.hessian(product_cost, (epsilon, eta))).subs({epsilon: 0, eta: 0})
    assert product_metric == s.eye(2)

    # Enumerate assignments of four external legs to a*v^2*(dv)^2.
    a, m2, lam, beta = s.symbols('a m2 lam beta')
    dots = {(i, j): s.Symbol(f'd{i}{j}') for i in range(4) for j in range(i+1, 4)}
    derivative_vertex = -s.I*a*sum(dots[tuple(sorted(order[2:]))] for order in permutations(range(4)))
    assert s.expand(derivative_vertex+4*s.I*a*sum(dots.values())) == 0
    # All momenta incoming, signature +---. Momentum conservation and equal
    # on-shell masses imply sum_{i<j} p_i.p_j = -2*m2.
    E, k = s.symbols('E k', real=True)
    momenta = [s.Matrix(t) for t in [(E,k,0,0), (E,-k,0,0), (-E,0,-k,0), (-E,0,k,0)]]
    lorentz = s.diag(1,-1,-1,-1)
    assert sum(momenta, s.zeros(4, 1)) == s.zeros(4, 1)
    assert all((q.T*lorentz*q)[0] == E*E-k*k for q in momenta)
    concrete_dots = {dots[i,j]: (momenta[i].T*lorentz*momenta[j])[0] for i,j in dots}
    assert s.expand(derivative_vertex.subs(concrete_dots)-8*s.I*a*(E*E-k*k)) == 0
    # Cubic reparametrization v=w+beta*w^3 preserves this on-shell combination.
    assert s.expand((lam+24*m2*beta)-8*(a+3*beta)*m2-(lam-8*a*m2)) == 0

    # Full normalized four-coordinate carrier has two additional massless modes.
    t, b, d = s.symbols('t b d', real=True)
    coords = s.Matrix([t,b,d])
    full = s.Matrix([s.sqrt(1-t*t-b*b-d*d), (b+t)/s.sqrt(2), (b-t)/s.sqrt(2), d])
    c_full = s.expand((full.T*p*full)[0])
    assert c_full == 1-2*t*t
    full_metric = (full.jacobian(coords).T*full.jacobian(coords)).applyfunc(s.simplify)
    inverse_metric = s.eye(3)-coords*coords.T
    assert (full_metric*inverse_metric-s.eye(3)).applyfunc(s.simplify) == s.zeros(3)
    full_potential = -s.log(c_full)/2
    assert s.hessian(full_potential, coords).subs({t:0,b:0,d:0}) == s.diag(2,0,0)
    gradient = inverse_metric*s.Matrix([s.diff(full_potential, x) for x in coords])
    for normal in (1,2):
        assert s.simplify(gradient[normal].subs({b:0,d:0})) == 0
        gamma = sum(inverse_metric[normal,j]*(2*s.diff(full_metric[j,0],t)-s.diff(full_metric[0,0],coords[j]))/2 for j in range(3))
        assert s.simplify(gamma.subs({b:0,d:0})) == 0

    # Covariance alone permits metric changes; these FAIL tensor-metric sewing.
    alpha = s.Symbol('alpha', real=True)
    deformed = 1+alpha*s.sin(theta)**2
    a_deformed = s.expand(s.series(deformed.subs(theta,v/F),v,0,3).removeO()).coeff(v,2)/2
    lambda_deformed = s.simplify(16*U/F**4-8*a_deformed*(2*U/F**2))
    assert s.simplify(lambda_deformed-(16-8*alpha)*U/F**4) == 0
    assert lambda_deformed.subs(alpha,2) == 0
    # Hold first factor at theta, move second through its vacuum. A conformal
    # f(e) correction gives f(e_first) instead of required f(0)=1.
    assert (deformed-1).subs(theta,s.pi/6) == alpha/4
    # An even stronger local countermetric makes the one-dimensional model free,
    # but again is not the metric of the declared neighboring-overlap readout.
    A = -s.log(s.cos(2*theta))/2
    free_metric = s.diff(A,theta)**2/(4*A)
    assert s.series(free_metric,theta,0,5).removeO().expand() == 1+2*theta**2+4*theta**4
    sextic = s.diff(U*A,theta,6).subs(theta,0)/F**6
    assert s.simplify(sextic-512*U/F**6) == 0
    assert s.simplify(sextic-4*(16*U/F**4)**2/(2*U/F**2)) == 0

    receipt_path = OWNER/'results/agda-ComparisonKineticReadout.json'
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
    visit('ComparisonKineticReadout')
    result = {
        'schema':'marici.nima.comparison-kinetic-readout.v1',
        'status':'counting_metric_readout_has_chart_invariant_tree_quartic_conditionally',
        'source_swap_images':image,
        'source_plane':'selected-point basis vector plus image(I-P)',
        'neighbor_readout':'D(n,m)=-log(<n,m>)/2 for unit probes; metric=2*Hessian at diagonal',
        'conditional_lagrangian':'F^2/2*(d theta)^2 - U*(-log(cos(2 theta))/2)',
        'canonical_field':'varphi=F*theta',
        'mass_squared':'2*U/F^2', 'on_shell_quartic':'16*U/F^4',
        'dimensionless_relation':'lambda*F^2/mass_squared=8',
        'canonical_sextic':'512*U/F^6 = 4*lambda^2/mass_squared; single-field tree truncation',
        'charts':rows,
        'additional_modes':'two massless even-direction modes; scalar plane is classically consistent, not a quantum decoupling theorem',
        'source_symmetric_metric_rival':str(lambda_deformed),
        'rival_disposition':'conformal rival preserves P and vacuum norm but violates independent tensor-metric sewing; no general uniqueness theorem for all metrics',
        'local_formal_import_sha256':imports,
        'source_sha256':{str(path.relative_to(ROOT)):sha(path) for path in (Path(__file__),receipt_path)},
        'scope':'Agda proves source plane and tangent-pairing identities plus cubic-chart algebra. Symbolic geometry and conventional tree vertex checks are conditional on the declared kinetic extension, spacetime/Fourier rules, and free scales F,U. No physical coupling or spacetime derivation.'
    }
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'mass_squared':result['mass_squared'],
                      'on_shell_quartic':result['on_shell_quartic'],'chart_count':len(rows),
                      'formal_imports':len(imports)}))


if __name__ == '__main__':
    main()
