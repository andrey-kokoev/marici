# The continuous autocorrelation half-form preserves strict radial faithfulness after completion

## Setting

Let `f` be a nonzero real source on the line and let

\[
X(z)=\int_{\mathbb R}f(u)e^{zu}\,du.
\]

Define its autocorrelation

\[
C(d)=\int_{\mathbb R}f(u)f(u+d)\,du.
\]

Assume `C` is integrable and has the exponential moments required at the
spectral points under consideration. The completed theta source satisfies much
stronger decay than this.

Because `f` is real,

\[
C(-d)=C(d).
\]

Define the continuous analytic half-form

\[
A(z)=\frac{C(0)}2+int_0^\infty C(d)e^{zd}\,dd,
\qquad \operatorname{Re}z<0.
\]

## Positive-real theorem

On the boundary,

\[
2\operatorname{Re}A(it)=|X(it)|^2.
\]

Since `C` is integrable, `A` is bounded and analytic in the left half-plane.
Its real part is the Poisson extension of the nonnegative boundary function
`|X(it)|^2/2`. Because `X` is not identically zero, that boundary function is
not zero almost everywhere. Therefore

\[
\operatorname{Re}A(z)>0
\qquad (\operatorname{Re}z<0).
\]

This is the continuous counterpart of the finite Fejér autocorrelation
half-form.

## Current identity at a zero

Fubini's theorem gives

\[
X(z)X(-z)=A(z)+A(-z).
\]

Define the oriented current

\[
J(z)=A(z)-A(-z)
=\int_0^\infty C(d)(e^{zd}-e^{-zd})\,dd.
\]

At a zero of `X`, the symmetric sum vanishes. Hence

\[
\begin{aligned}
J(z)&=2A(z), &&\operatorname{Re}z<0,\\
J(z)&=-2A(-z), &&\operatorname{Re}z>0.
\end{aligned}
\]

Therefore every zero in the domain of the exponential moments obeys

\[
\begin{aligned}
\operatorname{Re}z<0&\Longrightarrow\operatorname{Re}J(z)>0,\\
\operatorname{Re}z>0&\Longrightarrow\operatorname{Re}J(z)<0.
\end{aligned}
\]

At a boundary zero, the boundary identity gives zero normal component.

## Completion consequence

Strict radial faithfulness is not a fragile finite-matrix lower bound. It is a
pointwise positive-real theorem for the completed autocorrelation itself.
Thus no normalized-sequence escape or vanishing smallest eigenvalue is needed
for this part of the argument.

For the completed theta source, reality and rapid decay provide the required
autocorrelation and exponential moments. Subject to the standard Fubini and
boundary-value audit, the finite theorem passes directly to the full source.

## Remaining singular gate

The RH-bearing content is now concentrated entirely in polarization:

> Why must a zero of the completed theta transform have zero normal
> autocorrelation current?

If modular/adelic sewing supplies that source identity, radial faithfulness
forces the zero onto the critical seam immediately. Without it, the theorem
only assigns an exact outward or inward orientation to every hypothetical
off-seam zero.

The next attack should therefore derive—or finitely falsify—the polarization
identity itself. Completion stability of the radial detector is no longer the
obstruction.

