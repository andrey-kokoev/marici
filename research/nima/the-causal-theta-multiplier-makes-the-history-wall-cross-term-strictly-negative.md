# The causal theta multiplier makes the history–wall cross term strictly negative

## Result

In the established one-sided Hardy realization, the proposed cancellation

\[
\operatorname{Re}\langle f,(H_KD)f\rangle=0
\]

fails for every nonzero represented incidence vector.  Thus the direct
vanishing branch is unavailable; any comparison with the saturated
wall–tail-zero form must use an explicit congruence or Schur cancellation.

This is a statement about the causal-history Hilbert form.  It does not yet
identify the completed relative Green form and does not close G1.1.

## Frozen causal multiplier

Let

\[
m_\Phi(z)=\int_0^\infty \Phi(u)e^{-zu}\,du,
\qquad
M_\Phi=m_\Phi(0)=\int_0^\infty\Phi(u)\,du.
\]

The existing Hardy model gives

\[
H^*\simeq M_{m_\Phi},
\qquad
H\simeq M_{m_\Phi}^*,
\]

and the integrated-tail factorization gives

\[
B=H_KD=H-M_\Phi I.
\]

On boundary frequency \(\omega\), the symmetric multiplier of \(B\) is

\[
\operatorname{Re}m_\Phi(i\omega)-M_\Phi.
\]

## Strict sign

The completed theta kernel is real and positive on the open half-line.  Hence

\[
M_\Phi-\operatorname{Re}m_\Phi(i\omega)
 =\int_0^\infty
   \Phi(u)\bigl(1-\cos(\omega u)\bigr)\,du.
\]

For \(\omega\ne0\), the integrand is nonnegative and is positive on a set of
positive measure.  Therefore

\[
\operatorname{Re}m_\Phi(i\omega)-M_\Phi<0
\qquad(\omega\ne0).
\]

For every nonzero boundary vector \(f\in H^2\) for which the factorization is
represented, Plancherel now yields

\[
\operatorname{Re}\langle f,Bf\rangle
 =\int_{\mathbb R}
   \bigl(\operatorname{Re}m_\Phi(i\omega)-M_\Phi\bigr)
   |f(i\omega)|^2\,d\omega<0.
\]

Indeed a nonzero \(L^2\) boundary function cannot be supported only at the
single frequency \(\omega=0\).

The same polarization statement says that the Hermitian wall–tail correction
on a two-column incidence matrix \(Q=[f_1\ f_2]\) is

\[
C_Q=Q^*(B+B^*)Q,
\]

with

\[
x^*C_Qx
 =2\operatorname{Re}\langle Qx,BQx\rangle<0
\]

for every \(x\) with \(Qx\ne0\).  Thus it is negative definite when the two
incidence columns are linearly independent, and negative semidefinite with
kernel exactly \(\ker Q\) in general.

## Consequence for the two quadratic branches

The shifted-history graph and the saturated observer form differ on the
incidence plane by the nonzero Hermitian block

\[
2M_\Phi\operatorname{Re}(Q^*BQ)
 =M_\Phi Q^*(B+B^*)Q.
\]

It cannot be deleted by parity: parity can force an even–odd mixed entry to
vanish, but both diagonal entries remain strictly negative for nonzero even
and odd columns.

Therefore the next admissible construction is not another vanishing test.  It
is the explicit finite-dimensional pullback comparison:

1. freeze the actual columns of \(Q_p^{\mathrm{lin}}\) in the Hardy carrier;
2. compute the full Hermitian matrix \(Q^*(B+B^*)Q\);
3. retain it in the shifted-history Gram;
4. exhibit a block triangular congruence or Schur complement whose correction
   produces the saturated zero-cross-term Gram;
5. prove that this operation respects the common closed form domain, radical
   descent, cutoff naturality, and prime-uniform bounds.

## Status

This closes only the binary form-selection subquestion: **direct wall–tail
vanishing is impossible in the causal Hardy realization for nonzero incidence
vectors**.  Quadratic functoriality and G1.1 remain open pending the explicit
congruence/Schur comparison and completed Green-domain proof.
