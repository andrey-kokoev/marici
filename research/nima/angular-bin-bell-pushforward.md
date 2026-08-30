# Angular-bin Bell pushforward

Let \(x=\sin^2(\theta/2)\), so the massless two-body angular measure is a
constant multiple of \(dx\).  In the low-energy photon packet,

\[
\Phi_1=g,s^2,
\qquad
\Phi_2=2f,s^2(1-x+x^2),
\qquad
\Phi_5=0.
\]

For a helicity-blind angular bin \([L,U]\), the supported state is not obtained
by averaging normalized states or pointwise Bell values.  The canonical
positive pushforward is

\[
\rho_{[L,U]}
=
\frac{\int_L^U |\psi(x)\rangle\langle\psi(x)|\,dx}
{\int_L^U\langle\psi(x)|\psi(x)\rangle\,dx}.
\]

Writing

\[
W_0=\int_L^Udx,
\quad W_1=\int_L^U(1-x+x^2)dx,
\quad W_2=\int_L^U(1-x+x^2)^2dx,
\]

the exact Bell value is

\[
I_{[L,U]}
=\frac{8\sqrt2,gfW_1}{g^2W_0+4f^2W_2}.
\]

For the complete angular interval,

\[
I_{[0,1]}
=\frac{(20\sqrt2/3)gf}{g^2+(14/5)f^2}.
\]

All four probability tables normalize, and both no-signalling families vanish
identically.  The theorem extends to any common nonnegative scalar acceptance
weight.  Outcome- or setting-dependent acceptance is excluded by Entry 1578's
counterexample unless an independent state-specific support theorem is proved.

Reproduce with:

```text
uv run --with sympy python research/nima/check_angular_bin_bell_pushforward.py
```
