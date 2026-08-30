"""Exact two-port witness: determinant equality does not fix ordered current."""

from fractions import Fraction as F
import json


def transpose(a):
    return [list(row) for row in zip(*a)]


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def matvec(a, x):
    return [sum(a[i][j] * x[j] for j in range(2)) for i in range(2)]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def characteristic(a):
    return (F(1), -(a[0][0] + a[1][1]), det2(a))


def main():
    forward = [[F(1), F(1)], [F(0), F(1)]]
    reciprocal = transpose(forward)
    source = [F(0), F(1)]
    local_oscillator = [F(1), F(0)]
    forward_quadrature = dot(local_oscillator, matvec(forward, source))
    reciprocal_quadrature = dot(local_oscillator, matvec(reciprocal, source))
    current = forward_quadrature - reciprocal_quadrature
    reversed_current = reciprocal_quadrature - forward_quadrature
    checks = {
        "both_routes_have_unit_determinant": det2(forward) == det2(reciprocal) == 1,
        "scalar_characteristic_sections_agree": characteristic(forward) == characteristic(reciprocal),
        "ordered_heterodyne_records_differ": forward_quadrature != reciprocal_quadrature,
        "antisymmetric_current_is_nonzero": current == 1,
        "reciprocal_exchange_reverses_current": reversed_current == -current,
        "intensity_or_determinant_only_readout_is_insufficient": True,
        "physical_nonunitary_realization_requires_declared_environment_ports": True,
        "witness_does_not_supply_theta_euler_source_identity": True,
    }
    result = {
        "schema": "marici.aspect.reciprocal_ordered_current_heterodyne_witness.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "scalar_section": [str(x) for x in characteristic(forward)],
        "heterodyne_quadratures": {
            "forward": str(forward_quadrature),
            "reciprocal": str(reciprocal_quadrature),
            "antisymmetric_current": str(current),
        },
        "typed_boundary": {
            "source": "one calibrated coherent excitation and one phase-locked local oscillator",
            "constructor": "forward two-port shear versus its reciprocal transpose, including dilation ports if realized physically",
            "detector": "signed heterodyne cross quadrature before scalar aggregation",
            "hostile": "equal determinant and characteristic data with a nonzero exchange-odd ordered current",
            "completion": "falsifies determinant-only recovery but does not construct the theta-Euler comparison cell",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
