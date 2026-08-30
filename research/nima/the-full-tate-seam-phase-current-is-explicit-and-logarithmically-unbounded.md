# The full Tate seam-phase current is explicit and logarithmically unbounded

Write the critical-seam Tate coefficient as

\[
\chi_\infty(1/2+it)=e^{i\theta_\infty(t)}
\]

in the continuous branch with \(\theta_\infty(0)=0\). From event 10276,

\[
\frac{d}{ds}\log\chi_\infty(s)
=
\log\pi
-\frac12\psi((1-s)/2)
-\frac12\psi(s/2).
\]

On \(s=1/2+it\), the two digamma arguments are conjugate. Therefore the
entire phase-current family is

\[
\theta_\infty'(t)
=
\log\pi
-
\operatorname{Re}
\psi\left(\frac14+\frac{it}{2}\right).
\]

At \(t=0\), this recovers

\[
\theta_\infty'(0)
=
\log\pi+\gamma+\frac{\pi}{2}+3\log2.
\]

Reciprocity gives

\[
\theta_\infty(-t)=-\theta_\infty(t),
\]

so \(\theta_\infty'\) is even. The oriented one-form

\[
\theta_\infty'(t)\,dt
\]

is nevertheless reciprocal-odd because \(dt\) reverses under \(t\mapsto-t\).
This is the correctly typed odd port; classifying the scalar coefficient
alone by parity gives the wrong answer.

## High-frequency behavior

The digamma asymptotic

\[
\psi(z)=\log z-\frac1{2z}+O(|z|^{-2})
\]

in fixed sectors yields

\[
\theta_\infty'(t)
=
\log\frac{2\pi}{|t|}
+
O(|t|^{-2})
\]

as \(|t|\to\infty\). Hence the phase-current coefficient is logarithmically
unbounded below.

This has three consequences:

1. it is an orientation/connection current, not a positive Green energy;
2. uniform boundedness can be required only on compact \(t\)-ranges unless a
   source counterterm is present;
3. any completed odd observer over the full vertical seam must use a weighted
   or relative topology that admits logarithmic order.

The natural relative current is

\[
\theta_{\mathrm{rel}}'(t)
=
\theta_\infty'(t)-\log\frac{2\pi}{\langle t\rangle},
\]

but such a subtraction is authorized only if the source archimedean endpoint
cell supplies the reference logarithm. It cannot be introduced merely to
obtain a bounded function.

## Linking target

The causal-history/Wronskian theorem now has a complete scalar target:

\[
J_{\mathrm{Wr}}(t)
\stackrel{?}{=}
\log\pi
-
\operatorname{Re}
\psi\left(\frac14+\frac{it}{2}\right)
\]

with the orientation carried by \(dt\), and with any relative subtraction
derived from the same source cell.

The sharp hostile matches the central slope but replaces the current by a
bounded even function. It passes the \(t=0\) test while failing the
high-frequency gamma asymptotic and therefore cannot be the Tate seam
constructor.
