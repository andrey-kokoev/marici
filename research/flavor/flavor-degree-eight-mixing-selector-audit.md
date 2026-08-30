# Degree-eight invariant mixing-selector audit (WP125)

Owner: `marici.Figueiredo`.

## Bounded question

What is the first polynomial operator degree at which the full weak-basis
invariant two-bifundamental source class can evade WP124 and possess a
noncommuting interior mixing minimum?

Pre-objective process report: excitement `9/10`, confidence `7/10` that degree
eight is the threshold, expected information gain `9/10`. The attraction is a
clean boundary between linear assignment geometry and a genuine interior
selector. Confounds are fixed spectra, a two-family slice, EFT stability, and
the absence of independently derived coefficients. These reports are
non-evidential.

Frozen optionality snapshot: compare operator degrees four, six, and eight;
construct one exact noncommuting stationary point; require positive second
variation and lower energy than both slice endpoints; ten exact checks. Do
not infer a full `physical16` point prediction from a slice selector.

## Why degree six still cannot select generic mixing

Put `H_a=Phi_a Phi_a^dagger`. At fixed nondegenerate spectra, every
orientation-dependent invariant through field degree six has one alternating
pair and is a linear combination of terms

\[
\operatorname{Tr}\!\left[f(H_u)U g(H_d)U^\dagger\right]
=\sum_{ij} f(u_i)g(d_j)|U_{ij}|^2.
\]

This includes `Tr(H_uH_d)`, `Tr(H_u^2H_d)`, `Tr(H_uH_d^2)`, and products of
these with orientation-independent traces. The matrix `|U_ij|^2` is
unistochastic and therefore doubly stochastic. A linear functional reaches a
global minimum on the containing Birkhoff polytope at a permutation, and
permutations are themselves unistochastic. Hence a permutation is always a
global minimum. Degrees four and six cannot force a generic noncommuting
global minimum. Degeneracies only introduce flat stabilizer directions.

## First evasion at degree eight

Degree eight admits a trace word with two alternations,

\[
\operatorname{Tr}(H_uH_dH_uH_d),
\]

or equivalently the positive invariant

\[
K=\lVert[H_u,H_d]\rVert_F^2
=2\left[\operatorname{Tr}(H_u^2H_d^2)
-\operatorname{Tr}(H_uH_dH_uH_d)\right].
\]

This depends nonlinearly on `|U_ij|^2` and escapes the assignment argument.
It is a full weak-basis invariant and needs no reference port.

For the exact slice

\[
H_u=\operatorname{diag}(3,2,1),\qquad
H_d=R_{12}(\theta)\operatorname{diag}(6,4,1)R_{12}(\theta)^T,
\quad x=\sin^2\theta,
\]

one has

\[
C=\operatorname{Tr}(H_uH_d)=27-2x,
\qquad K=8x(1-x).
\]

Consider the conditional invariant potential

\[
V(x)=aC-qK,
\qquad a=28,\quad q=25.
\]

Its unique slice stationary point is

\[
x_*=\frac12+\frac{a}{8q}=\frac{16}{25},
\qquad \sin\theta_*=\frac45,
\]

with `V''=16q=400>0`. It is genuinely noncommuting:

\[
K(x_*)=\frac{1152}{625}>0.
\]

Moreover `V(x_*)=16852/25`, below both endpoint values `756` and `700`.
Thus degree eight is sufficient for an interior mixing selector in this exact
slice.

## What this does and does not select

The construction proves capability, not a flavor prediction. The selected
angle obeys

\[
x_*=\frac12+\frac{a}{8q};
\]

its numerical value is simply the source coefficient ratio. Choosing `a/q`
after inspecting CKM data is prohibited selector fitting. An independently
derived coefficient relation could turn the same map into a source-generated
prediction, but none is presently admitted.

The negative `-qK` term also requires a stabilizing degree-eight completion in
the unrestricted radial directions. The exact result is conditional on fixed
spectra and cannot be promoted to a globally stable two-flavon potential
without that completion. Nor does a single real rotation select three CKM
angles and the CP phase; the full contextual fiber remains non-singleton.

## Classification and falsifiers

- admitted domain: fixed nondegenerate spectra in an exact two-family
  orientation slice of the two-bifundamental field space;
- faithful quotient: restriction of `physical16`, never measured ten;
- probe family: trace invariants through degree eight, including `K`;
- operation: genuine conditional interior-mixing selector on the slice;
- rigidifier: no;
- reference port: no;
- physical instrument: not established;
- smallest falsifier: `V'(16/25)` nonzero or `V''(16/25)<=0`;
- source-authority falsifier: the ratio `a/q` is fitted from the desired
  mixing angle rather than derived before flavor readout;
- global-stability falsifier: an unbounded radial direction in the completed
  potential.

Post-objective process report: excitement `9/10`, confidence `9/10` in the
bounded threshold and slice construction, realized information gain `9/10`.
Raw delta: degrees four and six are merged into one assignment no-go; degree
eight opens one interior-selector branch; ten of ten exact checks pass; one
noncommuting slice minimum is constructed; full-point selection, source-fixed
coefficients, radial stability, matching, and a physical instrument remain
open. These ratings are non-evidential.
