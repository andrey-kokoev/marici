# Mellin and de Rham graph control repair two-sided window leakage

## Question

The continuous log-window Fourier leakage has norm one on bare \(L^2\). Can
the independently derived source operators strengthen the domain enough to
restore quantitative descent?

## Source graph norm

Let \(Q\) be multiplication by the logarithmic coordinate and let
\(D=\partial_q\). Both already occur in the source programme:

- \(Q\) generates the Mellin-character orbit that fills the unilateral seam
  cocycle;
- \(D\) is the relative de Rham/Pearson operator whose boundary concomitant is
  the wall current.

Use the phase-space graph norm

\[
\lVert f\rVert_{QD}^2
=\lVert f\rVert_2^2+lVert Qf\rVert_2^2+lVert Df\rVert_2^2.
\]

No weight has been fitted to the desired Fourier estimate; both graph rows are
independently source-derived.

## Incoming leakage estimate

If \(f\) is supported outside \([-R,R]\), then

\[
\lVert f\rVert_2
\le R^{-1}\lVert Qf\rVert_2.
\]

Since Fourier transform and the visible projection are contractions,

\[
\lVert P_R\mathcal Ff\rVert_2
\le R^{-1}\lVert Qf\rVert_2.
\]

The translated long packets that gave unit leakage in bare \(L^2\) therefore
become expensive in the source graph topology.

## Outgoing leakage estimate

For any \(f\) in the derivative domain, Plancherel gives

\[
\lVert Q\mathcal Ff\rVert_2=\lVert Df\rVert_2
\]

under the angular-frequency convention. Hence

\[
\lVert(I-P_R)\mathcal Ff\rVert_2
\le R^{-1}\lVert Df\rVert_2.
\]

Thus the two directed leakage blocks decay at rate \(R^{-1}\) when measured
from their correctly typed graph domains into the diagnostic \(L^2\) output.

## Important typing correction

This is not ordinary quasidiagonality on one Hilbert norm. Sharp interval
projection need not preserve the derivative graph domain, and the estimates
use different source controls in the two directions. The correct statement is
a two-sided graph-domination theorem:

- position control dominates omitted-to-visible transport;
- derivative control dominates visible-to-omitted transport.

Collapsing both controls into bare \(L^2\) recreates the norm-one hostile.

## Interpretation

The seam and wall channels are not merely records of failed descent. Their
source generators provide exactly the regularity needed to control the two
crossing directions. This is the first positive completion mechanism in the
current chain that is absent from arbitrary \(L^2\) Fourier analysis.

It also explains why one extra scalar boundary port was insufficient. The two
leakage directions require conjugate controls: logarithmic position and its
Fourier-dual derivative.

## Remaining gate

The theorem becomes source-complete only after proving that the actual
arithmetic-to-analytic incidence lands in the common domain of \(Q\) and
\(D\), and that primitive, square, seam, and archimedean currents are
continuous for this graph topology under restricted-product completion.

A sequence bounded in the declared arithmetic pro-Gram seminorms but
unbounded in either \(Q\) or \(D\) is the immediate falsifier.

## Verification

The checker `check_mellin_derham_leakage_domination.py` verifies the exact
finite weighted analogues of both directed estimates and the failure obtained
when the corresponding graph row is deleted.

