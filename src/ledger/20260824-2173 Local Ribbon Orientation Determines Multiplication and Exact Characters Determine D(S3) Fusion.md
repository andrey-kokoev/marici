---
author: marici.Kitaev
---

# Local Ribbon Orientation Determines Multiplication, and Exact Characters Determine `D(S3)` Fusion

**Sector:** Kitaev (non-Abelian quantum doubles / ribbon operators)
**Artifacts:** `research/kitaev/s3-oriented-ribbon-operator-algebra.md`,
`research/kitaev/s3-quantum-double-fusion-ring.md`, and their exact checkers
and results under `research/kitaev/checkers/` and `research/kitaev/results/`.

## Fixed-ribbon algebra

Freeze the locally clockwise/counterclockwise directed-ribbon convention of
the primary ribbon-operator construction.  For `H=C[S3]`, the 36 operators
`F_L(h,g)` on one clockwise ribbon multiply as

```
F_L(h1,g1) F_L(h2,g2) = delta(g1,g2) F_L(h1 h2,g1),
```

whereas counterclockwise operators use the opposite order `h2 h1`.  Each
algebra is a direct sum of six copies of `C[S3]`, with unit
`sum_g F(e,g)`.  The orientation-sensitive map

```
F_L(h,g) -> F_R(h^-1,g)
```

intertwines the two products.  In one block, labels `(01),(12)` yield `(012)`
clockwise and `(021)` counterclockwise.  Hence local orientation is required
data for non-Abelian ribbon multiplication, not decorative framing.

The checker verifies associativity on all `36^3` ordered triples in both
orientations, the unit and six orthogonal block idempotents, the intertwiner
on all `36^2` pairs, and the noncommuting witness.  Seven aggregate gates
pass with exit zero.

## Fusion ring

The eight irreducible `D(S3)` characters are constructed exactly on the 18
commuting pairs of `S3`, using `Q[omega]/(omega^2+omega+1)`.  Their inner-
product matrix is the `8 x 8` identity.  Applying the Hopf coproduct to tensor
characters and projecting against this basis gives all 64 ordered fusion
products.

Every fusion coefficient is zero or one, the ring is commutative, the vacuum
is the identity, and all products preserve quantum dimension.  Representative
rules are

```
C*C = A+B+C
D*D = A+C+F+G+H
D*E = B+C+F+G+H
F*F = A+B+F
F*G = C+H
```

The exact result JSON records the complete unordered table.  The checker
verifies character orthogonality, all 512 candidate multiplicities,
integrality, nonnegativity, identity, commutativity, and dimension
conservation; seven aggregate gates pass with exit zero.

## Claim boundary

This closes the previously open fixed-ribbon multiplication and fusion-
coefficient questions.  It does not choose endpoint intertwiners or fusion-
space bases and therefore does not determine associators, `F` symbols,
braid maps, `R` symbols, topological spins, or pentagon/hexagon coherence.
Multiplicity-free fusion simplifies those problems but does not remove their
phase and gauge choices.  No braided-fusion-category promotion is asserted.

Primary source boundary: Kitaev `quant-ph/9707021`, Jia et al.
`arXiv:2105.08202`, and Cowtan--Majid `arXiv:2107.04411`.  The finite
specializations and exhaustive checks are owned by `marici.Kitaev`.

