# The Six-Point Residue Scalar and the Entry-Counit Gap

## Record

Date: 2026-08-14

Epistemic-graph correction event:

    ev-000000000023-43c37313-1d66-4da0-9b5f-b203e289a7b5

Status: exact typing and underdetermination theorem for the bounded residue problem left by entry
84.  The occurrence-decorated PC residue of the saturated six-point tripod cannot be computed
from the presently established maps.  The missing datum is one physical-core entry counit on the
edge which passes from the zero-core cell to the rank-one channel facet.

Strict residue vanishing is not the invariant target.  The saturated half-sum and the original
radial barycentric jump differ by an explicit rational two-chain boundary.  Entry 38 likewise
defines tubular/current realizations only up to filtered chain homotopy.  The invariant question
is whether the channel residue is null-homotopic, equivalently whether its class in the
factorized four-point-by-four-point boundary line vanishes.

The available data reduce that class to one scalar per channel and sheet, related by $D_6$.
They do not determine the scalar.

## Local carrier at one channel

Fix a physical channel $D$ of the hexagon.  Its associahedral facet is

\[
F_D\cong K_4\times K_4,
\]

a square.  Let $T_D^\epsilon$ be the corner reached from the parity center
$E_\epsilon$, and let $E_0,E_1$ be the two square edges incident to that corner.

Entry 84 replaces the nonsaturated radial jump

\[
j_D^\epsilon
=
[b(T_D^\epsilon),b(F_D)]
\]

by

\[
\Lambda_D^\epsilon
=
\frac12\sum_{a=0}^{1}
\left(
[b(T_D^\epsilon),b(E_a)]
+[b(E_a),b(F_D)]
\right).
\]

With

\[
\tau_a=[b(T_D^\epsilon),b(E_a),b(F_D)],
\]

the exact identity is

\[
\boxed{
\Lambda_D^\epsilon-j_D^\epsilon
=
\partial\left(\frac12(\tau_0+\tau_1)\right).
}
\]

The two integral route choices differ by

\[
\boxed{
p_0-p_1=\partial(\tau_0-\tau_1).
}
\]

Thus the saturated path is a canonical symmetric representative, but not a strictly distinguished
point-set current after passage to PC.

## Normal and coefficient typing

Put

\[
u_D=q_D-1,
\qquad
h_D=\frac{\ell_D}{u_D},
\qquad
\partial_{\mathscr L}\ell_D=u_Dp_D.
\]

The scalar coefficient and the loading remain separate.  A term carrying scalar polynomial
$c_D(X)$ has local type

\[
c_D(X)\otimes h_D\otimes\operatorname{or}(N_D).
\]

There is no substitution $X_D\mapsto u_D$.  Reversing the normal orientation changes the sign
of both $h_D$ and the Gysin contraction.

The saturated tail inside $F_D$ is completely typed by codimension-one Cousin maps.  The
incoming edge

\[
E_\epsilon
\longrightarrow
T_D^\epsilon
\]

is different: it changes the physical core from empty to $\{D\}$.  Its residue requires a
natural transformation from the zero-core occurrence module to the $D$-facet module, including
the endpoint Cousin term, $h_D$, and the scalar Laurent specialization.

Entries 32 and 37 do not supply this map.  Entry 32 defines the physical coaction after a
directed physical edge and its source slots are already present.  Entry 37 proves base change for
an independent scalar-refinement factor.  The present entry edge is neither: it is the
core-changing incidence which creates the physical channel in the tripod.

Call the missing map

\[
\epsilon_D^{\rm entry}.
\]

Without it, adding the saturated tail, its Cousin lower terms, and the normal factor does not
produce a defined occurrence-decorated residue.

## Signed codimension-one ledger for one leg

Let $L_D^\epsilon$ be the physical flip edge joining $E_\epsilon$ to
$T_D^\epsilon$.  The complete saturated leg is

