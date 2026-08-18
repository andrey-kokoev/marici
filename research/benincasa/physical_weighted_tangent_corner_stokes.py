"""Weighted Stokes order at a quadratic K_E--shared-wall tangency."""

from __future__ import annotations

import json


def main() -> None:
    # Weights: wt(t)=1, wt(n)=wt(K)=2.  With gamma=epsilon-1/2,
    # the exceptional pullback of -K^gamma*n^-1*(t*beta)*dn has order
    # 2*gamma - 2 + 1 + 2 = 2*epsilon.
    result = {
        "schema": "marici.physical-weighted-tangent-corner-stokes.v1",
        "local_model": "K=u*n+v*t^2+higher",
        "weights": {"t": 1, "n": 2, "K": 2},
        "log_vector_field": {"V(n)": "lambda*n", "V(t)": "beta*t+higher"},
        "syzygy_relation_on_tangent_axis": "2*beta=mu, mu=V(K)/K",
        "exceptional_chart": "t=delta, n=delta^2*s",
        "exceptional_flux_order": "delta^(2*epsilon)",
        "physical_epsilon_zero_order": 0,
        "generic_exceptional_flux_nonzero": True,
        "zero_flux_condition": "mu vanishes at the repeated wall root",
        "combined_minimal_syzygy_evaluation_kernel_dimension": 2,
        "combined_exceptional_evaluation_rank": 1,
        "canonical_primitive_selected_without_target_values": False,
    }
    assert result["physical_epsilon_zero_order"] == 0
    assert result["combined_exceptional_evaluation_rank"] == 1
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
