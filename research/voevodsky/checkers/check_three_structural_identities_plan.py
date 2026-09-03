from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    plan = json.loads(Path(
        "research/voevodsky/categorical-rh-three-structural-identities-plan-v1.json"
    ).read_text(encoding="utf-8"))
    identities = {item["name"]: item for item in plan["identities"]}
    residuals = {item["identity"]: item for item in plan["residuals"]}

    assert plan["identity_count"] == len(identities) == 3
    assert plan["proved_identity_count"] == 3
    assert plan["undefined_identity_count"] == 0
    assert plan["undefined_completed_form_lift_count"] == 1
    assert identities["presentation_identity"]["state"] == "proved"
    assert residuals["presentation_identity"]["state"] == "zero"
    descent = identities["descent_identity"]
    assert descent["state"] == "proved_at_finite_rank"
    assert descent["parallel_arrows"] == [
        "direct_coarse_observation", "shifted_fine_reassembly"
    ]
    assert "loop" not in descent
    assert residuals["descent_identity"]["state"] == "zero_at_finite_rank"
    realization = identities["realization_identity"]
    assert realization["state"] == "proved_in_hilbert_modality"
    assert realization["completed_form_lift"]["state"] == "undefined"
    lift = realization["completed_form_lift"]
    assert lift["algebraic_gaussian_form"]["name"] == (
        "joint_completed_heat_quadratic_form_on_gaussian_span"
    )
    assert lift["endpoint_domain"]["name"] == "order_plus_endpoint_graph_completion"
    assert lift["source_local_completed_form"]["state"] == "constructed"
    assert lift["source_local_completed_form"]["carrier"] == (
        "H_0^s((-L,L)) for every L>0 and s>0"
    )
    assert lift["blocked_by"] == [
        "source_derived_cutoff_or_rigging_comparison_between_gaussian_and_local_weil_cores"
    ]
    assert lift["rh_bearing_gate"] == (
        "signed_tail_or_Schur_certificate_for_A_(L,s)>=0_for_every_L"
    )
    assert residuals["realization_identity"]["hilbert_state"] == "zero"
    assert residuals["realization_identity"]["completed_form_state"] == "not_formable"
    assert plan["conditional_higher_identity"]["not_counted_in_current_identity_count"]
    assert plan["rh_implication"] is False

    result = {
        "schema":"marici.voevodsky.three-structural-identities-plan-check.v1",
        "status":"three_identity_layers_typed",
        "identity_count":3,
        "proved_count":3,
        "undefined_count":0,
        "undefined_completed_form_lift_count":1,
        "descent_is_naturality_not_inverse_loop":True,
        "hilbert_realization_residual":"zero",
        "completed_form_residual_formable":False,
        "higher_identity_active":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
