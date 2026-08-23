# The canonical conditional adjacent block fails on the first asymmetric label orbit

After the pointwise shift failed, the next predeclared mechanism was the whole
conditional two-band block

\[
 \mathcal B_{nm}(a,b)=\int_0^{\pi/b}
 [H_{nm}(D)+H_{nm}(D+\pi/b)]\,dD.                     \tag{1}
\]

Labels are regrouped only by the source-mandated exchange orbit
`(n,m)<->(m,n)`. No other cross-label cancellation is allowed in this test.

## Hostile result

A direct quadrature at `a=1`, `b=8` gives stable signs under mesh refinement:

\[
 \mathcal B_{11}>0,
 \qquad
 \mathcal B_{12}+\mathcal B_{21}<0.
\]

Thus the dominant diagonal label can hide failure of the first asymmetric
label orbit in the scalar sum. This is precisely why the scalar quadrant
readout cannot identify a unique cancellation transport.

The current computation is convergence-tested floating-point reconnaissance,
not an interval certificate. It strongly falsifies the proposed label-orbit
block mechanism and supplies a small target for rigorous enclosure.

## Large-frequency expansion and retraction

For an exchange orbit, write `W(D)` and `J(D)` for the orbit sums. They are
even. With `L=pi/b`, Taylor expansion of the fixed block as `b` tends to
infinity gives

\[
 \boxed{
 \mathcal B(a,b)
 =\frac{4\pi}{b^2}\,[J''(0)-aW(0)]+O(b^{-4}).}          \tag{2}
\]

The cosine part contributes `4 pi J''(0)/b^2`; the sine part contributes
`-4 pi a W(0)/b^2`. This initially suggested testing

\[
 J''_{12+21}(0)-aW_{12+21}(0)<0                         \tag{3}
\]

as a persistent large-frequency obstruction. Higher-resolution finite
differences instead give a positive diagnostic value near `2.52e-4` at `a=1`
for the `{12,21}` orbit. The proposed negative large-`b` obstruction is
therefore **retracted**. Equation (2) predicts eventual recovery of the block
sign; the negative value at `b=8` is a finite-frequency interaction involving
higher terms.

This correction does not remove the stable `b=8` hostile result. It changes
the rigorous next step: interval-enclose that finite block, including the
moving folded-label cusps, rather than trying to certify the false sign (3).

Those moving cusps have now been removed exactly. The whole block equals the
original labelled integral over `0<=U-V<=2pi/b`; splitting by the signs of
`U,V` gives three positive-coordinate charts with unit Jacobian. See
`theta-adjacent-block-three-chart-reduction.md`. A directed quadrature can now
work on two rectangles and one triangle without interval absolute values.

## Classification

The following mechanisms are now falsified or strongly falsified in order:

1. fixed-label, fixed-`S` pointwise adjacent transport: exactly falsified;
2. conditionally integrated pointwise residual: boundary failure on the
   exchange orbit;
3. whole adjacent two-band block within each exchange orbit: negative hostile
   diagnostic at finite frequency; its initially proposed negative
   large-frequency obstruction is retracted.

What remains admissible is a canonical transport across different label
orbits, a larger source-declared block, or a different source-derived order.
None may be inferred solely from positivity of the final scalar expectation.
This does not falsify the Pick inequality and does not prove or disprove RH.

## Durable verification

- Diagnostic: `checkers/theta_conditional_adjacent_block_falsifier.py`
- Result: `results/theta-conditional-adjacent-block-falsifier.json`
> **Update.** A source-reflection-paired directed-binary64 enclosure at
> \((a,b)=(1,11)\) now separates the exchange-orbit block strictly below zero;
> see `theta-adjacent-block-directed-box-certificate.md`.  It remains
> deliberately non-formal until certified transcendental rounding, exact
> \(\pi\) endpoints, and the analytic tail estimate are closed.
