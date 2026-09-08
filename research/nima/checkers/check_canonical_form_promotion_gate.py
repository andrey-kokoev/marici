#!/usr/bin/env python3
"""Assemble the typed canonical-form promotion gate from admitted local results."""
import hashlib
import json
from pathlib import Path

inputs = {
    "coefficient_factorization": Path("research/nima/results/generic_oriented_residue_factorization.json"),
    "five_point_slice": Path("research/nima/results/fact5_associahedral_slice.json"),
    "slice_nonuniqueness": Path("research/nima/results/fact5_constraint_subspaces.json"),
    "boundary_recursion": Path("research/nima/results/fact5_generic_slice_residue_recursion.json"),
    "infinity_regular": Path("research/nima/results/fact5_projective_infinity.json"),
    "fixed_arrangement_uniqueness": Path("research/nima/results/polygon_fixed_arrangement_uniqueness.json"),
}
loaded = {}
digests = {}
for name, path in inputs.items():
    raw = path.read_bytes()
    value = json.loads(raw)
    assert value["status"] == "passed"
    loaded[name] = value
    digests[name] = hashlib.sha256(raw).hexdigest()

assert loaded["slice_nonuniqueness"]["positive_rivals"]
assert loaded["fixed_arrangement_uniqueness"]["zero_dimensional_exception"]
assert loaded["five_point_slice"]["ambient_channel_dimension"] == 5
assert loaded["five_point_slice"]["slice_dimension"] == 2

result = {
    "schema": "marici.canonical-form-promotion-gate.v1",
    "status": "passed",
    "strength": "dependency-checked conditional theorem; finite checker evidence does not supply missing source maps or an unbounded construction",
    "derived_arrows": [
        "polygon face-product bijection -> Laurent coefficient factorization",
        "det(Z^D) transport -> permutation-independent iterated residues",
        "fixed reduced arrangement + equal residues + infinity regularity -> unique rational top form",
        "bounded simple affine pentagon -> interval boundary residues",
    ],
    "required_source_inputs": [
        "dimension-(n-3) affine or projective embedding with polygon-channel facet equations",
        "positive region and face-incidence identification with the polygon dissection poset",
        "Jacobian/volume identity converting the scalar weighted sum to the embedded top form",
        "zero-dimensional base normalization and compatible orientation",
        "simple-pole and projective-infinity regularity of the candidate form",
    ],
    "physical_promotion_inputs": [
        "source-derived map from physical kinematics or wavefunction data to the embedded arrangement",
        "normalization and boundary-value or contour prescription when an analytic residue is claimed",
    ],
    "current_disposition": "conditional theorem established; canonical-form and physical identifications withheld because embedding, supports, generic Jacobian identity, and source normalization are not derived",
    "five_point_falsifier": "strict positive common-Jacobian rival slices have the same recursion and infinity behavior, so those properties do not select the reference embedding",
    "input_sha256": digests,
}
out = Path("research/nima/results/canonical_form_promotion_gate.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
