"""Source-bound comparison operators, formal generating series, scalarization controls."""
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import re
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
OWNER = ROOT/'research/nima'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    result_path = OWNER/'results/retained-comparison-series.json'
    result_path.unlink(missing_ok=True)
    source_path = OWNER/'agda/RetainedComparisonSeries.agda'
    source = source_path.read_text(encoding='utf-8')
    # These RHS images have fresh Agda refl proofs against the imported fillers.
    images = {}
    for name in ('identity', 'swap'):
        match = re.search(rf'^{name}-image-codes : .* ≡ \((\d+) , (\d+) , (\d+) , (\d+)\)$', source, re.M)
        assert match, name
        images[name] = tuple(map(int, match.groups()))
    identity, swap = images['identity'], images['swap']
    assert identity == (0, 1, 2, 3)
    assert swap == (0, 2, 1, 3)
    group = tuple((0,)+p for p in permutations((1, 2, 3)))
    index = {p: n for n, p in enumerate(group)}
    def compose(f, g):
        return tuple(g[f[x]] for x in range(4))  # g after f, as Boundary.compose
    def inverse(f):
        return tuple(f.index(x) for x in range(4))
    def matrix(f):
        return s.Matrix(4, 4, lambda x, y: int(y == f[x]))  # pullback
    matrices = {p: matrix(p) for p in group}
    eye, z = s.eye(4), s.Symbol('z')
    for f, g in product(group, repeat=2):
        assert matrices[compose(f, g)] == matrices[f]*matrices[g]
        assert matrices[f]*matrices[inverse(f)] == eye
        assert matrices[f].det()*matrices[g].det() == matrices[compose(f, g)].det()
    assert len({tuple(m) for m in matrices.values()}) == 6

    # The source loop has order two, so its FULL formal series is rational.
    p = matrices[swap]
    assert p*p == eye
    identity_series = eye/(1-z)
    swap_series = (eye+z*p)/(1-z*z)
    assert ((eye-z*p)*swap_series-eye).applyfunc(s.cancel) == s.zeros(4)
    response = (swap_series-identity_series).diff(z).subs(z, 0)
    assert response == p-eye
    assert response != s.zeros(4)
    trace_defect = s.factor(s.trace(swap_series-identity_series))
    assert s.cancel(trace_defect-(-2*z/(1-z*z))) == 0
    for n in range(13):
        assert p**n == (eye if n % 2 == 0 else p)
        assert s.trace(p**n) == (4 if n % 2 == 0 else 2)
    # Integrate the derived response in the finite counting pairing. Orthogonal
    # involution implies self-adjointness, hence a genuine scalar primitive.
    fields = s.Matrix(s.symbols('phi00 phi01 phi10 phi11'))
    residual = eye-p
    action = s.expand((fields.T*residual*fields)[0]/2)
    gradient = s.Matrix([s.diff(action, phi) for phi in fields])
    assert gradient == residual*fields
    assert s.expand(action-(fields[1]-fields[2])**2/2) == 0
    assert s.hessian(action, fields) == residual
    assert residual*residual == 2*residual
    assert (residual*(p*fields)) == -residual*fields
    assert s.expand(((p*fields).T*residual*(p*fields))[0]/2-action) == 0
    odd_projector = residual/2
    inverse_on_odd = residual/4
    assert odd_projector*odd_projector == odd_projector
    assert residual*inverse_on_odd == odd_projector
    assert inverse_on_odd*residual == odd_projector
    assert residual.rank() == 1 and residual.det() == 0
    assert s.Poly(action, *fields).total_degree() == 2
    assert all(s.diff(action, phi, 4) == 0 for phi in fields)
    integrable = []
    for f in group:
        r = eye-matrices[f]
        is_gradient = r == r.T
        assert is_gradient == (compose(f, f) == identity)
        integrable.append(is_gradient)
    assert sum(integrable) == 4  # identity and three transpositions; not the two 3-cycles

    # This generating series is NOT itself a multiplicative comparison weight.
    assert (identity_series*identity_series-identity_series).applyfunc(s.cancel) != s.zeros(4)

    # Enumerate scalar sign characters on ALL six admitted pointed bijections.
    characters = []
    for values in product((-1, 1), repeat=6):
        if values[index[identity]] != 1:
            continue
        if all(values[index[compose(f, g)]] == values[index[f]]*values[index[g]]
               for f, g in product(group, repeat=2)):
            characters.append(values)
    determinant = tuple(int(matrices[f].det()) for f in group)
    assert set(characters) == {tuple(1 for _ in group), determinant}
    assert int(p.det()) == -1
    assert len({tuple(m) for m in matrices.values()}) > len(set(determinant))
    three_cycle = (0, 2, 3, 1)
    assert matrices[three_cycle] != eye and matrices[three_cycle].det() == 1
    spectra = [s.factor((eye-z*matrices[f]).det()) for f in group]
    assert len(set(spectra)) == 3  # conjugacy data, not all six maps

    # Existing independent-expansion square: distinct schedules, equal operators.
    left = s.kronecker_product(p, eye)
    right = s.kronecker_product(eye, p)
    assert left*right == right*left
    assert left*right*left.inv()*right.inv() == s.eye(16)
    # Do not replace the source's commuting schedule pair with id versus swap.

    receipt_path = OWNER/'results/agda-RetainedComparisonSeries.json'
    receipt = json.loads(receipt_path.read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['ignore_interfaces']
    imports = {}
    def visit(module):
        path = OWNER/'agda'/(module.replace('.', '/')+'.agda')
        if not path.is_file() or module in imports:
            return
        imports[module] = digest(path)
        assert imports[module] == receipt['owner_source_inventory_sha256'][path.name].lower(), module
        for dep in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)', path.read_text(encoding='utf-8'), re.M):
            visit(dep)
    visit('RetainedComparisonSeries')
    assert 'BoundaryGeneratedQuestions' in imports and 'NativeTableRegression' in imports
    assert 'ObserverCoherenceCube' in imports
    result = {
        'schema': 'marici.nima.retained-comparison-series.v1',
        'status': 'source_comparison_series_and_quadratic_primitive_physical_selection_open',
        'source_images': images, 'source_boundary': 'BoundaryGeneratedQuestions.fourQ to itself, fixed selected point 00',
        'operator_variance': 'pullback: M(g after f)=M(f) M(g)',
        'formal_generating_series': {'identity': 'I/(1-z)', 'swap': '(I+z P)/(1-z^2)',
                                    'meaning': 'formal count of repeated comparison application; no convergence or physical time'},
        'first_derivative_of_series_difference': response.tolist(),
        'trace_series_difference': str(trace_defect),
        'derived_quadratic_action': str(action),
        'action_premises': 'linear pullback response and finite counting pairing; fields are formal source-value probes',
        'derived_action_gradient': [str(x) for x in gradient],
        'hessian_rank': 1, 'hessian_kernel_dimension': 3,
        'inverse_on_anti_invariant_sector': ' (I-P)/4; products with Hessian equal (I-P)/2, not I',
        'gradient_integrable_pointed_maps': sum(integrable),
        'quartic_vertex': 0,
        'orientation_weight_identity': 1, 'orientation_weight_swap': -1,
        'pointed_bijections': len(group), 'scalar_sign_characters': characters,
        'scalar_character_three_cycle_kernel': three_cycle,
        'matrix_representation_faithful_on_six_maps': True,
        'existing_independent_schedule_square_operator_defect': 0,
        'hostiles': ['truth quotient cannot retain first operator coefficient: Agda no-truth-factor',
                     'determinant loses nonidentity three-cycles', 'spectral determinant loses individual transpositions',
                     'iteration generating series is not a multiplicative comparison weight',
                     'retained schedule distinction alone does not force operator curvature'],
        'local_formal_import_sha256': imports,
        'source_sha256': {str(path.relative_to(ROOT)): digest(path) for path in (Path(__file__), receipt_path)},
        'scope': 'Exact source comparison representation, formal series, quadratic primitive of involutive residual in the counting pairing, and scalar character classification on S3. Not a physical action selection, partition functional, full-history faithful representation, or prediction of scalar coupling 3/5.'
    }
    # SymPy integer entries are serialized as ordinary JSON integers.
    result['first_derivative_of_series_difference'] = [[int(x) for x in row] for row in response.tolist()]
    result_path.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'derived_swap_orientation': -1,
                      'action': str(action), 'hessian_rank': 1, 'integrable_maps': sum(integrable),
                      'response': result['first_derivative_of_series_difference'],
                      'scalar_characters': len(characters), 'formal_imports': len(imports)}))


if __name__ == '__main__':
    main()
