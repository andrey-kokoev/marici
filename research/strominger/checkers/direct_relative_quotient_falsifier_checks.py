import json
from pathlib import Path


def values(p, functional):
    return {
        functional(x, y) % p
        for x in range(p)
        for y in range(p)
    }


records = []
gates = []
for p in (3, 5, 7, 11, 13, 17, 19):
    # ell(x,y)=x+s*y is transverse unless s is 1 or -1.
    slopes = [s for s in range(p) if s not in (1, p - 1)]
    for s in slopes:
        def ell(x, y, s=s, p=p):
            return (x + s * y) % p

        def ell_x(x, y, s=s, p=p):
            return (y + s * x) % p

        def q_plus(x, y, s=s, p=p):
            return (ell(x, y) + ell_x(x, y)) % p

        def q_minus(x, y, s=s, p=p):
            return (ell(x, y) - ell_x(x, y)) % p

        odd_values = values(p, q_minus)
        even_values = values(p, q_plus)
        joint_values = {
            (q_plus(x, y), q_minus(x, y))
            for x in range(p) for y in range(p)
        }
        odd_covariant = all(
            q_minus(y, x) == (-q_minus(x, y)) % p
            for x in range(p) for y in range(p)
        )
        even_invariant = all(
            q_plus(y, x) == q_plus(x, y)
            for x in range(p) for y in range(p)
        )
        inverse_two = pow(2, -1, p)
        reconstructs = all(
            ((q_plus(x, y) + q_minus(x, y)) * inverse_two) % p == ell(x, y)
            and ((q_plus(x, y) - q_minus(x, y)) * inverse_two) % p == ell_x(x, y)
            for x in range(p) for y in range(p)
        )
        passed = (
            len(odd_values) == p
            and len(even_values) == p
            and len(joint_values) == p * p
            and odd_covariant
            and even_invariant
            and reconstructs
        )
        gates.append(passed)
        records.append({
            "prime": p,
            "slope": s,
            "odd_port_order": len(odd_values),
            "even_port_order": len(even_values),
            "joint_port_order": len(joint_values),
            "odd_covariant": odd_covariant,
            "even_invariant": even_invariant,
            "joint_reconstructs_charts": reconstructs,
            "passed": passed,
        })

# Exact magnetic functional ell=3*x-2*y modulo seven.
p = 7


def magnetic_ell(x, y):
    return (3 * x - 2 * y) % p


def magnetic_ell_x(x, y):
    return (3 * y - 2 * x) % p


def magnetic_q_plus(x, y):
    return (magnetic_ell(x, y) + magnetic_ell_x(x, y)) % p


def magnetic_q_minus(x, y):
    return (magnetic_ell(x, y) - magnetic_ell_x(x, y)) % p


magnetic = {
    "odd_formula_matches_5_times_difference": all(
        magnetic_q_minus(x, y) == 5 * (x - y) % p
        for x in range(p) for y in range(p)
    ),
    "even_formula_matches_sum": all(
        magnetic_q_plus(x, y) == (x + y) % p
        for x in range(p) for y in range(p)
    ),
    "odd_port_order": len(values(p, magnetic_q_minus)),
    "even_port_order": len(values(p, magnetic_q_plus)),
    "joint_port_order": len({
        (magnetic_q_plus(x, y), magnetic_q_minus(x, y))
        for x in range(p) for y in range(p)
    }),
}
magnetic_gate = (
    magnetic["odd_formula_matches_5_times_difference"]
    and magnetic["even_formula_matches_sum"]
    and magnetic["odd_port_order"] == 7
    and magnetic["even_port_order"] == 7
    and magnetic["joint_port_order"] == 49
)
gates.append(magnetic_gate)

result = {
    "schema": "marici.strominger.direct_relative_quotient_falsifier.v1",
    "hostile_records": records,
    "magnetic": magnetic,
    "strong_prediction_falsified": True,
    "falsified_claim": "transversality forces every adequate carrier to have p^2 classes",
    "surviving_claim": "p^2 is minimal for joint chart faithfulness; p is sufficient for one selected parity relation",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = Path(__file__).parents[1] / "results" / "direct_relative_quotient_falsifier_checks.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps({
    "schema": result["schema"],
    "hostile_cases": len(records),
    "magnetic": magnetic,
    "strong_prediction_falsified": result["strong_prediction_falsified"],
    "surviving_claim": result["surviving_claim"],
    "gates_passed": result["gates_passed"],
    "gates_total": result["gates_total"],
    "all_passed": result["all_passed"],
}, indent=2))
raise SystemExit(0 if all(gates) else 1)
