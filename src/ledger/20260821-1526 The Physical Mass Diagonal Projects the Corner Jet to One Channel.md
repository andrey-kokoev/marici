---
author: marici.Nima
---

# 1526 — The Physical Mass Diagonal Projects the Corner Jet to One Channel

## Status

Closed all-grade specialization of Entry 1525 to equal adjacent edge energy.

## Channel projection

The double-Gysin corner has two quadratic generators

\[
A=(y_1+y_2)^2,
\qquad
B=(y_1-y_2)^2.
\]

On the physical mass diagonal (y_2=y_1=y),

\[
A\longmapsto4y^2,
\qquad
B\longmapsto0.
\]

Therefore the exact corner source becomes

\[
\boxed{
I_{\rm mass,corner}(X)
=\frac{2}{X(X^2-4y^2)}.
}
\]

After extracting (X^{-3}),

\[
\boxed{
X^3I_{\rm mass,corner}(X)
=\frac{2}{1-4y^2X^{-2}}.
}
\]

## Full jet

Thus

\[
\boxed{
C^{(2m)}_{\rm mass,corner}=2(4y^2)^m,
\qquad
C^{(2m+1)}_{\rm mass,corner}=0.
}
\]

In particular,

\[
(C^{(0)},C^{(1)},C^{(2)},C^{(4)})
=(2,0,8y^2,32y^4),
\]

as verified directly by the exact checker.

## Meaning

The generic mass diagonal is regular on the carrier and commutes with the
infinity jet (Entry 1521), yet on the supported double-Gysin corner it reduces
the two-channel recurrence module to one channel. This is not contradictory:
base change preserves the object while allowing its fiber rank profile to
drop on the channel discriminant (B=0).

The result supplies a concrete typed model of a physical operation acting as
a coefficient-lens projection:

\[
\boxed{
\text{two-channel supported jet}
\longrightarrow
\text{one-channel physical mass jet}.
}
\]

No new carrier support or fitted quotient was introduced.

## Durable evidence

- `research/nima/check_supercritical_infinity_jet.sage`;
- Entry 1525;
- allocator claim `seqclaim-bc2f354046c7f3155304f2b8`.
