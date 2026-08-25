# Prime Hilbert--Schmidt determinant-line cocycle

Author: `marici.Grothendieck`

## 0. Operator stimulus

The operator proposed a sequence in which two half-planes first acquire
distinct identities, their scalar sewing then loses integrality, and the
resulting oval is intrinsically a circle.  The Hilbert--Schmidt reduction
identified the critical seam as the boundary where the prime character
leaves `ell^2`.  This packet identifies the natural two-plane object inside
that chamber: the multiplicative cocycle of the regularized determinant.

## 1. Why literal measure domination is wrong

After removing repeated prime powers, the surviving current is

\[
d\vartheta(x)-dx.
\]

It is tempting to seek a positive Gram defect comparing the atomic measure
`d theta` with Lebesgue measure.  No local domination can hold: a sufficiently
small neighborhood of a prime `p` has arbitrarily small Lebesgue mass but
contains the atom `log(p)`.  Thus source-derived orthogonality cannot mean

\[
dx-d\vartheta\ge0
\]

as a measure, nor an ordinary contraction between the two raw `L^2` spaces.
The comparison must retain a relative or cocycle term.

## 2. The Hilbert--Schmidt determinant cocycle

For `A` in the Hilbert--Schmidt class, the regularized determinant is

\[
\det{}_2(I+A)=\det\bigl((I+A)e^{-A}\bigr).
\]

It is not multiplicative.  If `A` and `B` are Hilbert--Schmidt, then `AB` is
trace class and

\[
\boxed{
\det{}_2((I+A)(I+B))
=\det{}_2(I+A)\det{}_2(I+B)e^{-\operatorname{Tr}(AB)}.
}
\]

The “defect” is not an error.  It is a canonical multiplicative two-cocycle
on the Hilbert--Schmidt group.

For the diagonal prime operators

\[
P_s e_p=p^{-s}e_p,
\]

take `A=-P_s` and `B=-P_w`.  Whenever both spectral points lie in the right
chamber,

\[
\operatorname{Tr}(P_sP_w)
=\sum_p p^{-(s+w)}
\]

converges because `Re(s+w)>1`.  Therefore the two-point anomaly is

\[
\boxed{
c(s,w)=
\exp\left(-\sum_p p^{-(s+w)}\right).
}
\]

The individual linear traces need not exist.  Their two-plane product does.
This is the exact analytic sense in which distinction of the two chamber
coordinates precedes a well-defined coupled integral geometry.

## 3. Hermitian metric and seam degeneration

Set `w=bar(s)`.  Then

\[
h(s)=c(s,\bar s)
=\exp\left(-\sum_p p^{-2\operatorname{Re}s}\right)
\]

is positive throughout `Re(s)>1/2`.  As the fixed seam is approached,

\[
h(s)\longrightarrow0
\]

because `sum_p 1/p` diverges.

Thus the regularized determinant line has a canonical Hermitian metric in
the distinguished chamber and that metric degenerates exactly at the
critical line.  Its curvature density is

\[
\boxed{
-\partial_s\partial_{\bar s}\log h(s)
=\sum_p(\log p)^2p^{-2\operatorname{Re}s}>0.
}
\]

The two-plane geometry is therefore positively curved inside the chamber,
while its norm collapses at the seam.

## 4. The completed trace factor is a section

The factor

\[
\mathcal T(s)
=\frac{2\pi^{s/2}\xi(s)}{s\Gamma(s/2)}
\det{}_2(I-P_s)
\]

is naturally read as the completion-selected section of this determinant
line.  In the Euler chamber it equals

\[
(s-1)\exp\left(\sum_p p^{-s}\right),
\]

the exponentiated renormalized linear trace.

Its zeros are not failures of the nonvanishing `det_2` geometry.  They are
zeros of the selected section.  Distributionally,

\[
\frac1{2\pi}\Delta\log|\mathcal T|
=\sum_\rho m_\rho\delta_\rho.
\]

