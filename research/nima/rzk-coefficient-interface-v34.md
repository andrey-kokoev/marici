# v34: endpoint normal annihilators

**Nonflat base-change correction:**
[`rzk-coefficient-interface-v35.md`](rzk-coefficient-interface-v35.md) records
that the old six-normal product becomes mixed-sheet zero and replaces its
specialized interpretation by the seven generators of the alternating/Rees
annihilator.

`rzk/44-endpoint-normal-annihilators.rzk.md` internalizes the most direct
coefficient consequence of the 64-vertex endpoint normal cube.

The module retains two distinct primitive endpoint states and six legal
one-mark states: three odd short normals over the positive endpoint and three
even short normals over the negative endpoint. Its coefficient monomials have
six natural short-normal exponents; no normal is inverted.

Each marked state has differential

    marked(a) -> u_a endpoint_sigma

on its own branch. Rzk checks square-zero for all finite integral expressions.
For

    Delta = product_{i=0}^5 u_xi

it constructs explicit plus and minus primitives and proves

    Delta e_plus  = d(primitive_plus),
    Delta e_minus = d(primitive_minus).

A fresh 71-file headless closure passed in 29.97 seconds. Evidence:
`results/44-endpoint-normal-annihilators.typecheck.json`.

This reflects the new conceptual restriction: full short-normal multiplication
kills both endpoint primitive classes. It therefore cannot select one of the
earlier two relative components; it forgets their distinction. The complete
64-grade equivariant cohomology table and its free loop groups remain
certificate-level evidence rather than native Rzk computations.
