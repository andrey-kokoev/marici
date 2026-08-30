# Bounded rational lift tomography

## Question

WP985 asks what becomes faithful after the UV lift grammar in WP984 is frozen
to finite polynomial degree.

Let \(\Gamma,A,B,C\) be polynomials in a declared threshold coordinate
\(\epsilon\), with nonzero constant terms and degree bounds

\[
d_\Gamma,quad d_A,quad d_B,quad d_C.
\]

The normalized response is rational:

\[
R(\epsilon)
=\frac{N(\epsilon)}{D(\epsilon)}
=\frac{\Gamma(\epsilon)^2A(\epsilon)^4}
{B(\epsilon)C(\epsilon)^5}.
\]

Its degree bounds are

\[
M=2d_\Gamma+4d_A,qquad
Q=d_B+5d_C.
\]

## Finite response theorem

Take two normalized rational responses \(R_i=N_i/D_i\), with
\(D_i(0)=1\), numerator degree at most \(M\), and denominator degree at most
\(Q\). If their Taylor coefficients agree through order \(M+Q\), then

\[
N_1D_2-N_2D_1
\]

has degree at most \(M+Q\) and a zero of order at least \(M+Q+1\).
Therefore it vanishes identically and \(R_1=R_2\).

The complete jet tower through order

\[
K=M+Q
]

is thus faithful on the bounded rational response family.

## Constructor kernel remains

Response faithfulness is not UV-constructor faithfulness. The distinct
polynomial lifts

\[
U_1:quad \Gamma=(1+\epsilon)^2,quad A=1,
\]

and

\[
U_2:quad \Gamma=1,quad A=1+\epsilon
\]

with \(B=C=1\) both give

\[
R(\epsilon)=(1+\epsilon)^4.
\]

They agree at every jet order despite assigning the deformation to different
source vertices. No response-only instrument can distinguish them.

## Contextual partition

The bounded jet tower has two different faithfulness statements:

- it is faithful on normalized rational response functions;
- it identifies UV constructors only modulo exact equality of their full
  response functions.

Source identification requires complementary probes that couple differently
to \(\Gamma,A,B,C\), not merely higher derivatives of the same scalar
response.

The smallest falsifier is a source-generated multi-channel threshold family
whose joint response map has zero kernel on the frozen UV constructor domain.

## Reproduction

Run:

    python research/flavor/checkers/wp985_bounded_rational_lift_tomography.py

The generated result is
research/flavor/results/wp985_bounded_rational_lift_tomography.json.
