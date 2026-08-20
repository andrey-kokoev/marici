"""Fast exact bivariate nine-master connection in u=ell4 and v=ell3."""

from __future__ import annotations

import argparse
import json
import sys
import traceback
from dataclasses import dataclass

def _write_uncaught(exc_type, exc, tb):
    Path(__file__).with_name("bivariate_soft_gram_connection.error.txt").write_text(
        "".join(traceback.format_exception(exc_type, exc, tb)), encoding="utf-8"
    )
    sys.__excepthook__(exc_type, exc, tb)

sys.excepthook = _write_uncaught
from pathlib import Path
from typing import Iterable

import sympy as sp
from sympy.polys.matrices import DomainMatrix


SCHEMA = "marici.benincasa.nine_master_residue_connection.v1"
DEFAULT_RESULT = Path(__file__).with_suffix(".result.json")


@dataclass(frozen=True)
class Master:
    name: str
    source_numerator: sp.Expr
    pole: str
    numerator: sp.Expr
    parity: tuple[int, int]


@dataclass
class Reduction:
    coefficients: list[sp.Expr]
    primitives: dict[str, sp.Expr]
    attempts: list[dict[str, object]]
    cleared_residual: sp.Expr


def canonical(expr: sp.Expr) -> sp.Expr:
    """Canonical rational-function representative without heuristic floats."""

    return sp.cancel(expr)


def expression_string(expr: sp.Expr) -> str:
    # All connection entries have already passed through the fraction-field
    # RREF.  Re-cancelling every entry here is expensive and adds no proof.
    return sp.sstr(expr, order="lex")


def matrix_strings(matrix: sp.MatrixBase) -> list[list[str]]:
    return [
        [expression_string(matrix[row, col]) for col in range(matrix.cols)]
        for row in range(matrix.rows)
    ]


def total_degree_monomials(
    aa: sp.Symbol,
    bb: sp.Symbol,
    degree: int,
    parity: tuple[int, int],
) -> list[sp.Expr]:
    if degree < 0:
        return []
    answer: list[sp.Expr] = []
    for total in range(degree + 1):
        for degree_a in range(total + 1):
            degree_b = total - degree_a
            if (degree_a % 2, degree_b % 2) == parity:
                answer.append(aa**degree_a * bb**degree_b)
    return answer


