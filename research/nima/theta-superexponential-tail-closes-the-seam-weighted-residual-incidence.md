# Theta superexponential decay closes the seam-weighted residual incidence

Author: `marici.Nima`

## Question

The seam-length rigging gives the prime coefficient space

\[
 \mathcal E_{\rm seam}
 =\left\{x:\sum_p (\log p)|x_p|^2<\infty\right\}.
\]

The weighted-adjoint theorem reduced the joint boundary return to one
source-specific condition:

\[
 \sum_p\frac{\|r_p\|_{\mathcal H}^2}{\log p}<\infty,
\]

where

\[
 r_p=-p^{-1/2}\Phi\,\mathbf 1_{(\log p,\infty)}
\]

is the tail omitted by the prime seam cut. This packet verifies that condition
for the declared theta source, including the derivative and position controls
of the Mellin--de Rham graph norm.

## Declared source

On the positive folded chart,

\[
 \Phi(u)=\sum_{n\ge1}\phi_n(u),
\]

with

\[
 \phi_n(u)=
 \left(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}\right)
 e^{-\pi n^2e^{2u}}.
\]

This is the density presentation. No amplitude square root or fitted source is
introduced.

## Source-tail estimate

Put \(x=ne^u\). Each summand of \(\Phi\), and each summand obtained after one
derivative in \(u\), is a finite sum of terms of the form

\[
 n^a e^{bu}e^{-\pi n^2e^{2u}}.
\]

For every fixed polynomial degree, Gaussian absorption gives constants
\(C,c>0\) such that, for \(u\ge0\),

\[
 |\Phi(u)|+|\Phi'(u)|+u|\Phi(u)|
 \le C e^{-c e^{2u}}.
\]

Indeed, polynomial factors in \(x\) are absorbed into
\(e^{-(\pi/2)x^2}\), and the remaining sum over \(n\) is bounded by a
geometric Gaussian tail. The extra factor \(u\) is absorbed in the same way.

Consequently, for the graph norm

\[
 \|f\|_{\mathcal H}^2
 =\int_0^\infty
 \left(|f|^2+|f'|^2+u^2|f|^2\right)du,
\]

there are constants \(C_1,c_1>0\) with

\[
 \|\Phi\mathbf 1_{(R,\infty)}\|_{\mathcal H}^2
 \le C_1e^{-c_1e^{2R}}
 \qquad(R\ge0).
\]

The cutoff indicator is used only to denote the restricted tail; no
distributional derivative of the indicator is included. The seam endpoint is
an independently typed boundary port.

At \(R=\log p\), this becomes

\[
 \|r_p\|_{\mathcal H}^2
 \le \frac{C_1}{p}e^{-c_1p^2}.
\]

Therefore

\[
 \sum_p\frac{\|r_p\|_{\mathcal H}^2}{\log p}
 \le C_1\sum_p\frac{e^{-c_1p^2}}{p\log p}<\infty.
\]

## Consequence

The residual-tail hypothesis in the weighted-adjoint theorem is not an open
analytic assumption for the theta source. The seam-weighted incidence is
Hilbert--Schmidt, and every boundary-mediated return

\[
 R=B^*GB
\]

is trace class when \(G\) is bounded. On the centered seam, boundedness of the
reciprocal boundary resolvent therefore makes the relative Schur correction
trace class.

This does not regularize the bare Euler loop. Its primitive and square grades
still require the third regularized determinant. The result only proves that
the new boundary-mediated comparison is an ordinary Fredholm perturbation of
that already typed arithmetic object.

## Falsifier

The argument fails for a source whose restricted graph tails satisfy only

\[
 \|\Phi\mathbf 1_{(R,\infty)}\|_{\mathcal H}^2\asymp R^{-\alpha}.
\]

At prime seams this yields at best a logarithmic decay and does not by itself
force the weighted prime sum to converge. Thus the conclusion uses the actual
Gaussian theta source, not merely smoothness or membership in an unrestricted
Hilbert space.

## Remaining frontier

The joint prime boundary block now has its required completion class. The next
source gates are:

1. adjoin the archimedean and projective-infinity ports to the same Schur
   system;
2. prove reciprocal dagger compatibility of the relative Fredholm factor;
3. identify the resulting determinant-line comparison with the declared
   anti-diagonal phase observer;
4. only then test whether a zero-state can carry a nonzero boundary current.

