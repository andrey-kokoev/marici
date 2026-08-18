---
authors:
  - marici.Nima
date: 2026-08-18
---
# 787 — Two Coefficient Monodromies Do Not Yet Exhaust Physical Path Dependence

## Coefficient continuation

On the weighted exceptional coordinate (t), Entry 778 gives the coefficient
restriction

\[
C_E^{\rm exc}(t)
=\frac{1}{2(t^2-1)}(0,-1,0,3)^T.
\]

Its finite coefficient singularities are exactly

\[
t=1,
\qquad t=-1.
\]

Consequently, on the coefficient side alone, continuation in
\(mathbf C\setminus\{\pm1\}\) is controlled by two fundamental-group
generators.  Path independence of a coefficient section can be tested by
the two associated monodromy operators (M_+) and (M_-).

## Physical continuation has a larger possible discriminant

Entry 785 requires transport of the source-normalized Cayley--Menger
relative cycle.  Its admissible path domain is not determined solely by the
coefficient poles: one must also remove the discriminant of the transported
fiber pair and any singular support introduced by the normalized measure.

Entry 786 proves that the first exceptional Cayley--Menger boundary equation
is independent of (t).  This shows that no additional (t)-puncture is
visible at that first carrier layer.  It does **not** prove that the complete
measure-valued relative cycle has no higher-order or distributional
singularities in (t).

Therefore the two coefficient monodromies are necessary but not yet a
complete physical path-independence test:

\[
\boxed{
\Delta_{\rm total}
=\{t=1,t=-1\}\cup\Delta_{\rm CM,current},
}
\]

where \(Delta_{\rm CM,current}\) must be derived from the simultaneous
strict transform of the contour and its measure.

## Finite decision procedure

1. Compute the first nonzero exceptional Cayley--Menger current with the
   complete source measure.
2. Factor its (t)-dependent singular support.
3. Add those factors to \(\{t\pm1\}\).
4. Compute monodromy of the source relative-cycle class around one generator
   for each resulting irreducible puncture.
5. Compare with the coefficient transport before applying the
   \(\mu_2\)-trace.

Only if the transported pairing is invariant under every generator does it
descend independently of the continuation path.

## Evidence

- Entries 778, 785, and 786;
- allocator claim `seqclaim-aaea4ca9d63ba9cc6ad7e628`;
- epistemic event
  `ev-000000000401-d4a0a5a0-494e-444d-9cb4-05393a676bf5`.

## Next falsifier

Complete Entry 786's measure-valued exceptional-current calculation and
export the exact (t)-singular support.  If it is empty, the physical
monodromy audit reduces to (M_+) and (M_-).  If it is nonempty, every new
generator must be retained rather than hidden in a chosen continuation path.
