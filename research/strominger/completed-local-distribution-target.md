# The completed local target is a filtered puncture-distribution module

## Definition

For a finite labelled puncture set `P` and order bound `N`, define

\[
 \mathcal Y_{P}^{N}=\mathcal{PP}_{P}^{N}
 \oplus\mathcal E_{P}^{N}
 \oplus\mathcal B^{N}.
\]

The three summands have different types.

1. `PP_P^N` contains the prescribed finite-part Cauchy principal powers
   `(z-xi)^(-k)` and their conjugates, with `1<=k<=N` and source-derived
   smooth coefficient germs.
2. `E_P^N` contains point-supported distributions
   `partial_z^r partial_zb^s delta_xi`, `r+s<=N`.
3. `B^N` contains the smooth sphere background required by the Green
   normalization and zero-mode subtraction.

The completed local target is the strict filtered union

\[
 \mathcal Y_P^{\rm fin}=\underset{N}{\operatorname{colim}}\,
 \mathcal Y_P^N
 \subset\mathcal D'(S^2).
\]

Every state has finite distribution order. Arbitrary infinite delta jets,
independently chosen Laurent tails, and unprescribed extensions of singular
functions are excluded.

## Distributional completion

With the convention

\[
 \partial_{\bar z}\frac1{z-\xi}=\pi\delta_\xi,
\]

the higher principal powers satisfy

\[
 \partial_{\bar z}\frac1{(z-\xi)^k}
 =\pi\frac{(-1)^{k-1}}{(k-1)!}
 \partial_z^{k-1}\delta_\xi.
\]

Thus principal parts and point-supported jets are related by a fixed
distributional boundary map; they are not duplicate free coordinates.
Choosing a different finite-part extension changes the answer by an element
of `E_P^(k-1)`, so the prescription is part of the constructor type.

## Grade-three principal ports

For the invariant one-puncture grade-three response `R_xi`, the holomorphic
principal coefficients are

\[
\begin{aligned}
[z-\xi]^{-4}:&\ -\frac6{(1+\xi\bar z)^2},\\
[z-\xi]^{-3}:&\ \frac{36(\xi\bar\xi\bar z-\bar\xi+2\bar z)}
{(1+\xi\bar\xi)(1+\xi\bar z)^3},\\
[z-\xi]^{-2}:&\ -\frac{126\bar z(\xi\bar\xi\bar z-2\bar\xi+3\bar z)}
{(1+\xi\bar\xi)(1+\xi\bar z)^4},\\
[z-\xi]^{-1}:&\ \frac{336\bar z^2(\xi\bar\xi\bar z-3\bar\xi+4\bar z)}
{(1+\xi\bar\xi)(1+\xi\bar z)^5}.
\end{aligned}
\]

The antiholomorphic ports are their helicity-conjugate partners with the
magnetic relative sign. In particular, the leading coefficients on the real
incidence locus are

\[
 -\frac6{(1+\xi\bar\xi)^2},\qquad
 +\frac6{(1+\xi\bar\xi)^2},
\]

so neither route is absent.

## PSZ angular-momentum ports

The subleading source derivative

\[
 \partial_{\bar\xi}\log S
 =\frac{1+\xi\bar z}{(\bar\xi-\bar z)(1+\xi\bar\xi)}
\]

has a nonzero simple-pole port, while
`partial_xi partial_xibar log S` contains a delta function plus the fixed
sphere background. Therefore orbital and spin source records naturally land
in all three summands of `Y_P^fin`.

## Distinct-support faithfulness

For distinct labelled punctures, taking every local principal coefficient
and delta-jet coefficient is block diagonal by support. A distribution
supported at one puncture cannot cancel a distribution supported at another.
This establishes supportwise faithfulness of the local port before global
conservation relations are imposed. It does not yet prove faithfulness among
all jet orders at one puncture; that triangular local classification is a
later step.

## Evidence

`checkers/completed_local_distribution_target_checks.py` verifies the four
principal coefficients, the nonzero incidence-leading ports, the Cauchy to
delta-jet coefficient law, distinct-support block rank, and finite-order
filtration dimensions.
