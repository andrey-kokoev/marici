# Flux-Wilson doublet flag gate: WP1085

## Question

Can a flux Wilson line conditionally split WP1084's residual \(SU(2)\)
doublet into two ordered lines?

## Conditional split

A source-fixed generic \(SU(2)\) Wilson line

\[
W\sim \operatorname{diag}(e^{i\theta},e^{-i\theta})
\]

has two one-dimensional eigenspaces. For generic \(\theta\), its centralizer
is \(U(1)\), and the WP1084 \(B\)-triplet branching refines from

\[
3_B=2_B+1_B
\]

to

\[
3_B=1_{+\theta}+1_{-\theta}+1_0.
\]

This would give three lines and could supply the \(1+1+1\) eigenflag sought by
WP1083–WP1084.

## Source-supply audit

WP1072's unit-clock flux datum is only

\[
B/A=6n^2.
\]

It selects a flux integer sector, but does not select:

- a Wilson phase \(\theta\);
- an eigenbasis direction inside \(SU(2)\);
- an ordering or charge convention distinguishing \(+\theta\) from
  \(-\theta\);
- a cyclic ray;
- a nondestructive history dilation.

A trivial Wilson line leaves \(SU(2)\) unbroken. A generic Wilson line is
therefore a new source boundary condition, not a consequence of the admitted
flux integer.

## Classification

Conditional constructor, not a constructed selector. A source-fixed generic
Wilson line would split \(2+1\) into \(1+1+1\), but the current source does
not authorize it.

The remaining gate is to derive the Wilson-line boundary condition and charge
ordering from the UV/source packet, then test whether it selects a cyclic ray
and retains history. The integer flux sector must not be promoted into any of
those data.

Checker: `research/flavor/checkers/wp1085_flux_wilson_doublet_flag_gate.py`

Result: `results/wp1085_flux_wilson_doublet_flag_gate.json`
