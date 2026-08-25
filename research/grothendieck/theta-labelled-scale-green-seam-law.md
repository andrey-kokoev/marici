# Labelled scale flow has an exact positive seam defect

Author: `marici.Grothendieck`

## 1. Continuous label coordinate

Extend the positive scale labels from (q=\log n) to (q\ge0) by

\[
 \psi_q(u)=e^{-q/4}\psi_0(u+q),
 \qquad
 \psi_0(u)=\sqrt{\phi_1(u)},
 \qquad u\ge0.
\]

Then

\[
 (\partial_q-\partial_u)\psi_q=-\frac14\psi_q.
\]

Define the continuous labelled overlap

\[
 S(q,r;z)=\int_0^\infty e^{izu}\psi_q(u)\psi_r(u)\,du.
\]

The arithmetic matrix is recovered at (q=\log n, r=\log m).

## 2. Exact infinitesimal seam law

Differentiate under the integral.  Since

\[
 (\partial_q+\partial_r)(\psi_q\psi_r)
 =\partial_u(\psi_q\psi_r)-\frac12\psi_q\psi_r,
\]

integration by parts gives

\[
\boxed{
 (\partial_q+\partial_r+\tfrac12+iz)S(q,r;z)
 =-\psi_q(0)\psi_r(0).}
\]

In the coordinates

\[
 c=\frac{q+r}{2},
 \qquad d=q-r,
\]

this is

\[
\boxed{
 (\partial_c+\tfrac12+iz)S(c,d;z)
 =-b(c,d),}
\]

where

\[
 b(c,d)
 =e^{-c/2}
 \sqrt{\phi_1(c+d/2)\phi_1(c-d/2)}.
\]

This recovers exactly the moving-endpoint derivative found in the overlap
formula.

## 3. The infinitesimal defect is rank one and positive

As a kernel in the two label coordinates,

\[
 b(q,r)=a(q)a(r),
 \qquad a(q)=\psi_q(0).
\]

Thus the entire infinitesimal seam defect is the positive rank-one operator

\[
 |a\rangle\langle a|.
\]

The transport equation has the architecture

\[
 \boxed{
 \text{scale flow}
 +\text{spectral drift}
 =-\text{positive rank-one seam current}.}
\]

This is the continuous labelled analogue of the finite repair channels found
in the prime-two programme.

## 4. Exact finite prime-step identity

Let (ell=\log p).  The label shift obeys

\[
 \psi_{pn}(u)=p^{-1/4}\psi_n(u+\ell).
\]

Therefore

\[
\boxed{
 S_{mn}(z)-p^{1/2+iz}S_{pm,pn}(z)
 =B^{(p)}_{mn}(z),}
\]

where the finite sewing block is

\[
 B^{(p)}_{mn}(z)
 =\int_0^{\log p}e^{izu}\psi_n(u)\psi_m(u)\,du.
\]

At (z=iy), the matrix (B^{(p)}(iy)) is positive semidefinite because it is
the Gram matrix of

\[
 e^{-yu/2}\psi_n(u)\mathbf 1_{[0,\log p]}(u).
\]

For real (z\ne0), it is an oscillatory compression and is not automatically
positive.  The positive infinitesimal defect integrates to a phase-weighted
finite seam block.

## 5. Iterated valuation filtration

Iterating the prime-step identity yields

\[
 S_{mn}(z)
 =\sum_{j=0}^{k-1}p^{j(1/2+iz)}
 B^{(p)}_{p^jm,p^jn}(z)
 +p^{k(1/2+iz)}S_{p^km,p^kn}(z).
\]

When the terminal term decays in the relevant chamber, the overlap is an
infinite sum of transported seam blocks.  This is a matrix-valued
(p)-valuation decomposition, not merely the scalar prime recursion.

It retains cross-label correlations at every depth.

## 6. Deutschian audit

The law explains why scale transport necessarily generates a boundary repair
and why the infinitesimal repair has rank one.  Those facts are difficult to
vary once the positive translated label source and the fixed fold are given.

However, the derivation used only

\[
 \psi_q(u)=e^{-q/4}\psi_0(u+q)
\]

and half-line integration.  It applies to every sufficiently decaying
positive primitive (psi_0).  Therefore it is **not theta-specific** and
cannot by itself explain RH.

The new separation is:

\[
\begin{array}{ccl}
\text{translation plus fold}
&\Longrightarrow&
\text{positive rank-one seam law},\\
\text{theta Poisson coherence}
&\stackrel{?}{\Longrightarrow}&
\text{orientation of its oscillatory finite-step sum}.
\end{array}
\]

The second arrow remains the load-bearing theorem.

## 7. Next falsifier

Choose a hostile positive primitive (widetilde\psi_0), build all translated
labels by the same rule, and form (widetilde S).  It automatically satisfies
the rank-one infinitesimal law and every prime-step identity above.

Hence any proposed proof using only these identities is universal and cannot
distinguish theta from the hostile source.  The next admissibility condition
must involve the primal--dual Poisson correspondence of the primitive itself.

The cheapest discriminating calculation is therefore:

\[
\boxed{
\text{derive the Poisson action on the boundary vector }a(q)=\psi_q(0)
\text{ and its finite seam Gram blocks }B^{(p)}.}
\]

If the action closes to a positive or sign-regular doubled operator for theta
but not for the hostile primitive, labelled coherence has acquired genuine
RH-relevant content.

## 8. Scope

The continuous seam equation, rank-one boundary kernel, finite prime-step
identity, positivity on the nonoscillatory axis, and valuation iteration are
exact.  Their universality is also explicit.  No oscillatory orientation,
Poisson matrix correspondence, off-seam coercivity, or RH result is claimed.
