"""Exact joint-conservativity gate for the two QED D12 readouts."""

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]

# Rows are the transverse Bell and infinitesimal-transfer readouts on
# (g41/g2,g42/g2).
matrix = ((F(1), F(3, 2)), (F(1), F(1)))
observed = (F(157, 9240), F(1, 70))
determinant = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
assert determinant == -F(1, 2)

g41 = (observed[0]*matrix[1][1]-matrix[0][1]*observed[1])/determinant
g42 = (matrix[0][0]*observed[1]-observed[0]*matrix[1][0])/determinant
assert (g41, g42) == (F(41, 4620), F(5, 924))
assert matrix[0][0]*g41+matrix[0][1]*g42 == observed[0]
assert matrix[1][0]*g41+matrix[1][1]*g42 == observed[1]

payload = {
    "schema": "marici.jointly-conservative-d12-readouts.v1",
    "coefficient_basis": ["g41/g2", "g42/g2"],
    "readout_matrix": [[str(x) for x in row] for row in matrix],
    "readout_values": {
        "transverse_bell": str(observed[0]),
        "nonforward_transfer": str(observed[1]),
    },
    "determinant": str(determinant),
    "reconstruction": {"g41/g2": str(g41), "g42/g2": str(g42)},
    "strength": "exact finite-dimensional theorem in the one-loop QED D12 coefficient plane",
    "conclusion": "Neither declared readout is injective alone, but their product is injective. The pair is jointly conservative on the D12 Phi1 coefficient plane.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = HERE / "results" / "jointly-conservative-d12-readouts.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"jointly_conservative": True, "sha256": payload["content_sha256"]}))
