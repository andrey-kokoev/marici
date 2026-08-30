# GNS removes the amplitude gauge if the source kernel is already positive and Poisson invariant

The failed labelwise square-root lift suggests the correct order of
construction. One should not choose amplitudes first and then ask Fourier to
act on them. One should construct a source sesquilinear kernel first.

Let \(\mathcal D_\Theta\) be the linear source span of the signed theta/Hermite
density labels, including the external boundary coordinates. Seek a
sesquilinear form

\[
\mathfrak g:\mathcal D_\Theta\times\mathcal D_\Theta\to\mathbb C
\]

such that

\[
\mathfrak g(x,x)\ge0
\]

and the source Poisson involution \(F\) obeys

\[
\mathfrak g(Fx,Fy)=\mathfrak g(x,y).
\]

Then the quotient-completion

\[
\mathcal H_{\mathfrak g}
=
\overline{\mathcal D_\Theta/\operatorname{rad}\mathfrak g}
\]

is canonical up to unitary equivalence. The Poisson action descends to a
unitary on \(\mathcal H_{\mathfrak g}\). Any amplitude realization is merely a
Kolmogorov factorization

\[
\mathfrak g(x,y)
=
\langle Vx,Vy\rangle,
\]

and its phase gauge no longer carries authority.

This gives a clean replacement for the impossible additive rank-one lift.
The source need not assign one rank-one operator to every positive density.
It must supply one positive Poisson-invariant polarized kernel on the full
linear source.

The theorem is still nontrivial because the obvious candidates divide:

- the linear density pairing is Poisson-natural but has no established Green
  positivity;
- the square-root overlap is positive but has no inherited linear Poisson
  covariance;
- the mixed \(K\)-\(\Phi\) Bezoutian retains orientation and Green transfer,
  but its positivity is equivalent to a matrix-monotonicity theorem for the
  response ratio \(R=P/I\).

Therefore the first analytic inequality can now be stated exactly. On each
declared real zero-free interval, prove that

\[
\frac{R(y)-R(x)}{x-y}
\]

has the sign required by the congruence factors in the mixed Bezoutian, at all
matrix levels, not only on the diagonal. If this holds and the Poisson action
preserves the kernel, GNS produces the Hilbert carrier and unitary sewing
without any square-root choice.

Three independent gates remain:

1. positivity of every finite mixed-Theta Gram;
2. invariance of its radical under Poisson sewing;
3. joint faithfulness of the interior Green and external boundary ports after
   quotient.

The radical condition is essential. Equality of scalar kernels under Poisson
does not define a quotient action if \(F(\operatorname{rad}\mathfrak g)\) is
not contained in the radical.

The sharp hostile is a kernel whose diagonal values are positive and
Poisson-invariant but whose \(2\times2\) Gram determinant is negative. A
second hostile has a positive kernel but a Poisson map that moves a null
source direction into a visible one. Either blocks the GNS carrier before
completion.

Thus the representation-selection problem contracts to a kernel theorem:

> Derive a positive polarized mixed theta Green kernel on the linear source,
> prove Poisson invariance including its radical, and take its GNS
> completion.

This is preferable to inventing doubled amplitudes: the source kernel, rather
than an arbitrary factorization, fixes the completed geometry.
