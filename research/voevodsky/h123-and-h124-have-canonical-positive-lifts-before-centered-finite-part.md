# H123 and H124 have canonical positive lifts before centered finite part

## Purpose

Construct the positive versions of the two previously available pyramid faces,
so that all four faces are expressed in the same positive-lift language.

## Face H123: source--geometry--spectral

For an observer \(g\), the source representation satisfies

\[
U_S(g*g^*)=U_S(g)U_S(g)^*.
\]

Let \(\mathcal T_S\) denote the canonical/dual Hardy--Titchmarsh unitary from
the semilocal geometric carrier to the spectral carrier. Define

\[
X_{12}(g)=U_S(g),
\qquad
X_{13}(g)=\mathcal T_SU_S(g)\mathcal T_S^*.
\]

Then

\[
X_{13}(g)^*X_{13}(h)
=
\mathcal T_S
X_{12}(g)^*X_{12}(h)
\mathcal T_S^*.
\]

Thus \(H_{123}\) has an exact positive lift: it is unitary transport of the
source Gram, not merely equality after a signed trace.

For the \(k\)-successor \(\mathsf S_k\), functoriality of the semilocal
amplification and Hardy--Titchmarsh transform gives

\[
\boxed{
\mathsf S_k(H_{123,k}^{+})=H_{123,k+1}^{+}.}
\]

No centering or asymptotic quotient is needed for this face.

## Face H124: source--geometry--cutoff

Let \(P_\Lambda\) be the physical cutoff, \(Q_\Lambda\) its Fourier conjugate,
and \(A_g=U_S(g)\). The ordered cutoff product is not itself an ordinary
positive Gram at finite regulator. Its canonical positive lift is the exact
eight-leg feature

\[
\Theta_{24,\alpha}(g)
=\frac1{\sqrt2}
\bigl(\Psi_\alpha(P_\Lambda A_g),\Psi_\alpha(A_g)\bigr),
\]

with the actual transported left/right regulator placements retained. Its fixed
Hermitian and skew matrix readouts recover respectively

\[
\frac12(P_\Lambda\Delta Q_\Lambda+
\Delta Q_\Lambda P_\Lambda)
\]

and the placement commutator. Thus positivity belongs to the ambient eight-leg
Gram, while the cutoff trace is a signed matrix coefficient of that Gram.

The volume term has an independent source-derived positive feature. With the
Plancherel map \(j_S:g\mapsto\lambda_S(g)\), set

\[
X_{vol,\Lambda}(g)=\sqrt{2\log\Lambda}\,j_S(g).
\]

Then

\[
\langle X_{vol,\Lambda}(g),X_{vol,\Lambda}(h)\rangle
=2\log\Lambda\,\tau_S(\lambda_S(h)^*\lambda_S(g)).
\]

Therefore the positive lift of \(H_{124}\) is the pair

\[
\boxed{
H_{124,\alpha}^{+}(g)
=\bigl(\Theta_{24,\alpha}(g),X_{vol,\Lambda}(g)\bigr),}
\]

with fixed signed readout \(K_8\oplus(-I)\). Applying that readout recovers the
centered cutoff form; no claim that the ordered product itself is positive is
made.

## k-axis law for H124

For \(L=\log\Lambda\), the volume coordinate obeys the exact cocycle

\[
\|X_{vol,L'}(g)\|^2-
\|X_{vol,L}(g)\|^2
=2(L'-L)\|j_S(g)\|^2.
\]

The cutoff feature is transported by the exact physical successor and its
ordered boundary becomes stationary in the trace-norm asymptotic quotient.
Thus

\[
\boxed{
\mathsf S_k(H_{124,k}^{+})=H_{124,k+1}^{+}}
\]

when \(H_{124}^{+}\) is typed in the affine positive category carrying both
the cutoff Gram and its source-volume coordinate. Collapsing the pair to the
centered scalar before transport would lose this exact law.

## Consequence for the four-face pyramid

The positive-face status is now:

- \(H_{123}^{+}\): exact unitary Gram transport;
- \(H_{124}^{+}\): exact regulated cutoff Gram plus exact affine volume
  cocycle;
- \(H_{134}^{+}\): requires the Sonin/endpoint Douglas contraction;
- \(H_{234}^{+}\): requires the physical common-remainder lift.

The first two positive faces therefore supply the fixed sides of the positive
horn. The Schur--Douglas condition for the other two is the only missing
positive filler datum; it is not contaminated by an unresolved choice on
\(H_{123}\) or \(H_{124}\).

## Claim boundary

This construction does not assert positivity of the centered Weil finite part.
It realizes centering as a signed readout of two positive coordinates. That is
the correct positive lift of Connes's asymptotic face.
