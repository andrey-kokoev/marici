"""Radial infinity indicial audit for the complete Gysin Hom pole vector."""

from __future__ import annotations

import json
from pathlib import Path

from audit_gysin_hom_pole_lattice import source_factors
from check_gysin_multidivisor_extension import ROOT, inv


INPUT = ROOT / "research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json"
OUTPUT = ROOT / "research/nima/gysin-infinity-indicial-audit.json"
COMPLETE_VECTOR = (1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 2)


def polynomial(terms, prime):
    return {(int(a), int(b)): int(c) % prime for a, b, c in terms if int(c) % prime}


def add(left, right, prime):
    result = dict(left)
    for exponent, coefficient in right.items():
        result[exponent] = (result.get(exponent, 0) + coefficient) % prime
        if result[exponent] == 0:
            result.pop(exponent)
    return result


def multiply(left, right, prime):
    result = {}
    for (a, b), c in left.items():
        for (d, e), f in right.items():
            exponent = (a + d, b + e)
            result[exponent] = (result.get(exponent, 0) + c * f) % prime
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def monomial_times(poly, exponent):
    return {(a + exponent[0], b + exponent[1]): c for (a, b), c in poly.items()}


def leading(poly, slope, prime):
    if not poly:
        return 0, -10**9
    degree = max(a + b for a, b in poly)
    value = sum(
        coefficient * pow(slope, b, prime)
        for (a, b), coefficient in poly.items()
        if a + b == degree
    ) % prime
    return value, degree


def radial_fraction(u_fit, v_fit, prime):
    nu = polynomial(u_fit["numerator"], prime)
    du = polynomial(u_fit["denominator"], prime)
    nv = polynomial(v_fit["numerator"], prime)
    dv = polynomial(v_fit["denominator"], prime)
    numerator = add(
        multiply(monomial_times(nu, (1, 0)), dv, prime),
        multiply(monomial_times(nv, (0, 1)), du, prime),
        prime,
    )
    denominator = multiply(du, dv, prime)
    return numerator, denominator


def radial_entry(u_fit, v_fit, slope, prime):
    numerator, denominator = radial_fraction(u_fit, v_fit, prime)
    top, degree_top = leading(numerator, slope, prime)
    bottom, degree_bottom = leading(denominator, slope, prime)
    return {
        "order": degree_top - degree_bottom,
        "leading_value": top * inv(bottom, prime) % prime,
    }


def leading_homogeneous(poly):
    degree = max(a + b for a, b in poly)
    return {exponent: coefficient for exponent, coefficient in poly.items() if sum(exponent) == degree}


def has_exact_leading_ratio(u_fit, v_fit, expected, prime):
    numerator, denominator = radial_fraction(u_fit, v_fit, prime)
    top = leading_homogeneous(numerator)
    bottom = leading_homogeneous(denominator)
    if max(map(sum, top)) != max(map(sum, bottom)):
        return False
    return add(top, {exponent: -expected * value for exponent, value in bottom.items()}, prime) == {}


def centered(value, prime):
    return value if value <= prime // 2 else value - prime


def main():
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    prime = int(payload["prime"])
    entries = {(item["axis"], item["row"], item["col"]): item["fit"] for item in payload["entries"]}
    declared, additional = source_factors(prime)
    factors = declared + additional
    denominator_degree = sum(
        weight * max(a + b for a, b in factor)
        for weight, (_, factor) in zip(COMPLETE_VECTOR, factors)
    )
    samples = []
    for slope in (2, 3, 5, 7, 11):
        radial = [[None] * 4 for _ in range(4)]
        for row in range(4):
            for column in range(4):
                radial[row][column] = radial_entry(
                    entries[("u", row, column)],
                    entries[("v", row, column)],
                    slope,
                    prime,
                )
        t_diagonal = [centered(radial[i][i]["leading_value"], prime) for i in range(2)]
        e_diagonal = [centered(radial[i][i]["leading_value"], prime) for i in range(2, 4)]
        hom_differences = sorted(e - t for e in e_diagonal for t in t_diagonal)
        resonances = sorted(denominator_degree - difference for difference in hom_differences)
        t_lower_order = radial[1][0]["order"]
        column_shifts = [0, t_lower_order]
        sheared_resonances = sorted(
            denominator_degree + column_shifts[column] - (e_diagonal[row] - t_diagonal[column])
            for row in range(2)
            for column in range(2)
        )
        c_orders = [radial[row][column]["order"] for row in range(2, 4) for column in range(2)]
        samples.append({
            "slope": slope,
            "T_diagonal_residues": t_diagonal,
            "E_diagonal_residues": e_diagonal,
            "Hom_residue_differences": hom_differences,
            "numerator_resonance_degrees": resonances,
            "T_lower_radial_order": t_lower_order,
            "target_column_degree_shifts": column_shifts,
            "sheared_weighted_resonance_degrees": sheared_resonances,
            "C_radial_orders": c_orders,
            "multiplied_C_max_degree": denominator_degree + max(c_orders),
        })
    output = {
        "schema": "marici.nima.gysin_infinity_indicial_audit.v1",
        "prime": prime,
        "connection_source": str(INPUT.relative_to(ROOT)).replace("\\", "/"),
        "complete_pole_vector": list(COMPLETE_VECTOR),
        "complete_denominator_degree": denominator_degree,
        "generic_slope_samples": samples,
        "sample_invariant_diagonal_spectra": all(
            sample["T_diagonal_residues"] == [-2, 5]
            and sample["E_diagonal_residues"] == [-1, 1]
            for sample in samples
        ),
        "sample_invariant_resonance_degrees": all(
            sample["numerator_resonance_degrees"] == [15, 17, 22, 24]
            for sample in samples
        ),
        "sample_invariant_sheared_resonances": all(
            sample["T_lower_radial_order"] == 6
            and sample["sheared_weighted_resonance_degrees"] == [15, 17, 28, 30]
            for sample in samples
        ),
        "exact_diagonal_leading_ratios": {
            "T00": has_exact_leading_ratio(entries[("u", 0, 0)], entries[("v", 0, 0)], -2, prime),
            "T11": has_exact_leading_ratio(entries[("u", 1, 1)], entries[("v", 1, 1)], 5, prime),
            "E00": has_exact_leading_ratio(entries[("u", 2, 2)], entries[("v", 2, 2)], -1, prime),
            "E11": has_exact_leading_ratio(entries[("u", 3, 3)], entries[("v", 3, 3)], 1, prime),
        },
        "naive_unshifted_resonances": [15, 17, 22, 24],
        "infinity_target_column_degree_shifts": [0, 6],
        "fixed_complete_vector_degree_bound": 30,
        "bound_scope": "conditional on the complete pole vector; local pole-order stabilization remains required",
    }
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "denominator_degree": denominator_degree,
        "spectra_invariant": output["sample_invariant_diagonal_spectra"],
        "resonances_invariant": output["sample_invariant_resonance_degrees"],
        "exact_diagonal_ratios": all(output["exact_diagonal_leading_ratios"].values()),
        "naive_resonance_degrees": samples[0]["numerator_resonance_degrees"],
        "sheared_resonance_degrees": samples[0]["sheared_weighted_resonance_degrees"],
        "multiplied_C_max_degree": max(sample["multiplied_C_max_degree"] for sample in samples),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
