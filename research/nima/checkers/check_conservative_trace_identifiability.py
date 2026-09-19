from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research/benincasa/.tmp_sympy"))
import sympy as sp

OUT = ROOT / "research/nima/results/conservative-trace-identifiability.json"


def main() -> None:
    z = sp.symbols("z")
    dE, dW, dR = sp.symbols("dE dW dR")

    # Difference of two packets that share rho(0).  Grant, more strongly than
    # current authority permits, both the Stokes relation and equality of the
    # combined strict-packet readout R+2E.
    equations = sp.Matrix([
        [sp.Integer(-1), sp.Rational(1, 2), z],  # z dR = dE-dW/2
        [sp.Integer(2), sp.Integer(0), sp.Integer(1)],  # dR+2dE=0
    ])
    null = equations.nullspace()
    witness = sp.Matrix([sp.Integer(1), 2 + 4 * z, sp.Integer(-2)])

    checks = {
        "three_unidentified_coordinates": equations.cols == 3,
        "two_granted_scalar_constraints_rank_two": equations.rank() == 2,
        "one_dimensional_ambiguity_remains": len(null) == 1,
        "explicit_ambiguity_satisfies_both_constraints": equations * witness == sp.zeros(2, 1),
        "ambiguity_is_generically_nonzero": any(entry != 0 for entry in witness),
    }

    out = {
        "schema": "marici.nima.conservative-trace-identifiability.result.v1",
        "status": "combined_shell_and_stokes_data_leave_one_coordinate_ambiguity" if all(checks.values()) else "failed",
        "checks": checks,
        "difference_coordinates": ["delta_E", "delta_W", "delta_R"],
        "granted_constraints": [
            "z delta_R-delta_E+delta_W/2=0",
            "delta_R+2 delta_E=0",
        ],
        "residual_family": {
            "parameter": "t",
            "delta_E": "t",
            "delta_W": "(2+4*z)*t",
            "delta_R": "-2*t",
        },
        "consequence": "Even if the strict-packet combined row R+2E were independently identified (it currently is not), that equality plus common rho(0) and Stokes compatibility would still fail to identify E, W, and R entrywise. One additional independently sourced coordinate equality is necessary and sufficient at generic z.",
        "minimal_next_test": "Identify any one of E, W, or R independently on the conservative/cyclic common source. The other two then follow algebraically from the combined row and Stokes relation, provided those two relations are independently authorized on both sides.",
        "claim_boundary": "This is an identifiability theorem for coordinate differences. It neither authorizes the combined strict-packet equality nor constructs the missing independent coordinate comparison.",
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] == "failed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
