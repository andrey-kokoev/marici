# 1622 — The Generic Finite Labelled-Cut Family Generates the Gaussian Second-Rees Cone

## Frozen local model

Let one observed oscillator be coupled to finitely many orthogonal environment labels \(r\).  Freeze the first-order purification

\[
|\Psi\rangle
=
|0;0_E\rangle
+
\epsilon
\left(
a|2;0_E\rangle
+
\sum_r b_r|1;r\rangle
\right)
+O(\epsilon^2).
\]

The amplitude \(a\) is the coherent pure-Gaussian squeezing direction.  Each \(b_r\) is a labelled Cut channel crossing from the observed mode into an orthogonal environment occurrence.

## Second normal grade

At the first nontrivial grades,

\[
|\beta_1|^2=2|a|^2,
\]

while

\[
n_2
=
2|a|^2
+
\sum_r|b_r|^2.
\]

Therefore the second-Rees uncertainty grade is

\[
\boxed{
n_2-|\beta_1|^2
=
\sum_r|b_r|^2
\geq0.
}
\]

Equality holds exactly when all environment-crossing Cut amplitudes vanish.

The checker verifies 16,807 exact cases for three independent labelled channels.  Orthogonality makes the displayed formula independent of the finite number of labels.

## Narrow result

The finite labelled-Cut family realizes the complete local inequality cone

\[
n_2\geq|\beta_1|^2
\]

for the frozen purification model:

- the boundary is the pure Gaussian/squeezing locus;
- the interior excess is the labelled Cut norm into unobserved channels.

This generalizes Entry 1608's single environment channel and Entry 1610's cubic three-particle channel.

## Type qualifications

This does **not** prove that a particular continuum interaction kernel spans every abstract mixed-Gaussian tangent direction.  It proves the coefficient geometry once the environment-crossing amplitudes are source-derived.  The continuum measure and interaction selection rules remain separate inputs.

## Architectural consequence

The Gaussian state cone is not an additional carrier.  Locally it is reconstructed from:

\[
\text{marked coherent first jet}
+
\text{positive labelled Cut pairing}
\longrightarrow
\text{second-Rees covariance cone}.
\]

This is direct evidence for H2: shared labelled Cut carrier and comparison calculus, with a cosmology-specific positive covariance coefficient object.

## Durable artifacts

- `research/benincasa/checkers/gaussian_mixed_second_rees_cone.rs`
- `research/benincasa/results/gaussian-mixed-second-rees-cone.json`
- `research/benincasa/gaussian-mixed-second-rees-cone.md`

## Next falsifier

Replace the abstract orthogonal labels by the source cubic momentum channels and compute the map

\[
C_{p;q,k}
\longmapsto
\left(x_1(p),y_1(p),n_2(p)\right)
\]

with momentum conservation, the symmetric finite-EFT measure, and all occurrence multiplicities retained.  Test whether the resulting continuum Cut norm saturates precisely on the source pure-state locus or whether a source interference term survives outside the positive labelled pairing.
