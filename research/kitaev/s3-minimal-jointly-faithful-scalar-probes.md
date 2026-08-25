# A minimum jointly faithful scalar probe family for `D(S3)`

Owner: `marici.Kitaev`

## Bounded question

Within the frozen scalar probe surface consisting of topological twist and
the eight Hopf-link amplitudes `S_A,...,S_H`, how many probes are required to
separate all eight anyon labels?

Exactly three.  Exhaustive enumeration of every subset finds four minimum
families:

\[
(\theta,S_C,S_D),\quad (\theta,S_C,S_E),\quad
(\theta,S_D,S_F),\quad (\theta,S_E,S_F).
\]

The packet selects `(theta,S_D,S_F)` as a representative.

## Exact signatures

In label order `A,B,C,D,E,F,G,H`, the selected signatures are

| sector | `theta` | `S_D` | `S_F` |
|---|---:|---:|---:|
| A | 1 | 1/2 | 1/3 |
| B | 1 | -1/2 | 1/3 |
| C | 1 | 0 | -1/3 |
| D | 1 | 1/2 | 0 |
| E | -1 | -1/2 | 0 |
| F | 1 | 0 | 2/3 |
| G | `omega` | 0 | -1/3 |
| H | `omega^2` | 0 | -1/3 |

All eight rows differ.  Twist closes the centralizer-irrep kernel found in
the pure-charge monodromy packet: it separates `D/E` and all of `F/G/H`.
The two reference Hopf-link probes separate the remaining electric/flux
collisions.

## Minimality

No one- or two-probe subset of the nine-candidate surface is faithful.  The
checker enumerates all such subsets.  Three representative two-probe
falsifiers show why each ingredient matters:

- `(theta,S_F)` collides `A,B`;
- `(theta,S_D)` collides `C,F`;
- `(S_D,S_F)` collides `G,H`.

These examples explain the selected family, while exhaustive enumeration
proves the surface-relative lower bound.

## Physical typing

`theta` requires a framed self-twist process.  `S_D` and `S_F` require
constructible reference anyons in the transposition-trivial and
three-cycle-trivial sectors, linked transport, fusion back to a scalar
record, and normalization.  The theorem is conditional on those constructors
being admitted.  A numerical table alone does not supply them.

Carrier geometry supplies framed self-rotation, linked ribbon classes, and
reference-port placement.  The quantum coefficient lens supplies sector
preparation, braid amplitudes, fusion-to-vacuum effects, and the complex
scalar values.

## Verification

`python -u research/kitaev/checkers/check_s3_minimal_scalar_probe_family.py`
passes seven aggregate gates.  It exhausts all subsets of the nine probes,
records all four minimum families, verifies the selected signatures, and
checks the three explicit two-probe collisions.  Fresh stdout matches the
saved JSON after newline normalization.

## Claim boundary

The minimum is relative to the declared scalar candidate surface and counts
each complex twist or Hopf-link amplitude as one probe.  It is not an
absolute experimental-resource lower bound: a richer multi-outcome
instrument, full monodromy tomography, adaptive protocol, or differently
costed complex quadratures changes the optimization problem.  Joint scalar
faithfulness also does not select a decoder or state preparation.

The modular values derive from the finite-group Fourier transform of
[Koornwinder et al.](https://arxiv.org/abs/math/9904029) in the physical
quantum-double setting of [Kitaev](https://arxiv.org/abs/quant-ph/9707021).

## Falsifiers

A duplicate row in the selected signature table, any faithful one- or
two-probe subset, a twist that fails to separate the stated centralizer
irreps, or a changed candidate/cost surface presented as the same theorem
falsifies the claim.
