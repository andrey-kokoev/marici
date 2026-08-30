# 3258 — Integral Kummer Shifts Remove the Quarter Adapter Defects

Date: 2026-08-27

Status: replicated finite-field falsification of intrinsic Kummer-local-system
support.

## Hostile question

Entry 3256 established that the two quarter fibers carry order-four Kummer
characters. Are their rank drops invariants of those local systems, or do they
depend on the selected meromorphic lattice at the exact exponent?

Integral shifts

\[
\gamma\longmapsto\gamma+n,qquad n\in\mathbb Z,
\]

preserve the local inertia

\[
\exp(2\pi i\gamma).
\]

On the open complement (K\ne0), they are meromorphic gauge equivalences by
powers of (K). An intrinsic local-system rank defect should therefore persist
along the integral orbit.

## Exact census

At both primes (32003) and (32009), the (-i) orbit gives

\[
\begin{array}{c|c}
\gamma&(\operatorname{rank}M,\operatorname{rank}[M;L])\\
\hline
-9/4&(479,505)\\
-5/4&(479,500)\\
-1/4&(479,505)\\
3/4&(479,505),
\end{array}
\]

while the (+i) orbit gives

\[
\begin{array}{c|c}
\gamma&(\operatorname{rank}M,\operatorname{rank}[M;L])\\
\hline
-11/4&(479,505)\\
-7/4&(479,498)\\
-3/4&(479,505)\\
1/4&(479,505).
\end{array}
\]

Every tested integral translate has the same inertia as its quarter point, but
only the exact representatives (-5/4) and (-7/4) lose augmented rank.

## Falsified interpretation

The claim that the rank drops are intrinsic support of the order-four Kummer
local systems is falsified.

The surviving narrow classification is:

\[
\text{resonance of the selected meromorphic pole-depth lattice}.
\]

The open Kummer local system remains unchanged under the integral shift, while
its chosen extension across (K=0), together with the finite readout lattice,
does not. The unequal defect dimensions five and seven are therefore not a
contradiction between conjugate Kummer sectors; they are data of two different
resonant extensions.

## Consequence

Entries 3210–3244 remain valid as statements about the frozen adapter lattice.
Entry 3256 remains valid as a character classification but must not be read as
assigning the defects to intrinsic Kummer support.

The physical cosmology branch is closed more strongly:

- no physical exponent support;
- no intrinsic order-four local-system support;
- no new Carrier stratum;
- only presentation-sensitive meromorphic-extension resonance remains.

Further work is justified only if a source-derived Deligne-lattice,
Bernstein--Sato, or regulator-renormalization problem needs these exact
resonant extensions.

## Artifacts

- `research/benincasa/checkers/exponent_adapter_integral_orbit.py`
- `research/benincasa/results/exponent_adapter_integral_orbit.json`
- sequence claim `seqclaim-e5153996e1b4bd5c42d5623e`
