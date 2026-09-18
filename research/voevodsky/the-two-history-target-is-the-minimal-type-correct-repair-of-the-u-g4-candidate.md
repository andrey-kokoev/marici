# The two-history target is the minimal type-correct repair of the U-G4 candidate

## Fresh audit

The adopted `u-g4-owner-construction-packet.v2` retracts the formula

\[
(U_{\rm pair}x,J_{RL}U_{\rm pair}x)
\]

because `U_pair` produces a tensor-pair history while `J_RL` accepts one doubled one-variable radial graph.

Subsequent work constructs a continuous componentwise fold

\[
F^{WJ}_{\rm rad}=C_u\oplus C_u:
H^1(\mathbb R)_W\oplus H^1(\mathbb R)_J
\longrightarrow
\mathcal G_{\rm rad}^{W}\oplus\mathcal G_{\rm rad}^{J}.
\]

It is unitary onto its folded range, injective, cutoff-uniform, and automatically satisfies the two wall conditions. It does not construct a contraction to one radial history.

## Minimal repaired target

Do not contract the independent \(W\) and \(J\) histories. Define

\[
\mathcal B_{G4}^{(2)}
=\operatorname{Graph}(J_{RL})_W
\oplus
\operatorname{Graph}(J_{RL})_J.
\]

Its coordinates are ordered as

\[
(q_W,\rho_{0,W},E_W,W_W,R_W+2E_W;
 q_J,\rho_{0,J},E_J,W_J,R_J+2E_J).
\]

Give it the direct-sum graph pairing

\[
\langle q_W,q'_W\rangle_{G_D}
+\langle J_{RL}q_W,J_{RL}q'_W\rangle_{\rm border}
+\langle q_J,q'_J\rangle_{G_D}
+\langle J_{RL}q_J,J_{RL}q'_J\rangle_{\rm border}.
\]

This retains both source histories and introduces no fitted mixing coefficient.

## Type-correct candidate

Let

\[
U_{\rm pair}^{WJ}:\Theta_{\rm Pair}^{\mathbb Z_+}
\to H^1(\mathbb R)_W\oplus H^1(\mathbb R)_J
\]

be the already constructed pair-band history assignment. Put

\[
C_{\rm pair,rad}^{(2)}
=F^{WJ}_{\rm rad}U_{\rm pair}^{WJ}.
\]

The minimally repaired candidate is

\[
U_{G4}^{(2)}(x)=
\left(
C_{\rm pair,rad}^{(2)}x,
(J_{RL}\oplus J_{RL})C_{\rm pair,rad}^{(2)}x
\right).
\]

Unlike the v1 formula, every displayed composition now has matching source and target types.

## Why one history is not canonical

Any contraction

\[
M:H_W\oplus H_J\to H
\]

requires at least a choice of two coefficient operators. Neither the source pair labels nor the graph-norm bound selects such coefficients. Taking \(M(W,J)=W+J\), a normalized sum, or a projection would therefore be additional structure and could erase a kernel direction. The direct sum is the initial source-faithful repair.

## Remaining analytic and authority gates

Type correction does not complete `U_G4`. The following remain:

1. prove `J_RL` is closed/continuous on each folded graph domain;
2. prove continuous endpoint and Wronskian traces there;
3. prove holomorphic divisibility of \(\rho_0+E-W/2\) by \(z\) at zero;
4. prove radical-zero for the completed source tensor pairing against an explicit dual;
5. run recursive provenance closure excluding `T_PB` and equivalent comparison-side ancestors;
6. obtain authenticated owner adoption of the changed two-history target.

## Lattice update

Refine the G4 coordinate into

- \(q_{\rm type}\): a composable target/map formula exists;
- \(q_{\rm an}\): its completed analytic estimates hold;
- \(q_{\rm auth}\): the repaired packet is owner-authorized.

The present value is

\[
(q_{\rm type},q_{\rm an},q_{\rm auth})=(1,0,0).
\]

Combined with the source-tail/interface coordinates, the current point is

\[
(t,g,j,k,q_{\rm type},q_{\rm an},q_{\rm auth},c)
=(1,1,1,0,1,0,0,\bot).
\]

## Claim boundary

This constructs a type-correct candidate architecture, not an authoritative analytic `U_G4`. It does not permit formation of the final comparison residual and has no RH implication.
