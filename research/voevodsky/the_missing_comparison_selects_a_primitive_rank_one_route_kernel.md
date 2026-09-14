# The missing comparison selects a primitive rank-one route kernel

## Question

What structural role remains for the comparison from the anchored rank-three pyramid lattice to the two-coordinate physical response plane?

## Claim boundary

This packet gives the necessary integral normal form. It does not compute the two response coefficients from source periods.

## Rank constraint

The physical anchor and two relative edge flows form a unimodular basis

\[
L=\mathbb Z\langle d_1,\beta_{12},\beta_{13}\rangle
\cong\mathbb Z^3.
\]

The retained physical algebraic response has two coordinates

\[
R=\mathbb Z\langle e_6,v_{\rm alg}\rangle.
\]

Since \(d_1\) is already detected primitively by \(e_6\), choose compatible target and source coordinates so that a candidate integral comparison has the form

\[
Q=
\begin{pmatrix}
1&u&v\\
0&a&b
\end{pmatrix}.
\]

Subtracting \(u\) and \(v\) multiples of the anchored column from the two edge columns is an integral change of response representatives. It reduces the essential map to

\[
Q_{\rm red}=
\begin{pmatrix}
1&0&0\\
0&a&b
\end{pmatrix}.
\]

Thus the entire complementary readout is the primitive covector

\[
(a,b):\mathbb Z\langle\beta_{12},\beta_{13}\rangle\to\mathbb Z.
\]

## Required kernel

The map has full rank two precisely when \((a,b)\ne(0,0)\). Its image is primitive in the physical lattice precisely when

\[
\gcd(a,b)=1.
\]

In that case its route kernel is the primitive line

\[
K_{\rm route}
=
\mathbb Z\langle b\beta_{12}-a\beta_{13}\rangle.
\]

The complementary transmitted direction can be chosen by Bézout coefficients \(r,s\) satisfying

\[
ra+sb=1.
\]

Then

\[
r\beta_{12}+s\beta_{13}
\longmapsto v_{\rm alg}.
\]

## Role of the missing thing

The comparison is therefore not meant to make all three primitive pyramid directions observable in two coordinates. Its role is to:

1. preserve the anchored \(e_6\) vertex primitively;
2. select one primitive linear combination of the two route flows as \(v_{\rm alg}\);
3. identify the orthogonal algebraic issue—not necessarily metric orthogonality—as a source-derived rank-one route kernel;
4. prove that this quotient is saturated, equivalently \(\gcd(a,b)=1\).

Without the kernel declaration, a two-coordinate readout silently discards one coherence direction. Without the gcd condition, it retains the direction only with an integral index defect.

## Information flow

The correct flow is

\[
L
\longrightarrow
L/K_{\rm route}
\xrightarrow{\sim}
\mathbb Z\langle e_6,v_{\rm alg}\rangle
\longrightarrow
\text{physical period readout}.
\]

The quotient occurs after the four vertex classes and their coherent edge transports have been assembled. Quotienting earlier would prevent the route kernel from being identified as a relation among actual paths.

## Disposition

The missing comparison plays the role of a primitive route quotient. Its complete integral certificate is reduced to two integers \((a,b)\), with acceptance conditions \((a,b)\ne0\) and \(\gcd(a,b)=1\), plus proof that the resulting kernel line is the physically null route relation.

Verification:

- `research/voevodsky/checkers/check_primitive_rank_one_route_kernel.py`
- `research/voevodsky/results/primitive_rank_one_route_kernel.json`
