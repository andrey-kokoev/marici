# The wall–tail cross term does not vanish from the history factorization alone

## Scope

This note tests the proposed shortcut

\[
\operatorname{Re}\langle f,Bf\rangle=0,
\qquad B=H_KD,
\]

on the represented first-Adams incidence range.  It does **not** identify the
completed Green form and does not close G1.1.

## Exact operator identity

The established integrated-tail factorization is

\[
H_\Phi=M_\Phi I+B,
\qquad B=H_KD.
\]

Therefore

\[
B+B^*=H_\Phi+H_\Phi^*-2M_\Phi I
\]

and

\[
2\operatorname{Re}\langle f,Bf\rangle
 =\langle f,(H_\Phi+H_\Phi^*-2M_\Phi I)f\rangle.
\]

Thus the desired vanishing is equivalent to an **isometry-on-the-range
condition for the symmetric part** of theta convolution:

\[
\langle f,(H_\Phi+H_\Phi^*)f\rangle
 =2M_\Phi\|f\|^2.
\]

It is not a consequence of the Volterra factorization, parity, or the ordered
port identity by themselves.

## Minimal exact hostile

Take a two-frequency Hilbert model with

\[
H_\Phi=\operatorname{diag}(M,M-a),\qquad
B=H_\Phi-MI=\operatorname{diag}(0,-a),
\]

where \(M>0\) and \(a>0\).  For the non-wall mode \(f=e_2\),

\[
\operatorname{Re}\langle f,Bf\rangle=-a\ne0.
\]

The model preserves the exact mass-plus-tail decomposition and has a
self-adjoint convolution multiplier.  Hence neither self-adjointness nor the
mass split forces cross-term cancellation away from the wall mode.

## Fourier reduction for the actual incidence vectors

Whenever the completed realization is a translation-invariant convolution
model with multiplier \(m_\Phi(\xi)\), Plancherel gives

\[
\operatorname{Re}\langle f,Bf\rangle
 =\int \bigl(\operatorname{Re}m_\Phi(\xi)-M_\Phi\bigr)
       |\widehat f(\xi)|^2\,d\xi.
\]

Consequently, for the candidate even and odd generators one must evaluate

\[
\int (\operatorname{Re}m_\Phi-M_\Phi)|\widehat\Phi|^2,
\qquad
\int (\operatorname{Re}m_\Phi-M_\Phi)
       |\widehat{\Phi'}|^2.
\]

These are the first concrete scalar tests.  Parity only removes mixed
odd/even pairings; it does not make either diagonal integral zero.

## Verdict

The direct-vanishing repair is **not structurally available**.  It can survive
only if the source-authorized completed representation proves the displayed
multiplier integrals vanish on both columns of \(Q_p^{\mathrm{lin}}\).
Otherwise the proof needs an explicit block congruence or Schur cancellation
between the shifted-history graph and Fourier-saturated observer forms.

The earliest unresolved datum is therefore sharper: freeze the completed
multiplier/form domain, evaluate the two diagonal cross terms and their
polarized mixed term, and only then choose between vanishing and congruence.
