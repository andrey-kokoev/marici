#!/usr/bin/env python3
"""Register the exact uniform source estimate; do not assume its RH-strength inequality."""
import json
from pathlib import Path

# Algebraic finite fixture verifies the nesting logic only. The arithmetic inequality
# is deliberately represented as an open obligation, not a passing check.
checks={
 "incoming_feature":"sum_j c_j E(z_j) exp(i z_j r)",
 "outgoing_feature":"sum_j c_j E*(z_j) exp(i z_j r)",
 "uniform_estimate":"integral_0^infty |outgoing|^2 dr <= integral_0^infty |incoming|^2 dr",
 "finite_Gram_equivalent":"c* G_out c <= c* G_in c for every finite packet and coefficient vector",
 "rung_enlargement":"the same constant 1 applies because every smaller packet is a principal compression",
 "Hardy_operator_equivalent":"I-M_Theta M_Theta* >= 0",
 "Pick_equivalent":"(1-Theta(z)conj(Theta(w)))/(2pi i(conj(w)-z)) is positive on every finite packet",
 "RH_strength":"for the completed Xi Clark function this is the Hermite-Biehler/zero-confinement condition",
}
out={
 "schema":"marici.voevodsky.uniform-source-estimate-contract.v1",
 "checks":checks,
 "target_constant":1,
 "quantifiers":"all N>=1, all upper-half-plane z_1,...,z_N, all c in C^N",
 "source_formula":"E and E* are the fixed codiagonal moment sewings of the completed theta transform; no zero list enters the formulation.",
 "known_certified_subset":"one nested six-point family through N=6",
 "proved":False,"passed":True,"rh_proved":False,
 "disposition":"The requested uniform estimate is not a technical bound remaining after normalization; it is exactly the sole RH-strength co-defect inequality. It cannot be inferred from finitely many packets or from one-sided passivity.",
 "admissible_next_proof_inputs":[
  "a source decomposition of G_in-G_out into positive prime/gamma/endpoint Grams valid for arbitrary packets",
  "a uniform complementary-bulk contraction plus the parity-reduced endpoint Douglas domination",
  "a coherent all-rung source contraction with norm at most one"
 ]
}
p=Path(__file__).parents[1]/"results"/"uniform_source_estimate_contract.json";p.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,indent=2))
