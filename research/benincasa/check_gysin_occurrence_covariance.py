"""Occurrence covariance audit for the Gysin extension cocycle of Entry 757."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research/nima"))
import check_gysin_multidivisor_extension as source  # noqa: E402

DEFAULT_INPUT = ROOT / "research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json"
DEFAULT_OUTPUT = ROOT / "research/benincasa/gysin-occurrence-covariance-d10.json"


def transported_connection(entries, axis, u, v, prime):
    """Target G31 connection in (u',v') with u=u', v_source=2-v'."""
    source_v = (2 - v) % prime
    source_axis = "u" if axis == "u" else "v"
    matrix = source.connection(entries, source_axis, u, source_v, prime)
    if matrix is None:
        return None
    if axis == "v":
        matrix = [[(-value) % prime for value in row] for row in matrix]
    # Entry 756 contributes the constant frame gauge -I_4.  Its conjugation
    # is trivial, but retaining it here documents that orientation was used.
    orientation = prime - 1
    return [
        [orientation * value * orientation % prime for value in row]
        for row in matrix
    ]


def transported_factors(u, v, prime):
    """Pull D_src through (u',v')->(u,2-v_source), including derivatives."""
    data = source.factors_and_derivatives(u, (2 - v) % prime, prime)
    if data is None:
        return None
    divisor, dlog_u, dlog_source_v = data
    return divisor, dlog_u, (-dlog_source_v) % prime


def covariance_census(entries, prime, pole, degree, seed):
    mons = source.monomials(degree)
    unknowns = 4 * len(mons)
    target_rows = unknowns + 32
    matrix = []
    state_u = seed ^ (pole << 17) ^ degree
    state_v = seed ^ 0x9E3779B97F4A7C15 ^ (degree << 23)
    accepted = 0
    while len(matrix) < target_rows:
        state_u = (state_u * 6364136223846793005 + 1447) % prime
        state_v = (state_v * 2862933555777941757 + 1451) % prime
        u, v = state_u, state_v
        factor_data = transported_factors(u, v, prime)
        if factor_data is None:
            continue
        divisor, dlog_u, dlog_v = factor_data
        au = transported_connection(entries, "u", u, v, prime)
        av = transported_connection(entries, "v", u, v, prime)
        if au is None or av is None:
            continue
        accepted += 1
        for axis, a, dlog in [(0, au, dlog_u), (1, av, dlog_v)]:
            divisor_power = pow(divisor, pole, prime)
            for i in range(2):
                for j in range(2):
                    row = [0] * (unknowns + 1)
                    for q in range(2):
                        for k in range(2):
                            block = (2 * q + k) * len(mons)
                            for index, (du, dv) in enumerate(mons):
                                value = pow(u, du, prime) * pow(v, dv, prime) % prime
                                exponent = du if axis == 0 else dv
                                derivative = 0
                                if exponent:
                                    derivative = exponent * (
                                        pow(u, du - 1, prime) * pow(v, dv, prime)
                                        if axis == 0
                                        else pow(u, du, prime) * pow(v, dv - 1, prime)
                                    ) % prime
                                coefficient = 0
                                if q == i and k == j:
                                    coefficient += derivative - pole * dlog * value
                                if q == i:
                                    coefficient += value * a[k][j]
                                if k == j:
                                    coefficient -= value * a[i + 2][q + 2]
                                row[block + index] = coefficient % prime
                    row[-1] = (-divisor_power * a[i + 2][j]) % prime
                    matrix.append(row)
    coefficient_rank = source.rank([row[:-1] for row in matrix], unknowns, prime)
    augmented_rank = source.rank(matrix, unknowns + 1, prime)
    return {
        "pole_bound": pole,
        "numerator_degree": degree,
        "unknowns": unknowns,
        "sample_points": accepted,
        "equations": len(matrix),
        "coefficient_rank": coefficient_rank,
        "augmented_rank": augmented_rank,
        "augmented_rank_defect": augmented_rank - coefficient_rank,
    }


def poly_from_terms(terms, prime):
    return {(int(du), int(dv)): int(c) % prime for du, dv, c in terms if int(c) % prime}


def clean_poly(poly, prime):
    return {exponent: coefficient % prime for exponent, coefficient in poly.items() if coefficient % prime}


def poly_divmod(dividend, divisor, prime):
    """Sparse lexicographic division by one polynomial over GF(prime)."""
    work = dict(dividend)
    quotient = {}
    remainder = {}
    lead_d = max(divisor)
    coeff_d = divisor[lead_d]
    inv_d = pow(coeff_d, prime - 2, prime)
    while work:
        lead = max(work)
        coeff = work[lead]
        if lead[0] >= lead_d[0] and lead[1] >= lead_d[1]:
            exponent = (lead[0] - lead_d[0], lead[1] - lead_d[1])
            scale = coeff * inv_d % prime
            quotient[exponent] = (quotient.get(exponent, 0) + scale) % prime
            for term, value in divisor.items():
                target = (term[0] + exponent[0], term[1] + exponent[1])
                next_value = (work.get(target, 0) - scale * value) % prime
                if next_value:
                    work[target] = next_value
                else:
                    work.pop(target, None)
        else:
            remainder[lead] = coeff
            work.pop(lead)
    return {e: c for e, c in quotient.items() if c}, remainder


def valuation(poly, factor, prime):
    if not poly:
        return 10**9, {}
    value = 0
    residual = dict(poly)
    while True:
        quotient, remainder = poly_divmod(residual, factor, prime)
        if remainder:
            return value, residual
        residual = quotient
        value += 1


def reduced_denominator_valuations(payload):
    prime = int(payload["prime"])
    half = pow(2, prime - 2, prime)
    quarter = pow(4, prime - 2, prime)
    y = {(1, 0): half, (0, 1): half, (0, 0): prime - 1}
    def linear_combination(*polys):
        result = {}
        for scale, poly in polys:
            for exponent, coefficient in poly.items():
                value = (result.get(exponent, 0) + scale * coefficient) % prime
                if value:
                    result[exponent] = value
                else:
                    result.pop(exponent, None)
        return result
    one = {(0, 0): 1}
    factors = [
        ("u", {(1, 0): 1}),
        ("v", {(0, 1): 1}),
        ("y", y),
        ("1-y", linear_combination((1, one), (-1, y))),
        ("1+y", linear_combination((1, one), (1, y))),
        ("v-u", {(0, 1): 1, (1, 0): prime - 1}),
        ("y-u^2", linear_combination((1, y), (-1, {(2, 0): 1}))),
        ("y+u^2", linear_combination((1, y), (1, {(2, 0): 1}))),
        ("P6", clean_poly({
            (0, 0): 1, (1, 0): -1, (0, 1): -1, (0, 2): quarter,
            (1, 1): half, (2, 0): -7 * quarter, (2, 1): 1,
            (3, 0): 1, (3, 1): -1, (4, 0): 1,
        }, prime)),
    ]
    maxima = {name: 0 for name, _ in factors}
    per_entry = []
    for item in payload["entries"]:
        if item["row"] < 2 or item["col"] >= 2:
            continue
        numerator = poly_from_terms(item["fit"]["numerator"], prime)
        denominator = poly_from_terms(item["fit"]["denominator"], prime)
        vals = {}
        remainder = dict(denominator)
        for name, factor in factors:
            denominator_valuation, denominator_residual = valuation(remainder, factor, prime)
            numerator_valuation, _ = valuation(numerator, factor, prime)
            net = max(denominator_valuation - numerator_valuation, 0)
            vals[name] = net
            maxima[name] = max(maxima[name], net)
            remainder = denominator_residual
        per_entry.append({
            "axis": item["axis"], "row": item["row"], "col": item["col"],
            "valuations": vals,
            "residual_term_count": len(remainder),
            "residual_is_unit": not remainder or all(e == (0, 0) for e in remainder),
        })
    reflected_labels = {
        "u": "u'",
        "v": "2-v'",
        "y": "y'=(u'-v')/2",
        "1-y": "1-y'",
        "1+y": "1+y'",
        "v-u": "2-v'-u'",
        "y-u^2": "y'-u'^2",
        "y+u^2": "y'+u'^2",
        "P6": "P6(u',2-v')",
    }
    return {
        "source_order": list(maxima),
        "source_max_pole_vector": [maxima[name] for name in maxima],
        "source_max_poles": maxima,
        "target_pullback_labels": reflected_labels,
        "target_max_pole_vector": [maxima[name] for name in maxima],
        "all_residual_denominators_units": all(e["residual_is_unit"] for e in per_entry),
        "entries": per_entry,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-degree", type=int, default=10)
    parser.add_argument("--max-pole", type=int, default=2)
    parser.add_argument("--seed", type=lambda x: int(x, 0), default=0x243F6A8885A308D3)
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    prime = int(payload["prime"])
    entries = {(i["axis"], i["row"], i["col"]): i["fit"] for i in payload["entries"]}
    source_census_path = ROOT / "research/nima/gysin-multidivisor-extension-census-d10.json"
    source_census = json.loads(source_census_path.read_text(encoding="utf-8"))
    source_results = {
        (r["pole_bound"], r["numerator_degree"]): r for r in source_census["results"]
    }

    target_results = []
    mismatches = []
    for pole in range(args.max_pole + 1):
        for degree in range(args.max_degree + 1):
            result = covariance_census(entries, prime, pole, degree, args.seed)
            target_results.append(result)
            original = source_results[(pole, degree)]
            signature = (
                result["coefficient_rank"], result["augmented_rank"],
                result["augmented_rank_defect"],
            )
            original_signature = (
                original["coefficient_rank"], original["augmented_rank"],
                original["augmented_rank_defect"],
            )
            if signature != original_signature:
                mismatches.append({"pole": pole, "degree": degree,
                                   "source": original_signature, "target": signature})

    pole_data = reduced_denominator_valuations(payload)
    output = {
        "schema": "marici.gysin-extension-occurrence-covariance.v1",
        "prime": prime,
        "source_chart": "G12",
        "target_chart": "G31",
        "base_map": {"u_target": "u_source", "v_target": "2-v_source"},
        "frame_map": {
            "matrix": "-I4",
            "origin": "Entry 756 Poincare-residue orientation",
            "connection_conjugation": "(-I4) A (-I4)^-1 = A",
            "one_form_transport": "du_source=du_target; dv_source=-dv_target",
        },
        "hom_differential_transport": (
            "A_T,E^G31_u(u',v')=A_T,E^G12_u(u',2-v'); "
            "A_T,E^G31_v(u',v')=-A_T,E^G12_v(u',2-v')"
        ),
        "cocycle_transport": (
            "C^G31_u(u',v')=C^G12_u(u',2-v'); "
            "C^G31_v(u',v')=-C^G12_v(u',2-v')"
        ),
        "uniform_census": {
            "case_count": len(target_results),
            "mismatch_count": len(mismatches),
            "mismatches": mismatches,
            "all_defects_one": all(r["augmented_rank_defect"] == 1 for r in target_results),
            "results": target_results,
        },
        "source_induced_pole_transport": {
            "source_divisor_order": [
                "u", "v", "y", "1-y", "1+y", "v-u",
                "y-u^2", "y+u^2", "P6",
            ],
            "target_pullback_order": [
                "u'", "2-v'", "(u'-v')/2", "1-(u'-v')/2",
                "1+(u'-v')/2", "2-v'-u'",
                "(u'-v')/2-u'^2", "(u'-v')/2+u'^2",
                "P6(u',2-v')",
            ],
            "exponent_lattice_matrix": "I9",
            "uniform_entry_757_vector": [1] * 9,
            "extra_jacobian_poles": [0] * 9,
            "minimal_nonuniform_vector_determined_by_transition": False,
            "reason": (
                "the affine chart isomorphism permutes source divisors with unit "
                "Jacobian and transports every exponent vector; it does not select one"
            ),
        },
        "serialized_fit_pole_diagnostic_not_source_induced": pole_data,
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "case_count": len(target_results),
        "mismatch_count": len(mismatches),
        "all_defects_one": output["uniform_census"]["all_defects_one"],
        "fit_diagnostic_max_pole_vector": pole_data["source_max_pole_vector"],
        "fit_diagnostic_residual_units": pole_data["all_residual_denominators_units"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
