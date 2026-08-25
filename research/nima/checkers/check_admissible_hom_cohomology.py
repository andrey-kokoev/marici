"""Hostile witness: ordinary vanishing can use a forbidden higher filler."""


def h_minus_one_dimension(chain_dim, rank_out, rank_in):
    return chain_dim - rank_out - rank_in


# Full Hom segment: u maps onto z, and z maps to zero.
ordinary_dimension = h_minus_one_dimension(
    chain_dim=1,
    rank_out=0,
    rank_in=1,
)

# Contract excludes u but permits z. The admitted incoming boundary has rank 0.
admissible_dimension = h_minus_one_dimension(
    chain_dim=1,
    rank_out=0,
    rank_in=0,
)

assert ordinary_dimension == 0
assert admissible_dimension == 1

witness = {
    "code": "admissible_coherence_obstructed",
    "ordinary_dimension": ordinary_dimension,
    "admissible_dimension": admissible_dimension,
    "excluded_filler": "u",
    "exclusion_basis": "fault_or_support_contract",
}

print("ordinary H^-1 dimension:", ordinary_dimension)
print("admissible H^-1 dimension:", admissible_dimension)
print("rejection witness:", witness)
print("PASS: unrestricted vanishing does not authorize coherence flattening")