class ExactReducer:
    """Solve polynomial Griffiths--Dwork identities over QQ(a1,lambda)."""

    # Bounds are (degree at s=1/2, degree at s=3/2).  A simple-pole
    # derivative is cleared only to K0^(3/2), so it never needs s=3/2.
    # Double-pole derivatives are cleared to K0^(5/2).  These finite
    # schedules are fixed before inspecting the connection coefficients.
    SIMPLE_BOUNDS = ((0, -1), (1, -1), (2, -1), (3, -1))
    DOUBLE_BOUNDS = ((0, 0), (1, 1), (2, 3), (3, 5), (3, 7))

    def __init__(
        self,
        aa: sp.Symbol,
        bb: sp.Symbol,
        parameter_field,
        polynomial: sp.Expr,
        masters: list[Master],
    ) -> None:
        self.a = aa
        self.b = bb
        self.field = parameter_field
        self.K = sp.Poly(polynomial, aa, bb, domain=parameter_field).as_expr()
        self.Ka = sp.diff(self.K, aa)
        self.Kb = sp.diff(self.K, bb)
        self.masters = masters
        self.basis_common = {
            clearing_level: [
                master.numerator
                * self.K
                ** (
                    clearing_level
                    - (0 if master.pole == "simple" else 1)
                )
                for master in masters
            ]
            for clearing_level in (1, 2)
        }

    def polynomial_dict(self, expr: sp.Expr) -> dict[tuple[int, int], object]:
        poly = sp.Poly(sp.expand(expr), self.a, self.b, domain=self.field)
        return dict(poly.terms())

    def exact_column(
        self,
        monomial: sp.Expr,
        axis: str,
        s: sp.Rational,
        clearing_level: int,
    ) -> sp.Expr:
        if axis == "U":
            numerator = self.K * sp.diff(monomial, self.a) - s * monomial * self.Ka
        else:
            # d(V da/K^s) = (-K V_b + s V K_b) da db/K^(s+1).
            numerator = -self.K * sp.diff(monomial, self.b) + s * monomial * self.Kb
        output_level = int(s + sp.Rational(1, 2))
        return sp.expand(numerator * self.K ** (clearing_level - output_level))

    def candidates(
        self,
        target_parity: tuple[int, int],
        bounds: tuple[int, int],
        clearing_level: int,
    ) -> tuple[list[sp.Expr], list[tuple[str, sp.Expr]]]:
        candidates: list[sp.Expr] = []
        labels: list[tuple[str, sp.Expr]] = []

        for index, master in enumerate(self.masters):
            if master.parity == target_parity:
                candidates.append(self.basis_common[clearing_level][index])
                labels.append((f"basis:{index}", sp.Integer(1)))

        for s, degree, tag in zip(
            (sp.Rational(1, 2), sp.Rational(3, 2)),
            bounds,
            ("half", "three_half"),
        ):
            if degree < 0:
                continue
            u_parity = (target_parity[0] ^ 1, target_parity[1])
            v_parity = (target_parity[0], target_parity[1] ^ 1)
            for monomial in total_degree_monomials(self.a, self.b, degree, u_parity):
                candidates.append(self.exact_column(monomial, "U", s, clearing_level))
                labels.append((f"U:{tag}", monomial))
            for monomial in total_degree_monomials(self.a, self.b, degree, v_parity):
                candidates.append(self.exact_column(monomial, "V", s, clearing_level))
                labels.append((f"V:{tag}", monomial))
        return candidates, labels

    def linear_system(
        self, candidates: list[sp.Expr], target: sp.Expr
    ) -> tuple[DomainMatrix, list[tuple[int, int]]]:
        column_dicts = [self.polynomial_dict(candidate) for candidate in candidates]
        target_dict = self.polynomial_dict(target)
        monomials = sorted(
            set(target_dict).union(*(set(column) for column in column_dicts)),
            key=lambda item: (sum(item), item),
        )
        zero = self.field.zero
        rows = [
            [column.get(monomial, zero) for column in column_dicts]
            + [target_dict.get(monomial, zero)]
            for monomial in monomials
        ]
        return DomainMatrix.from_list(rows, self.field), monomials

    def solve(
        self,
        target: sp.Expr,
        target_parity: tuple[int, int],
        target_name: str,
        clearing_level: int,
    ) -> Reduction:
        attempts: list[dict[str, object]] = []
        schedule = self.SIMPLE_BOUNDS if clearing_level == 1 else self.DOUBLE_BOUNDS
        for bounds in schedule:
            print(f"reduce {target_name}: trying bounds {bounds}", flush=True)
            candidates, labels = self.candidates(target_parity, bounds, clearing_level)
            augmented, monomials = self.linear_system(candidates, target)
            rref, pivots = augmented.rref()
            inconsistent = bool(pivots and pivots[-1] == len(candidates))
            rank_augmented = len(pivots)
            rank_coefficient = rank_augmented - int(inconsistent)
            attempt = {
                "primitive_degree_bounds": {
                    "s=1/2": bounds[0],
                    "s=3/2": bounds[1],
                },
                "equations": len(monomials),
                "unknowns": len(candidates),
                "rank_coefficient": rank_coefficient,
                "rank_augmented": rank_augmented,
                "consistent": not inconsistent,
            }
            attempts.append(attempt)
            print(
                f"reduce {target_name}: rank {rank_coefficient}/{rank_augmented} "
                f"({'closed' if not inconsistent else 'obstructed'})",
                flush=True,
            )
            if inconsistent:
                continue

            rref_matrix = rref.to_Matrix()
            solution = [sp.Integer(0)] * len(candidates)
            for row, pivot in enumerate(pivots):
                if pivot < len(candidates):
                    # DomainMatrix.rref has already normalized this element in
                    # QQ(a1,lambda); a second generic ``cancel`` can dominate
                    # the entire runtime for the even-even block.
                    solution[pivot] = rref_matrix[row, -1]

            coefficients = [sp.Integer(0)] * len(self.masters)
            primitives = {
                "U_s=1/2": sp.Integer(0),
                "V_s=1/2": sp.Integer(0),
                "U_s=3/2": sp.Integer(0),
                "V_s=3/2": sp.Integer(0),
            }
            reconstructed = sp.Integer(0)
            for value, candidate, (label, monomial) in zip(
                solution, candidates, labels
            ):
                if value == 0:
                    continue
                reconstructed += value * candidate
                if label.startswith("basis:"):
                    coefficients[int(label.split(":", 1)[1])] += value
                else:
                    axis, tag = label.split(":", 1)
                    exponent = {
                        "half": "1/2",
                        "three_half": "3/2",
                    }[tag]
                    primitives[f"{axis}_s={exponent}"] += value * monomial
            residual = sp.Poly(
                sp.expand(target - reconstructed),
                self.a,
                self.b,
                domain=self.field,
            ).as_expr()
            if residual != 0:
                raise AssertionError("RREF solution failed its cleared polynomial identity")
            return Reduction(coefficients, primitives, attempts, residual)

        last = attempts[-1]
        raise RuntimeError(
            "bounded Griffiths--Dwork closure obstruction: "
            f"rank(A)={last['rank_coefficient']} < "
            f"rank([A|b])={last['rank_augmented']} at {schedule[-1]}"
        )


