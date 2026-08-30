# 1637 — A Split General-Gaussian Internal State Pushes the Cubic Cut to a Positive Scalar Gain

## Question

Entry 1636 obtains strict observed filtration only after vacuum pushforward of the internal modes.  Does a general Gaussian internal state reintroduce coupling to the full internal moment tower?

## Frozen factorization

For a generic labelled channel away from observed/internal coincidence support, write

\[
L_{p;qk}
=
C_{p;qk}
a_p^\dagger
\otimes
(a_q^\dagger a_k^\dagger).
\]

Assume the initial density matrix is split between the observed mode and the internal pair.  Push the fixed internal Gaussian state forward:

\[
\mu_{qk}
=
\operatorname{Tr}
\left[
\rho_{qk}
(a_q a_k)(a_q^\dagger a_k^\dagger)
\right].
\]

For distinct labelled occurrences,

\[
\mu_{qk}
=
\langle(N_q+1)(N_k+1)\rangle.
\]

## Gaussian Wick reduction

Let

\[
n_q=\langle a_q^\dagger a_q\rangle,
\qquad
c_{qk}=\langle a_q^\dagger a_k\rangle,
\qquad
\beta_{qk}=\langle a_q a_k\rangle.
\]

Then

\[
\boxed{
\mu_{qk}
=(n_q+1)(n_k+1)
+|c_{qk}|^2
+|\beta_{qk}|^2.
}
\]

This is positive and invariant under \(q\leftrightarrow k\).

The checker verifies 194,481 exact Wick packets.

## Observed generator

The reduced trace-balanced number-moment generator is

\[
\mathcal L_p^\dagger f
=
\mu_{qk}
(N_p+1)[f(N_p+1)-f(N_p)].
\]

The internal Gaussian data enter only through a positive scalar coefficient.  The observed moment degree remains unchanged.

## Narrow result

\[
\boxed{
\text{A fixed split Gaussian internal state preserves the strict observed moment tower and q-k occurrence covariance.}
}
\]

Vacuum is therefore not essential for the generic pushforward; Gaussian Wick closure is sufficient.

## Supported qualification

If the source Gaussian covariance correlates \(p\) directly with \(q\) or \(k\), the initial state is not split across the observed/internal partition and the reduced map need not be state-independent or completely positive.  Translational invariance confines such correlations to labelled coincidence or opposite-momentum supports.  Those supports must be tested separately; they cannot be folded into the generic scalar.

Coincident \(q=k\) occurrences likewise carry extra bosonic contraction terms and remain occurrence-resolved.

## Architectural consequence

Generic Gaussian internal pushforward is a coefficient evaluation map

\[
\mathbb M_{qk}^{\rm Gauss}
\longrightarrow
\mathbb R_{\ge0},
\qquad
\rho_{qk}\mapsto\mu_{qk},
\]

followed by the strict observed channel.  This fits the existing labelled Cut carrier and sector-specific positive moment coefficients.

## Durable artifacts

- `research/benincasa/checkers/gaussian_internal_pushforward.rs`
- `research/benincasa/results/gaussian-internal-pushforward.json`
- `research/benincasa/gaussian-internal-pushforward.md`

## Next falsifier

Analyze the first supported observed/internal correlation stratum, e.g. \(q=-p\) in a translationally invariant anomalous Gaussian state.  Construct the assignment map on that support and test whether a completely positive reduced channel exists after adjoining the correlated partner, or whether the correct object is a non-CP initial-correlation process tensor.
