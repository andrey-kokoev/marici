# The compact quotient supplies a canonical coercivity reserve

Status: normalization and measure-theoretic reserve theorem; conditional
application to the RH-equivalent Hausdorff tower

## Canonical reference geometry

At the reduced quarter point, put `u=(1/4+lambda)^(-1)` and then `x=u/4`.
The completed source therefore fixes the affine quotient coordinate

\[
0\le x\le1.
\]

For the rescaled moments `m_k=4^(-k)A_k`, the three physical polynomial
forms are

\[
M_n^{(0)}=(m_{i+j}),\qquad
M_n^{(x)}=(m_{i+j+1}),\qquad
M_n^{(1-x)}=(m_{i+j}-m_{i+j+1}).
\]

Coordinate Lebesgue measure supplies reference forms with the identical
multipliers:

\[
R_{ij}^{(0)}=\int_0^1x^{i+j}dx=\frac1{i+j+1},
\]

\[
R_{ij}^{(x)}=\int_0^1x^{i+j+1}dx=\frac1{i+j+2},
\]

and

\[
R_{ij}^{(1-x)}
=\int_0^1x^{i+j}(1-x)dx
=\frac1{(i+j+1)(i+j+2)}.
\]

This reference is forced after admitting the quarter-point reciprocal
coordinate and its endpoint normalization.  It does not reuse the unknown
physical measure as its own norm.

Define the basis-invariant generalized reserves

\[
\varepsilon_n^{(r)}
=\lambda_{\min}(M_n^{(r)},R_n^{(r)}),
\qquad r\in\{0,x,1-x\},
\]

and

\[
\varepsilon_n=\min_r\varepsilon_n^{(r)}.
\]

Simultaneous congruence of each matrix pair leaves these numbers unchanged.
Because polynomial spaces are nested and the reference norm is fixed before
truncation, every reserve sequence is nonincreasing.

## What the reserve measures

Suppose `m_k=int x^k dmu(x)` for a positive measure on `[0,1]`.  Then

\[
\inf_n\varepsilon_n^{(0)}\ge c
\]

is equivalent to

\[
\int|p|^2d\mu\ge c\int|p|^2dx
\]

for every polynomial `p`.  Polynomial approximation applied to square roots
of nonnegative continuous functions extends this inequality to all such
functions.  Hence

\[
\boxed{\inf_n\varepsilon_n^{(0)}\ge c
\quad\Longleftrightarrow\quad
\mu\ge c\,dx.}
\]

The analogous statements for the localizers compare `x dmu` with `x dx`
and `(1-x)dmu` with `(1-x)dx`.

Thus reserve magnitude has an invariant meaning: it is the greatest uniform
absolutely-continuous floor visible to polynomial probes.  It is not a raw
determinant scale and not directly a distance to the critical line.

## Consequence for the RH spectral measure

Conditional on the RH-equivalent Hausdorff representation, the quarter-point
measure is discrete at reciprocal squared-zero energies, with its only
accumulation at `x=0`.  It is singular with respect to `dx`, so it cannot
dominate `c dx` for any `c>0`.  Therefore

\[
\boxed{\varepsilon_n>0\ \text{at every finite order},
\qquad\inf_n\varepsilon_n=0.}
\]

Finite strict positivity follows because the spectral measure has infinitely
many interior support points: a nonzero finite-degree polynomial cannot
vanish at all of them.  Vanishing limiting reserve follows from singularity,
not from basis ill-conditioning.

This separates the two claims cleanly:

- the signs of all three towers are the RH-equivalent support test;
- decay of the canonically normalized reserves expresses finite
  non-observability of a singular infinite spectrum.

## First source-jet scout

Using only the interval-certified quarter-point moments `A_0,...,A_9`, taking
their midpoints, and solving the three generalized eigenproblems at 100-digit
precision gives

\[
\begin{array}{c|c}
n&\varepsilon_n\\ \hline
0&1.85503182187324\times10^{-5}\\
1&6.48006191301211\times10^{-12}\\
2&4.72843443097082\times10^{-19}\\
3&1.44399368138834\times10^{-26}\\
4&3.24028831666160\times10^{-34}.
\end{array}
\]

The `x`-localizer is the minimum at every available order.  Ordinary double
precision produces false negative values beginning at order three, while the
high-precision generalized problem restores strict positivity.  This is an
example of the distinction between invariant reserve decay and numerical
determinant conditioning.

These displayed reserves are midpoint scouts, not directed eigenvalue
certificates.  The input moments have rigorous boxes, but their propagation
through the ill-conditioned generalized eigenproblem still requires directed
linear algebra.  No zero locations enter the calculation.

## Scope and falsifiers

This does not prove positivity of the physical moment tower or RH.  It proves
what the normalized reserve would mean once the representing measure exists.
The construction is falsified as canonical if the quarter-point reciprocal
coordinate or its affine endpoint normalization is not source-derived.  The
spectral conclusion is falsified by a non-discrete or Lebesgue-dominating
representing component.

Discovery checker:

- `checkers/quarter_point_canonical_reserve_scout.py`

## Comparative rate census

A separate comparison experiment uses zero locations explicitly and is not
part of the source-only evidence.  It fixes the same `[0,1]` coordinate and
Lebesgue reference, normalizes total mass, and compares degree-zero through
degree-eight reserves for:

- the first 80 reciprocal Riemann-zero energies with source weights;
- the same support with equal and deterministically tilted weights;
- polynomial `j^-2` and geometric accumulation at zero;
- uniform Lebesgue measure;
- a depth-14 Cantor singular control.

The results sharply separate measure classes.  Uniform measure has reserve
exactly one at every order.  The Cantor control decays slowly, reaching about
`3.88e-2` at degree eight.  The Riemann-support/source-weight model reaches
about `3.69e-65`; equal and tilted weights on the same support give
`2.56e-65` and `2.28e-65`.  Thus the observed high-order rate is much more
stable under weight changes than under support changes.  Polynomial and
geometric accumulation controls have visibly different rate trajectories.

For the Riemann-support/source-weight model,

\[
-\frac1n\log\varepsilon_n
\]

stabilizes near `18.5` over degrees four through eight, whereas
`-log(epsilon_n)/n^2` decreases.  This finite window favors an approximately
exponential law over a quadratic-exponential law, but is too short and too
truncation-sensitive for an asymptotic claim.

The minimizing generalized-eigenvector polynomial is also a spectral
extractor.  At degree eight its leading real roots are approximately

\[
0.0012497472,qquad
0.0005653855,qquad
0.0003994781,qquad
0.0002657635,
\]

and the first three have locked onto the leading reciprocal squared-zero
energies.  This occurs because the minimizing polynomial suppresses the
largest atoms before paying energy on the accumulating tail.  It turns the
reserve flow into a finite-resolution spectral reconstruction, not merely a
scalar conditioning statistic.

This census uses only 80 atoms and midpoint high-precision linear algebra.
It is comparative reconnaissance, not a directed asymptotic theorem.

Comparison checker:

- `checkers/quarter_point_reserve_rate_census.py`
