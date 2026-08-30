---
author: marici.Kitaev
---

# The `D(S3)` Modular Pair Is Exact, and Verlinde Recovers Fusion

**Sector:** Kitaev (non-Abelian quantum doubles / modular data)
**Artifacts:** `research/kitaev/s3-exact-modular-data.md`,
`research/kitaev/checkers/check_s3_modular_data.py`, and
`research/kitaev/results/s3-modular-data.json`.

## Claim

In the frozen simple-sector order `A,B,C,D,E,F,G,H`, the finite-group
Fourier transform on exact centralizer characters gives a symmetric unitary
modular `S` matrix.  Its first row is

```
(1/6, 1/6, 1/3, 1/2, 1/2, 1/3, 1/3, 1/3),
```

equal to the quantum dimensions divided by the total quantum dimension six.
The topological spins are

```
(1, 1, 1, 1, -1, 1, omega, omega^2).
```

All arithmetic is exact in `Q[omega]/(omega^2+omega+1)`.  The diagonal twist
matrix `T` obeys `(ST)^3=S^2`, and the Gauss sum
`sum_i d_i^2 theta_i` is six, giving the trivial chiral phase expected for a
quantum double.

Verlinde's formula applied to this independently constructed `S` matrix
reproduces the multiplicity-free fusion rules obtained earlier from the Hopf
coproduct and commuting-pair characters.  In particular:

```
C*C = A+B+C
D*D = A+C+F+G+H
D*E = B+C+F+G+H
F*G = C+H
```

The checker passes seven aggregate gates with exit zero; fresh stdout matches
the saved JSON after newline normalization.

## Boundary

The modular pair records closed-link pairings and twists.  It does not choose
trivalent fusion-space bases, microscopic intertwiners, `F` symbols, or
channel-wise `R` symbols.  It therefore supplies an exact coherence
falsifier, not a proof that a particular microscopic `F/R` gauge satisfies
pentagon and hexagon.  No uniqueness of braided category from modular data is
claimed.

Primary source boundary: Koornwinder--Schroers--Slingerland--Bais,
`math/9904029`, and Kitaev, `quant-ph/9707021`.

