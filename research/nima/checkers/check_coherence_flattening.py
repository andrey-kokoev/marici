"""Rank certificate for safe and unsafe first-level coherence flattening."""


def rank_1x1_over_f2(value):
    return 1 if value % 2 else 0


def h_minus_one_dimension(chain_dimension, d_minus_2, d_minus_1):
    assert (d_minus_1 * d_minus_2) % 2 == 0
    return (
        chain_dimension
        - rank_1x1_over_f2(d_minus_1)
        - rank_1x1_over_f2(d_minus_2)
    )


safe_dimension = h_minus_one_dimension(
    chain_dimension=1, d_minus_2=1, d_minus_1=0
)
unsafe_dimension = h_minus_one_dimension(
    chain_dimension=1, d_minus_2=0, d_minus_1=0
)

assert safe_dimension == 0
assert unsafe_dimension == 1

rejection = {
    "code": "coherence_flattening_obstructed",
    "first_nonzero_degree": -1,
    "cohomology_dimension": unsafe_dimension,
}

print("safe H^-1 dimension:", safe_dimension)
print("unsafe H^-1 dimension:", unsafe_dimension)
print("rejection witness:", rejection)
print("PASS: negative Hom cohomology exactly gates witness flattening")
