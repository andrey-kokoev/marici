import importlib.util
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
BASE_PATH = Path(__file__).with_name("rank12_u0_v2_exact_primitive_witness.py")
RESULT = ROOT / "research/benincasa/results/rank12-u0-v2-exceptional-overlap-homotopy.json"

spec = importlib.util.spec_from_file_location("p_chart_checker", BASE_PATH)
pchart = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pchart)
s, a, b = pchart.s, pchart.a, pchart.b


def q_geometry():
    k = (
        a**4
        + 2 * (s - 1) * a**2 * b
        + (-s - sp.Rational(5, 2) * s**2 - sp.Rational(1, 2)) * a**2
        + (s + 1) ** 2 * b**2
        + (sp.Rational(1, 2) + s / 2 + 3 * s**2 / 2 - 5 * s**3 / 2) * b
        + s / 4 + 7 * s**2 / 8 - 11 * s**3 / 4 + 25 * s**4 / 16 + sp.Rational(1, 16)
    )
    k1 = 4 * s * a**2 + 4 * s * (s - 1) * b + s * (-1 + 6 * s - 5 * s**2)
    return k, k1, b - s, a + (1 - s) / 2


def q_classes(k1):
    return [
        (1, 1, 1, sp.Integer(1)),
        (1, 0, 1, sp.Integer(1)),
        (0, 1, 1, sp.Integer(1)),
        (0, 0, 1, a * b),
        (0, 0, 1, a),
        (0, 0, 3, -a * k1 / 2),
        (0, 0, 1, b),
        (0, 0, 3, -b * k1 / 2),
        (0, 0, 3, -k1 / 2),
        (0, 0, 1, sp.Integer(1)),
        (0, 0, 1, a**2),
        (0, 0, 1, b**2),
    ]


def q_common_and_target(cls, k, l1, l2):
    aa, bb, h, numerator = cls
    ea, eb, ek = 2 - aa, 2 - bb, (5 - h) // 2
    common = numerator * l1**ea * l2**eb * k**ek
    target = sp.diff(numerator, s) * l1**ea * l2**eb * k**ek
    if aa:
        target -= numerator * l1 ** (ea - 1) * l2**eb * k**ek * sp.diff(l1, s) * aa
    if bb:
        target -= numerator * l1**ea * l2 ** (eb - 1) * k**ek * sp.diff(l2, s) * bb
    target -= numerator * l1**ea * l2**eb * sp.diff(k, s) * k ** (ek - 1) * sp.Rational(h, 2)
    return sp.expand(common), sp.expand(target)


def solve_exact(defect, degree):
    columns = []
    labels = []
    for sa, sb in [(1, 1), (1, 0), (0, 1), (0, 0)]:
        for exponent in pchart.monomials(degree):
            for is_q in (False, True):
                columns.append(pchart.exact(sa, sb, exponent, is_q))
                labels.append((sa, sb, exponent, is_q))

    dictionaries = [sp.Poly(column, a, b, domain=sp.QQ.frac_field(s)).as_dict() for column in columns]
    rhs_dictionary = sp.Poly(defect, a, b, domain=sp.QQ.frac_field(s)).as_dict()
    monomials = sorted(set(rhs_dictionary).union(*(dictionary.keys() for dictionary in dictionaries)))
    equations = []
    unknowns = sp.symbols(f"x0:{len(columns)}")
    for monomial in monomials:
        equations.append(sum(dictionary.get(monomial, 0) * unknown
                             for dictionary, unknown in zip(dictionaries, unknowns))
                         - rhs_dictionary.get(monomial, 0))
    solution_set = sp.linsolve(equations, unknowns)
    if solution_set is sp.EmptySet:
        return None, len(monomials), len(columns)
    solution = next(iter(solution_set))
    free = set().union(*(value.free_symbols for value in solution)) - {s}
    specialized = tuple(sp.factor(value.subs({symbol: 0 for symbol in free})) for value in solution)
    residual = sp.Poly(
        sp.together(sum(value * column for value, column in zip(specialized, columns)) - defect),
        a, b,
        domain=sp.QQ.frac_field(s),
    )
    if not residual.is_zero:
        raise AssertionError("reported overlap homotopy has nonzero residual")
    nonzero = [
        {"label": [sa, sb, list(exponent), "q" if is_q else "p"], "coefficient": str(value)}
        for (sa, sb, exponent, is_q), value in zip(labels, specialized) if value != 0
    ]
    return {"free_parameter_count": len(free), "nonzero_terms": nonzero}, len(monomials), len(columns)


def main():
    p_classes, _ = pchart.source_columns()
    kq, k1q, l1q, l2q = q_geometry()
    qcls = q_classes(k1q)
    substitution = {s: 1 / s, a: a / s, b: b / s}
    basis = [(0, 2, "Omega111"), (1, 1, "Omega101"),
             (2, 1, "Omega110"), (6, -1, "e4")]
    generators = []
    for class_index, weight, label in basis:
        cp = pchart.common(p_classes[class_index])
        tp = pchart.target(p_classes[class_index])
        _, tq = q_common_and_target(qcls[class_index], kq, l1q, l2q)
        transported_tq = sp.cancel(s**12 * tq.subs(substitution, simultaneous=True))
        defect = sp.factor(transported_tq + weight * s ** (weight + 1) * cp
                           + s ** (weight + 2) * tp)

        solution = None
        census = []
        for degree in range(9):
            candidate, equations, columns = solve_exact(defect, degree)
            census.append({"degree": degree, "equations": equations, "columns": columns,
                           "membership": candidate is not None})
            if candidate is not None:
                solution = {"degree": degree, **candidate}
                break
        generators.append({
            "class_index": class_index,
            "label": label,
            "frame_weight": weight,
            "defect_zero_before_exact_reduction":
                sp.Poly(defect, a, b, domain=sp.QQ.frac_field(s)).is_zero,
            "degree_census": census,
            "exact_homotopy": solution,
        })

    result = {
        "schema": "marici.benincasa.rank12_u0_v2_exceptional_overlap_homotopy.v2",
        "status": "passed" if all(item["exact_homotopy"] is not None for item in generators) else "failed",
        "transport": "T(Pq)=s^12 Pq(1/s,a/s,b/s)",
        "defect_formula": "T(Tq)+w*s^(w+1)*Cp+s^(w+2)*Tp",
        "generators": generators,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "schema": result["schema"],
        "status": result["status"],
        "generators": [{
            "label": item["label"],
            "weight": item["frame_weight"],
            "raw_zero": item["defect_zero_before_exact_reduction"],
            "first_exact_degree": item["exact_homotopy"]["degree"] if item["exact_homotopy"] else None,
            "nonzero_terms": len(item["exact_homotopy"]["nonzero_terms"]) if item["exact_homotopy"] else None,
        } for item in generators],
    }))
    if result["status"] != "passed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
