"""Branch-puncture specialization census on the generic q_G12 residue."""

import json
from pathlib import Path

import sympy as sp


c, a, b = sp.symbols("c a b")
X1, X2, X3 = sp.symbols("X1 X2 X3")
S1, S2, S3 = sp.symbols("S1 S2 S3")
nu1, nu2, nu3 = sp.symbols("nu1 nu2 nu3")
CM = sp.Matrix([
    [0, 1, 1, 1, 1],
    [1, 0, c**2, a**2, b**2],
    [1, c**2, 0, S2, S1],
    [1, a**2, S2, 0, S3],
    [1, b**2, S1, S3, 0],
])
K = sp.expand(-CM.det() / 2)
E = X1 + X2 + X3
K_G = sp.expand(K.subs(c, -E))
lines = {
    "L1": (b, X2 + X3, a),
    "L2": (a, X1 + X3, b),
    "L3": (a, -X3 - b, b),
    "L23": (b, X1, a),
}
hom = {S1: X1**2, S2: X2**2, S3: X3**2}
samples = [
    {X1: 2, X2: 3, X3: 4},
    {X1: 3, X2: 5, X3: 6},
]

records = {}
for name, (solved, value, residual) in lines.items():
    restricted_generic = sp.expand(K_G.subs(solved, value))
    restricted = sp.expand(restricted_generic.subs(hom))
    symbolic_poly = sp.Poly(restricted, residual)
    sample_records = []
    squarefree_degrees = set()
    for sample in samples:
        poly = sp.Poly(restricted.subs(sample), residual)
        gcd = sp.gcd(poly, poly.diff())
        sf_degree = poly.degree() - gcd.degree()
        squarefree_degrees.add(sf_degree)
        generic_sample = restricted_generic.subs(sample).subs(
            {S1: sample[X1]**2 + nu1, S2: sample[X2]**2 + nu2, S3: sample[X3]**2 + nu3}
        )
        disc_normal = sp.Poly(
            sp.expand(sp.discriminant(generic_sample, residual)), nu1, nu2, nu3
        )
        normal_terms = [
            (sum(mon), mon, coeff) for mon, coeff in disc_normal.terms() if coeff != 0
        ]
        minimum_normal_order = min(order for order, _, _ in normal_terms)
        leading_monomials = [
            list(mon) for order, mon, _ in normal_terms if order == minimum_normal_order
        ]
        sample_records.append({
            "sample": {str(k): v for k, v in sample.items()},
            "degree": poly.degree(),
            "gcd_degree": gcd.degree(),
            "squarefree_degree": sf_degree,
            "discriminant_minimum_normal_order": minimum_normal_order,
            "discriminant_leading_monomials": leading_monomials,
        })
    records[name] = {
        "symbolic_factorization": str(sp.factor(symbolic_poly.as_expr())),
        "samples": sample_records,
    }
    records[name]["observed_squarefree_degrees"] = sorted(squarefree_degrees)

generic_sf = {name: 4 for name in lines}
homogeneous_sf = {
    name: records[name]["observed_squarefree_degrees"][0] for name in lines
}
losses = {name: generic_sf[name] - homogeneous_sf[name] for name in lines}
assert losses == {"L1": 2, "L2": 2, "L3": 2, "L23": 0}
assert sum(losses.values()) == 6
expected_leading = {
    "L1": [2, 0, 0],
    "L2": [0, 2, 0],
    "L3": [0, 0, 2],
    "L23": [0, 0, 0],
}
for name, expected in expected_leading.items():
    for sample_record in records[name]["samples"]:
        assert sample_record["discriminant_leading_monomials"] == [expected]

result = {
    "schema": "marici.residue-branch-specialization-defect.v1",
    "line_records": records,
    "generic_squarefree_degrees": generic_sf,
    "homogeneous_squarefree_degrees": homogeneous_sf,
    "puncture_losses": losses,
    "total_residue_rank_loss": sum(losses.values()),
    "five_pole_rank_loss_decomposition": {"lower_deletion": 19, "q_G12_restriction": 6},
    "normal_label_assignment": expected_leading,
    "square_free_N2_intersection": 0,
}

out = Path(__file__).with_name("residue-branch-specialization-defect.json")
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
