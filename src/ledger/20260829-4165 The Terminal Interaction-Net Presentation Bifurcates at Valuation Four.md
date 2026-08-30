# 4165 — The Terminal Interaction-Net Presentation Bifurcates at Valuation Four

## Claim under test

Entry 4160 required a terminal mixed-Rees presentation before fitting another equality-costalk coordinate. The first finite gate is whether the source-derived two-adic elimination admits one fixed pivot chart through the grade where the terminal classes attach.

## Frozen computation

The source-fixed structural presentation was unchanged:

- matrix size $14422\times2278$;
- fixed denominator $2$ on every de Rham row;
- multiplication rows retain source units;
- $K$-depth $3$;
- labelled denominator depth $2$;
- ambient degree $14$.

The same sparse elimination algorithm was applied at the equality-locus points $(3,3,7)$ and $(3,3,9)$. These points have different terminal Smith valuations, respectively $(8,22)$ and $(8,12)$.

## Common pre-bifurcation object

After valuations $0,1,2,3$, both fibers have:

- cumulative detected rank $2190$;
- exactly $156$ residual rows;
- exactly $56$ active original columns;
- identical cumulative pivot schedule;
- identical labelled active-column support.

Thus the post-valuation-$3$ object is a common rank-four terminal presentation. It is the latest fiberwise reduction stage that can be lifted without choosing a kinematic pivot chart.

## Valuation-four bifurcation

Both fibers add rank two at valuation $4$, but only one pivot is common:

| role | original column | source label |
|---|---:|---|
| common pivot | 2178 | `[3,2,2,2,2,2,[1,5]]` |
| $(3,3,7)$-only pivot | 1947 | `[3,2,1,1,1,1,[14,0]]` |
| $(3,3,9)$-only pivot | 2224 | `[3,2,2,2,2,2,[5,1]]` |

The resulting tails are not the same presentation:

| point | residual rows | active columns |
|---|---:|---:|
| $(3,3,7)$ | 155 | 55 |
| $(3,3,9)$ | 143 | 42 |

The $(3,3,9)$ active support is a strict subset of the $(3,3,7)$ support. Therefore the divergence is not merely a different numerical value on a fixed two-generator matrix; the specialized elimination itself changes chart at valuation $4$.

## Narrow conclusion

There is no single fixed pivot schedule through valuation $4$ on the tested equality locus.

The source-derived object to lift is the common $156\times56$ post-valuation-$3$ presentation. The valuation-$4$ pivot exchange is evidence for an atlas of terminal reduction charts, not evidence for either pivot label as a preferred equality coordinate.

This sharpens Entry 4160: the varying fifth-order attachment is encoded in the determinantal geometry of the common rank-four tail. It is not readable from one specialized Smith basis.

## Next falsifier

Lift the common $156\times56$ tail over the unspecialized local parameter ring while retaining its original column labels. Compute the rank-two valuation-$4$ determinantal ideal before choosing either pivot chart.

Accept a terminal coordinate only if a source-derived Fitting generator or invariant ideal controls both specialized charts and reproduces the observed terminal valuations. A coordinate obtained from either column 1947 or column 2224 alone is inadmissible.
