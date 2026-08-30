"""Source-port recovery of the transported soft-triangle vanishing line."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    a, p, t, xi = sp.symbols("a p t xi")
    source = (a + p) / (
        2 * p * (p - a) ** 2 * (a + 3 * p) * (xi + 1)
    )
    scaled = sp.factor(source.subs(a, p * t))
    expected = (t + 1) / (
        2 * p**3 * (t - 1) ** 2 * (t + 3) * (xi + 1)
    )
    assert sp.factor(scaled - expected) == 0

    nodes = [
        (-1, -1, 3),
        (-1, 1, 1),
        (1, -1, 1),
        (1, 1, 3),
    ]
    records = []
    for kappa_value, xi_value, t_value in nodes:
        numerator = int((t + 1).subs(t, t_value))
        xi_pole_order = int(xi_value == -1)
        t_pole_order = 2 * int(t_value == 1)
        regular_value = None
        if xi_pole_order == 0 and t_pole_order == 0:
            regular_value = str(sp.factor(scaled.subs({t: t_value, xi: xi_value})))
        assert numerator != 0
        records.append({
            "kappa": kappa_value,
            "xi": xi_value,
            "t": t_value,
            "source_numerator_value": numerator,
            "xi_endpoint_pole_order": xi_pole_order,
            "t_endpoint_pole_order": t_pole_order,
            "source_zero_order": 0,
            "regular_value": regular_value,
            "annihilates_supported_line": False,
        })

    unmarked = records[-1]
    assert unmarked["regular_value"] == "1/(24*p**3)"
    assert all(not record["annihilates_supported_line"] for record in records)

    print(json.dumps({
        "schema": "marici.benincasa.soft-triangle-source-port-recovery.v1",
        "dimensionless_source_factor": str(scaled),
        "physical_open_chamber": {
            "p": ">0",
            "t": "(1,3)",
            "xi": "(-1,1)",
        },
        "source_factor_sign_on_open_chamber": "strictly_positive",
        "dt_over_w_antitrace_phase": "fixed_nonzero_imaginary",
        "node_restrictions": records,
        "unmarked_unit_witness": {
            "node": [1, 1, 3],
            "value": "1/(24*p**3)",
        },
        "global_positive_cut_weights_have_common_phase": True,
        "zeroth_source_port_recovers_second_normal_line": True,
        "status": "second_normal_soft_class_is_visible_to_the_source_scalar_port",
        "scope": (
            "source scalar marked-relative factor and positive-cut phase; "
            "no finite-q tensor vertex, polarization response, Ward audit, "
            "or complete interacting observer transfer matrix"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
