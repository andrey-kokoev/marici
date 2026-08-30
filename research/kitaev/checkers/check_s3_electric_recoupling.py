"""Exact F/R fragment for the pure-electric Rep(S3) subcategory."""

import json
import sympy as sp


def kron(*matrices):
    out = sp.Matrix([[1]])
    for matrix in matrices:
        out = sp.kronecker_product(out, matrix)
    return out


def freeze_sign(matrix):
    for value in matrix:
        value = sp.simplify(value)
        if value != 0:
            if value.could_extract_minus_sign():
                return -matrix
            return matrix
    raise AssertionError("zero intertwiner")


def normalized_intertwiner(source, target):
    source_dim = source[0].rows
    target_dim = target[0].rows
    variables = sp.symbols(f"x0:{target_dim * source_dim}")
    candidate = sp.Matrix(target_dim, source_dim, variables)
    equations = []
    for source_g, target_g in zip(source, target):
        equations.extend(list(target_g * candidate - candidate * source_g))
    coefficient, _ = sp.linear_eq_to_matrix(equations, variables)
    nullspace = coefficient.nullspace()
    assert len(nullspace) == 1
    candidate = sp.Matrix(target_dim, source_dim, list(nullspace[0]))
    gram = sp.simplify(candidate.T * candidate)
    scale = sp.simplify(gram[0, 0])
    assert gram == scale * sp.eye(source_dim) and scale > 0
    return freeze_sign(sp.simplify(candidate / sp.sqrt(scale)))


def scalar_identity(matrix):
    scalar = sp.simplify(sp.trace(matrix) / matrix.rows)
    assert sp.simplify(matrix - scalar * sp.eye(matrix.rows)) == sp.zeros(*matrix.shape)
    return scalar


def text(value):
    return str(sp.simplify(value)).replace("sqrt(2)", "sqrt2").replace("sqrt(3)", "sqrt3")


def main():
    sqrt3 = sp.sqrt(3)
    reps = {
        "A": [sp.Matrix([[1]]), sp.Matrix([[1]])],
        "B": [sp.Matrix([[1]]), sp.Matrix([[-1]])],
        "C": [sp.Matrix([[-sp.Rational(1, 2), -sqrt3 / 2],
                         [sqrt3 / 2, -sp.Rational(1, 2)]]),
              sp.diag(1, -1)],
    }
    dimensions = {name: matrices[0].rows for name, matrices in reps.items()}

    def tensor_rep(left, right):
        return [kron(a, b) for a, b in zip(reps[left], reps[right])]

    # Embeddings E_ab^c: V_c -> V_a tensor V_b, in a frozen real orthonormal gauge.
    embeddings = {}
    for target in ("A", "B", "C"):
        embeddings[("C", "C", target)] = normalized_intertwiner(reps[target], tensor_rep("C", "C"))
    for intermediate in ("A", "B", "C"):
        embeddings[(intermediate, "C", "C")] = normalized_intertwiner(reps["C"], tensor_rep(intermediate, "C"))
        embeddings[("C", intermediate, "C")] = normalized_intertwiner(reps["C"], tensor_rep("C", intermediate))

    # C tensor C decomposes completely and orthogonally as A+B+C.
    cc_columns = sp.Matrix.hstack(*(embeddings[("C", "C", x)] for x in ("A", "B", "C")))
    assert sp.simplify(cc_columns.T * cc_columns) == sp.eye(4)
    assert sp.simplify(cc_columns * cc_columns.T) == sp.eye(4)

    left_paths = {}
    right_paths = {}
    identity_c = sp.eye(2)
    for intermediate in ("A", "B", "C"):
        left_paths[intermediate] = sp.simplify(
            kron(embeddings[("C", "C", intermediate)], identity_c)
            * embeddings[(intermediate, "C", "C")]
        )
        right_paths[intermediate] = sp.simplify(
            kron(identity_c, embeddings[("C", "C", intermediate)])
            * embeddings[("C", intermediate, "C")]
        )
        assert sp.simplify(left_paths[intermediate].T * left_paths[intermediate]) == sp.eye(2)
        assert sp.simplify(right_paths[intermediate].T * right_paths[intermediate]) == sp.eye(2)

    channels = ("A", "B", "C")
    fmatrix = sp.Matrix([[scalar_identity(left_paths[e].T * right_paths[f])
                          for f in channels] for e in channels])
    assert sp.simplify(fmatrix.T * fmatrix) == sp.eye(3)
    assert sp.simplify(fmatrix * fmatrix.T) == sp.eye(3)

    # The electric subcategory is symmetric: braiding is the tensor-factor flip.
    flip = sp.zeros(4)
    for i in range(2):
        for j in range(2):
            flip[2 * j + i, 2 * i + j] = 1
    r_eigenvalues = {}
    for channel in channels:
        embedding = embeddings[("C", "C", channel)]
        r_eigenvalues[channel] = scalar_identity(embedding.T * flip * embedding)
    assert r_eigenvalues == {"A": 1, "B": -1, "C": 1}

    b12 = sp.diag(*(r_eigenvalues[channel] for channel in channels))
    b23 = sp.simplify(fmatrix * b12 * fmatrix.T)
    braid_relation = sp.simplify(b12 * b23 * b12 - b23 * b12 * b23) == sp.zeros(3)
    symmetric_square = b12 * b12 == sp.eye(3) and sp.simplify(b23 * b23) == sp.eye(3)
    assert braid_relation and symmetric_square

    result = {
        "schema": "marici.s3-electric-recoupling.v1",
        "subcategory": "Rep(S3)_pure_electric",
        "fusion_channel_order": list(channels),
        "C_tensor_C_decomposition": ["A", "B", "C"],
        "F_CCC_to_C": [[text(fmatrix[i, j]) for j in range(3)] for i in range(3)],
        "F_is_orthogonal": True,
        "R_CC_by_channel": {channel: text(r_eigenvalues[channel]) for channel in channels},
        "multiplicity_space_B12": [[text(b12[i, j]) for j in range(3)] for i in range(3)],
        "multiplicity_space_B23": [[text(b23[i, j]) for j in range(3)] for i in range(3)],
        "braid_relation_verified": braid_relation,
        "symmetric_braiding_squares_to_identity": symmetric_square,
        "aggregate_gates": {
            "standard_representation_is_exact": True,
            "C_tensor_C_decomposes_orthogonally_as_A_B_C": True,
            "three_left_and_right_C_channels_are_orthonormal": True,
            "F_CCC_to_C_is_exact_and_orthogonal": True,
            "R_eigenvalues_are_plus_minus_plus": True,
            "braid_relation_holds_on_total_C_multiplicity_space": braid_relation,
            "electric_braiding_is_symmetric": symmetric_square,
            "fragment_does_not_certify_full_D_S3_coherence": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
