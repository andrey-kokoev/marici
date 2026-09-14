# The regular anticanonical del Pezzo complement is torsion-free

## Question

Can topology exclude the zero parity class \((a,b)=(0,0)\) before computing the Picard action?

## Geometric input

A degree-two del Pezzo surface is the blow-up of \(\mathbb P^2\) at seven points in general position. Its integral Picard group has basis

\[
H,E_1,\ldots,E_7
\]

and anticanonical class

\[
[D]=-K_S=3H-E_1-\cdots-E_7.
\]

This vector is primitive because its coefficients have greatest common divisor one. For a regular parameter value, the infinity divisor \(D\) is a smooth connected genus-one curve. Let

\[
U=S\setminus D.
\]

## Gysin calculation

The integral Gysin sequence contains

\[
H^0(D;\mathbb Z)
\overset{[D]}{\longrightarrow}
H^2(S;\mathbb Z)
\longrightarrow
H^2(U;\mathbb Z)
\longrightarrow
H^1(D;\mathbb Z)
\longrightarrow
H^3(S;\mathbb Z).
\]

Here

\[
H^2(S;\mathbb Z)\cong\mathbb Z^8,
\qquad
H^1(D;\mathbb Z)\cong\mathbb Z^2,
\qquad
H^3(S;\mathbb Z)=0.
\]

The first map sends \(1\) to the primitive vector \([D]\), so its cokernel is free of rank seven. Therefore there is a short exact sequence

\[
0\longrightarrow\mathbb Z^7
\longrightarrow H^2(U;\mathbb Z)
\longrightarrow\mathbb Z^2
\longrightarrow0.
\]

Since the quotient is free, the sequence splits as abelian groups. Consequently

\[
H^2(U;\mathbb Z)\cong\mathbb Z^9.
\]

In particular, the regular ambient complement has no integral torsion.

## Effect on the extension parity

The four local presentations obey

\[
L_{a,b}
=
\frac{\mathbb Z\langle e_6,v_{\rm alg},m\rangle}
{\langle2m-ae_6-bv_{\rm alg}\rangle}.
\]

Their torsion order is \(\gcd(2,a,b)\). Thus \(L_{0,0}\) contains \(\mathbb Z/2\), whereas the other three presentations are free.

If \(L_{a,b}\) is realized as the indicated integral subquotient inside the regular complement lattice, torsion-freeness excludes

\[
(a,b)=(0,0).
\]

The ambient parity is therefore nonzero:

\[
(a,b)\in\{(1,0),(0,1),(1,1)\}.
\]

## Scope

This uses the smooth regular anticanonical fiber and the standard integral Gysin sequence. It does not identify which nonzero class occurs, and it does not assert that the singular fiber complement has the same cohomology without a specialization theorem.

Combined with the preceding symmetry enumeration, a nontrivial induced involution on the parity plane would now select its unique nonzero fixed vector.

## Disposition

The zero parity class is excluded for an extension embedded in the regular degree-two del Pezzo complement. The remaining decisive calculation is the induced mod-two Picard action of either quartic involution, or one direct integral intersection distinguishing the three nonzero classes.
