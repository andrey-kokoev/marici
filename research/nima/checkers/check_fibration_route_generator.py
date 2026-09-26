"""Compare actual bare regrouping with an explicitly additional transport model."""
from pathlib import Path
import hashlib
import json
import re
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
OWNER = ROOT / 'research/nima'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    x, y, r, a, b, coupling = s.symbols('x y r a b lambda')
    coefficients = s.symbols('c0:5')
    potential = sum(c*x**n for n, c in enumerate(coefficients))
    # Total space (x,y,r) -> base (x,y), with scalar fiber r. These lifts
    # are extra data, not consequences of regrouping a fixed table.
    def input_lift(state, step):
        u, v, w = state
        return u+step, v, w
    def output_lift(state, step):
        u, v, w = state
        return u, v+step, w+step*potential.subs(x, u)
    state = (x, y, r)
    input_output = output_lift(input_lift(state, a), b)
    output_input = input_lift(output_lift(state, b), a)
    assert input_output[:2] == output_input[:2]  # common comparison fiber
    defect = s.expand(input_output[2]-output_input[2])
    assert s.expand(defect-b*(potential.subs(x, x+a)-potential)) == 0
    loop = output_lift(input_lift(input_output, -a), -b)
    assert loop[:2] == state[:2]
    assert s.expand(loop[2]-r-defect) == 0
    curvature = s.diff(defect, a, b).subs({a: 0, b: 0})
    assert s.expand(curvature-s.diff(potential, x)) == 0
    primitive = s.integrate(curvature, x)
    assert s.expand(primitive-(potential-potential.subs(x, 0))) == 0
    assert s.diff(defect, coefficients[0]) == 0  # constant is invisible
    # Ordinary mixed partials of the same scalar do commute. The nonzero
    # object is the mixed derivative of a composition defect, not their difference.
    assert s.expand(s.diff(defect, a, b)-s.diff(defect, b, a)) == 0
    quartic = {coefficients[n]: coupling/s.factorial(4) if n == 4 else 0 for n in range(5)}
    quartic_curvature = s.factor(curvature.subs(quartic))
    assert quartic_curvature == coupling*x**3/6
    assert s.diff(quartic_curvature, x, 3) == coupling
    assert curvature.subs({c: 0 for c in coefficients}) == 0
    assert s.expand(quartic_curvature-coupling*x**4/24) != 0
    assert s.expand(quartic_curvature.subs(coupling, s.Rational(3, 5))-
                    quartic_curvature.subs(coupling, s.Rational(6, 5))) != 0

    receipt_path = OWNER / 'results/agda-FibrationRouteInterchange.json'
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
    visit('FibrationRouteInterchange')
    result = {
        'schema': 'marici.nima.fibration-route-generator.v1',
        'status': 'bare_regrouping_flat_extra_transport_has_curvature',
        'total_space': '(x,y,r) -> (x,y); r is a scalar fiber coordinate, not physical time or action by default',
        'transport_provenance': 'declared polynomial toy connection; not derived from TableFibrationCycle',
        'finite_route_defect': str(defect), 'mixed_route_derivative': str(curvature),
        'reconstructed_polynomial': str(primitive), 'lost_constant': str(coefficients[0]),
        'quartic_response': str(quartic_curvature), 'coupling_extracted_by_third_x_derivative': str(coupling),
        'hostiles': {'bare_grouping_nonzero_row_defect': 'excluded by Agda readout-commutes',
                     'ordinary_mixed_partials_noncommuting': 'false',
                     'route_derivative_equals_potential': 'false for the quartic model',
                     'recover_potential_constant_from_defect': 'impossible in this model',
                     'toy_transport_selects_coupling': 'false; coefficient remains an input'},
        'local_formal_import_sha256': imports,
        'source_sha256': {str(path.relative_to(ROOT)): sha(path) for path in (Path(__file__), receipt_path)},
        'scope': 'Actual endpoint-fiber interchange is formal and universe-polymorphic. Extra polynomial connection calculation is symbolic, degree <=4. No physical generating functional or source-selected transport is derived.'
    }
    (OWNER/'results/fibration-route-generator.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'mixed_route_derivative': str(curvature),
                      'quartic_response': str(quartic_curvature), 'lost_constant': str(coefficients[0])}))


if __name__ == '__main__':
    main()
