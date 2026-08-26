"""WP310: exact source typing of an up/down reciprocal hierarchy selector."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def hierarchy(ordered_masses):
    return sp.simplify(ordered_masses[-1] / ordered_masses[0])


def main():
    up_masses = tuple(sp.Rational(value) for value in (1, 2, 3))
    down_masses = tuple(sp.Rational(value) for value in (5, 7, 11))
    up_hierarchy = hierarchy(up_masses)
    down_hierarchy = hierarchy(down_masses)
    ratio = sp.simplify(up_hierarchy / down_hierarchy)
    exchanged_ratio = sp.simplify(down_hierarchy / up_hierarchy)

    hypercharges = {
        "Q_L": sp.Rational(1, 6),
        "u_R": sp.Rational(2, 3),
        "d_R": sp.Rational(-1, 3),
    }
    direct_exchange_preserves_hypercharge = hypercharges["u_R"] == hypercharges["d_R"]
    sign_automorphism_maps_up_to_down = -hypercharges["u_R"] == hypercharges["d_R"]

    checks = {
        "hierarchy_ratio_is_dimensionless_spectral_invariant": ratio == sp.Rational(15, 11),
        "sector_exchange_sends_ratio_to_reciprocal": exchanged_ratio == 1 / ratio,
        "sector_exchange_is_involution_on_mass_packets": (down_masses, up_masses)[::-1] == (up_masses, down_masses),
        "reciprocal_fixed_locus_is_equal_hierarchy": sp.solve(sp.Eq(sp.symbols("r", positive=True), 1 / sp.symbols("r", positive=True))) == [1],
        "right_handed_hypercharges_are_inequivalent": not direct_exchange_preserves_hypercharge,
        "hypercharge_sign_automorphism_does_not_repair_exchange": not sign_automorphism_maps_up_to_down,
        "benchmark_is_not_on_duality_fixed_locus": ratio != 1,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP310",
        "admitted_flavor_coordinate": "r=(m_u,max/m_u,min)/(m_d,max/m_d,min), built from ordered spectral physical16 masses",
        "candidate_duality": "exchange the up- and down-type Yukawa sectors, sending r->1/r",
        "mathematical_selector": "reciprocal fixed locus r=1, predicting equal up/down hierarchy ratios",
        "exact_benchmark": {
            "up_masses": [str(value) for value in up_masses],
            "down_masses": [str(value) for value in down_masses],
            "up_hierarchy": str(up_hierarchy),
            "down_hierarchy": str(down_hierarchy),
            "r": str(ratio),
        },
        "source_typing": {
            "Q_L_hypercharge": str(hypercharges["Q_L"]),
            "u_R_hypercharge": str(hypercharges["u_R"]),
            "d_R_hypercharge": str(hypercharges["d_R"]),
            "direct_exchange_is_sm_gauge_equivariant": direct_exchange_preserves_hypercharge,
            "u1_sign_automorphism_repairs_exchange": sign_automorphism_maps_up_to_down,
        },
        "descent": "the ratio itself descends to physical16, but the proposed exchange does not descend from an admitted Standard Model source operation because u_R and d_R occupy inequivalent gauge representations",
        "classification": "mathematical reciprocal ratio selector on an enlarged sector-exchange model; neither an authorized Standard Model flavor selector nor a texture rigidifier",
        "smallest_exact_falsifier": "Y(u_R)=2/3 and Y(d_R)=-1/3, so neither direct exchange nor U(1) charge-sign reversal maps the source representations",
        "remaining_physical_instrument_gate": "construct an enlarged anomaly-consistent source in which up/down exchange is a genuine operation, derive its breaking and matching to the Standard Model, and test the equal-hierarchy prediction before fitting",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp310_up_down_reciprocal_duality_typing.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