def build_geometry():
    a1, lam, c, aa, bb = sp.symbols("a1 lambda c a b")
    x = a1 * lam
    y = lam
    z = sp.Integer(1)
    E = x + y + z
    q = E + c
    cayley_menger = sp.Matrix(
        [
            [0, 1, 1, 1, 1],
            [1, 0, c**2, aa**2, bb**2],
            [1, c**2, 0, y**2, x**2],
            [1, aa**2, y**2, 0, z**2],
            [1, bb**2, x**2, z**2, 0],
        ]
    )
    K = sp.expand(cayley_menger.det())
    K0 = sp.expand(K.subs(c, -E))
    K1 = sp.expand(sp.diff(K, c).subs(c, -E))
    return a1, lam, c, aa, bb, x, y, z, E, q, K, K0, K1


def build_masters(aa: sp.Symbol, bb: sp.Symbol, K1: sp.Expr) -> list[Master]:
    specifications = [
        ("e1", aa * bb, "simple"),
        ("e2", aa, "simple"),
        ("e3", aa, "double"),
        ("e4", bb, "simple"),
        ("e5", bb, "double"),
        ("e6", sp.Integer(1), "double"),
        ("e7", sp.Integer(1), "simple"),
        ("e8", aa**2, "simple"),
        ("e9", bb**2, "simple"),
    ]
    masters: list[Master] = []
    for name, source_numerator, pole in specifications:
        numerator = (
            source_numerator
            if pole == "simple"
            else -sp.Rational(1, 2) * source_numerator * K1
        )
        poly = sp.Poly(source_numerator, aa, bb)
        monomial = poly.monoms()[0]
        masters.append(
            Master(
                name,
                source_numerator,
                pole,
                sp.expand(numerator),
                (monomial[0] % 2, monomial[1] % 2),
            )
        )
    return masters


def derivative_common_numerator(
    master: Master, K0: sp.Expr, K1: sp.Expr, lam: sp.Symbol
) -> tuple[int, sp.Expr]:
    K_lambda = sp.diff(K0, lam)
    if master.pole == "simple":
        # d(N/sqrt(K))/dlam = -.5 N K_lam/K^(3/2).
        return 1, sp.expand(-sp.Rational(1, 2) * master.source_numerator * K_lambda)
    D = -sp.Rational(1, 2) * master.source_numerator * K1
    # d(D/K^(3/2)) = D_lam/K^(3/2) - 3 D K_lam/(2 K^(5/2)).
    return 2, sp.expand(
        sp.diff(D, lam) * K0 - sp.Rational(3, 2) * D * K_lambda
    )


def exact_gysin_data(
    a1: sp.Symbol,
    lam: sp.Symbol,
    x: sp.Expr,
    y: sp.Expr,
    E: sp.Expr,
):
    R = sp.Matrix(
        [
            [
                0,
                1,
                (E**2 + y**2) / 2,
                (E**2 + x**2) / 2,
            ],
            [
                0,
                0,
                -(E**2 + x**2) / 2,
                -x**2 * (E**2 + y**2) / (2 * y**2),
            ],
        ]
    ).applyfunc(canonical)
    c7 = (x**2 - y**2) * (x**2 * y**2 - E**4)
    c8 = 2 * x**2 * (E**2 + y**2)
    c9 = -2 * y**2 * (E**2 + x**2)
    v = sp.Matrix([0, c7, c8, c9]).applyfunc(canonical)
    kernel_basis = sp.Matrix.hstack(sp.Matrix([1, 0, 0, 0]), v)
    assert (R * kernel_basis).applyfunc(canonical) == sp.zeros(2, 2)
    assert R.rank() == 2
    assert kernel_basis.rank() == 2
    # The displayed vectors span the generic kernel because both dimensions are two.
    return R, v, kernel_basis


