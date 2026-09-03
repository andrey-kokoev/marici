# Widder representation and Angenent zero number do not exclude Weil double contact

## Problem

A proposed closure of the finite-contact gate combines the exact heat equation for the normalized shifted-Gaussian Weil kernel with Widder representation of nonnegative heat solutions and Angenent's zero-number theorem.

## Bold conjecture tested

If a nonzero heat solution is nonnegative on the broad-variance side of a first threshold, Widder representation and zero-number monotonicity force strict positivity at the threshold and therefore exclude a finite double contact.

## Named rival

A nonnegative threshold trace may have an isolated even-order zero. Forward Gaussian convolution immediately makes it strictly positive, while backward continuation may become negative. Both Widder and Angenent permit this configuration.

## Exact falsifier

Let

\[
G_a(x)=\frac1{\sqrt{4\pi a}}e^{-x^2/(4a)}
\]

and choose `A>B>0` and `s_*>0`. Put

\[
c=\sqrt{\frac{B+s_*}{A+s_*}},
\qquad
u(s,x)=G_{A+s}(x)-cG_{B+s}(x).
\]

Each summand solves `partial_s nu=partial_x^2 nu`. Their ratio is

\[
\frac{G_{A+s}(x)}{G_{B+s}(x)}
=
\sqrt{\frac{B+s}{A+s}}
\exp\!\left(
\frac{(A-B)x^2}{4(A+s)(B+s)}
\right).
\]

For fixed `s`, the ratio has its unique minimum at `x=0`. At `s=s_*` that minimum equals `c`. Hence

\[
\nu(s_*,x)\ge0,
\qquad
\nu(s_*,0)=\partial_x\nu(s_*,0)=0,
\qquad
\partial_x^2\nu(s_*,0)>0.
\]

The minimum ratio increases strictly with `s`, so

\[
\nu(s,x)>0\quad(s>s_*),
\qquad
\nu(s,0)<0\quad(s<s_*).
\]

## Widder compatibility

The threshold trace `mu(dx)=nu(s_*,x)dx` is a nonzero positive measure. For every `tau>0`, the Gaussian semigroup gives

\[
\nu(s_*+\tau,\cdot)=G_\tau*\mu.
\]

This is already a Widder representation. It yields strict positivity for positive `tau` because the Gaussian kernel is strictly positive, but it does not imply strict positivity of the density of `mu` at `tau=0`. Thus the desired contact is compatible with Widder's conclusion.

## Angenent compatibility

At the threshold the zero at `x=0` has even multiplicity two. On the narrower side it bounds a negative interval; on the broader side the two boundary zeros have merged and disappeared. This is the zero-number drop allowed by Angenent's theorem. The theorem does not reverse this implication.

## Exact heat equation for the Weil kernel

With `s=1/(4t)` and the positive scalar normalization converting `exp[-t(u-xi)^2]` to `G_s(u-xi)`, the source-side kernel is

\[
U(s,\xi)=(\mathcal W*G_s)(\xi)
\]

and therefore satisfies

\[
\partial_sU=\partial_\xi^2U
\]

as a smooth convolution of a tempered distribution for every `s>0`. Verifying this equation does not distinguish `U` from the falsifier above.

## Strongest surviving requirement

A successful contact exclusion must add a property not shared by arbitrary positive threshold traces. Candidates must be arithmetic and independently verified, for example:

- a strict source-side inequality at every critical point;
- a prime-moment constraint incompatible with the value, slope, and curvature equations;
- a completed Weil-form margin on a window containing the relevant inverse Gaussian factor;
- a source-derived representation forcing the threshold measure to have a strictly positive density everywhere.

The last option cannot assume that the underlying Weil distribution is positive, because that is already the target.

## Disposition

The Widder--Angenent conjecture is falsified with zero residual: the explicit two-Gaussian solution satisfies the exact heat equation, admits a positive Widder trace, obeys Angenent zero-number monotonicity, and realizes the prohibited double contact. The branch is closed unless a new arithmetic hypothesis is supplied. Continue with prime moment matrices and blockwise explicit-formula bounds.
