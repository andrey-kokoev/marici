# Continuous-mode optical attachment pullback

## Question

Under which analytic conditions do detector couplers and effects pull back through continuous optical propagation, mode conversion, and loss?

## Claim boundary

This packet treats bounded linear propagation on frequency–polarization mode spaces and effect-valued detector attachments. It proves an operator-level transport law. It does not construct a laboratory detector, nonlinear medium, unbounded field observable, or time-domain realization.

## Continuous mode objects

For an accessible optical port \(p\), take the one-particle mode space

\[
H_p=L^2(\Omega_p,\mu_p;\mathbb C^2),
\]

where \(\Omega_p\) is a declared frequency band and \(\mathbb C^2\) carries polarization. More general finite multiplicity fibers may replace \(\mathbb C^2\).

A typed propagation or mode-conversion map from port \(p\) to port \(q\) is a bounded operator

\[
V:H_p\to H_q.
\]

Lossy passive propagation is represented by a contraction,

\[
V^*V\le I_{H_p}.
\]

An instrument coupler is a bounded map \(C:H_q\to K\) into a detector acceptance space. Its effect is

\[
E=C^*C,
\qquad 0\le E\le I_{H_q}
\]

when \(C\) is contractive.

## Pullback of couplers and effects

The coupler pulls back by composition:

\[
V^*_{m cpl}(C)=CV:H_p\to K.
\]

The corresponding effect pulls back by conjugation:

\[
V^*_{m eff}(E)=V^*EV.
\]

If \(E\) is positive, then \(V^*EV\) is positive. If \(E\le I\) and \(V\) is contractive, then

\[
0\le V^*EV\le V^*V\le I.
\]

Thus contractions preserve admissible individual effects.

For composable bounded propagation maps

\[
H_p\xrightarrow{V}H_q\xrightarrow{W}H_r,
\]

one has

\[
(WV)^*E(WV)=V^*(W^*EW)V.
\]

Therefore effect pullback is strictly contravariant at the operator level, while coupler pullback follows associativity of composition.

## Normalization obstruction from loss

Let \((E_i)_i\) be a normalized detector family on \(H_q\):

\[
\sum_iE_i=I_{H_q}.
\]

After pullback,

\[
\sum_iV^*E_iV=V^*V.
\]

The pulled family remains normalized exactly when \(V\) is an isometry. For a proper contraction it is subnormalized. The missing positive effect is

\[
E_{\rm loss}=I_{H_p}-V^*V.
\]

Adding this as a declared no-detection or loss channel restores normalization. It is not permissible to renormalize the detected effects silently, because that conditions on detection and changes the operational model.

This supplies an analytic obstruction absent from the finite typed-port model: loss does not block effect transport, but it blocks preservation of normalized detector completeness unless the missing channel is retained.

## Frequency-dependent fields

A decomposable propagation operator may be given by a measurable Jones-operator field

\[
(V\psi)(\omega)=V(\omega)\psi(\omega).
\]

Bounded transport requires

\[
\operatorname*{ess\,sup}_{\omega\in\Omega}
\|V(\omega)\|<\infty.
\]

Passivity requires this essential supremum to be at most one. Frequency-dependent detector fields obey the same measurability and essential-boundedness conditions. Band changes additionally require a declared measurable frequency map and measure-compatible pullback; equal fiber dimension alone does not define one.

## Categorical consequence

On a category whose port morphisms carry bounded contractions, effect attachments form a contravariant indexed category under conjugation. Normalized detector attachments form such an indexed category only on isometries, or after enlarging every pullback by its explicit loss effect.

Port deletion and multiple geometric preimages remain governed by the previously constructed correspondence semantics. Operator conjugation transports an attachment along one admitted geometric lift; it does not select a lift.

## Exact diagnostic

A two-polarization finite compression uses horizontal and vertical projector effects. Pullback through attenuation \(V=\operatorname{diag}(1,1/2)\) preserves positivity but changes their sum from \(I\) to \(\operatorname{diag}(1,1/4)\). The loss effect is \(\operatorname{diag}(0,3/4)\). Pullback through a polarization swap is normalized, and direct versus iterated conjugation agree exactly.

## Disposition

Continuous-mode optical effect transport is derived by bounded-operator conjugation. Individual effects pull back through contractions; normalized detector families require isometric propagation or an explicit loss channel. This yields a strict operator-level contravariant law on each admitted geometric lift and identifies loss normalization as the principal analytic obstruction.