def induced_plane_connection(
    final_block: sp.Matrix,
    kernel_basis: sp.Matrix,
    lam: sp.Symbol,
) -> tuple[bool, sp.Matrix, sp.Matrix]:
    differentiated = (final_block * kernel_basis + kernel_basis.diff(lam)).applyfunc(
        canonical
    )
    induced = sp.zeros(2, 2)
    residual = sp.zeros(4, 2)
    # B=(e6,v_alg), and the e8 coefficient of v_alg is generically nonzero.
    pivot = canonical(kernel_basis[2, 1])
    for column in range(2):
        beta = canonical(differentiated[2, column] / pivot)
        alpha = canonical(differentiated[0, column])
        induced[:, column] = sp.Matrix([alpha, beta])
        residual[:, column] = (differentiated[:, column] - kernel_basis * induced[:, column]).applyfunc(
            canonical
        )
    invariant = residual == sp.zeros(4, 2)
    return invariant, induced.applyfunc(canonical), residual


def polynomial_valuation(poly: sp.Poly, divisor: sp.Poly) -> tuple[int, sp.Poly]:
    valuation = 0
    quotient = poly
    while quotient.rem(divisor).is_zero:
        quotient = quotient.exquo(divisor)
        valuation += 1
    return valuation, quotient


def residue_mod_irreducible(
    coefficient: sp.Expr, variable: sp.Symbol, divisor_expr: sp.Expr
) -> dict[str, object]:
    coefficient = sp.cancel(coefficient)
    if coefficient == 0:
        return {"pole_order": 0, "residue_mod_Q": "0"}
    numerator_expr, denominator_expr = sp.fraction(coefficient)
    divisor = sp.Poly(divisor_expr, variable, domain=sp.QQ)
    numerator = sp.Poly(numerator_expr, variable, domain=sp.QQ)
    denominator = sp.Poly(denominator_expr, variable, domain=sp.QQ)
    numerator_order, numerator_unit = polynomial_valuation(numerator, divisor)
    denominator_order, denominator_unit = polynomial_valuation(denominator, divisor)
    pole_order = denominator_order - numerator_order
    if pole_order <= 0:
        return {"pole_order": 0, "residue_mod_Q": "0"}
    if pole_order != 1:
        return {"pole_order": pole_order, "residue_mod_Q": None}
    modulus = divisor
    derivative = sp.Poly(sp.diff(divisor.as_expr(), variable), variable, domain=sp.QQ)
    denominator_inverse = sp.invert(denominator_unit, modulus)
    derivative_inverse = sp.invert(derivative, modulus)
    residue = (numerator_unit * denominator_inverse * derivative_inverse).rem(modulus)
    return {
        "pole_order": 1,
        "residue_mod_Q": expression_string(residue.as_expr()),
    }


def common_denominator(expressions: Iterable[sp.Expr]) -> sp.Expr:
    answer = sp.Integer(1)
    for expression in expressions:
        answer = sp.lcm(answer, sp.fraction(sp.cancel(expression))[1])
    return sp.factor(answer)



