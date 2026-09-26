"""Separate native coefficient arithmetic, conditional Cayley algebra, and analytic admission."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json
import re
import sympy as s
import check_clifford_retained_order as source

OWNER = Path(__file__).resolve().parents[1]


def main():
    out = OWNER/'results/rational-rotor-source-audit.json'
    out.unlink(missing_ok=True)
    I,E1,E2,J = [s.Matrix(2,2,x) for x in source.BASIS]
    t,u = s.symbols('t u', real=True)
    def cayley(v):
        return ((1-v*v)*I+2*v*J)/(1+v*v)
    assert s.simplify(cayley(t).T*cayley(t)-I) == s.zeros(2)
    assert s.simplify(cayley(t)*cayley(u)-cayley((t+u)/(1-t*u))) == s.zeros(2)
    assert s.simplify(cayley(-t)-cayley(t).T) == s.zeros(2)
    assert cayley(0) == I and cayley(1) == J and cayley(-1) == -J
    assert s.simplify(s.diff(cayley(t),t)-2*J*cayley(t)/(1+t*t)) == s.zeros(2)
    assert s.diff(cayley(t),t).subs(t,0) == 2*J
    # Formal Maurer-Cartan differential, not a selected physical clock.
    composed = (t+u)/(1-t*u)
    assert s.simplify(2*s.diff(composed,t)/(1+composed**2)-2/(1+t*t)) == 0

    def homogeneous(m,n):
        den = m*m+n*n
        assert den != 0
        return (s.Rational(n*n-m*m,den)*I+s.Rational(2*m*n,den)*J)
    pairs = [(m,n) for m,n in product(range(-2,3),repeat=2) if (m,n)!=(0,0)]
    for m,n in pairs:
        assert homogeneous(m,n).T*homogeneous(m,n) == I
        for r,z in pairs:
            M,N = m*z+n*r,n*z-m*r
            assert homogeneous(m,n)*homogeneous(r,z) == homogeneous(M,N)
    assert homogeneous(1,0) == -I

    # ANY rational matrix square root of J would commute with J, so is even.
    variables = s.symbols('x00 x01 x10 x11')
    X = s.Matrix(2,2,variables)
    matrix,_ = s.linear_eq_to_matrix(list(X*J-J*X),variables)
    kernel = matrix.nullspace()
    span = s.Matrix.hstack(s.Matrix(list(I)),s.Matrix(list(J)))
    assert len(kernel) == 2
    assert s.Matrix.hstack(span,*kernel).rank() == 2
    aa,bb = s.symbols('aa bb')
    root_equations = [aa*aa-bb*bb,2*aa*bb-1]
    elimination = s.groebner(root_equations,aa,bb,order='lex')
    assert elimination.reduce(4*bb**4-1)[1] == 0
    factors = s.factor_list(4*bb**4-1,bb)[1]
    assert len(factors) == 2
    assert all(s.Poly(f,bb,domain=s.QQ).degree()==2 and s.Poly(f,bb,domain=s.QQ).is_irreducible
               for f,_ in factors)
    root = (I+J)/s.sqrt(2)
    assert root*root == J

    # An explicit rational rotor fails inherited pointwise source algebra.
    anchor,odd = (1,0,0,0),(0,1,-1,0)
    tensor = lambda a,b:s.Matrix([x*y for x in a for y in b])
    B = (tensor(anchor,anchor),tensor(anchor,odd),tensor(odd,anchor),tensor(odd,odd))
    hadamard = lambda a,b:s.Matrix([x*y for x,y in zip(a,b)])
    assert hadamard(B[1],B[2]) == s.zeros(16,1)
    # Ad(cayley(1/2)) sends e1 -> (-7/25)e1-(24/25)e2.
    V = cayley(s.Rational(1,2))
    c,d = s.Rational(-7,25),s.Rational(24,25)
    assert V*E1*V.T == c*E1-d*E2
    assert V*E2*V.T == d*E1+c*E2
    transformed1,transformed2 = c*B[1]-d*B[2],d*B[1]+c*B[2]
    assert hadamard(transformed1,transformed2) != s.zeros(16,1)
    assert B[1].dot(B[1]) == transformed1.dot(transformed1)

    formal_path = OWNER/'agda/RationalRotorNumerators.agda'
    receipt_path = OWNER/'results/agda-RationalRotorNumerators.json'
    receipt = json.loads(receipt_path.read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['ignore_interfaces']
    assert hashlib.sha256(formal_path.read_bytes()).hexdigest() == receipt['source_sha256'].lower()
    visited = set()
    def audit_imports(module):
        path = OWNER/'agda'/(module.replace('.','/')+'.agda')
        if not path.exists() or module in visited:
            return
        visited.add(module)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == receipt['owner_source_inventory_sha256'][path.name].lower()
        for dep in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)',path.read_text(encoding='utf-8'),re.M):
            audit_imports(dep)
    audit_imports('RationalRotorNumerators')
    assert 'RationalComponentArithmetic' in visited and 'ComponentArithmetic' in visited

    result = {
        'schema':'marici.nima.rational-rotor-source-audit.v1',
        'classification':'native_rational_coefficients_support_conditional_cayley_rotors_but_not_divisible_time_or_product_selection',
        'native_coefficient_input':'Constructed component semiring, signed quotient and rational localization; fresh polynomial proof instantiates the actual rationalRing.',
        'cayley':'V(t)=((1-t^2)I+2tJ)/(1+t^2); V(t)V(u)=V((t+u)/(1-tu)), completed by a homogeneous chart at infinity',
        'formal_tangent':'Vprime(t)=2J V(t)/(1+t^2); 2dt/(1+t^2) is the invariant angular differential',
        'rational_refinement_obstruction':'J has no square root anywhere in Mat_2(Q), so no additive divisible-parameter group valued there can reach J.',
        'admission_hostile':'The explicit rational adjoint rotor at t=1/2 preserves the active-vector counting norm but sends the zero pointwise product B1*B2 to a nonzero product.',
        'checked_homogeneous_products':len(pairs)**2,
        'fresh_local_imports':sorted(visited),
        'scope':'Constructed coefficient arithmetic and conditional rational Clifford algebra identities. Native response-to-implementer selection, metric compatibility, real completion, path selection and active-dynamics interpretation are not derived. The absence of a located admission constructor is not a universal impossibility theorem.',
        'input_sha256':{str(path.relative_to(OWNER)):hashlib.sha256(path.read_bytes()).hexdigest()
                        for path in (Path(__file__),Path(source.__file__),formal_path,receipt_path,
                                     OWNER/'agda/NativeTableRules.agda',OWNER/'agda/NativeRationalComponentArithmetic.agda')}
    }
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