The integer winding around an oval is consequently the divisor charge of a
determinant-line section.  In a local holomorphic frame the oval becomes a
circle; the background cocycle supplies the intrinsic metric in which its
norm is measured.

## 5. What this explains

The operator's picture now has a precise realization:

\[
\boxed{
\begin{array}{c}
\text{prime characters enter the Hilbert--Schmidt chamber;}\\
\text{two chamber coordinates acquire a trace-class pairing;}\\
\text{their regularized determinant has a multiplicative anomaly;}\\
\text{completion selects a scalar section of the anomaly line;}\\
\text{zeros are integral phase defects of that section;}\\
\text{the metric itself degenerates on the fixed seam.}
\end{array}
}
\]

“Loss of integrality” should therefore be typed as failure of a nonvanishing
integral trivialization of the determinant line, not disappearance of the
integer prime labels.

## 6. Why positive curvature is not RH

A positively curved Hermitian line bundle may possess holomorphic sections
with zeros.  Therefore positivity of the cocycle metric does not prove that
`T` is nonvanishing.  The hostile quartet multiplier changes the divisor of
the section while preserving the background symmetry and integral charges.

The missing theorem must couple the completion-selected section to the
cocycle metric strongly enough to exclude interior divisor charge.  Possible
forms are:

1. a covariantly constant or parallel-section identity;
2. a source-derived norm conservation law;
3. a boundary condition plus curvature equation with a uniqueness theorem;
4. a modular sewing law fixing the section as the unique nonvanishing lift
   of its Euler-chamber frame.

Merely computing the positive curvature repeats the earlier mistake of
treating a metric certificate as semantic faithfulness.

## 7. Sharp target

Let

\[
\nabla\mathcal T
=d\mathcal T+\mathcal A\,\mathcal T
\]

be the Chern covariant derivative for the cocycle metric.  The next exact
calculation is to express `nabla T` using the completed theta source and the
primitive-prime discrepancy current.  The desired outcome is not assumed
parallelism, but a closed source equation whose only singular boundary term
is supported at `Re(s)=1/2`.

A chamber-interior source term with nonzero integral would falsify the
determinant-line localization mechanism.

## 8. Scope

The Hilbert--Schmidt cocycle, prime pairing, Hermitian metric, and curvature
formula are exact.  Interpreting `T` as the completion-selected scalar
section is a faithful organization of the established factorization.
No covariant equation excluding zeros has yet been derived.  RH is not
proved.

## 9. First covariant test: prime parallelism fails

In the holomorphic frame used above, the prime cocycle metric has Chern
connection

\[
\mathcal A^{1,0}
=\partial\log h
=\left(\sum_p(\log p)p^{-(s+\bar s)}\right)ds.
\]

Therefore, in the Euler chamber,

\[
\boxed{
\frac{\nabla^{1,0}\mathcal T}{\mathcal T}
=\left[
\frac1{s-1}
-\sum_p(\log p)p^{-s}
+\sum_p(\log p)p^{-(s+\bar s)}
\right]ds.
}
\]

The three terms have distinct types:

1. the endpoint continuum current;
2. the holomorphic primitive-prime trace;
3. the Hermitian two-plane prime norm.

They do not cancel identically.  On the far positive real ray,

\[
\frac{\nabla^{1,0}\mathcal T}{\mathcal T}
=\frac1{s-1}+O(2^{-s}\log2).
\]

Hence `T` is not a parallel section of the prime determinant line.  This
falsifies the simplest item in the target list without touching RH.

The conclusion is structural: the prime cocycle supplies the correct
Hilbert--Schmidt chamber and seam degeneration, but not the full physical
connection.  Endpoint and gamma sectors must alter the metric or enter as a
coupled relative connection before any conservation law can hold.

The revised target is a *completed anomaly line*

\[
\mathcal L_{\rm end}\widehat\otimes
\mathcal L_{\Gamma}\widehat\otimes
\mathcal L_{\rm prime},
\]

with pole cancellation performed before its Chern connection is evaluated.
Treating the three displayed currents as independent positive connections
would repeat the already established endpoint--gamma--prime gluing error.
