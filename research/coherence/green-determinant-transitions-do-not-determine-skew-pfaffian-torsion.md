# Green determinant transitions do not determine skew Pfaffian torsion

## Two line invariants

For ordered correlations

\[
\rho_0,\ldots,\rho_{n-2},
\]

the positive Green Gram determinant is

\[
\det K=
\prod_{i=0}^{n-2}(1-\rho_i^2).
\]

For even \(n=2m\), the ordered skew-chain Pfaffian is

\[
\operatorname{Pf}M
=
\rho_0\rho_2\cdots\rho_{2m-2}.
\]

The first expression is symmetric in all adjacent correlations. The second remembers their parity positions. Therefore the Green determinant line and skew Pfaffian torsion retain different information.

## Exact hostile

Consider four-point chains with gap correlations

\[
A=(1/2,1/3,1/4),
\]

\[
B=(1/3,1/2,1/4).
\]

They have equal Green determinants:

\[
\det K_A=
\det K_B=rac58.
\]

But their skew Pfaffians differ:

\[
\operatorname{Pf}M_A=rac18,
\qquad
\operatorname{Pf}M_B=rac1{12}.
\]

Both still satisfy the internal identity

\[
\det M=(\operatorname{Pf}M)^2.
\]

The failure is not Pfaffian inconsistency. It is loss of ordered parity data when passing to the positive Green determinant.

## Consequence for the graded/pro target

The scalar Green determinant cocycle cannot supply the Pfaffian line by choosing a square root. The two determinants belong to different matrix families:

```text
Green Gram determinant
  records every gap through 1-rho_i^2

skew Pfaffian torsion
  records even-position gaps through rho_(2i)
```

A full target must carry both:

- the positive determinant/innovation line of the Green realization;
- the oriented parity-sensitive Pfaffian line of the skew sewing theory.

Any comparison between them requires additional ordered constructor data and cannot be inferred from determinant magnitude.

## Refinement implication

Swapping adjacent gap labels leaves the Green determinant unchanged but can change Pfaffian torsion. Thus determinant-line transition coherence does not settle Pfaffian-line coherence. The latter must be transported along the ordered metric word itself.

This keeps the next Agda task sharply typed: prove the full skew-chain Pfaffian recurrence from ordered gaps, rather than attempting to extract it from the already formalized Green Gram determinant.

## Verification

```text
python research/coherence/check_green_determinant_vs_skew_pfaffian_hostile.py
```

Artifacts:

- `check_green_determinant_vs_skew_pfaffian_hostile.py`
- `green-determinant-vs-skew-pfaffian-hostile.v1.json`
