# The RH A2 exchange is the generalized-minor law of relative-flag transport

Author: `marici.Nima`

Date: 2026-08-26

Status: exact minor algebra and divisor-typing theorem

## Relative transporter

The source-generated positive-root word

\[
M(a,b,c)=X_1(a)X_2(b)X_1(c)
\]

has the explicit form

\[
M(a,b,c)=
\begin{pmatrix}
1&a+c&ab\\
0&1&b\\
0&0&1
\end{pmatrix}.
\]

This matrix is the finite relative transporter between the reference flag and
the moving flag. Its meaningful coordinates are not only its entries. They
include generalized minors selected by ordered primal and dual ports.

## Four nontrivial minor coordinates

Define

\[
P=M_{13}=ab,
\qquad
Q=M_{23}=b,
\qquad
R=M_{12}=a+c,
\]

and let (S) be the minor using rows (1,2) and columns (2,3):

\[
S=
\det
\begin{pmatrix}
a+c&ab\\
1&b
\end{pmatrix}
=bc.
\]

They satisfy the exact exchange relation

\[
QR=P+S.
\]

This is the finite Plücker relation behind the (A_2) coordinate mutation.
After one frozen coordinate is normalized to unity, it takes the familiar
form in which a product of exchanged variables equals one plus the remaining
monomial.

The relation is not fitted to a pentagon. It follows directly from the
ordered minors of the source-generated relative transporter.

## Reconstruction on the open cell

When (Q\ne0), the chamber parameters are reconstructed by

\[
a=\frac{P}{Q},
\qquad
b=Q,
\qquad
c=\frac{S}{Q}.
\]

The exchange relation then gives

\[
R=\frac{P+S}{Q}.
\]

Thus the flag-minor packet retains the factorization data on the open cell.
Scalar determinant compression does not: every transporter above has
determinant one.

## Three different divisor types

The exact coordinates separate three failures.

### Factorization chart wall

The braid refactorization used previously divides by

\[
R=a+c.
\]

Hence (R=0) is a chart wall. The matrix (M) remains invertible there, and
the complete relative flag need not be singular.

### Positive-chamber boundary

The positive chamber requires

\[
P>0,
\qquad
Q>0,
\qquad
S>0.
\]

These conditions recover (a,b,c>0). A sign change in one chamber minor is
an orientation failure even if the braid chart remains valid.

### Distinguished-readout divisor

An RH zero can be identified with one of these divisors only after the
theta/Tate construction proves which generalized minor, or which section of
the associated line bundle, equals the completed scalar readout.

Without that identification, neither (R=0), (P=0), nor (S=0) may be
called the Riemann-zero locus. They are different ordered-port failures.

## Categorical meaning

The relative-flag category carries a functor to a minor algebra:

- source constructor words map to relative transporters;
- ordered primal--dual probes map transporters to generalized minors;
- the braid cell maps to the Plücker exchange relation;
- chart walls map to localization failures;
- positivity maps to a sign chamber of real minor values.

The scalar determinant functor sends every (M(a,b,c)) to one and therefore
forgets the entire exchange geometry. A theta readout must instead be a named
minor functor with source authority.

## Decisive next gate

Construct the finite theta/Tate relative transporter in the same ordered
three-port frame and compute all four minors before scalar projection. Then
identify the completed scalar section among them by an exact source-derived
equality.

The route is falsified if:

- the four source minors do not obey (QR=P+S);
- no fixed ordered minor equals the scalar section;
- equality requires a spectral-dependent frame chosen after seeing zeros;
- the claimed positive chamber changes under an admitted presentation.

This is now the smallest finite bridge from the categorical (A_2) object to
an RH-bearing scalar divisor.

