#!/usr/bin/env python3
"""Exact finite-field hostile comparison for RS-1's first source object."""


def rank_mod(matrix, p):
    work = [[value % p for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inv = pow(work[pivot_row][col], -1, p)
        work[pivot_row] = [(value * inv) % p for value in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and work[r][col]:
                factor = work[r][col]
                work[r] = [
                    (a - factor * b) % p
                    for a, b in zip(work[r], work[pivot_row])
                ]
        pivot_row += 1
    return pivot_row


def norm_packet(p):
    # In the regular basis of F_p[C_p], multiplication by nu is the all-ones
    # matrix: each output coefficient is the augmentation of the input.
    norm_matrix = [[1] * p for _ in range(p)]
    norm_rank = rank_mod(norm_matrix, p)
    kernel_dimension = p - norm_rank
    norm_vector = [1] * p
    assert sum(norm_vector) % p == 0
    norm_line_dimension = 1
    homology_dimension = kernel_dimension - norm_line_dimension
    # nu^2=p*nu=0: the all-ones matrix squares to p times itself.
    square = [
        [sum(norm_matrix[i][k] * norm_matrix[k][j] for k in range(p)) % p
         for j in range(p)]
        for i in range(p)
    ]
    assert all(value == 0 for row in square for value in row)
    return kernel_dimension, homology_dimension


def main():
    observed = {}
    for p in (2, 3, 5, 7):
        kernel, homology = norm_packet(p)
        assert kernel == p - 1
        assert homology == p - 2
        observed[p] = homology

    assert observed == {2: 0, 3: 1, 5: 3, 7: 5}

    free_four_syndrome = 4 - 1
    modular_five_syndrome = observed[5]
    assert free_four_syndrome == modular_five_syndrome == 3
    descriptors = {
        "free": ("Q", 4, "augmentation_kernel"),
        "modular": ("F5", 5, "augmentation_kernel_mod_norm_line"),
    }
    assert descriptors["free"] != descriptors["modular"]

    print("PASS: modular norm homology has dimension p-2 for p=2,3,5,7")
    print("PASS: C5 residual and free four-branch syndrome both have rank three")
    print("HOSTILE PASS: coefficient field, channel count, and quotient typing differ")
    print("GATE: rank equality does not define a comparison map")


if __name__ == "__main__":
    main()
