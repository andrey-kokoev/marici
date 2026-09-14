# The first prime crossing adds an infinite-rank truncated-translation defect

## Archimedean window

Connes--Consani choose multiplicative support inside

\[
(1/2,2),
\]

so that the geometric explicit formula contains no rational-prime term. On this window they reduce the remaining archimedean obstruction to one compact hostile mode controlled by the scalar evaluation `g-hat(0)`.

The natural question is whether crossing the first prime merely adds another finite-rank evaluation defect.

## Logarithmic form of a prime contribution

Pass to additive logarithmic coordinates. Let `h` be a test vector supported in an interval `I`, and let

\[
f=h*h^*
\]

be its additive convolution square. For a prime power `q=p^k`, the explicit formula samples

\[
f(\log q)
=
\int_\mathbb R h(x+\log q)\overline{h(x)}\,dx.
\]

Let `T_a` be translation by `a=log q`, with the appropriate compression to the support interval. Then

\[
f(a)=\langle T_a h,h\rangle.
\]

After pairing the reciprocal point `-a`, the Hermitian prime-power contribution is represented, up to its positive arithmetic weight and the global Weil sign, by

\[
T_a+T_a^*.
\]

Thus the first prime does not enter as a scalar evaluation vector. It enters as a truncated shift operator.

## Infinite-rank theorem

Let

\[
A_a=P_I T_a P_I
\]

on `L^2(I)`. If the overlap

\[
I\cap(I-a)
\]

has positive measure, then `A_a` has infinite rank.

Indeed, choose infinitely many orthonormal functions supported in the overlap. Translation sends them to an orthonormal family supported in `I`, and compression does not alter them. Therefore the range of `A_a` contains an infinite orthonormal family.

Consequently

\[
\boxed{
\operatorname{rank}(A_a+A_a^*)=\infty
}
\]

generically whenever the support window is wide enough for the prime shift to overlap itself. Any exceptional cancellation between the two shift directions can be avoided by choosing subintervals whose translated supports are disjoint.

## First-prime threshold

Before the support ratio reaches `2`, the shifts by `plus-or-minus log 2` do not contribute to the explicit formula. Once the window crosses that threshold and the translated support overlaps, the prime-two term activates an infinite-dimensional correlation channel.

Therefore the defect architecture changes discontinuously:

\[
\boxed{
\text{archimedean hostile correction: effectively rank one}
\quad\longrightarrow\quad
\text{first prime correction: infinite-rank truncated shift}.
}
\]

This explains why the Connes--Consani rank-one repair cannot be extended by simply adding one scalar coordinate per prime.

## Finite number of primes does not mean finite-rank defect

For compact multiplicative support, only finitely many prime powers appear. But each one acts on an infinite-dimensional test-function space through a translation compression. Hence

\[
\sum_{p^k\le R}
\frac{\log p}{p^{k/2}}
(A_{\log p^k}+A_{\log p^k}^*)
\]

is a finite sum of infinite-rank operators, not a finite-rank perturbation in general.

The phrase “only finitely many primes” controls arithmetic support, not operator rank.

## Why point evaluations cannot dominate it uniformly

Let `ell_1,...,ell_N` be finitely many continuous scalar endpoint observations. Their common kernel has finite codimension and remains infinite-dimensional. Within a small overlap subinterval one can choose a nonzero `h` annihilated by every `ell_j`. The truncated prime shift correlation can still be nonzero on such an `h`.

Therefore no inequality of the form

\[
|\langle(A_a+A_a^*)h,h\rangle|
\le
C\sum_{j=1}^N|\ell_j(h)|^2
\]

can hold on the full support space. A finite endpoint repair cannot control the first prime channel by itself.

## Required semilocal mechanism

A viable semilocal positive trace must absorb the prime translation into its **bulk** operator, not leave it in a finite-dimensional endpoint remainder. The source carrier must contain a representation of the discrete multiplicative translation `p^k`, and the positive trace comparison must preserve its interference with the archimedean scaling sector.

Thus the desired finite-place identity must have the shape

\[
W_S(g*g^*)
=
\operatorname{Tr}(A_S(g)A_S(g)^*)
-E_{arch}(g)
-E_{boundary,S}(g),
\]

where the prime shifts are already inside `A_S(g)`, while only a genuinely finite-dimensional boundary residue remains outside.

Treating the prime sum itself as `E_boundary,S` cannot retain a rank-one or finite-rank repair theorem.

## Relation to cross-prime polarization

Different prime shifts act on the same `L^2(I)` carrier. A common positive trace can therefore retain cross-prime products when `A_S(g)` is squared. Assigning separate scalar defects to each prime would instead orthogonalize those channels and erase deterministic cross-prime polarization.

The infinite-rank result consequently supports the common-carrier requirement established in earlier audits.

## Disposition

Crossing the first prime threshold fundamentally changes the operator problem:

\[
\boxed{
\text{the prime-two contribution is an infinite-rank truncated translation,
not one additional endpoint atom.}
}
\]

The archimedean rank-one correction remains useful only if a semilocal trace construction incorporates every active prime shift into the positive bulk before terminal polarization. No finite collection of endpoint evaluations can dominate the prime sector on the full test space.
