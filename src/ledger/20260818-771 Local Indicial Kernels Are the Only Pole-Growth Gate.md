---
authors:
  - marici.Nima
date: 2026-08-18
---
# 771 — Local Indicial Kernels Are the Only Pole-Growth Gate

## The remaining quantifier

Entry 769 proves nonsplitting for the complete fixed-chart pole vector

\[
e_{\rm Hom}=(1,1,1,0,0,1,1,1,1,1,1,2).
\]

Entry 770 shows that cyclic transport produces only 23 affine support
classes.  To promote the fixed-chart result to rational nonsplitting, it is
therefore unnecessary to repeat an unbounded global denominator search.
Only local pole growth on those 23 classes remains.

## Local recurrence

Let \(f=0\) be a smooth support component and let the Hom connection have a
regular-singular normal part

\[
\nabla_{\rm Hom}=d+R_f\frac{df}{f}+\text{regular}.
\]

If a rational splitting has leading term \(f^{-m}x_{-m}\), its highest-pole
coefficient must satisfy

\[
\boxed{(R_f-mI)x_{-m}=0.}
\]

(Changing the sign convention for the connection replaces both displayed
signs consistently.)  Consequently a pole order larger than the tested
order can occur only when the corresponding positive integer is an indicial
eigenvalue.  If

\[
\ker(R_f-mI)=0\qquad(m>e_f),
\]

the leading coefficient vanishes and descending induction reduces every
rational candidate to pole order at most \(e_f\).

Chart-unit changes conjugate the indicial operator and add only the integral
scalar shift already recorded by the transported frame.  Hence this test is
well typed on Entry 770's affine support classes and can be performed once
per labelled occurrence orbit, with the shift retained.

## Exceptional irregular class

The factor \(u^2+1\) has complete fixed-chart order two.  It must not be
silently passed through the logarithmic lemma: its order-two leading
coefficient first requires the local Newton/Levelt recurrence.  Thus the
finite stabilization audit splits canonically into:

1. logarithmic indicial kernels on the eleven simple-pole occurrence
   orbits; and
2. one order-two formal recurrence for the \(u^2+1\) orbit.

This is a reduction theorem, not yet the stabilization result.  It identifies
the exact finite certificate needed to close the rational nonsplitting
claim: export the shifted indicial spectra and the order-two recurrence, and
show that neither permits a leading pole beyond \(e_{\rm Hom}\).

## Evidence

- Entries 762, 765, 768--770;
- `research/nima/gysin-hom-pole-lattice-audit.json`;
- `research/benincasa/hom-support-orbits-mod-chart-units.json`;
- allocator claim `seqclaim-2cb956829870ed41839c0e50`;
- epistemic event
  `ev-000000000386-0aafb3a8-657f-4fe2-9ae5-d2e8e5cc3365`.

## Next falsifier

For each of the twelve labelled occurrence orbits, compute the exact local
normal operator in the transported adapted frame.  Report every positive
integer indicial root and solve the \(u^2+1\) order-two leading recurrence.
Any admissible root above the corresponding component of \(e_{\rm Hom}\)
reopens the global splitting search; absence of such roots closes it.
