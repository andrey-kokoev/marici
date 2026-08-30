# The cross-tower Ward cell is a balanced defect equalizer, not an annihilator

## Correction to the kernel target

The tentative horizontal cell was

\[
Z_X^{\mathrm{arith}}(s)\longrightarrow\ker W_X,
\]

where (W_X) is the finite prime-exclusion Ward packet. This target conflicts
with a source invariant already proved for the canonical Mellin-transported
theta packet.

The vacuum coefficient is fixed:

\[
(c_s)_1=\Omega_1\ne0.
\]

Every primitive exclusion contains the vacuum label, hence

\[
\lVert P_{p\nmid n}c_s\rVert^2
\ge |\Omega_1|^2>0.
\]

Consequently a canonical zero-state cannot lie in (ker W_X), even at one
prime. The obstruction is not failure of arithmetic coherence. It is the
presence of a legitimate source boundary charge.

## Forced categorical shape

Let (mathcal D_X) be a typed defect object. The input tower supplies

\[
W_X:C_X\longrightarrow\mathcal D_X,
\]

while the control/output boundary system must independently supply

\[
B_{X,s}:Y_{X,s}\longrightarrow\mathcal D_X.
\]

The admissible state is not the kernel of either map. It belongs to their
equalizer pullback:

\[
\mathcal Z_{X,s}
=
C_X\mathop{\times}_{\mathcal D_X}Y_{X,s},
\qquad
W_X(c)=B_{X,s}(y).
\]

This is the missing comparison channel sensed in the coherence-tower audit.
It does not add a fourth tower. It provides the common codomain in which the
input curvature and control boundary current can be compared without erasing
their provenance.

## Why a scalar balance is insufficient

If both maps are compressed to one number, unrelated prime channels may
cancel. Therefore (mathcal D_X) must retain at least:

- the prime label;
- valuation grade, including primitive and square channels;
- endpoint or seam incidence;
- cutoff restriction maps.

The equality must hold in this typed object before any scalar sum.

## Revised RH-bearing route

The conservation law should have the form

\[
(2\operatorname{Re}s-1)N_{X,s}
=
W_X(c)-B_{X,s}(y),
\]

with (N_{X,s}>0) for a nonzero admissible state. Membership in the balanced
equalizer makes the right-hand side vanish and then forces

\[
\operatorname{Re}s=\frac12.
\]

This is fundamentally different from asking scalar nullity to annihilate a
positive Ward packet.

## The next finite construction

At cutoff (X=\{2\}):

1. derive the exclusion component (W_2(c)), retaining the vacuum;
2. derive (B_{2,s}(y)) from the primitive, square, seam, and archimedean
   boundary operations;
3. type both in one defect module without identifying them by hand;
4. compute the residual
   
   \[
   R_{2,s}=W_2(c)-B_{2,s}(y);
   \]

5. reject the route if the first source-labelled coefficient of (R_{2,s})
   is nonzero.

The true obstacle is now construction of (B_{X,s}). Calling the Ward packet
itself a boundary current would make the equalizer tautological.

## Falsifier

Any one of the following closes the route:

- no independently source-derived boundary map into (mathcal D_X);
- a nonzero typed residual at cutoff (\{2\});
- equality only after scalar aggregation;
- loss of the vacuum component;
- failure of the equalizer under cutoff restriction or completion.

