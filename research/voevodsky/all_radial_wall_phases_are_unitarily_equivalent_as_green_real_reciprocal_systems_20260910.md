# All radial wall phases are unitarily equivalent as Green--Real reciprocal systems

## Question

Does the unit phase \(u\) label genuinely different abstract radial boundary systems, or only different trivializations of the second oriented channel?

## Claim boundary

For any unit phases \(u,v\), an explicit diagonal unitary carries the complete carrier, fold, wall, reciprocal involution, Green form, and twisted Real structure at \(u\) to those at \(v\). Hence the phase is not an invariant of the abstract enriched radial system. It may remain meaningful relative to an externally fixed channel frame or coupling.

## Problem

The radial structures are

\[
C_uq=(q(r),u q(-r)),
\]

\[
\Lambda_u=\{(c,uc):c\in\mathbb C\},
\]

\[
W_u=
\begin{pmatrix}
0&u^{-1}\\
u&0
\end{pmatrix},
\]

and

\[
J_u=\operatorname{diag}(1,u^2)K.
\]

The formulas depend on \(u\), but formula dependence need not be invariant dependence.

## Bold conjecture

Different unit phases define inequivalent Green--Real reciprocal boundary systems and may have different observer stability.

## Named rivals

1. A diagonal channel gauge identifies every pair of phases.
2. The gauge preserves the wall but not reciprocal exchange.
3. It preserves sewing but not the twisted Real structure.
4. Abstract equivalence removes all possible physical significance of \(u\).

## Phase-change unitary

For \(|u|=|v|=1\), define

\[
G_{v,u}
=
\begin{pmatrix}
1&0\\
0&v/u
\end{pmatrix}.
\]

This is unitary and satisfies the groupoid laws

\[
G_{w,v}G_{v,u}=G_{w,u},
\qquad
G_{u,u}=I,
\qquad
G_{v,u}^{-1}=G_{u,v}.
\]

Thus the phases form a gauge groupoid rather than an ordered family.

## Fold naturality

Directly,

\[
G_{v,u}C_uq
=(q(r),v q(-r))
=C_vq.
\]

Hence

\[
G_{v,u}C_u=C_v.
\]

The phase-decorated folds are the same whole-line identification in different radial channel frames.

## Wall naturality

For \((c,uc)\in\Lambda_u\),

\[
G_{v,u}(c,uc)=(c,vc)\in\Lambda_v.
\]

Therefore

\[
G_{v,u}\Lambda_u=\Lambda_v.
\]

## Reciprocal naturality

A direct matrix calculation gives

\[
G_{v,u}W_uG_{v,u}^{-1}=W_v.
\]

Equivalently,

\[
G_{v,u}W_u=W_vG_{v,u}.
\]

Rival 2 fails.

## Real naturality

Because the Real maps are anti-linear, their comparison law is

\[
G_{v,u}J_u=J_vG_{v,u}.
\]

Indeed both sides act on \((a,b)\) as

\[
(\bar a,v^2\overline{(v/u)b})
=
(\bar a,uv\bar b).
\]

The left side gives the same expression from

\[
G_{v,u}(\bar a,u^2\bar b)
=(\bar a,uv\bar b).
\]

Thus rival 3 fails.

## Differential and Green naturality

The gauge is constant and diagonal, so it commutes with

\[
\mathbb D=\operatorname{diag}(\partial_r,-\partial_r).
\]

It also preserves

\[
J_\partial=\operatorname{diag}(-1,1):
\qquad
G_{v,u}^*J_\partial G_{v,u}=J_\partial.
\]

Therefore it is an equivalence of the full Green-domain systems, not only their boundary fibers.

## Reciprocal parity naturality

The eigenspaces

\[
X_\pm(u)=\{(f,\pm uf)\}
\]

satisfy

\[
G_{v,u}X_\pm(u)=X_\pm(v).
\]

Hence the two-sector essential-margin theorem is phase-independent after transport.

## Observer margins

If

\[
A_v=V_{v,u}A_uG_{v,u}^{-1}
\]

for a unitary target comparison \(V_{v,u}\), then

\[
m(A_v)=m(A_u),
\]

and their Gramian and Calkin spectra agree by unitary conjugation. Therefore no wall phase can repair or destroy coercivity inside the abstract gauge-equivalence class.

## Relative phase remains possible

Rival 4 overstates the conclusion. The phase becomes invariant only relative to additional fixed data that is not transformed by \(G_{v,u}\), for example:

- a laboratory channel basis;
- a fixed external coupling vector;
- a source injection whose second-channel phase is independently normalized;
- comparison with another wall whose gauge has already been fixed.

Such data define a relative phase. A contract must name that external frame before treating \(u\) as observable.

## Constructor-role classification

The maps \(G_{v,u}\) have role `channel_gauge_comparison`. They are not:

- reciprocal dynamics;
- complementary observers;
- physical phase readouts;
- symmetry quotient maps.

A `relative_phase_readout` requires a second fixed object and must fail gauge invariance if that object is held fixed. The two roles cannot be conflated.

## Strongest falsification attempt

The strongest possible obstruction was simultaneous preservation of wall, reciprocal involution, twisted Real structure, and Green form. The explicit diagonal unitary satisfies all four comparison squares and the fold naturality square. No invariant of the isolated enriched system distinguishes \(u\) from \(v\).

## Disposition

The bold conjecture is rejected for the isolated radial system. Unit wall phases are gauge-equivalent, and observer stability is phase-independent under the corresponding unitary transport. Any physical or cross-sector significance of \(u\) must be relational and sourced by external frame data.
