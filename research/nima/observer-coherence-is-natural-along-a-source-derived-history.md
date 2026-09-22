# Observer coherence is natural along a source-derived history

## Result

There is now a history-indexed coherence check anchored to the actual seven-reading decoder, rather than only to arbitrary invertible coordinates.

On the declared finite history, observer comparisons and their composed routes commute with transport to earlier source stages. Pulling a later physical-row constraint backward through any of the tested observer routes produces the same correlated history fiber.

All checks pass. This is an exact synthetic source history, not a claim that a physical acquisition history has been supplied or verified.

## 1. The historical carriers and their actions

Use the ordered forgotten blocks `(2,3)`, `(5,7)`, `(11,13)` at background two. Write P and Q for the two orders and set H=P-Q.

The three admitted carriers are:

| Stage | Source carrier | Dimension |
|---|---|---:|
| 0 | first-block P/Q span | 2 |
| 1 | two-block P/Q span | 4 |
| 2 | the seven-dimensional three-block ideal slice | 7 |

The prescribed history arrows append H in the next block. Their matrices are verified against actual marked-path multiplication.

These are ambient stage carriers, not claims that fixed multiplication creates independent source information. A compatible history must satisfy

`x1=T10*x0`, `u2=T21*x1`.

The joint history therefore retains correlations between stages. An arbitrary stage-two ideal element need not be reachable through this particular history.

## 2. The observation anchor is a specified reading contract

The final seven readings are those in

`../voevodsky/seven-labelled-readings-reconstruct-the-entire-forgotten-ideal-slice.md`.

Their 7-by-8 matrix R is independently rebuilt from the actual ordered-cut recorder. If D is the published decoder matrix, the checks include

`R D = identity`.

The reading model digest, source-coordinate conventions, transition matrices, labels, normalizations and exact-synthetic uncertainty contract are recorded in the history model.

The moment jets are derived from the reconstructed ideal element. Their dimensions at orders one, two and three are 3, 6 and 7. Order zero is identically zero on the final ideal slice.

At each order, four invertible, filtration-compatible coordinate realizations provide observer comparisons. They are presentations of these full finite jets, not replacements for the historical nonsplit scalar-observer enrichments.

## 3. Naturality with respect to earlier realizations

Let B[h,m,i] map a stage-h source to the order-m future observation in observer realization i. These are predictions of the specified final experiment, not claims that its readings were already acquired at stage h.

For history transport T from h to k, observer comparison F from i to j, and jet truncation P, the checker verifies

`B[k,m,i] T = B[h,m,i]`,

`F B[h,m,i] = B[h,m,j]`,

and the mixed square

`P F B[k,m,i] T = B[h,q,j]`.

Composed observer routes also satisfy these equations. Thus the compatibility of observer comparisons is itself natural along the source history. This is the requested coherence between observer coherence and past realizations, on the stated model.

There are 4,608 higher-route checks, alongside 576 mixed depth/history squares and the source and observer naturality squares.

## 4. History depth shifts the effective observation order

The calculation identifies a concrete interaction between the two depth directions. Each prescribed future ideal factor consumes one derivative cut.

At historical stage h=0 or 1, an order-m final jet sees only order

`m-(2-h)`

of the earlier packet. Negative effective order gives zero.

The resulting ranks on the admitted stage carriers are:

| Earlier stage | Final jet order 1 | Order 2 | Order 3 |
|---|---:|---:|---:|
| 0 | 0 | 1 | 2 |
| 1 | 1 | 3 | 4 |
| 2, ideal carrier | 3 | 6 | 7 |

The checker verifies the coordinate formula underlying this table, not merely its ranks. It is a concrete instance of the source-product derivative law: the future ideal factors use cuts before the observer can resolve earlier interactions.

## 5. A later reading refines the past without rewriting it

Retain the initial terminal fact

`a_P+a_Q=1`.

Append H twice. The final canonical vacuum reading is `a_P`. If the later reading is one, then the compatible initial source is P:

`a_P=1`, `a_Q=0`.

The full 13-coordinate history system, including all transition equations, initially has a one-dimensional affine fiber after imposing the terminal fact. The later reading reduces it to a point.

The checker pulls this same physical vacuum constraint through different observer presentations and back to all three stages. All 192 resulting affine-history comparisons agree. These are complete rational affine fibers, not a finite enumeration of possible histories.

The old terminal record remains unchanged. A later contradictory vacuum value makes the history fiber empty; it does not authorize overwriting the old reading or its metadata.

## 6. Why a coarse observer cannot perform the same retrodiction

The two initial sources P and Q have the same terminal reading. After appending the two ideal factors, their difference is the cubic forgotten relation.

Every final jet of order at most two misses this difference, but the canonical vacuum row distinguishes it. The checker verifies that no covector on the depth-two carrier can represent this vacuum constraint.

Therefore observer coherence does not conjure the missing past distinction from coarse observations. The later reading must be acquired, supplied as exact symbolic data, or justified independently. No inverse or coherence witness can replace that requirement.

## 7. Retention and scope

The synthetic ledger keeps acquisition labels, stages, model bindings, normalization and uncertainty alongside values. Fixture mutation tests reject changes to those historical fields. This is a pinned-example integrity check, not a general archival validator or authentication service.

Both source support and the prescribed dynamics remain assumptions requiring independent justification for a physical application. Seven-reading consistency cannot establish either. No noisy observation model is admitted here.

This closes a finite history-naturality test. It does not classify every past realization, transport all marked-source actions, or solve the actual nonsplit observer tower's comparison problem.

## Verification

`python research/nima/checkers/check_history_indexed_observer_coherence.py`

Artifact:

`research/nima/results/history-indexed-observer-coherence.json`

The artifact includes the reading anchors, history transitions, observer anchors, rank table, immutable synthetic evidence example and the refined correlated history.
