import json
from pathlib import Path


# D: Q^2 -> Q has rank one.
forward = {
    "even_dimension": 2,
    "odd_dimension": 1,
    "rank": 1,
}
forward["even_cohomology_dimension"] = forward["even_dimension"] - forward["rank"]
forward["odd_cohomology_dimension"] = forward["odd_dimension"] - forward["rank"]
forward["graded_index"] = forward["even_cohomology_dimension"] - forward["odd_cohomology_dimension"]

# D^T: Q -> Q^2 has the same rank and nonzero singular spectrum.
reverse = {
    "even_dimension": 1,
    "odd_dimension": 2,
    "rank": 1,
}
reverse["even_cohomology_dimension"] = reverse["even_dimension"] - reverse["rank"]
reverse["odd_cohomology_dimension"] = reverse["odd_dimension"] - reverse["rank"]
reverse["graded_index"] = reverse["even_cohomology_dimension"] - reverse["odd_cohomology_dimension"]

assert forward["graded_index"] == 1
assert reverse["graded_index"] == -1

shared_quadratic_data = {
    "rank": 1,
    "nonzero_singular_values_squared": [1],
    "hilbert_schmidt_norm_squared": 1,
}

# Supertrace(I)=dim_even-dim_odd. A scalar Cartan identity with I on an
# imbalanced 2|1 space contradicts vanishing supertrace of an odd
# supercommutator.
supertrace_identity_forward = forward["even_dimension"] - forward["odd_dimension"]
assert supertrace_identity_forward == 1

result = {
    "forward_incidence": forward,
    "reverse_incidence": reverse,
    "shared_ungraded_quadratic_data": shared_quadratic_data,
    "quadratic_data_determine_parity": False,
    "supertrace_identity_on_forward_complex": supertrace_identity_forward,
    "scalar_cartan_identity_possible_on_imbalanced_finite_complex": False,
    "verdict": "parity and determinant orientation require ordered source incidence",
}

output = Path(__file__).parents[1] / "results" / "rh-source-incidence-parity.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