def derive_bivariate():
    u,v,c,aa,bb=sp.symbols("u v c a b")
    x=sp.Integer(1)
    y=(u+v)/2-x
    z=(u-v)/2
    E=sp.factor(x+y+z)
    assert E==u and sp.factor(x+y-z)==v
    CM=sp.Matrix([
      [0,1,1,1,1],
      [1,0,c**2,aa**2,bb**2],
      [1,c**2,0,y**2,x**2],
      [1,aa**2,y**2,0,z**2],
      [1,bb**2,x**2,z**2,0]])
    Kfull=sp.expand(CM.det())
    K0=sp.expand(Kfull.subs(c,-E))
    K1=sp.expand(sp.diff(Kfull,c).subs(c,-E))
    field=sp.QQ.frac_field(u,v)
    masters=build_masters(aa,bb,K1)
    reducer=ExactReducer(aa,bb,field,K0,masters)

    connections={}
    certificates={}
    for parameter in (u,v):
        A=sp.zeros(9,9)
        rows=[]
        for column,master in enumerate(masters):
            clearing,target=derivative_common_numerator(master,K0,K1,parameter)
            red=reducer.solve(target,master.parity,f"{master.name}/{parameter}",clearing)
            A[:,column]=sp.Matrix(red.coefficients)
            reconstructed=sum(A[row,column]*reducer.basis_common[clearing][row]
                              for row in range(9))
            for exponent,label in ((sp.Rational(1,2),"1/2"),
                                   (sp.Rational(3,2),"3/2")):
                for axis in ("U","V"):
                    primitive=red.primitives[f"{axis}_s={label}"]
                    if primitive!=0:
                        reconstructed+=reducer.exact_column(
                            primitive,axis,exponent,clearing)
            assert sp.Poly(sp.expand(target-reconstructed),aa,bb,domain=field).is_zero
            rows.append({"master":master.name,"attempts":red.attempts,
                         "cleared_identity":True})
        connections[str(parameter)]=A
        certificates[str(parameter)]=rows

    Au,Av=connections["u"],connections["v"]
    curvature=(Av.applyfunc(lambda q:sp.diff(q,u))
               -Au.applyfunc(lambda q:sp.diff(q,v))+Au*Av-Av*Au)
    curvature=curvature.applyfunc(canonical)
    assert curvature==sp.zeros(9)

    R,valg,kernel_basis=exact_gysin_data(u,v,x,y,E)
    C=R.T
    final_idx=[5,6,7,8]
    directions={}
    for name,param,A in (("u",u,Au),("v",v,Av)):
        A4=A.extract(final_idx,final_idx)
        invariant,Aalg,residual=induced_plane_connection(A4,kernel_basis,param)
        assert invariant and residual==sp.zeros(4,2)
        rhs=A4*C-C.diff(param)
        minor=C.extract([1,2],[0,1])
        Bell=(minor.inv()*rhs.extract([1,2],[0,1])).applyfunc(canonical)
        gysin_residual=(C.diff(param)+C*Bell-A4*C).applyfunc(canonical)
        directions[name]={"A4":A4,"Aalg":Aalg,"Bell":Bell,
                          "gysin_residual":gysin_residual}

    def residue(A,param):
        Rm=sp.zeros(A.rows,A.cols); higher=[]
        for i in range(A.rows):
            for j in range(A.cols):
                q=canonical(A[i,j])
                if q==0: continue
                second=sp.factor(sp.limit(param**2*q,param,0))
                if second!=0: higher.append([i+1,j+1,expression_string(second)])
                Rm[i,j]=sp.factor(sp.limit(param*q,param,0))
        return Rm,higher

    Ru,hu=residue(Au,u); Rv,hv=residue(Av,v)
    assert not hu and not hv
    Rue,_=residue(directions["u"]["Bell"],u)
    Rve,_=residue(directions["v"]["Bell"],v)
    Rua,_=residue(directions["u"]["Aalg"],u)
    Rva,_=residue(directions["v"]["Aalg"],v)

    def corner_limit(M,param):
        out=sp.zeros(M.rows,M.cols); finite=True
        for i in range(M.rows):
            for j in range(M.cols):
                q=sp.factor(sp.limit(M[i,j],param,0))
                if q.has(sp.oo,sp.zoo,sp.nan) or q in (sp.oo,-sp.oo,sp.zoo):
                    finite=False
                out[i,j]=q
        return finite,out
    fu,Ruc=corner_limit(Ru,v)
    fv,Rvc=corner_limit(Rv,u)

    def strings(M):
        return matrix_strings(M)

    result={
      "schema":"marici.benincasa.bivariate_soft_gram_connection.v2",
      "status":"pass",
      "coordinates":{"X1":"1","X2":"(u+v)/2-1","X3":"(u-v)/2",
                     "E":"u","ell3":"v","B":"u*v"},
      "basis_order":[m.name for m in masters],
      "connection_u":strings(Au),"connection_v":strings(Av),
      "certificates":certificates,
      "flatness":{"curvature_zero":True},
      "gysin_horizontality":{
        "u_residual":strings(directions["u"]["gysin_residual"]),
        "v_residual":strings(directions["v"]["gysin_residual"]),
        "u_zero":directions["u"]["gysin_residual"]==sp.zeros(4,2),
        "v_zero":directions["v"]["gysin_residual"]==sp.zeros(4,2)
      },
      "residues":{"Ru":strings(Ru),"Rv":strings(Rv),
                  "Ru_algebraic":strings(Rua),"Rv_algebraic":strings(Rva),
                  "Ru_elliptic":strings(Rue),"Rv_elliptic":strings(Rve),
                  "higher_u":[],"higher_v":[]},
      "corner_limits":{"Ru_at_v0":{"finite":fu,"matrix":strings(Ruc)},
                       "Rv_at_u0":{"finite":fv,"matrix":strings(Rvc)}},
      "interpretive_boundary":[
        "Exact QQ(u,v) de Rham connection for the frozen q_G12 nine-master module.",
        "Nonfinite raw corner residues require predeclared logarithmic blowup/gauge reduction.",
        "No integral or physical-chain compatibility is inferred."
      ]
    }
    out=Path(__file__).with_name("bivariate_soft_gram_connection.json")
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"status":"ok","output":str(out),
                      "Ru_corner_finite":fu,"Rv_corner_finite":fv},indent=2))
    return result

if __name__=="__main__":
    derive_bivariate()
