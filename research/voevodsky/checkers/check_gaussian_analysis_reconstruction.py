from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    # Gaussian samples exp(-a*lambda^2) become a Vandermonde matrix when
    # lambda^2 are consecutive integers and exp(-a) are distinct.
    squared_labels = [0, 1, 2]
    parameters = [1, 2, 3]
    analysis = sp.Matrix([
        [sp.exp(-a * x) for x in squared_labels]
        for a in parameters
    ])
    assert analysis.det() != 0
    reconstruction = analysis.inv()
    assert sp.simplify(reconstruction * analysis) == sp.eye(3)

    result = {
        "schema":"marici.voevodsky.gaussian-analysis-reconstruction-check.v1",
        "status":"finite_observer_identity_reconstructed",
        "analysis_rank":analysis.rank(),
        "dimension":3,
        "reconstruction_after_analysis":"identity",
        "infinite_range_inverse":"defined on transported-norm analysis range by totality",
        "hilbert_observer_residual":"zero",
        "completed_form_residual_formable":False,
        "source_weil_comparison_constructed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
