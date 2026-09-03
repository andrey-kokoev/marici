from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/rh-conformance-positivity-metaobserver-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    t, sigma, d = sp.symbols("t sigma d", positive=True, real=True)

    # Even hostile rho_-=-(delta_1+delta_-1)/2.
    heat = -sp.exp(-t)
    heat_jets = [sp.simplify((-1) ** order * sp.diff(heat, t, order)) for order in range(6)]
    assert all(value == -sp.exp(-t) for value in heat_jets)
    for order in range(5):
        assert sp.simplify(heat_jets[order + 1] + sp.diff(heat_jets[order], t)) == 0

    kernel = -sp.exp(-2 * sigma) * sp.cos(d)
    for order in range(5):
        character_jet = sp.diff(kernel, d, 2 * order).subs(d, 0)
        heat_jet_at_width = sp.diff(heat, t, order).subs(t, 2 * sigma)
        assert sp.simplify(character_jet - heat_jet_at_width) == 0

    assert heat.is_negative
    assert kernel.subs(d, 0).is_negative
    positive_heat = sp.exp(-t)
    positive_kernel = sp.exp(-2 * sigma) * sp.cos(d)
    assert positive_heat.is_positive
    assert positive_kernel.subs(d, 0).is_positive

    status = contract["status"]
    assert status["conformance_implies_positivity"] == "refuted"
    result = {
        "schema":"marici.voevodsky.rh-conformance-positivity-metaobserver-check.v1",
        "status":"metaobserver_coordinate_separation_verified",
        "heat_coherence_orders_checked":6,
        "cross_family_jet_identities_checked":5,
        "signed_hostile_conforms":True,
        "signed_hostile_positive":False,
        "conformance_implies_positivity":False,
        "metaobserver_requires_equalizer_and_cone":True,
        "uniform_positive_source_transformation_supplied":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
