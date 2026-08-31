# The G3-to-G4 unit arrow is one normalized Schur-return identification

> **Superseded target.** The successor packet
> `a-holomorphic-relative-return-cannot-be-similar-to-a-nonconstant-positive-green-schur-return.md`
> proves that the holomorphic-similarity route proposed here is generically
> impossible. Retain the calculations below only as a sufficient-condition
> diagnostic, not as the active G4 frontier.

## Positive G3 block

On the coherent/disagreement decomposition, write the retained positive Green
Gram as

\[
\mathbb B(s)=
\begin{pmatrix}
B_{cc}(s)&B_{cd}(s)\\
B_{dc}(s)&B_{dd}(s)
\end{pmatrix}.
\]

The G3 mixed margin gives

\[
N(s)=B_{cc}(s)^{-1/2}B_{cd}(s)B_{dd}(s)^{-1/2},
\]

\[
\|N(s)\|\le1-\delta_{\rm mix}<1.
\]

Its positive Schur return on the coherent block is

\[
Q_G(s)
=B_{cc}^{-1}B_{cd}B_{dd}^{-1}B_{dc}.
\]

Conjugation by \(B_{cc}^{1/2}\) gives

\[
B_{cc}^{1/2}Q_GB_{cc}^{-1/2}=N N^*.
\]

Therefore

\[
r(Q_G)\le\|N\|^2
\le(1-\delta_{\rm mix})^2<1.
\]

In particular, \(I-Q_G\) is invertible with a cutoff-uniform inverse bound.
If \(Q_G\in\mathcal S_2\), then

\[
\det_2(I-Q_G)
e0.
\]

## Analytic G4 return

The closed-loop determinant cone instead supplies

\[
K_{\rm rel}(s)
=(I-L(s))^{-1}B(s)^\dagger(I-A(s))^{-1}B(s).
\]

The symbols in these two formulas have different present types:

- \(B_{cc},B_{dd}\) are positive Green Gram blocks;
- \(B_{cd}\) is the coherent/disagreement mixed Gram;
- \(I-L\) is the ordered analytic Euler-loop block;
- \(I-A\) is the analytic boundary-history block;
- \(B^\dagger\) is the seam-metric incidence adjoint.

Equal source labels and equal dimensions do not identify the returns.

## Exact missing comparison

A sufficient G3-to-G4 comparison is a bounded holomorphic similarity
\(S(s)\) satisfying

\[
S(s)K_{\rm rel}(s)S(s)^{-1}=Q_G(s)
\]

on the reduced carrier, with cutoff-natural extensions to the completed
charts.  A slightly weaker admissible datum is an analytic intertwiner that is
bijective on all generalized eigenvalue-one root spaces and preserves their
Keldysh chains.

Under the similarity,

\[
r(K_{\rm rel}(s))<1,
\]

so the reciprocal relative determinant section is a holomorphic unit:

\[
d_{\rm rel}(s)=\det_2(I-K_{\rm rel}(s))\ne0.
\]

The inverse bound also excludes spectral pollution at eigenvalue one under
\(\mathcal S_2\)-norm completion.

## Consequence for the Xi section

The theta Mellin--Poisson functional already trivializes the Euler,
primitive, square, seam, endpoint, and archimedean determinant-line section as
\(\xi(s)\).  The relative line may be tensored into that compiler only as a
unit.  The comparison above supplies exactly that unit theorem.

After it is proved, zeros and their multiplicities are unchanged by the
relative factor, while every relative eigenvalue-one collision retains its
closed cone-state interpretation.  Without it, the relative determinant may
introduce an additional divisor and cannot be silently included in the Xi
compiler.

## Why a scalar determinant identity is insufficient

One cannot define the comparison unit as

\[
\xi(s)/d_{\rm rel}(s).
\]

That quotient assumes the absence and multiplicity of the relative divisor.
The required arrow must compare the two source operator returns before taking
determinants.

## Reduced G4 frontier

The scalar Xi trivialization and the reciprocal relative determinant line are
separately constructed.  Their remaining compatibility is the single typed
operator question:

\[
K_{\rm rel}
\quad\text{versus}\quad
Q_G.
\]

Proving a source-derived similarity or generalized-root-space equivalence
turns the G3 mixed margin into the G4 unit theorem.  No current scalar
calculation supplies that comparison, so no RH conclusion is authorized.
