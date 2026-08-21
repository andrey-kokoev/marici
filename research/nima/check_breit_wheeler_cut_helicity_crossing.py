"""Cross the physical cut matrix into the all-incoming Phi1,Phi2,Phi5 basis."""

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from check_nonforward_breit_wheeler_cut import (  # noqa: E402
    cut_matrix, helicity_polarization
)


# Antipodal polarization transport: the standard spherical frame at -n turns
# an incoming helicity vector into the complex conjugate outgoing vector at n.
antipodal_rows = []
for theta in (0.23, 0.71, 1.17):
    for h in (-1, 1):
        lhs = helicity_polarization(np.pi-theta, np.pi, h)
        rhs = np.conjugate(helicity_polarization(theta, 0, h))
        residual = np.max(np.abs(lhs-rhs))
        assert residual < 4e-16
        antipodal_rows.append({"theta": theta, "helicity": h, "residual": float(residual)})


def extract_phi_discontinuities(C):
    # Column zero is the physical incoming ++ state.  The outgoing states occur
    # in the unitarity bra.  After crossing them into the source paper's
    # all-incoming convention their helicity labels are reversed.  The mixed
    # channel also carries the standard one-crossing polarization phase.
    return {
        "ImPhi1": C[0, 0],    # physical ++ -> ++ : all-incoming --++
        "ImPhi2": C[3, 0],    # physical ++ -> -- : all-incoming ++++
        "ImPhi5_a": -C[1, 0], # physical ++ -> +- : all-incoming -+++
        "ImPhi5_b": -C[2, 0], # physical ++ -> -+ : Bose-related presentation
    }


samples = []
for s, t in ((8.0, -0.75), (10.0, -1.0), (14.0, -2.0)):
    theta = np.arccos(1+2*t/s)
    low = cut_matrix(s, theta, order=20)
    high = cut_matrix(s, theta, order=32)
    convergence = np.max(np.abs(high-low))
    phis = extract_phi_discontinuities(high)
    mixed_residual = abs(phis["ImPhi5_a"]-phis["ImPhi5_b"])
    imaginary_residual = max(abs(z.imag) for z in phis.values())
    assert convergence < 2e-8
    assert mixed_residual < 3e-14
    assert imaginary_residual < 3e-14
    samples.append({
        "s": s,
        "t": t,
        "theta": float(theta),
        "quadrature_convergence": float(convergence),
        "mixed_helicity_residual": float(mixed_residual),
        "imaginary_residual": float(imaginary_residual),
        "discontinuities": {k: float(v.real) for k, v in phis.items()},
    })

payload = {
    "schema": "marici.breit-wheeler-cut-helicity-crossing.v1",
    "antipodal_transport": antipodal_rows,
    "physical_matrix_order": ["++", "+-", "-+", "--"],
    "initial_column": "++",
    "crossing_map": {
        "ImPhi1": "C[++,++]",
        "ImPhi2": "C[--,++]",
        "ImPhi5": "-C[+-,++]=-C[-+,++]",
    },
    "samples": samples,
    "conclusion": "The geometric antipodal frame identity is not itself the amplitude-label crossing rule. Because the physical outgoing states occur in the unitarity bra, conversion to the source all-incoming convention reverses their helicity labels; the mixed channel has one additional crossing phase. The initial-++ cut column maps to (Phi1,-Phi5,-Phi5,Phi2).",
    "next_gate": "Integrate these three discontinuities against the fixed-t inverse-cubic kernel and compare with the independently known low-energy coefficients.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "breit-wheeler-cut-helicity-crossing.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"crossing_map": "passed", "sha256": payload["content_sha256"]}))
