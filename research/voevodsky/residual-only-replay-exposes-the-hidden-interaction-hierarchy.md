# Residual-only replay exposes the hidden interaction hierarchy

## What changed from the archive experiment

The earlier replay kept the original source in a capsule. That verified handoff discipline, not our understanding of what was missing.

This experiment keeps NO original source capsule. At each reduction it extracts just the missing linear coordinates and serializes them as a typed residual. The decoder receives only the final terminal value, those residual bundles and the fixed source-model metadata.

Exact reconstruction succeeds. More importantly, the coordinates explain the loss.

## 1. The smallest cubic source model

Take three consecutive forgotten diamonds, on (2,3), (5,7), (11,13), at background two. Each block has two paths:

    P = its sorted path,
    Q = its reversed path,
    H = Q-P.

The eight block-concatenated paths span an eight-dimensional source slice. Write a_b for the coefficient of the path whose reversed blocks form the bit set b.

Define, for each subset T of the three blocks,

    m_T = sum_(b contains T) a_b.

These are signed linear interaction coordinates, not probabilities. They are actual ordered Fox records: select the first Q seam in every block in T and leave all other buffers forgotten. The corresponding |T|-cut coefficient is exactly m_T.

Equivalently, expand the source in the basis having H in blocks T and P elsewhere. Its coefficient in that basis is m_T. This identifies the residuals with actual products of source relations, not arbitrary extra storage fields.

## 2. The hierarchy that the records see

The complete forgotten record maps on this slice have ranks:

| Cut order | Rank | Coordinates needed |
|---|---:|---|
| 0, terminal | 1 | total coefficient |
| 1 | 4 | total plus three single-block interactions |
| 2 | 7 | those plus three pair interactions |
| 3 | 8 | those plus the triple interaction |

Thus reducing order 3->2->1->0 loses respectively 1, 3 and 3 independent coordinates. The replay retains exactly those dimensions as residual bundles.

This is minimal among linear residual encodings on this fixed slice, by rank deficiency. There is no reduction in total information dimension: terminal plus residuals has 1+3+3+1=8 coordinates. The gain is a structured explanation of what each view omits, not magical lossless compression.

Deleting any residual order leaves a nonzero H-product indistinguishable from zero in all remaining coordinates.

## 3. Exact reconstruction without the original input

Inclusion-exclusion gives

    a_b = sum_(T contains b) (-1)^(|T|-|b|) m_T.

The decoder implements this formula using only the received bundles. Every handoff is serialized through JSON, and missing bundles are rejected rather than silently filled with zero.

Checks cover all eight path basis vectors, all eight interaction basis vectors and a mixed rational source: 17 sources, 51 reduction handoffs. Basis checks plus linearity establish reconstruction throughout this finite rational slice.

The source ideal filtration is also identified, not guessed from labels. An interaction involving |T| copies of H belongs to I^|T|. Its first nonzero selected Fox coefficient occurs at that order. Using D_k(I^r)=0 for k<r gives the exact intersections with the slice:

    dimensions of V, V intersect I, V intersect I^2,
    V intersect I^3, V intersect I^4 = (8,7,4,1,0).

This does not assert that the full filtered source extension splits as a source bimodule.

## 4. The residuals affect future behavior

Compatible block concatenation multiplies interaction modes by joining their block labels; ideal orders add. Twenty exact basis-product checks verify this against actual marked-path multiplication. Bilinearity extends these checks to the corresponding packet spans.

A particularly simple prediction test starts with P and Q in the first diamond. They have identical terminal records. Multiply each by the last two forgotten diamond relations and apply the existing cubic vacuum row:

    prediction from P = 1,
    prediction from Q = 0.

Therefore the omitted initial distinction is not merely an archival detail. It changes a later source-dependent prediction. No function of the initial terminal record alone can supply both correct answers.

The action checks cover the stated compatible forgotten-block concatenations, not every action of the complete marked source algebra.

## 5. What the vacuum row really recovers

The owning vacuum row selects the all-P path. Its value is

    v = a_empty
      = m_empty - sum_(|T|=1) m_T
                  + sum_(|T|=2) m_T - m_{123}.

If all lower-order moments have been retained, this determines the last missing interaction:

    m_{123} = m_empty - sum singles + sum pairs - v.

On the pure cubic k=(P-Q)(P-Q)(P-Q), every lower-order moment is zero, m_{123}=-1, and v=1. This is the familiar invisible cubic witness.

But for a general source in the same eight-path slice, the vacuum reading is a combination of ALL interaction orders. It does not by itself identify the triple-interaction coefficient.

Terminal plus vacuum has rank only two, leaving six source directions undetermined. This six is NOT the previously computed six-dimensional acquisition kernel; the objects and comparison maps are different.

Crucially, the rank-seven order-two record here is the FULL forgotten Fox record on this slice. It is not the previously selected O_2 or the 449 retained-degree-two receiver. Those selected detectors do not automatically provide these seven coordinates. The condition needed to recover the top residual must therefore be checked, never assumed.

## Understanding gained

The retention requirement is not just “save something hidden.” It is:

1. identify which independent source interactions the current view omits;
2. preserve their actual coefficients and typed location;
3. propagate them under the admitted source actions;
4. distinguish a new measurement of a mixture from recovery of an individual missing component.

The vacuum row detects the cubic witness because that witness has no lower-order interactions. That successful witness test alone does not make vacuum acquisition an inverse for arbitrary source loss.

## Reproduction

    python research/voevodsky/checkers/check_diamond_cube_residual_retention.py

Artifacts:

- `results/diamond-cube-residual-retention.json`
- `results/diamond-cube-residual-envelope.json`

All checks pass. This is an exact finite source calculation, not a numerical receiver deployment, noisy inverse theorem, or completed-source reconstruction result.
