# The prime-labelled direct sum is a strict Schur arithmetic network

## Upper-half-plane chart

Use the centered chart

\[
s=\frac12-iz,
\qquad
\operatorname{Im}z>0.
\]

For each prime \(p\), let \(L_p=\log p\) and define the oriented delay atom

\[
S_p(z)=p^{-1/2}e^{iL_pz}.
\]

Then

\[
|S_p(z)|
=p^{-1/2}e^{-L_p\operatorname{Im}z}
< p^{-1/2}.
\]

## Labelled direct sum

On the prime coefficient space define

\[
S_{\rm ar}(z)
=
\bigoplus_p S_p(z).
\]

Its operator norm satisfies

\[
\|S_{\rm ar}(z)\|
=
\sup_p|S_p(z)|
\le2^{-1/2}.
\]

Thus the all-prime assembly is a strict operator-valued Schur function with a
cutoff-independent margin

\[
1-2^{-1/2}>0.
\]

No scalar summation occurs. Prime labels are retained, and cutoff inclusion is
ordinary orthogonal direct sum.

## Schur kernel

The de Branges--Rovnyak kernel

\[
K_S(z,w)
=
\frac{
I-S_{\rm ar}(z)S_{\rm ar}(w)^*
}{-i(z-\overline w)}
\]

is positive on the upper half-plane, with the conventional normalization of
the denominator. Positivity holds primewise and hence on the direct sum.

This supplies the multi-parameter passivity certificate that pointwise signs
alone could not provide.

## Cayley boundary law

Since \(\|S_{\rm ar}(z)\|<1\), the source Cayley transform is bounded:

\[
\Theta_{\rm ar}(z)
=i\bigl(I+S_{\rm ar}(z)\bigr)
  \bigl(I-S_{\rm ar}(z)\bigr)^{-1}.
\]

It is an operator-valued Nevanlinna function. With the opposite Green sign
convention, use \(-\Theta_{\rm ar}\) as the anti-Nevanlinna source law.
The sign is fixed by the centered chart orientation, not chosen after a zero
test.

The reciprocal lower-half-plane chart is obtained by Fourier--Poisson
transport and \(s\mapsto1-s\).

## Passive realization

Each delay atom has a conservative shift realization on its valuation or
delay line. Their orthogonal direct sum gives a passive arithmetic
realization of \(S_{\rm ar}\). The Cayley transform converts its scattering
port to an impedance boundary relation.

Minimality reduces labelwise to cyclicity of the boundary vector for each
shift. No cross-prime dark state is introduced by the orthogonal direct sum.

## Euler determinant character

In the Euler domain,

\[
S_p(z)=p^{-s}.
\]

Therefore

\[
\det(I-S_{{\rm ar},X}(z))^{-1}
=
\prod_{p\le X}(1-p^{-s})^{-1}
=
\zeta_X(s).
\]

The powers of each delay loop generate all prime-power grades. Near the
critical strip this determinant must again be interpreted through the
primitive, square, and \(\det_3\) strata; strict Schur boundedness does not
make the all-prime operator trace class.

## What this constructs

The previously unspecified arithmetic/source law now has a canonical
candidate:

\[
D_U(z)=\Theta_{\rm ar}(z)
\]

or its sign-reversed Green convention. It is:

- source-derived from prime delays;
- prime-labelled;
- strict Schur before Cayley transformation;
- Nevanlinna after Cayley transformation;
- cutoff-natural;
- passively realizable.

## Remaining coupled characteristic

The paired history Schur function is

\[
M_U(z)
=
\Theta_{\rm ar}(z)
+B^\dagger(A-z)^{-1}B
\]

with signs fixed by the block convention. Although both summands now have
typed half-plane orientation, no identity yet proves

\[
\det_{\rm rel}M_U(z)=E(z)\xi(s).
\]

Moreover, Cayley transformation changes the scalar determinant by
\(\det(I-S_{\rm ar})^{-1}\) and a numerator factor. Those factors must be
tracked in the graded determinant line to avoid inserting or deleting the
Euler divisor.

## Disposition

A passive, cutoff-natural, all-prime arithmetic constitutive law exists as the
Cayley transform of the strict prime-delay direct sum. This closes existence
of a source \(D_U\) candidate. G4 remains open at its coupled determinant-line
comparison with the theta Xi section and at completed anomaly bookkeeping. No
RH conclusion is authorized.
