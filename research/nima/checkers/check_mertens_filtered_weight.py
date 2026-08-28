import json
from fractions import Fraction


diagonal = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 5), Fraction(1, 7)]
cutoff = [1, 1, 0, 0]
permutation = [3, 1, 2, 0]


def cutoff_trace(values, projection):
    return sum(
        (value for value, retained in zip(values, projection) if retained),
        Fraction(0),
    )


transported_diagonal = [diagonal[index] for index in permutation]
transported_cutoff = [cutoff[index] for index in permutation]

original = cutoff_trace(diagonal, cutoff)
operator_only = cutoff_trace(transported_diagonal, cutoff)
filtered_pair = cutoff_trace(transported_diagonal, transported_cutoff)

assert original == Fraction(5, 6)
assert operator_only == Fraction(10, 21)
assert filtered_pair == original
assert sorted(diagonal) == sorted(transported_diagonal)

result = {
    "schema": "marici.nima.mertens-filtered-weight.v1",
    "original_cutoff_trace": str(original),
    "operator_only_transport_trace": str(operator_only),
    "filtered_pair_transport_trace": str(filtered_pair),
    "full_spectrum_preserved": True,
    "operator_only_transport_preserves_weight": False,
    "filtered_pair_transport_preserves_weight": True,
    "mertens_functional_type": "prime_filtered_boundary_weight",
    "next_gate": "filtered_boundary_completion_naturality",
}
print(json.dumps(result, indent=2, sort_keys=True))

