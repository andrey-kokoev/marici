# 2708 — The Finite Rank-Twenty-Six Adapter Fails the Differentiated Euler Test

## Frozen test

Entry 2701 fixes the canonical coefficient derivative of the unspecialized source. Test whether the finite de Rham adapter preserves the differentiated Euler relation

\[
x\nabla_jD_0+y\nabla_jD_1+z\nabla_jD_2=27D_j,
\qquad j=0,1,2.
\]

Each covariant derivative is constructed from both required terms:

1. an exact seven-node interpolation derivative of the parameter-dependent raw $D_i$ coefficients;
2. the finite Gauss--Manin connection image of $D_i$.

Only afterward is the defect reduced by the complete finite presentation.

## Result at ambient degree 14

At the reference point and two independent controls, every direction fails. The reduced defect supports are identical at all three points:

\[
(32,32,39).
\]

Thus all nine point-direction identities fail with a stable pattern.

## Truncation falsifier

The reference-point computation was repeated after raising the ambient relation degree from (14) to (16). The reduced supports remained exactly

\[
(32,32,39).
\]

The defect therefore survives the declared ambient enlargement.

## Narrow conclusion

The source identity and its canonical derivative remain valid. What fails is their transport through the current finite Gauss--Manin adapter at second-jet level.

This does not disprove the rank-26 coefficient system or the existence of a physical Leray covector. It withdraws the stronger claim that the present finite adapter already computes the complete differentiated source connection.

No correction cell is added after observing the defect.

## Artifacts

- `research/benincasa/check_rank26_differentiated_euler_quotient.py`
- `research/benincasa/rank26-differentiated-euler-quotient-ambient-14-three-points.json`
- `research/benincasa/rank26-differentiated-euler-quotient-ambient-16-reference.json`

## Next falsifier

Decompose the stable defect by labelled pole level, (K)-depth, and numerator degree. Determine the first omitted source-derived relation or derivative term. If no omitted term exists, retire this finite presentation as a model of the second-jet Gauss--Manin connection.
