"""Exact Hermitian Jordan invariance and the fixed-Clark-port rank gate.

The polynomial kernel fixture only separates numerator rank from divided-
difference rank. It is not an arithmetic or positivity certificate.
"""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]


def main():
    U = sp.Matrix([[1, 0, 0], [1, 1, 0], [0, 1, 1]])
    a,b,c,e,f,g,h,j,k = sp.symbols('a b c e f g h j k', real=True)
    Q = sp.Matrix([[a,b+sp.I*h,c+sp.I*j], [b-sp.I*h,e,f+sp.I*k], [c-sp.I*j,f-sp.I*k,g]])
    parameters = (a,b,c,e,f,g,h,j,k)
    solution = next(iter(sp.linsolve(list(U.T*Q*U-Q), parameters)))
    invariant = Q.subs(dict(zip(parameters, solution)), simultaneous=True)
    expected = sp.Matrix([[a,-e/2+sp.I*h,-e],[-e/2-sp.I*h,e,0],[-e,0,0]])
    assert invariant == expected
    assert U.T*invariant*U == invariant
    assert sp.factor(invariant.det()) == -e**3
    C = sp.Matrix([[0,0,-1,1],[0,0,-1,1],[-1,-1,0,0],[1,1,0,0]])/2
    assert C.rank() == 2
    singular = invariant.subs(e, 0)
    assert singular[:, 2] == sp.zeros(3, 1)
    assert sp.factor(singular[:2,:2].det()) == -h**2
    # An injective map can still pull back a degenerate invariant form.
    # This algebraic example does not assert a source-derived Clark map.
    J = sp.Matrix([[1,0,1],[0,0,-1],[-a,-2*sp.I*h,0],[0,0,0]])
    assert sp.simplify(J.conjugate().T*C*J-singular) == sp.zeros(3)
    assert J.subs({a:0,h:1}).rank() == 3
    assert singular.subs(h,0) == sp.diag(a,0,0)

    # A full divided difference may have larger rank than its numerator.
    w,z = sp.symbols('w z', real=True)
    X = lambda t: t**3+t
    numerator = 2*sp.I*(X(w)*sp.diff(X(z),z)-sp.diff(X(w),w)*X(z))
    kernel = sp.cancel(numerator/(-sp.I*(z-w)))
    polynomial = sp.expand(kernel)
    coefficient = sp.Matrix([[polynomial.coeff(w,i).coeff(z,j) for j in range(3)] for i in range(3)])
    assert coefficient == sp.Matrix([[2,0,2],[0,-4,0],[2,0,6]])
    nodes = (0,1,2)
    N = sp.Matrix([[numerator.subs({w:x,z:y}) for y in nodes] for x in nodes])
    K = sp.Matrix([[kernel.subs({w:x,z:y}) for y in nodes] for x in nodes])
    assert N.rank() == 2 and K.rank() == 3 and K.det() == -128
    # The even-degree 2x2 block is positive; the odd-degree block is negative.
    assert coefficient.extract([0,2],[0,2]).det() == 8
    assert coefficient[0,0] == 2 and coefficient[1,1] == -4
    result = {
        'schema': 'marici.voevodsky.clark-history-jordan-metric-gate.v1',
        'passed': True,
        'hermitian_invariant_form': [[str(x) for x in invariant.row(i)] for i in range(3)],
        'determinant': '-e^3',
        'fixed_clark_coefficient_rank': 2,
        'consequence_under_invariance': 'Any fixed-port Clark pullback has e=0, hence d^2 is in its radical. If h!=0 its rank is two and d survives; a positive semidefinite pullback also has h=0.',
        'abstract_injective_rank_three_map_with_degenerate_pullback_checked': True,
        'polynomial_kernel_fixture': {
            'X': 'z^3+z', 'kernel': str(polynomial),
            'nodes': list(nodes), 'numerator_rank': 2, 'divided_difference_rank': 3,
            'divided_difference_determinant': '-128', 'divided_difference_inertia': [2,1,0],
        },
        'source_map_from_history_to_full_clark_kernel_constructed': False,
        'scope': 'Exact algebraic necessary conditions. The polynomial fixture and abstract map do not identify an arithmetic source realization.',
    }
    out = ROOT / 'research/voevodsky/results/clark-history-jordan-metric-gate.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
