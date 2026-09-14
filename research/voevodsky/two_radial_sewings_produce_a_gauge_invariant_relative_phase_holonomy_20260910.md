# Two radial sewings produce a gauge-invariant relative-phase holonomy

## Question

If one wall phase is gauge, what invariant appears when two independently specified radial sewings are compared in the same channel frame?

## Claim boundary

The composition of two reciprocal swaps is a diagonal orientation-preserving transport determined by the phase ratio. Under a common channel gauge, this ratio and the conjugacy invariants of the transport are unchanged. Thus relative phase first appears in a two-sewing loop, not in an isolated wall. No physical interpretation follows without a source-derived realization of both sewings and a readout.

## Problem

For unit phases \(u,v\), define

\[
W_u=
\begin{pmatrix}
0&u^{-1}\\
u&0
\end{pmatrix},
\qquad
W_v=
\begin{pmatrix}
0&v^{-1}\\
v&0
\end{pmatrix}.
\]

Each isolated system is gauge-equivalent to every other. We ask whether their comparison contains an invariant.

## Bold conjecture

Because each phase is individually gauge, any composition of two wall sewings is also phase-independent.

## Named rivals

1. The ratio \(v/u\) survives a common gauge.
2. The product of two orientation-reversing swaps is an orientation-preserving holonomy.
3. Its spectrum is invariant but cannot be operationally read without an interference-sensitive observer.
4. Allowing independent gauges at the two walls removes even the ratio unless a connecting transport identifies their frames.

## Two-sewing composition

Direct multiplication gives

\[
H_{v,u}
=W_vW_u
=
\begin{pmatrix}
u/v&0\\
0&v/u
\end{pmatrix}.
\]

Therefore

\[
\det H_{v,u}=1,
\qquad
H_{v,u}^{-1}=H_{u,v}.
\]

The two reciprocal reversals compose to an orientation-preserving diagonal transport.

Its eigenvalues are

\[
\frac uv,
\qquad
\frac vu,
\]

and its trace is

\[
\operatorname{tr}H_{v,u}
=
\frac uv+rac vu
=2\operatorname{Re}(v/u).
\]

Thus rival 1 survives.

## Common-gauge invariance

A common change of second-channel frame by \(w\in U(1)\) sends

\[
(u,v)\longmapsto(wu,wv).
\]

The ratio is unchanged:

\[
\frac{wv}{wu}=rac vu.
\]

Equivalently, the diagonal gauge \(G_w=\operatorname{diag}(1,w)\) satisfies

\[
W_{wu}=G_wW_uG_w^{-1},
\qquad
W_{wv}=G_wW_vG_w^{-1},
\]

so

\[
H_{wv,wu}=G_wH_{v,u}G_w^{-1}=H_{v,u}.
\]

The final equality holds because both matrices are diagonal.

## Independent-gauge qualification

If the two walls belong to unrelated channel frames, one may gauge them independently and alter \(v/u\). A relative phase becomes defined only after a connecting comparison identifies those frames.

Thus the typed loop is not merely the pair \((W_u,W_v)\). It is

\[
X_u
\xrightarrow{T_{v,u}}
X_v
\xrightarrow{W_v}
X_v
\xrightarrow{T_{u,v}}
X_u
\xrightarrow{W_u}
X_u,
\]

where the connecting transports are declared. In a common trivialization they reduce to the product above.

Rival 4 therefore identifies the required source datum rather than refuting the relative invariant.

## Green orientation

Each reciprocal swap is a Green anti-isometry:

\[
W_u^*J_\partial W_u=-J_\partial,
\qquad
W_v^*J_\partial W_v=-J_\partial.
\]

Their product is a Green isometry:

\[
H_{v,u}^*J_\partial H_{v,u}=J_\partial.
\]

Hence the relative holonomy preserves orientation after two reversals.

## Real structure

Within each phase fiber, the twisted Real map is

\[
J_u=\operatorname{diag}(1,u^2)K.
\]

The phase-change transport \(G_{v,u}\) satisfies

\[
G_{v,u}J_u=J_vG_{v,u}.
\]

For the common-frame loop, ordinary conjugation sends

\[
H_{v,u}\longmapsto H_{u,v}=H_{v,u}^{-1}.
\]

Thus the Real operation reverses loop orientation. The Real-invariant scalar trace retains only

\[
2\operatorname{Re}(v/u),
\]

while an oriented complex readout is required to distinguish \(v/u\) from its inverse.

## Observer requirement

A channel-diagonal intensity observer sees only unit modulus and cannot distinguish the holonomy eigenvalues. To read the relative phase, an observer must compare the two orientation channels coherently, for example through an off-diagonal matrix coefficient.

Such a map has constructor role `relative_phase_observer`. Its signature requires:

- two wall systems;
- a connecting frame transport;
- coherent access to both orientation channels;
- a declared loop orientation;
- a readout distinguishing at least the desired conjugacy invariant.

A single-wall boundary trace lacks this source arity.

## Complementarity qualification

Detecting \(v/u\) adds relational information, but it does not automatically supply an essential lower margin on an infinite carrier. A finite-dimensional holonomy readout is a finite-rank observer. It may repair a finite phase ambiguity or residual kernel but cannot replace a cofinite complementary observer.

Thus `relative_phase_observer` and `essential_observer` are independent roles.

## Strongest falsification attempt

The complete gauge equivalence of isolated phases seems to remove phase information. It does remove absolute phase. But once two sewings share a frame, only simultaneous gauge transformations are admissible, and their ratio survives. Conversely, without a connecting frame, the ratio is not defined. The invariant is therefore relational, neither absolute nor fictitious.

## Disposition

The bold conjecture is rejected. Two reciprocal sewings generate a gauge-invariant relative holonomy after their channel frames are identified. Its spectrum and Real trace are intrinsic to the typed loop. This gives the programme its first relational phase observable while preserving the distinction between finite phase readout and stable complementary observation.
