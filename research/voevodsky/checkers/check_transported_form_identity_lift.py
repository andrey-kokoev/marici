from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    analysis = sp.Matrix([[1, 1], [1, 2]])
    reconstruction = analysis.inv()
    source_form = sp.Matrix([[3, 1], [1, 4]])
    # K on the analysis range is defined so K(Ax,Ay)=q(x,y).
    range_form = reconstruction.T * source_form * reconstruction
    pulled_back = analysis.T * range_form * analysis
    assert sp.simplify(pulled_back - source_form) == sp.zeros(2)
    assert reconstruction * analysis == sp.eye(2)

    result = {
        "schema":"marici.voevodsky.transported-form-identity-lift-check.v1",
        "status":"form_transport_identity_verified",
        "analysis_reconstruction_identity":True,
        "form_pullback_exact":True,
        "independent_return_map_required":False,
        "source_kernel_required":True,
        "closability_required_in_infinite_dimension":True,
        "source_weil_comparison_separate":True,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
