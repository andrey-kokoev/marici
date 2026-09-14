# Erratum: the recent conductor pairings do not yet compute (a,b)

The claimed value

\[
(a,b)=(1,0)
\]

must be withdrawn.

## Why the e6 argument is not yet typed

The coefficient

\[
\tau\mapsto-\frac12e_6
\]

comes from the soft-node center \((u,v)=(2,0)\). Its own source packet explicitly states “no global Betti normalization claim.” The paired total-energy infinity nodes have now been globally oriented, but no integral transport map has been constructed from this soft center to the generic marked total-energy extension.

Consequently the primitive component-difference interpretation is a candidate normalization, not yet a proved identification with the ordered integral source generator \(e_6\).

## Why the v_alg argument computes the wrong block

The exact rank-nine total-energy residue states

\[
\operatorname{Res}_{E=0}(e_6)=0
\]

and that the nilpotent has zero algebraic-kernel component along \(v_{\rm alg}\). It identifies the remaining problem as

> the off-diagonal marked top-column residue in the canonical rank-twelve localization extension.

The conductor calculation using

\[
\omega_v=\frac{N_v\,da}{\partial_bQ}
\]

is a valid residue calculation for the algebraic form, but it has not been shown to equal that missing marked top-column pairing. Its value \(-4\) therefore does not prove \(b=0\).

## Correct status

Neither proposed bit is presently established. All four numerical classes remain open:

\[
(a,b)\in\{(0,0),(1,0),(0,1),(1,1)\}.
\]

The new geometry remains valuable and exact:

- the full double-conic central fiber;
- the global smoothing square root \(g(m)\);
- the four width-two marks;
- the Bunch--Davies oriented Cech half-boundary;
- the opposite-point geometric matching.

What is missing is no longer vague. One must specialize the **marked rank-twelve top relative generator** along that explicit Cech chain. Its resulting algebraic column can then be paired with integral duals to \(e_6\) and \(v_{\rm alg}\).

Certificate:

- `research/voevodsky/checkers/audit_claimed_direct_parity_pairings.py`;
- `research/voevodsky/results/claimed_direct_parity_pairings_audit.json`.
