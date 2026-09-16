# Convolution-degree naturality does not prove the Douglas bound and isolates the needed ambient contraction

## Attempt

The generic degree system supplies fixed feature maps

\[
A_{S,r}:E_r\to\mathcal H_S,
\qquad
A_{B,r}:E_r\to\mathcal H_B.
\]

Convolution by \(a\in E_s\) gives the exact source successor

\[
L_a^{(r)}:E_r\to E_{r+s}.
\]

The desired comparison is a family of contractions \(C_r\) satisfying

\[
A_{B,r}=C_rA_{S,r}
\]

and the degree-naturality equations.

## Canonical comparison

On the algebraic range of \(A_{S,r}\), the only source-labelled candidate is

\[
C_r(A_{S,r}p)=A_{B,r}p.
\]

This map is well defined and contractive exactly when

\[
\|A_{B,r}p\|
\le
\|A_{S,r}p\|
\]

for every \(p\in E_r\).

Thus defining \(C_r\) from the two feature maps is equivalent to the desired positivity inequality. It does not prove it.

## Naturality is automatic after positivity

Suppose the inequality holds in degrees \(r\) and \(r+s\). For \(a\in E_s\), both routes applied to \(A_{S,r}p\) give the source-labelled vector associated with \(a*p\).

Therefore the canonical contractions commute with degree successors automatically on generated ranges.

Hence convolution-degree coherence adds no norm estimate beyond positivity. It organizes the result but cannot create the contraction.

## Required noncircular input

A proof must construct an ambient contraction before comparing the Schur and defect features.

One needs a source carrier \(\mathcal H_{src}\), a contraction

\[
T_{src}:\mathcal H_{src}\to\mathcal H_{src}
\]

with

\[
\|T_{src}\|\le1
\]

proved independently, and feature maps satisfying

\[
A_{S,r}=J_SA_{src,r},
\]

\[
A_{B,r}=J_BT_{src}A_{src,r}.
\]

The desired inequality would then follow from the contraction theorem for \(T_{src}\).

## Available ambient contractions

Prior source architecture supplies several genuine contractions or isometries:

1. orthogonal parity projections;
2. conditional expectations onto invariant source sectors;
3. Hardy projections;
4. canonical/dual unitary transforms;
5. semilocal Sonin amplification as a two-space Hilbert isomorphism;
6. orthogonal projection onto an endpoint-augmented graph carrier.

None is yet identified with the Krein--Langer defect feature.

## Odd-parity candidate

Let \(R\) be the source reflection involution and define

\[
P_-=rac{I-R}{2}.
\]

Then

\[
P_-^2=P_-^*=P_-,
\qquad
\|P_-\|=1.
\]

On the endpoint graph carrier, \(P_-\) selects the odd endpoint line. This is a legitimate independently contractive source operation.

It would prove the desired bound if one could establish the source identities

\[
A_{B,r}=J_BP_-A_{src,r}
\]

and

\[
A_{S,r}=J_SA_{src,r}
\]

with \(J_B\) no larger than \(J_S\) on the selected range.

## Limitation of the parity candidate

Krein--Langer theory says that the full negative feature is the Blaschke model space \(K_B\). Its dimension equals the forbidden divisor multiplicity.

An odd endpoint projection has rank one in the parity-reduced endpoint fiber. It can represent the full defect only when the source-compressed negative space is exactly that one endpoint direction.

If additional divisor directions survive source observation, parity projection cannot absorb them.

Thus the exact identification to test is

\[
A_{B,r}(E_r)
=
A_{B,r}(E_r)\cap K_{endpoint,odd}.
\]

Equivalently, every non-endpoint Blaschke direction must be annihilated by the source observation map.

## Hostile audit

An off-axis divisor mode provides the hostile fixture. If its reproducing vector has nonzero pairing with some degree-\(r\) source observation, then the defect range is larger than the endpoint odd line and the parity contraction route fails.

This test uses off-axis data only to falsify an overclaim. It is not the objective of the construction.

## Exact next test

For the source evaluation map \(\mathcal O_r\), compute the projection of its range onto the Blaschke model space:

\[
P_{K_B}\mathcal O_r(E_r).
\]

Determine whether this projection is:

1. zero;
2. the single odd endpoint line;
3. a larger divisor subspace.

Only case 2 is compatible with the endpoint-parity contraction mechanism.

## Degree propagation

Because convolution successors act by Mellin multiplication, a divisor direction invisible at degree one can become visible at higher degree only if multiplication changes the annihilator of the source evaluation range.

Therefore the test must be made on the graded union

\[
E_{fin}
=
\bigcup_{r\ge0}E_r.
\]

If this union is evaluation-faithful on the analytic strip, every surviving Blaschke direction will eventually be detected. Then endpoint-only absorption is possible only when the compressed defect truly has endpoint index one.

## Disposition

The generic-\(r\) natural transformations are now typed, but their canonical Douglas maps are contractive if and only if the target inequality already holds.

The first noncircular candidate is the independently contractive odd-parity projection on the endpoint-augmented source graph. The decisive analytical test is whether the source-compressed Krein--Langer defect range is exactly the odd endpoint line.
