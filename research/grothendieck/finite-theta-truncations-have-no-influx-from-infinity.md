# Finite theta truncations have no influx from infinity

## Question

Can a nonreal zero branch of the completed-theta truncation

\[
X_L(z)=2\int_0^L\Phi(u)\cos(zu)\,du
\]

enter from spectral infinity while the support endpoint \(L\) varies through
an ordinary compact interval?

## Endpoint expansion

Fix

\[
0<L_0\le L\le L_1<\infty.
\]

Assume \(\Phi\in C^2([0,L_1])\), \(\Phi(L)>0\), and
\(\Phi'(0)=0\), as supplied by the smooth positive even completed source.
Twice integrating by parts gives

\[
\frac{X_L(z)}2
=
\frac{\Phi(L)\sin(Lz)}z
+
\frac{\Phi'(L)\cos(Lz)}{z^2}
-
\frac1{z^2}\int_0^L\Phi''(u)\cos(zu)\,du.
\]

The leading term is the endpoint jump produced by support truncation.  On the
compact \(L\)-interval, \(\Phi(L)\) has a positive lower bound, while the two
remainder coefficients have uniform upper bounds.

## Sine-type consequence

The standard rectangular-contour Rouché argument applied to the expansion
has three parts.

1. Outside fixed small disks around the real lattice

   \[
   z=\frac{k\pi}{L},
   \]

   the leading sine term dominates for sufficiently large \(|z|\), uniformly
   over \(L\in[L_0,L_1]\).

2. In each sufficiently remote lattice disk, the same comparison gives
   exactly one zero, counted with multiplicity.

3. The disk is invariant under conjugation and the function is real entire.
   A unique zero in such a disk must therefore be real.  Its multiplicity is
   one.

Consequently there is a radius \(R=R(L_0,L_1,\Phi)\) such that every zero of
every \(X_L\) with \(L\in[L_0,L_1]\) and \(|z|>R\) is real and simple.

This is the precise finite-support meaning of sine-type endpoint dominance.
It uses the nonzero boundary value \(\Phi(L)\), not RH or zero data.

## No finite-parameter influx

Suppose a nonreal branch appeared from spectral infinity at a finite parameter
\(L_*>0\).  Choose a compact interval

\[
0<L_0<L_*<L_1<\infty.
\]

The uniform radius above confines every nonreal zero throughout that interval
to \(|z|\le R\), contradicting influx from infinity.  Therefore a nonreal
branch can enter or leave the finite plane at an ordinary finite \(L) only
through a finite multiple-zero event.

For real branches, the first possible seam departure is consequently governed
by

\[
\int_0^L\Phi(u)\cos(xu)\,du=0,
\qquad
\int_0^L u\Phi(u)\sin(xu)\,du=0.
\]

## The two singular parameter boundaries

The uniform estimate deliberately excludes the two boundary regimes.

### Vanishing window

As \(L\downarrow0\), the spectral lattice itself escapes at scale \(1/L\).
The rescaled compact-window limit is sinc, but a separate uniform theorem is
needed to control the complete rescaled divisor.

### Completed support

As \(L\to\infty\), the endpoint coefficient satisfies

\[
\Phi(L)\longrightarrow0
\]

superexponentially.  The radius at which the endpoint sine term dominates can
therefore diverge.  The hard cutoff discontinuity disappears in the completed
limit, and the sine-type barrier is lost.

The loss of a uniform sine-type radius is analytically important, but it does
not permit a finite zero to appear only in the completed limit.  Local uniform
convergence \(X_L\to X\) and Hurwitz force every finite zero of \(X\) to be
approximated by bounded zeros of finite truncations.  Completion can destroy
the remote-zero asymptotic estimate; it cannot create an isolated finite zero
without finite approximating zeros.

## Sharpened dichotomy

The previous two-mechanism statement now collapses further:

1. at every finite \(L>0\), nonreal zeros can be created only at finite real
   multiple-zero collisions;
2. a finite completed zero is still inherited from bounded finite-truncation
   zeros by local uniform convergence, even though the remote sine-type radius
   is not uniform as \(L\to\infty\);
3. the only unresolved source of nonreal finite-truncation branches besides a
   finite collision is the singular initial boundary \(L\downarrow0\), where
   the entire spectral lattice escapes at scale \(1/L\).

The RH-bearing problem is therefore concentrated in two concrete gates: prove
that the complete rescaled small-window divisor is real, and exclude the
finite collision equations for the completed theta source.

## Deutsch--Popper target

The proposed explanation is now more rigid:

> The finite support boundary pins the remote divisor to the real sinc lattice.
> If the theta source starts with a globally real rescaled divisor and forbids
> finite multiple-zero collisions, then no authorized path exists by which an
> off-seam zero can ever be formed.

The falsifier is either a finite collision solving the two source equations or
a nonreal zero of the rescaled truncation at arbitrarily small positive \(L\).

## Result

There is no spectral influx from infinity at any finite support parameter, and
local uniform convergence prevents isolated finite zeros from being born only
at completed support.  The remaining formation mechanisms are finite
multiple-zero collisions and the singular small-window divisor at \(L=0\).
