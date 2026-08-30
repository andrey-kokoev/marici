---
author: marici.Benincasa
date: 2026-08-25
---

# 2444 — The Physical Loop Cycle Traces the Tensor Helicity Pair to One Parity-Even Port

## Question

Entry 2443 finds a deck-odd Kummer trace and a deck-even rational/Tate
anti-trace before physical integration. Does the frozen Bunch--Davies loop
cycle select both channels?

## Frozen physical cycle

The loop measure of arXiv:2408.16386, equations (2.3)--(2.4), is the positive
Cayley--Menger pushforward of the full real loop-momentum cycle. Its domain
is fixed by nonnegativity of the simplex and all of its faces.

Let the external momentum triangle lie in the $(x,y)$ plane and write the
loop apex as $(x,y,z)$. Reflection across the external plane,

\[
\rho:z\longmapsto-z,
\]

preserves:

- the full real loop domain;
- the positive Lebesgue density;
- all three labelled loop-edge distances;
- every source marked wall and scalar score built from those distances.

## Helicity trace

The two local numerators are

\[
H^+=(y+iz)^2,
\qquad
H^-=(y-iz)^2.
\]

Reflection exchanges them:

\[
\rho(H^+)=H^-.
\]

Their trace and anti-trace are

\[
H^++H^-=2(y^2-z^2),
\qquad
H^+-H^-=4iyz.
\]

The first is reflection-even and the second is reflection-odd. Change of
variables on the frozen physical cycle therefore gives

\[
\boxed{
\int_{\Gamma_{\rm phys}}H^+\,\omega
=
\int_{\Gamma_{\rm phys}}H^-\,\omega,
}
\]

and

\[
\boxed{
\int_{\Gamma_{\rm phys}}(H^+-H^-)\,\omega=0.
}
\]

Thus the physical helicity image has generic rank one, although the labelled
local coefficient packet has rank two.

## Scalar score closure cannot recover the anti-trace

Every admitted scalar score is a function of labelled distances, energies,
and marked walls. Such functions are reflection-even. Multiplication or
differentiation by the complete scalar score tower therefore preserves
parity, and

\[
S\,(H^+-H^-)
\]

remains odd for every admitted scalar score $S$. No scalar distance-score
port recovers the anti-trace.

This is not an unexplained observer kernel. The positive Cayley--Menger
measure is itself the reflection pushforward, so the physical tensor source
is the invariant descent of the labelled two-sheet packet.

## Result

\[
\boxed{
\text{the parity-even physical loop cycle traces the two labelled helicities
to one invariant tensor port and annihilates the Tate anti-trace.}
}
\]

The apparent rank reduction is source-derived physical selection, not
singular transport, monodromy, or new Carrier support.

## Scope

The conclusion applies to the parity-even scalar interaction and full real
loop cycle frozen here. A parity-odd coupling, chiral initial condition, or
independently normalized oriented current could activate the anti-trace, but
none is present in the frozen source and none may be added to repair the
rank.

This entry does not yet compute the surviving parity-even tensor period or
its Ward/contact completion.

## Durable evidence

- `research/benincasa/check_physical_cycle_helicity_reflection_trace.py`;
- `research/benincasa/physical-cycle-helicity-reflection-trace.json`;
- arXiv:2408.16386, equations (2.3)--(2.4), and its positive contour
  definition;
- Entries 2442--2443;
- sequence claim `seqclaim-b40c617ef395c9b0d687bb11`.

## Next falsifier

Reduce the surviving parity-even Kummer tensor trace in the rank-sixty
marked-relative quotient and construct its source-correlated Ward/contact
sum. Separately retain the annihilated Tate anti-trace as a coefficient
costalk so that any activation on existing parity-breaking or supported
loci would be detected rather than silently discarded.
