# The four-component Clifford bicomplex separates the local Weil current from the oscillator index but does not yet produce endpoint evaluation

## Four Clifford directions

Let `gamma_1,...,gamma_4` be Hermitian `4x4` matrices satisfying

\[
\gamma_j\gamma_k+
\gamma_k\gamma_j
=2\delta_{jk}I_4.
\]

On

\[
\mathcal H=L^2(\mathbb R_t)\otimes\mathbb C^4,
\]

define

\[
D=-i\partial_t,
\qquad
X=M_t.
\]

For a finite prime set `S`, let

\[
A_S(t)=A_\infty(t)+
\sum_{p\in S}
\operatorname{Im}\log(1-p^{-1/2-it}),
\]

and put

\[
V_S=A_S'.
\]

The proposed total Clifford operator is

\[
\boxed{
\mathbb D_S
=
\gamma_1D+
\gamma_2A_S+
\gamma_3X+
\frac12\gamma_4.
}
\]

The four terms represent spectral differentiation, local-factor phase, endpoint coordinate, and endpoint displacement `1/2`.

## Exact square

The scalar multiplication operators `A_S` and `X` commute. The mass `1/2` commutes with every scalar coefficient, while its Clifford generator anticommutes with the other generators. Hence all cross terms vanish except those containing `D`:

\[
[D,A_S]=-iV_S,
\qquad
[D,X]=-iI.
\]

Define the Hermitian involutions

\[
\Gamma_{12}=-i\gamma_1\gamma_2,
\qquad
\Gamma_{13}=-i\gamma_1\gamma_3.
\]

Then

\[
\boxed{
\mathbb D_S^2
=
D^2+A_S^2+X^2+
\frac14
+
\Gamma_{12}V_S
+
\Gamma_{13}.
}
\]

This is the desired algebraic separation:

- `Gamma_12 V_S` contains gamma and all finite-prime powers;
- `Gamma_13` is the canonical endpoint/Heisenberg orientation;
- the positive scalar bulk is oscillator-like;
- all phase-square cross-prime terms remain only in the common scalar bulk.

## Matrix-channel extraction

The Clifford trace relations give

\[
\operatorname{tr}_{Cl}(\Gamma_{12})=0,
\qquad
\operatorname{tr}_{Cl}(\Gamma_{13})=0,
\]

\[
\operatorname{tr}_{Cl}(\Gamma_{12}^2)=4,
\qquad
\operatorname{tr}_{Cl}(\Gamma_{13}^2)=4,
\]

and

\[
\operatorname{tr}_{Cl}(\Gamma_{12}\Gamma_{13})=0.
\]

Therefore the two signed directions can be extracted independently from the square:

\[
\frac14\operatorname{tr}_{Cl}
\left(
\Gamma_{12}\mathbb D_S^2
\right)
=V_S,
\]

\[
\frac14\operatorname{tr}_{Cl}
\left(
\Gamma_{13}\mathbb D_S^2
\right)
=I.
\]

At the level of unbounded local symbols, the first identity exactly recovers the completed smooth local Weil current.

## Heat insertion

Because the scalar principal part contains

\[
D^2+X^2,
\]

the operator has compact resolvent under the standard oscillator closure, provided the archimedean phase has the required relative-growth bounds. Thus

\[
e^{-u\mathbb D_S^2}
\]

is expected to be trace class for every `u>0` at a finite prime stage.

For an observer `chi(X)` or a suitably regular representation `vartheta(f)`, define the two matrix-weighted heat traces

\[
T_{loc,S}(u;f)
=
\operatorname{Tr}
\left(
\Gamma_{12}\vartheta(f)
e^{-u\mathbb D_S^2}
\right),
\]

\[
T_{end,S}(u;f)
=
\operatorname{Tr}
\left(
\Gamma_{13}\vartheta(f)
e^{-u\mathbb D_S^2}
\right).
\]

The first nonzero local heat coefficient of `T_loc,S` is proportional to the pairing with `V_S`. Hence it reproduces the gamma--prime current after the same small-time normalization as the two-component calculation.

## Failure of the naive endpoint extraction

The second Clifford channel extracts the constant symbol

\[
\frac14\operatorname{tr}_{Cl}
(\Gamma_{13}\mathbb D_S^2)=1.
\]

Its heat coefficient consequently produces a real-axis integral or oscillator index term. The completed endpoint functional instead requires analytic evaluations

\[
\widehat g(i/2),
\qquad
\widehat g(-i/2),
\]

and, on convolution squares,

\[
2\operatorname{Re}
\left(
\widehat g(i/2)
\overline{\widehat g(-i/2)}
\right).
\]

A local heat coefficient of a differential operator depends on real-axis jets of its inserted symbol. It cannot equal off-axis analytic evaluation for arbitrary smooth real-axis observers. Analytic continuation is global and is invisible to the local heat expansion.

Thus `Gamma_13` records endpoint **orientation**, but not the endpoint evaluation functional.

## Resolvent rather than heat localization

The endpoint points are zeros of

\[
z^2+
\frac14.
\]

Accordingly their evaluations are naturally residues of the resolvent

\[
(X^2+
\tfrac14)^{-1}
\]

after analytic continuation, not local coefficients of

\[
e^{-u(X^2+1/4)}.
\]

A completed trace must therefore combine two different operations:

1. a graded heat coefficient for the gamma--prime phase derivative;
2. a contour/residue functional for the endpoint pair.

The source functional equation must sew these operations before positivity is considered.

## Candidate mixed trace

At finite Paley--Wiener radius, define schematically

\[
\mathcal T_{S,L}(f)
=
-\lim_{u\downarrow0}
 c_uT_{loc,S}(u;f)
+
\operatorname{Res}_{z=i/2,-i/2}
\operatorname{Tr}
\left(
J_{end}\vartheta(f)
(z-X)^{-1}
\right).
\]

The first term gives gamma plus primes; the second gives the swap-polarized endpoint evaluations. This has the correct source sectors, but it is a sum of signed regularized traces, not an ordinary positive trace.

A successful rung-four formula would need a single nonlocal functional calculus in which the heat coefficient and endpoint residues arise as boundary values of one contour trace. Only then could a contour deformation or reflection-positivity argument potentially turn the completed expression into a positive norm.

## Positivity audit

The total operator square is positive:

\[
\mathbb D_S^2\succeq0.
\]

But both extraction matrices `Gamma_12` and `Gamma_13` have eigenvalues `plus-or-minus 1`. Hence

\[
\operatorname{Tr}
(\Gamma_{jk}B^*B)
\]

is a supertrace and has no fixed sign. Positivity of `mathbb D_S^2` does not imply positivity of either extracted Weil channel.

The four-component construction solves compactness and algebraic separation, not the cone problem.

## Disposition

The four-component bicomplex exists and its square is exactly

\[
\boxed{
\mathbb D_S^2
=D^2+A_S^2+X^2+
\frac14+
\Gamma_{12}V_S+
\Gamma_{13}.
}
\]

It realizes the gamma--prime current as one Clifford coefficient and endpoint orientation as another. The endpoint value itself remains a resolvent residue rather than a heat coefficient.

The next viable construction is a contour trace for the Clifford resolvent whose continuous boundary contribution is the local heat anomaly and whose poles at `plus-or-minus i/2` give the swap endpoint block. Establishing a positive contour factorization of that single trace is the remaining rung-four gate.
