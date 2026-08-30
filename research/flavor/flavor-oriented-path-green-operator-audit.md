# Oriented-Path Green Operator Audit

## Question

Can a source Green operation force the complete polynomial (I+F+F^2)
which WP863 found to be coefficient-underdetermined?

## Claim boundary

Let (F) be the normalized oriented length-three path shift derived in the
WP852--WP854 chain, so (F^3=0).  If the source kinetic operation is exactly
the oriented discrete derivative

\[
K=I-F,
\]

then the Green equation (KG=GK=I), with (G) in the marked path algebra,
has the unique solution

\[
G=I+F+F^2.
\]

This is stronger than choosing a geometric sum: the unit coefficient of every
allowed path is forced by an executable algebraic equation.  A bipartite
Gaussian mediator with off-diagonal kinetic block (K) realizes the same
inverse through exact Schur elimination.  Conditional on that source action,
the WP863 completion coefficient is no longer free.

The inverse does not itself derive its kinetic input.  The most general marked
three-step kinetic operator with a direct two-step term is

\[
K_{\rho,\delta}=I-\rho F-\delta F^2,
\]

and exact inversion gives

\[
K_{\rho,\delta}^{-1}
=I+\rho F+(\rho^2+\delta)F^2.
\]

Thus strict nearest-neighbour locality removes (delta), while the normalized
unitary transport law must separately fix (|\rho|=1).  The sign is not fixed
by the unreferenced path algebra: with (U=\operatorname{diag}(1,-1,1)),

\[
UFU^\dagger=-F,
\qquad
U(I-F)U^\dagger=I+F.
\]

Only a retained boundary/reference port reduces the groupoid enough to make
this relative sign observable.  It creates the relational experiment already
typed in WP855 and WP859; it does not reveal an absolute sign.

## End-to-end gate audit

- Asymmetry: the marked oriented boundary makes (F) and the boundary
  difference unavoidable, conditional on the oriented-cycle source.
- Magnitude: partial-isometry normalization fixes unit path transport only if
  the kinetic identity and hopping share the source normalization.  A free
  (ho) otherwise remains.
- Sign: fixed only relative to the retained boundary reference; without that
  port, the two signs are conjugate presentations.
- RG basin: the positive Kirchhoff lowering generator of WP859 has the global
  basin and gap, but no theorem yet identifies that generator with the
  Gaussian mediator's renormalization law.
- Threshold survival: WP860 still requires the marked path projector to be a
  reducing subspace of the complete threshold interaction algebra.
- Physical readout: the lossless complementary difference port is a
  source-level readout, but its calibrated map into `physical16` remains
  absent.

## Smallest exact falsifiers

The magnitude falsifier is (K_\rho=I-\rho F) with (ho\ne1).  It preserves
strict nearest-neighbour locality and nilpotence while changing the Green
operator.  The locality falsifier is a nonzero (delta F^2).  The sign
falsifier is the exact conjugacy between (I-F) and (I+F) when no reference
port is retained.

## Disposition

Progressive conditional theorem, not yet the requested complete source
principle.  Green inversion repairs WP863's arbitrary (F^2) coefficient if
the source independently supplies the normalized oriented derivative
(I-F).  The remaining problem is now localized: derive that derivative,
the Kirchhoff basin, the reducing threshold projector, and the calibrated
readout as interfaces of one microscopic source rather than combining four
compatible packets.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp864_oriented_path_green_operator_audit.py
```
