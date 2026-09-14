# The same-parity record lattice repairs the Aspect readout integrally

## Question

Is the determinant-two defect of the Aspect complementary readout intrinsic, or does it disappear when the codomain is given its actual image lattice?

## Claim boundary

This constructs the minimal integral codomain on which the simulation readout is an isomorphism. It does not establish that a laboratory record system realizes this lattice.

## Image lattice

For

\[
R=
\begin{pmatrix}
1&-1\\
1&1
\end{pmatrix},
\]

define

\[
L_{\rm rec}=\operatorname{im}R
=\{(u,v)\in\mathbb Z^2:u=v\pmod2\}.
\]

A basis is

\[
\lambda_1=(1,1)^T,
\qquad
\lambda_2=(-1,1)^T.
\]

These are exactly the columns of \(R\). Therefore

\[
R:\mathbb Z^2_{\rm route}\longrightarrow L_{\rm rec}
\]

has identity coordinate matrix in the route basis and \((\lambda_1,\lambda_2)\) record basis. It is an integral isomorphism.

## Primitive closed record

The primitive closed route vector

\[
z=(1,1)^T
\]

maps to

\[
Rz=(0,2)^T=\lambda_1+\lambda_2.
\]

Although \((0,2)\) is nonprimitive in the ambient lattice \(\mathbb Z^2\), it is primitive in \(L_{\rm rec}\): its coordinates in the record basis are \((1,1)\), whose gcd is one. The apparent doubling is therefore a codomain-lattice mismatch, not information loss inside the image lattice.

## Detector coordinates

The dark and complementary scalar coordinates remain integer-valued on \(L_{\rm rec}\), but they obey the parity constraint

\[
u=v\pmod2.
\]

They are not two independently selectable integer counters. A record with values \((0,1)\), for example, is outside the admitted lattice.

## Relation to the conductor defect

Typing the readout codomain as \(L_{\rm rec}\) repairs the route/readout index-two mismatch completely. It does not repair

\[
H_0(B)\cong(\mathbb Z/2)^2
\]

in the conductor comparison, because that defect occurs in a different degree and lattice. No cancellation or transfer follows from the matching prime.

## Physical acceptance test

A physical realization must establish one of the following from detector construction and calibration:

1. allowed joint records form the same-parity lattice \(L_{\rm rec}\);
2. a finer ambient record lattice exists together with an independently calibrated reason that only \(L_{\rm rec}\) is reached by coherent route states.

Independent arbitrary integer dark and complementary counts would instead make \(R\) non-surjective and reinstate the index-two mismatch.

## Disposition

The Aspect complementary readout is integrally exact when its codomain is its same-parity image lattice. The remaining issue is physical authority for that record lattice, not algebraic invertibility of the route readout. The conductor two-primary defect remains unchanged.
