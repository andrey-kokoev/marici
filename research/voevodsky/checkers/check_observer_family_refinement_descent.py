from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    # Exact fixture: rank N=3 and refinement factor m=4.
    N, m = 3, 4
    H = sp.symbols(f"H0:{2*m*(N-1)+m+1}")
    d = [H[q] - H[q + 1] for q in range(len(H) - 1)]

    coarse = sp.Matrix(N, N, lambda i, j: H[m * (i + j)] - H[m * (i + j + 1)])
    descended = sp.zeros(N)
    for r in range(m):
        descended += sp.Matrix(N, N, lambda i, j: d[m * (i + j) + r])
    assert coarse == descended

    # Each summand is a sparse principal compression of a shifted fine-mesh Hankel matrix.
    size = m * (N - 1) + 1
    selectors = []
    for r in range(m):
        fine_shifted = sp.Matrix(size, size, lambda p, q: d[p + q + r])
        selector = sp.zeros(size, N)
        for i in range(N):
            selector[m * i, i] = 1
        compressed = selector.T * fine_shifted * selector
        expected = sp.Matrix(N, N, lambda i, j: d[m * (i + j) + r])
        assert compressed == expected
        selectors.append(True)

    result = {
        "schema":"marici.voevodsky.observer-family-refinement-descent-check.v1",
        "status":"mesh_refinement_descent_verified",
        "fixture_rank":N,
        "refinement_factor":m,
        "telescoping_identity":True,
        "sparse_principal_compressions":all(selectors),
        "positivity_arrow":"fine shifted meshes imply coarse mesh",
        "reverse_arrow":False,
        "all_rank_uniformity":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