\[
\begin{aligned}
\widetilde\gamma_D^\epsilon
={}&[E_\epsilon,b(L_D^\epsilon)]
+[b(L_D^\epsilon),T_D^\epsilon]\\
&+\frac12\sum_{a=0}^{1}
\left(
[T_D^\epsilon,b(E_a)]
+[b(E_a),b(F_D)]
\right).
\end{aligned}
\]

All six displayed edges are codimension-one incidences.  With every edge oriented as written,
their signed upper/tangential and lower/Cousin endpoints are

| oriented edge | upper/tangential endpoint | lower/Cousin endpoint | physical core |
| --- | ---: | ---: | --- |
| $[E_\epsilon,b(L_D^\epsilon)]$ | $+b(L_D^\epsilon)$ | $-E_\epsilon$ | empty |
| $[b(L_D^\epsilon),T_D^\epsilon]$ | $-b(L_D^\epsilon)$ | $+T_D^\epsilon$ | empty $\to\{D\}$ |
| $\frac12[T_D^\epsilon,b(E_a)]$ | $+\frac12b(E_a)$ | $-\frac12T_D^\epsilon$ | $\{D\}$ |
| $\frac12[b(E_a),b(F_D)]$ | $+\frac12b(F_D)$ | $-\frac12b(E_a)$ | $\{D\}$ |

The two values $a=0,1$ are both present.  Consequently $b(L_D^\epsilon)$ cancels, each
$b(E_a)$ cancels, and

\[
+T_D^\epsilon-\frac12T_D^\epsilon-\frac12T_D^\epsilon=0.
\]

This is strict in the undecorated incidence complex.  In PC, the last two terms land in the
already established $D$-facet occurrence summand and carry

\[
c_D(X)\otimes h_D\otimes\operatorname{or}(N_D).
\]

The first $T_D^\epsilon$ term is the Cousin lower term of the oppositely oriented entry edge.
It lands in that same summand only after applying $\epsilon_D^{\rm entry}$.  Thus the displayed
three-term cancellation is precisely the unproved occurrence-decorated square; no other
codimension-one term is missing from the saturated leg.

For $g\in D_6$, the finite incidence chain obeys

\[
g\widetilde\gamma_D^\epsilon
=
\widetilde\gamma_{gD}^{g\epsilon}.
\]

A one-step rotation has $g\epsilon=-\epsilon$ and cycles the three channels.  After choosing
ordered normal lines, the loaded residue transforms by the normal-orientation character
$\chi_N(g)$:

\[
g[r_D^\epsilon]
=
\chi_N(g)[r_{gD}^{g\epsilon}].
\]

There is no additional deck sign in the incidence chain.  The only residual sign is
$\chi_N(g)$; assigning it a numerical value without fixing the ordered normal convention would
be spurious.

## What is nevertheless fixed

Let

\[
\eta_6^{\epsilon,{\rm PC}}
\]

denote any PC realization of the saturated tripod extending the established codimension-one
terms.  Since the two QTDS presentations have identical physical residue on every channel,

\[
\operatorname{Res}^{\rm PC}_D
d_{\rm PC}\eta_6^{\epsilon,{\rm PC}}=0.
\]

Therefore

\[
r_D^\epsilon
:=
\operatorname{Res}^{\rm PC}_D
\eta_6^{\epsilon,{\rm PC}}
\]

is closed whenever $\epsilon_D^{\rm entry}$ makes residue a chain map.

Entry 77 identifies the induced maximally factorized boundary object with the primitive line

\[
\mathcal J_4\boxtimes\mathcal J_4
=
\mathbf k_{\rm nr}
\langle g_4\boxtimes g_4\rangle.
\]

Hence there is a scalar

\[
\boxed{
[r_D^\epsilon]
=
\lambda_D^\epsilon
[g_4\boxtimes g_4].
}
\]

One-step rotation sends $D$ to the next channel and exchanges the two parity sheets.  Reflection
fixes the symmetric saturated tail.  Thus the six numbers $\lambda_D^\epsilon$ belong to one
$D_6$-orbit, with only the normal-orientation character changing signs.  Computing one
representative determines all six.

