# The charge-window cross-character pairing is an exact boundary Stokes value

## Setup

Let
\[
O(q)=\operatorname{sgn}(q)
\]
be the canonical odd boundary-charge representative, and let
\[
V_L(q)=W_{2L}(q)-W_L(q)
\]
be the adjacent comoving-window residual.

Each \(W_t\) is even and vanishes at both spatial ends. Hence \(V_L\) is even, zero-charge, and its derivative \(DV_L\) is odd.

## Exact cross-character identity

On the distributional Stokes core,
\[
\langle O,DV_L\rangle
=
\int_{\mathbb R}\operatorname{sgn}(q)V_L'(q)\,dq.
\]

Integration by parts gives
\[
\langle O,DV_L\rangle
=
-\langle DO,V_L\rangle.
\]
Since
\[
DO=2\delta_0,
\]
we obtain
\[
\langle O,DV_L\rangle
=
-2V_L(0).
\]

Using
\[
W_t(0)=H(t)-H(-t)=2H(t)-1,
\]
the constant terms cancel in the difference:
\[
V_L(0)=2\bigl(H(2L)-H(L)\bigr).
\]
Therefore
\[
\langle O,DV_L\rangle
=
4\bigl(H(L)-H(2L)\bigr).
\]

Because \(H\) is strictly decreasing,
\[
\langle O,DV_L\rangle>0
\qquad(L>0).
\]

This is the first exact nonzero cross-character Green/Stokes pairing between the canonical charge channel and the comoving zero-charge residual.

## Equivalent incidence form

The same scalar is visible at the incidence level:
\[
\langle \delta_0,V_L\rangle
=
V_L(0)
=
2\bigl(H(2L)-H(L)\bigr).
\]

The two expressions are linked by the exact boundary relation
\[
\langle O,DV_L\rangle
=
-2\langle\delta_0,V_L\rangle.
\]

Thus the sign and normalization do not come from a fitted imaginary Gram entry. They come from the source orientation
\[
DO=2\delta_0
\]
and distributional integration by parts.

## Prime-labelled specialization

For \(L=\log p\),
\[
\beta_p
=
4\bigl(H(\log p)-H(2\log p)\bigr)
>0.
\]

The construction is exactly prime-diagonal and cutoff-natural because it acts independently on each labelled interval.

Moreover,
\[
0<\beta_p\le4.
\]
Hence Euler loading by
\[
p^{-1/2-\sigma}\cdot\frac12p^{-1}
\]
produces an absolutely summable diagonal series dominated by
\[
2\sum_p p^{-3/2-\sigma},
\]
uniformly through \(\sigma=0\).

So this cross block has no primitive seam divergence.

## What this closes

The following local gates are now exact:

- opposite reflection characters are respected;
- the charge and residual channels remain separate;
- the mixed pairing is nonzero with source-fixed sign;
- prime diagonality and cutoff naturality hold;
- Euler-loaded global upper convergence holds through the seam.

## What remains open

The coefficient \(\beta_p\) is a geometric window value. It has not yet been identified with the frozen arithmetic Euler odd coefficient or primitive first cumulant.

Also,
\[
\beta_p\to0
\]
as \(p\to\infty\), because both \(H(\log p)\) and \(H(2\log p)\) approach the same tail limit. Therefore this raw pairing is not uniformly coercive in the unweighted prime frame.

It may nevertheless be exactly the correct bounded mixed incidence after Euler normalization. The required theorem is a source comparison between \(\beta_p\) and the arithmetic charge coefficient in the declared weighted metric.

## Hostile

A direct pairing of the even delta incidence with the odd derivative incidence vanishes:
\[
\langle\delta_0,DV_L\rangle=V_L'(0)=0.
\]
The nonzero source pairing requires one return-level channel and one incidence-level channel, or the equivalent integration-by-parts comparison. Pairing both at the same parity level loses orientation.

## Frontier

The first Adams edge now has an explicit local candidate:
\[
O
\quad\text{paired with}\quad
D(W_{2L}-W_L),
\]
with exact value
\[
4\bigl(H(L)-H(2L)\bigr).
\]

The next irreducible calculation is arithmetic calibration, not construction of the local cross-character form.
