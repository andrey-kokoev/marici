# Exact positive factorization forces unitary translation covariance after quotient

## Apparent loophole

The preceding obstruction assumed that a source contraction respects translations. Could one construct a noncovariant positive carrier and recover translation invariance only after terminal polarization?

For an exact factorization of the Weil form, the answer is no. Translation covariance is forced on the minimal Hilbert realization even if it is absent from the presentation.

## General theorem

Let `D` be a complex vector space with a real translation action `tau_a`, and let `Q` be a positive semidefinite Hermitian form satisfying

\[
Q(\tau_af,\tau_ag)=Q(f,g)
\qquad(a\in\mathbb R).
\]

Suppose an arbitrary feature map into a Hilbert space realizes it:

\[
Q(f,g)=\langle Af,Ag\rangle_{\mathcal H}.
\]

No covariance of `A` is assumed.

Define the minimal carrier

\[
\mathcal H_A=\overline{\operatorname{span}}A(D).
\]

On its dense generating set, put

\[
U_a(Af)=A(\tau_af).
\]

This is well-defined. Indeed, if `Af=0`, then `Q(f,f)=0`; translation invariance gives

\[
Q(\tau_af,\tau_af)=0,
\]

and hence `A tau_a f=0`. More generally, every linear relation among feature vectors remains a relation after translation.

Moreover,

\[
\langle U_aAf,U_aAg\rangle
=Q(\tau_af,\tau_ag)
=Q(f,g)
=\langle Af,Ag\rangle.
\]

Thus `U_a` extends uniquely to an isometry of `H_A`. Since `U_{-a}` is its inverse,

\[
\boxed{
U_a\text{ is a unitary group on the minimal positive carrier, and }
U_aA=A\tau_a.
}
\]

Therefore every exact positive factorization of a translation-invariant form has a canonical covariant minimalization.

## Consequence for off-axis evaluation modes

Suppose a continuous linear functional `ell_rho` on the minimal carrier extracts an arithmetic divisor coordinate and satisfies

\[
\ell_\rho(U_aAf)
=e^{-ia\rho}\ell_\rho(Af).
\]

By Riesz representation, `ell_rho(v)=<v,h_rho>` for some Hilbert vector `h_rho`. Then

\[
U_a^*h_\rho=e^{-ia\bar\rho}h_\rho.
\]

Every eigenvalue of a unitary operator has modulus one. Since

\[
|e^{-ia\bar\rho}|=e^{-a\operatorname{Im}\rho},
\]

this is possible for every real `a` only if

\[
\operatorname{Im}\rho=0
\]

or `h_rho=0`.

Hence a faithful bounded divisor readout from any exact positive factorization excludes off-axis divisor coordinates.

## Unbounded readouts do not reproduce the stated form topology

One might let `ell_rho` be unbounded. But if the original test-space form is completed using the norm

\[
\|f\|_Q=Q(f,f)^{1/2},
\]

an evaluation that is not continuous in this norm does not descend to the Hilbert completion. It cannot serve as a bounded terminal observable or participate in a Hilbert Gram factorization there.

Retaining such evaluations requires a rigged Hilbert extension. Their cross-pairing then lies outside the positive Hilbert norm and must be supplied as an additional indefinite boundary form. This is again the Krein realization, not a positive factorization of the complete Weil pairing.

## Application to the Suzuki proposal

Assume one found a possibly noncovariant source map `A_src` with

\[
W(f*g^*)=\langle A_{src}f,A_{src}g\rangle.
\]

Because the Weil convolution form is translation invariant, minimalizing `A_src` automatically produces the unitary group above. Thus deliberately breaking covariance in the source presentation cannot evade the off-axis character obstruction.

The same applies to a factorization built from endpoint, gamma, and prime sectors with complicated noncovariant intermediate maps. If the final Hilbert inner product equals the complete Weil form, its closed minimal span carries canonical unitary translations.

## Relation to RH equivalence

This theorem does not independently prove positivity of the Weil form. It explains why every successful exact positive factorization necessarily contains a Hilbert--Polya representation after minimalization: translation invariance manufactures a unitary group, and its self-adjoint generator supports only real spectral parameters.

Therefore searching for a noncovariant positive factorization cannot be easier in principle. The spectral confinement is not an optional property imposed on the constructor; it is forced by positivity plus exact equality.

## Remaining possibility: restricted, non-invariant observer spaces

A finite rung-four family need not be invariant under every translation. On such a subspace, a positive factorization need not carry a full unitary group and can exist without deciding the global zero geometry. This is the legitimate local loophole.

But universal positivity over all centers closes that loophole: the translation orbit generates an invariant dense subspace, and the unitary minimalization theorem applies.

## Disposition

The covariance assumption in the global contraction no-go is redundant:

\[
\boxed{
\text{positive exact factorization}
+
\text{translation invariance of the Weil form}
\Longrightarrow
\text{unitary covariance on the minimal carrier}.
}
\]

Consequently no noncovariant source presentation can hide exponentially growing off-axis characters inside a positive Hilbert norm. It can only postpone their appearance to an unbounded or indefinite terminal boundary form.