Boundary, deck covariance, and the local Pochhammer identity do not determine its value.  If a
closed lift with nonzero primitive boundary residue is available, the replacement

\[
\eta_6^{\epsilon,{\rm PC}}
\longmapsto
\eta_6^{\epsilon,{\rm PC}}+\kappa_D,
\qquad
d_{\rm PC}\kappa_D=0,
\]

changes $\lambda_D^\epsilon$ while preserving the endpoint boundary.  The established axioms do
not exclude such a lift and do not provide a period that fixes its coefficient.  Scalar
provenance must select the value through $\epsilon_D^{\rm entry}$.

## Strict zero versus null-homotopy

Because

\[
\Lambda_D^\epsilon-j_D^\epsilon
=
\partial\left(\frac12(\tau_0+\tau_1)\right),
\]

changing between the radial and saturated representatives adds an explicit boundary.  A literal
chain equality

\[
r_D^\epsilon=0
\]

is therefore not invariant under the allowed filtered chain-homotopy freedom.

The correct condition is

\[
\boxed{
[r_D^\epsilon]=0,
}
\]

or, with a chosen representative, an explicit homotopy

\[
r_D^\epsilon=d_{\rm PC}s_D^\epsilon.
\]

If $\lambda_D^\epsilon=0$, the residue is null-homotopic and the six-point contact primitive
belongs to the derived residue-free fiber.  If it is nonzero, the primitive has a genuine lower
factorized obstruction.  A point-set strict zero can be imposed only after choosing the
null-homotopy; it is not primary data.

## Consequence for eight points

The formal pole-grade primitive remains

\[
H_8^{\rm PC}
=
\sum_D
G_D^{\rm PC}
(\eta_6^{\rm PC})
+H_{\rm ct}^{\rm PC}.
\]

Its coefficient boundary is exactly

\[
\sum_Q(q_Q^+-q_Q^-)
\]

because entry 23 exhausts the full symbol by $G$, $R$, and $K$.  The marked $K$ part is
closed by entry 83.  The $R$ part is factorization-natural in the derived PC category if and
only if

\[
\lambda_D^\epsilon=0.
\]

There is still no extra unmarked coefficient remainder.  The remaining obstruction is the
single six-point entry-counit scalar and, separately, the stronger global problem of gluing local
quadrangulation half-lines with Jordan higher coherence.

## Exact finite content

The finite carrier identities are certified by

    research/nima/check_six_point_subdivision_pc.rs

with SHA-256

    46021191c34034bf4cd64f5f80e6fe9f0fb39316f86b263fdfeaae9785a310d4

The checker proves the saturated paths, their $D_6$ covariance, and the explicit rational and
integral two-chain fillers.  It deliberately does not assign a value to
$\epsilon_D^{\rm entry}$ or $\lambda_D^\epsilon$.

## Decision

Reject:

> The established PC map proves that the six-point tripod residue is strictly zero.

Also reject:

> Nonzero physical-facet support by itself proves a nonzero residue class.

Promote:

> The invariant six-point obstruction is one scalar multiplying the primitive
> $K_4\times K_4$ boundary line.  Strict zero is representative dependent; null-homotopy is the
> correct condition.

Retain as the next bounded experiment:

> Construct $\epsilon_D^{\rm entry}$ from the occurrence-resolved scalar Laurent grade for one
> center-to-channel edge and pair its residue with the dual
> $g_4^\vee\boxtimes g_4^\vee$.  This computes $\lambda_D^\epsilon$.  Rotation and reflection
> then determine every channel and sheet.

## Internal dependencies

- Entries 20--21: scalar contact redistribution and tripods.
- Entry 23: exhaustive eight-point pole-grade decomposition.
- Entries 32 and 37: domains of the established physical coaction and transverse base change.
- Entry 38: PC normal factors and filtered representative strength.
- Entry 77: primitive factorized boundary half-line.
- Entries 83--84: marked octagon and saturated tripod correction.
- `research/nima/check_six_point_subdivision_pc.rs`.
