# Virtual–Cut balance cancels the moment-filtration shift

For one observed production jump \(L=a^\dagger\), the trace-balanced adjoint
generator is

\[
\mathcal L^\dagger(O)
=
a O a^\dagger
-\frac12\{aa^\dagger,O\}.
\]

The production term and virtual anticommutator separately raise polynomial
degree by two.  Their principal symbols are identical and cancel.

For number moments \(O=f(N)\), the exact result is

\[
\boxed{
\mathcal L^\dagger f(N)
=(N+1)\bigl[f(N+1)-f(N)\bigr].
}
\]

If \(f\) has degree \(D\), the finite difference has degree \(D-1\), so the
complete expression has degree at most \(D\).  Hence the balanced generator
defines a same-level map

\[
\mathcal L_D:\mathbb M_{\le D}\to\mathbb M_{\le D}
\]

on the number-moment subalgebra, and restriction between degree cutoffs
commutes strictly.

The checker verifies degrees through 32 and the leading coefficient
\(D N^D\).  Extension from number moments to every Weyl monomial requires the
same principal-symbol cancellation, but lower-degree ordering terms must still
be audited in the full phase-space basis.
