# Fixed-width Gaussian Hardy packets are total, so leakage vanishing is not a weaker gate

## Proposed weakening

The Hardy-block audit reduced a Suzuki-based proof to forcing

\[
H_\Theta f=0,
\qquad
H_\Theta=P_-M_\Theta|_{H^2_+},
\]

not necessarily for every Hardy vector, but perhaps only for the Gaussian observer family.

This note tests whether that restriction is genuinely weaker.

## Totality theorem

Fix `t>0` and put

\[
g_t(x)=e^{-t x^2}.
\]

Let

\[
f_{t,a}=P_+\tau_a g_t,
\qquad
(\tau_a g_t)(x)=g_t(x-a),
\qquad a\in\mathbb R.
\]

Then

\[
\boxed{
\overline{\operatorname{span}}\{f_{t,a}:a\in\mathbb R\}=H^2_+.
}
\]

### Proof

Under the Fourier realization `H^2_+ = L^2(0,infinity)`, one has, up to normalization,

\[
\widehat{f_{t,a}}(\lambda)
=1_{(0,\infty)}(\lambda)
 e^{-ia\lambda}e^{-\lambda^2/(4t)}.
\]

Suppose `h in L^2(0,infinity)` is orthogonal to every such vector. Then

\[
0=
\int_0^\infty
h(\lambda)e^{-\lambda^2/(4t)}e^{ia\lambda}\,d\lambda
\qquad(a\in\mathbb R).
\]

The product

\[
h(\lambda)e^{-\lambda^2/(4t)}1_{(0,\infty)}(\lambda)
\]

belongs to `L^1(R)` by Cauchy--Schwarz. Its Fourier transform vanishes everywhere. Fourier uniqueness implies the product vanishes almost everywhere. Since the Gaussian multiplier is strictly positive, `h=0`. The orthogonal complement is therefore trivial.

## Consequence for Suzuki leakage

The Hankel leakage `H_Theta` is bounded because `Theta` is unimodular on the boundary. If

\[
H_\Theta f_{t,a}=0
\qquad\text{for every }a\in\mathbb R
\]

at even one fixed width `t>0`, continuity and totality imply

\[
H_\Theta=0
\quad\text{on all of }H^2_+.
\]

Thus

\[
\boxed{
\text{exact leakage cancellation on all Gaussian centers at one width}
\iff
\text{full Hardy invariance}.
}
\]

In the completed-zeta specialization, the right side is the same innerness/Hermite--Biehler gate used by Suzuki. Restricting to a continuum of Gaussian centers therefore does not weaken the universal problem.

## Derivative and finite-rung variants

Applying finitely many center derivatives multiplies the Fourier packet by powers of `lambda`:

\[
\widehat{\partial_a^j f_{t,a}}(\lambda)
=(-i\lambda)^j e^{-ia\lambda}e^{-\lambda^2/(4t)}1_{(0,\infty)}.
\]

For every fixed `j`, the multiplier is nonzero almost everywhere on `(0,infinity)`. The same proof shows that all translates of any one derivative order are total. Consequently rung four does not avoid the obstruction if its parameter family includes every center and exact leakage vanishing is asserted centerwise.

Likewise, restricting the width to a nonempty set does not help: one positive width already suffices.

## What remains weaker

There are only three genuine restrictions:

1. **finitely many centers:** gives a finite-dimensional compression and cannot imply full innerness;
2. **a compact center interval with no analyticity propagation:** potentially weaker, although the Fourier transform above is analytic enough that exact vanishing on an open interval often propagates to every center;
3. **an inequality rather than vanishing:** for example, a source-derived estimate comparing the indefinite Weil term with `||H_Theta f||^2`.

The second option is also largely closed. For Gaussian packets, the map

\[
a\longmapsto H_\Theta f_{t,a}
\]

is weakly real-analytic (indeed it has Gaussian Fourier decay). If it vanishes on any nonempty open interval, scalarization against every target vector and analytic continuation force it to vanish for all real `a`. Totality again gives `H_Theta=0`.

Therefore no continuum-box exact cancellation theorem can be an intermediate abstract result: it either stays approximate or proves the full innerness gate.

## Intertwined source maps

Suzuki's actual source feature is `P_D varphi`, not automatically the bare packet `P_+ tau_a g_t`. To transfer the theorem one needs a source-side intertwiner

\[
P_D\varphi_{t,a}=A f_{t,a}
\]

with `A:H^2_+ -> H^2_+` bounded and having dense range. Under that hypothesis, vanishing of `H_Theta P_D varphi_{t,a}` for every center again gives `H_Theta=0`.

Hence a proposed Gaussian exception must identify a genuine failure of dense range in the exact Suzuki source map. Merely observing that the tests are Gaussian or rung four is insufficient.

## Revised constructive target

The additive identity cannot have exact zero leakage on a universal Gaussian orbit without proving RH. A noncircular intermediate theorem must instead retain the defect:

\[
Q_W(\varphi)
=
Q_S(\varphi)
-\|H_\Theta A\varphi\|^2
+Q_{\mathrm{res}}(\varphi),
\]

and prove that the positive bulk dominates the leakage plus any residual cross term on the desired restricted family.

This is not a `Suzuki squared` tautology: it asks for an exact source comparison identifying which Hardy block enters the arithmetic form. The next algebraic task is to derive that comparison from Suzuki's meromorphic expansion of `P_D`, without assuming the zero-indexed orthonormal basis.

## Disposition

The hoped-for weaker inclusion

\[
P_D(\text{all Gaussian centers})\subseteq\ker H_\Theta
\]

is unlikely to be intermediate. Whenever the source map has dense Hardy range, it is equivalent to

\[
H_\Theta=0.
\]

Universal Gaussian exact cancellation therefore collapses back to RH. The only viable abstract use of the Hardy defect is a quantitative domination identity, not a vanishing theorem.
