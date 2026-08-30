# 2272 — The Spectral Gaussian Source Gives a Finite-\(q\) Transfer with No Physical Rank Loss

## Frozen source enlargement

Entry 2267 proves that the scalar weighted-correlator source does not determine
a finite-soft tensor continuation.  Before inspecting any rank locus, freeze
the minimal covariant massless Gaussian precision operator

\[
A_g=\sqrt{-\Delta_g}.
\]

On the flat boundary this gives the radial precision \(A_0(k)=k\), and hence
the covariance \(K(k)=1/(2k)\) used by the conformal massless scalar state.
This is a declared source model, not a reconstruction fitted to a desired
determinant.

## Finite-momentum metric vertex

For a spectral function \(A=\sqrt L\), its Fréchet derivative between
eigenmodes of \(L\) with eigenvalues \(k^2\) and \(k'^2\) is

\[
(\delta A)_{p'p}
=
\frac{k'-k}{k'^2-k^2}(\delta L)_{p'p}
=
\frac{(\delta L)_{p'p}}{k'+k}.
\]

Take a transverse traceless metric mode \(h_s(q)\), with
\(p'=-p-q\).  Freeze the symmetric finite-soft slice in which \(q\) is
normal to the plane of the three equilateral hard momenta.  Transversality
removes the \(p_iq_j\) term, so up to the
common sign convention

\[
(\delta L)_{p'p}
=h_s^{ij}p_ip_j.
\]

Thus each labelled occurrence receives a positive physical weight

\[
w_e(q)=\frac{k_e^2}{k_e+\sqrt{k_e^2+q^2}}>0
\]

times its plus/cross quadrupole contraction.  A common nonzero normalization
does not affect rank.

## Homogeneous three-occurrence transfer

In the integral scaled angular convention, the scalar-plus-cross transfer is

\[
T(q)=
\begin{pmatrix}
1&2w_1&0\\
1&-w_2&-w_2\\
1&-w_3&w_3
\end{pmatrix}.
\]

Its determinant factors exactly as

\[
\boxed{
\det T(q)
=-2(w_1w_2+w_2w_3+w_3w_1).
}
\]

For positive finite energies every \(w_e>0\), hence

\[
\det T(q)<0.
\]

There is no physical positive-energy finite-\(q\) rank-loss locus on this
source-defined symmetric slice.  Generic orientations remain a separate
extension of the test.

## Covariance checks

- **Gauge:** only transverse traceless contractions survive; longitudinal
  additions proportional to \(q_i\) vanish.
- **Cyclic:** rotating the labelled triangle and \(q\) permutes the three
  \(w_e\) and rows; the determinant factor is symmetric.
- **Ward:** as \(q\to0\), \(w_e\to k_e/2\), reproducing Entry 2254's
  quadrupole Ward response up to its common source normalization.

## Rank-loss classification

Over the complexified base, possible degeneracy is

\[
w_1w_2+w_2w_3+w_3w_1=0,
\]

or a failure of the spectral denominators \(k_e+|p_e+q|\).  Neither meets the
positive-energy chamber.  The denominator conditions are ordinary energy
support of the enlarged coefficient object, not new occurrence incidence.

This is a progressive protective-belt result: it establishes finite-\(q\)
contextual faithfulness for the frozen spectral Gaussian source on the normal
tensor-momentum slice, not for every orientation or possible covariantization
of the scalar state.

## Verification

`research/benincasa/checkers/spectral_gaussian_finite_q_transfer.rs` verifies
the divided-difference identity, determinant factorization, and strict
positive-energy sign on 512 exact weight packets.
