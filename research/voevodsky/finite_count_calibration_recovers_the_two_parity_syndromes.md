# Finite-count calibration recovers the two parity syndromes

## Question

Under Aspect's exact efficiency and independent-dark-count model, can measured three-channel count statistics recover the two source pair-parity observables?

## Claim boundary

This is an exact finite photon-number theorem for occupations \(0,1,2\) in each channel, using the packet's parameters \(\eta=9/25\) and \(d=1/10\). It does not cover afterpulsing, dead time, correlated backgrounds, or actual data.

## Single-channel response

For source occupation \(n\in\{0,1,2\}\), binomial loss followed by an independent Bernoulli dark event gives measured count \(m\in\{0,1,2,3\}\) with

\[
R_{mn}=(1-d)\binom n m\eta^m(1-\eta)^{n-m}
+d\binom n{m-1}\eta^{m-1}(1-\eta)^{n-m+1}.
\]

At the declared calibration values,

\[
R=
\begin{pmatrix}
9/10&72/125&1152/3125\\
1/10&97/250&1424/3125\\
0&9/250&1017/6250\\
0&0&81/6250
\end{pmatrix}.
\]

The first three measured-count rows form a square matrix \(A\) with

\[
\det A=\frac{531441}{15625000}\ne0.
\]

Therefore the source occupation distribution is exactly recoverable from the calibrated probabilities for measured counts zero, one, and two. One left inverse is \((A^{-1}\ 0)\), where

\[
A^{-1}=
\begin{pmatrix}
81130/59049&-15520/6561&2560/729\\
-28250/59049&28250/6561&-8000/729\\
6250/59049&-6250/6561&6250/729
\end{pmatrix}.
\]

## Three-channel inversion

For independent calibrated channels, the joint response is

\[
R^{\otimes3}.
\]

It has full column rank \(27\), and the tensor cube of the single-channel left inverse recovers the complete source distribution on \(\{0,1,2\}^3\).

The source parity expectations then follow by linear evaluation:

\[
\langle O_1\rangle
=
\sum_n(-1)^{n_1+n_3}p_n,
\]

\[
\langle O_2\rangle
=
\sum_n(-1)^{n_2+n_3}p_n.
\]

Thus finite efficiency and independent Bernoulli dark counts do not destroy the two syndrome observables on this declared finite source class; they condition an invertible calibration problem.

## Deliberate failure

Threshold-only detection merges occupations one and two. Its response has fewer distinguishable source columns and cannot recover arbitrary parity on \(\{0,1,2\}\). Likewise, setting \(\eta=0\) makes every optical occupation invisible and collapses the response rank.

## Disposition

The detector-response calibration constructor is exact for the finite three-mode \(0..2\) source class. Remaining physical inputs are raw trial frequencies, validation of independence/no-dead-time assumptions, and the encoder from conductor coordinates to source occupations.
