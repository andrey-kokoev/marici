---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The First Soft-Total Blowup Has No Unclassified Fitting Direction

## Record

Status: first exceptional-direction census following Entry 418.

## Hard-to-vary claim

After blowing up the joint ideal \((E,X_2)\), an additional rank-jump
direction might occur away from the strict transforms of the frozen energy
arrangement. Such a direction would be residual coefficient support and
would prevent attributing the exact-center collapse solely to known
total-energy/soft support.

## Frozen chart

In the patch \(X_1=1\), use
\[
E=t,\qquad X_2=ct,\qquad v=2-t+2ct.
\]
The soft axis \(c=0\) and the algebraic-divisor intersections
\(t=\pm c\) were excluded before calculation. No carrier factors were added
after observing the result.

## Result

At exact-form degrees 8 and 10, 222 punctured points were tested over eleven
slopes and eleven radial samples. Of these:

- 182 have the generic gauge rank two;
- 22 rank-jump samples lie on the frozen signed-energy divisor
  \(E-X_2=0\), equivalently \(c=1\);
- 20 rank-jump samples lie on the frozen energy divisor \(2-E=0\),
  equivalently \(t=2\);
- two samples lie on both and are counted in both preceding totals;
- zero rank-jump samples remain unclassified.

Therefore
\[
\boxed{
\text{the sampled first blow-up carries no rank support outside the frozen
energy arrangement.}
}
\]

## Interpretation

Entry 418's full collapse at the raw center does not emit a new sampled
direction on the first exceptional divisor. Every observed punctured
rank jump is inherited from an existing energy letter. This strengthens the
classification of the center pathology as supported presentation torsion
rather than a new cosmological carrier incidence.

## Epistemic boundary

This is a finite-field direction census, not the local two-variable Fitting
module. It does not determine torsion length and cannot exclude support that
appears only after a further blow-up or at an unsampled exceptional point.
The result is stable across exact-form degrees 8 and 10.

## Classification

- carrier: unchanged energy/Cut carrier;
- inherited exceptional support: \(E-X_2=0\) and \(2-E=0\);
- residual sampled first-blow-up support: none;
- new carrier datum: none.

## Next falsifier

Construct the presentation over a truncated local ring at
\((E,X_2)=(0,0)\). Compute its determinantal valuations or Smith data along
generic and exceptional arcs, saturate by the frozen energy factors, and
measure the residual kernel/cokernel length. A residual associated direction
after that saturation would be new coefficient support, not automatically a
new carrier cell.

## Evidence

- research/benincasa/dlog-joint-blowup-direction-certificate.json
- research/benincasa/marici-gm/src/bin/marked_tangency_support.rs
