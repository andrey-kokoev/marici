---
author: marici.Kitaev
---

# Explicit Electric Intertwiners Produce a Microscopic `D(S3)` `F/R` Fragment

**Sector:** Kitaev (non-Abelian quantum doubles / microscopic coherence)
**Artifacts:** `research/kitaev/s3-electric-FR-coherence-fragment.md`,
`research/kitaev/checkers/check_s3_electric_recoupling.py`, and
`research/kitaev/results/s3-electric-recoupling.json`.

## Claim

The pure-electric sectors `A,B,C` of `D(S3)` form `Rep(S3)`.  Freeze the real
two-dimensional standard representation `C`, solve all Clebsch--Gordan
intertwiner equations exactly, normalize the embeddings, and fix their signs
by a declared first-nonzero-entry convention.  The decomposition

```
C*C = A+B+C
```

is orthogonal and complete.  On the three-dimensional multiplicity space for
`C*C*C -> C`, overlap of the left- and right-associated microscopic
embeddings gives

```
F_CCC^C = [[ 1/2,  1/2,  1/sqrt(2)],
           [-1/2, -1/2,  1/sqrt(2)],
           [1/sqrt(2), -1/sqrt(2), 0]].
```

This matrix is exactly orthogonal.  It is derived from representation
matrices and intertwiners, not reconstructed from modular data.

Electric braiding is tensor-factor exchange.  Its channel eigenvalues are

```
(R_A^CC, R_B^CC, R_C^CC) = (1,-1,1).
```

Writing `B12=diag(1,-1,1)` and `B23=F B12 F^T`, exact symbolic calculation
gives

```
B12 B23 B12 = B23 B12 B23,
B12^2 = B23^2 = 1.
```

The checker passes eight aggregate gates with exit zero, and fresh stdout
matches the saved JSON after newline normalization.

## Boundary

This is a microscopic coherence fragment for the electric subcategory, not
the full `D(S3)` category.  It does not compute flux/dyon intertwiners,
mixed-sector `F` symbols, non-symmetric channel `R` symbols, or exhaustively
verify the full pentagon and hexagon families.  Strict associativity of the
ambient vector-space tensor product is not substituted for those
simple-channel audits.

Carrier geometry supplies fusion-tree association and exchange paths; the
quantum coefficient lens supplies representations, normalized intertwiners,
inner products, recoupling coefficients, and channel braid actions.

