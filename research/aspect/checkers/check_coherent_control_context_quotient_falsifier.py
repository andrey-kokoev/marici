import json
from pathlib import Path

import sympy as sp


I2 = sp.eye(2)
U = I2
V = -I2
a, b, c, d = sp.symbols("a b c d", complex=True)
rho = sp.Matrix([[a, b], [c, d]])

channel_U = sp.simplify(U * rho * U.conjugate().T)
channel_V = sp.simplify(V * rho * V.conjugate().T)

CU = sp.diag(1, 1, 1, 1)
CV = sp.diag(1, 1, -1, -1)
psi_in = sp.Matrix([1, 0, 1, 0]) / sp.sqrt(2)
psi_U = sp.simplify(CU * psi_in)
psi_V = sp.simplify(CV * psi_in)
X_control = sp.kronecker_product(sp.Matrix([[0, 1], [1, 0]]), I2)
expect_U = sp.simplify((psi_U.conjugate().T * X_control * psi_U)[0])
expect_V = sp.simplify((psi_V.conjugate().T * X_control * psi_V)[0])

checks = {
    "ordinary_channels_identical": channel_U == channel_V,
    "controlled_implementations_differ": CU != CV,
    "controlled_outputs_orthogonal": sp.simplify((psi_U.conjugate().T * psi_V)[0]) == 0,
    "identity_phase_x_readout": expect_U == 1,
    "minus_identity_phase_x_readout": expect_V == -1,
    "readout_gap": sp.simplify(expect_U - expect_V) == 2,
    "control_not_well_defined_on_channel_quotient": channel_U == channel_V and CU != CV,
}

result = {
    "schema": "marici.aspect.coherent-control-context-quotient-falsifier.v1",
    "status": "falsified_as_stated" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "falsified_clause": "The contextual-equivalence class at one declared boundary is final extensional content.",
    "repair": "Require contextual equivalence to be a congruence for every admitted higher-order constructor; retain lift cells when a constructor does not descend to the quotient.",
}

out = Path(__file__).parents[1] / "results" / "coherent_control_context_quotient_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "falsified_as_stated" else 1)
