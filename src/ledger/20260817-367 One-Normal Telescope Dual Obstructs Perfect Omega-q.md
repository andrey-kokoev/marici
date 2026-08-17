# One-Normal Telescope Dual Obstructs Perfect Omega-q

## Result

The corrected D03 dualizing complex of Entry 366 does **not** admit a
bounded finite-projective compression over the unlocalized Entry-352
structure sheaf. Consequently neither does

\[
\omega_q=\operatorname{pr}_{\widetilde G}^{!}\omega_{\widetilde b}.
\]

The obstruction already occurs on one ordinary short-normal incidence; it
does not depend on the exceptional divisor or on Entry 176.

## Projective-generator witness

Fix one short normal (u=u_0). In the target let

\[
a=(\{x_0\},\varnothing),
\qquad A_a=A[u^{-1}],
\]

and in the corrected carrier let

\[
y=([\{x_0\}],\varnothing).
\]

This is the unique degree-zero source point over (a), so (U_y=\{y\}).
For the source representable projective (P_y), direct image is the
costandard target module

\[
R\widetilde b_*P_y=C_a(A[u^{-1}]).
\]

Indeed its stalk at (t) is (A[u^{-1}]) exactly when (t\le a), and is
zero otherwise. There is no higher section cohomology because the source
open is a singleton.

By adjunction, the stalk of the relative dualizing complex at (y) is

\[
(\omega_{\widetilde b})_y
\simeq
R\operatorname{Hom}_X(C_a(A[u^{-1}]),\mathcal O_X).
\]

## Surviving telescope-dual sector

Resolve (C_a(A[u^{-1}])) by the standard target representables and dualize.
After all spectator parameters are made units, filter by whether the
terminal target state has inverted (u). The non-inverted associated
sector has the common coefficient

\[
D_u:=R\operatorname{Hom}_A(A[u^{-1}],A).
\]

Its finite incidence carrier is the target-chain complex whose first point
lies below (a) and whose terminal point does not invert (u). The exact
enumeration gives chain ranks

\[
(2,43,96,54),
\]

boundary ranks modulo (101)

\[
(0,2,41,54),
\]

and homology

\[
(0,0,1,0).
\]

Its Euler characteristic is (1). Vanishing in the other degrees modulo
(101) bounds the corresponding rational homology by zero there; the
Euler characteristic therefore forces a free rank-one rational class in
degree two. Thus one copy of (D_u) survives the incidence cancellation.

The complementary associated sector is a finite complex of
(A[u^{-1}])-modules. Any later filtered differential from that sector has
finitely generated image, so it cannot exhaust the non-finitely-generated
part of the surviving (D_u) class.

## Algebraic non-finiteness

The standard telescope resolution

\[
0\longrightarrow\bigoplus_{n\ge0}A
\xrightarrow{1-u\,\mathrm{shift}}
\bigoplus_{n\ge0}A
\longrightarrow A[u^{-1}]\longrightarrow0
\]

shows that (D_u) has a nonzero degree-one cohomology module. After
localizing at the height-one prime ((u)), it is the familiar completion
quotient

\[
\widehat{A_{(u)}}/A_{(u)},
\]

which is not finitely generated. Hence the stalk
((\omega_{\widetilde b})_y) is not a perfect (A[u^{-1}])-pulled-back
incidence object. A bounded complex of finite projective sheaves would have
perfect stalks, giving the required contradiction.

The occurrence costandard factor preserves and reflects perfectness by
Entry 363. Therefore

\[
\boxed{\omega_q\text{ is not perfect over the unlocalized D03 carrier}.}
\]

## Entry-176 consequence

Entry 176's exceptional cap is a finite rank-one local relative chain map.
It cannot be identified with the actual (omega_q): besides the previously
proved type mismatch, (omega_q) contains the non-perfect ordinary-normal
telescope-dual sector above, whereas a bounded rank-one exceptional cap is
perfect. No support functor can turn a perfect rank-one object into this
global dualizing complex by an isomorphism.

Entry 176 may still define a local exceptional summand or a map after a
normal/nonresonant localization that kills the telescope obstruction. That
is a different statement from identification with the unlocalized global
(omega_q).

## Evidence boundary

`research/voevodsky/check_d03_ringed_carrier_typing.rs` verifies the unique
source witness, enumerates the entire associated completion-sector chain
complex, checks its modular ranks and free Euler class, and retains the full
dualizing-term census. The non-finiteness of the localization dual follows
from the displayed telescope resolution. No exceptional geometry,
orientation choice, or fitted coefficient enters the obstruction.
