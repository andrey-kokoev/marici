# `q_G12` positive-chamber branch-selection audit

## Question

Does the literal positive source chamber uniquely select the cyclic `sqrt(K)` branch and its conductor normalization?

## Result

No. Positivity of the base variables does not select a point of the square-root double cover.

The frozen positive-chain census states

\[
a,b,c\ge0,\qquad X_1,X_2,X_3>0,
\]

and proves that the ten source pole hyperplanes and generic nonsoft collision strata do not intersect that chain. This controls marked-pole activation. It does not declare a sign or phase of `sqrt(K)`.

Even on a connected region where `K>0`, both `+sqrt(K)` and `-sqrt(K)` are real analytic sheets. Choosing “the positive chain” specifies a base region, not a lift of that region to the double cover. One still needs a basepoint sheet, an oriented geometric-volume convention, or a source contour normalization.

The cyclic log-smoothness artifact explicitly retains all twelve signed Cayley–Menger face branches. The only frozen “chosen positive sheet” statement occurs in a specific `X1` soft strict-transform chart and fixes a local leading measure ratio there. It neither supplies a generic nonsoft basepoint nor transports a branch through the three two-site charts.

## Cyclic implication

Because the sourced three-cycle preserves `K` and the positive inequalities, any chosen branch can be transported cyclically without changing the base variables’ positivity. But the globally sign-reversed branch is equally compatible with those data. Thus positive-chamber invariance reduces the branch choices to a common global sign only if one additionally proves connected branch-free transport paths; it does not select that sign.

The frozen artifacts also do not prove that the required paths avoid all conductor and `K=0` loci, so even the reduction to one global sign remains conditional.

## Strongest falsification attempt

Define `sqrt(K)` as the positive real square root wherever `K>0`. This is a valid extra convention, but no cited source artifact declares it as the normalization of the physical measure in the generic nonsoft three-chart problem. Replacing it by the negative root preserves every polynomial identity and positive-chain inequality while reversing all normalized wall forms.

## First missing datum

The first missing datum is a source-authorized lifted basepoint

\[
(x_0,\sqrt{K(x_0)})
\]

in a declared nonsoft chamber, followed by explicit paths to all three charts and proof that they avoid branch/conductor support. The path lifts determine the transition signs; the measure normalization must then fix the remaining global sign.

## Acceptance test

1. declare the basepoint and root value;
2. certify connected paths and nonvanishing of `K` along them;
3. transport the root through the sourced three-cycle;
4. verify three-cycle closure and conductor finite-part equality;
5. reverse the basepoint sign as a deliberate global-normalization failure.

## Disposition

The positive chamber does not select the analytic branch. It supplies a cyclic-invariant base domain only. A lifted basepoint, source path, and measure normalization remain necessary.

## Evidence

- `research/benincasa/generic_lower_positive_chain_census_result.json`
- `research/benincasa/check_cyclic_q_log_smoothness.rs`
- `research/benincasa/x1-soft-physical-strict-transform.json`
- `research/nima/qG12-cyclic-reduced-factor-transport.md`
