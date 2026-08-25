"""Smallest scalar-invisible obstruction to chain homotopy, over F_2."""

F = ((1, 0), (0, 1))
G = ((1, 0), (0, 0))
P = (1, 0)


def left_project(p, matrix):
    return tuple(
        sum(p[i] * matrix[i][j] for i in range(2)) % 2
        for j in range(2)
    )


projected_f = left_project(P, F)
projected_g = left_project(P, G)
E = tuple(
    tuple((F[i][j] - G[i][j]) % 2 for j in range(2))
    for i in range(2)
)

# The complexes are concentrated in degree zero. Hom^{-1}=0, so the
# boundary subspace in Hom^0 is {0}; a nonzero E cannot be a homotopy.
hom_minus_one_dimension = 0
obstruction_rank = 1 if E == ((0, 0), (0, 1)) else None

assert projected_f == projected_g == (1, 0)
assert hom_minus_one_dimension == 0
assert E != ((0, 0), (0, 0))
assert obstruction_rank == 1

witness = {
    "code": "projected_equality_without_chain_homotopy",
    "projected_maps_equal": True,
    "hom_obstruction_degree": 0,
    "obstruction_rank": obstruction_rank,
}

print("P F:", projected_f)
print("P G:", projected_g)
print("F-G:", E)
print("rejection witness:", witness)
print("PASS: scalar equality does not imply homotopy-coherent equivalence")
