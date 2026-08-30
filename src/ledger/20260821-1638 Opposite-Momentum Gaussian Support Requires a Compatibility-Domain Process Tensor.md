# 1638 — Opposite-Momentum Gaussian Support Requires a Compatibility-Domain Process Tensor

## Supported frontier

Entry 1637 proves a strict CP observed channel when the observed mode is initially split from the internal Gaussian pair.  Test the first translationally invariant support where that split fails:

\[
q=-p.
\]

## Correlated Gaussian family

Use the standard two-mode-squeezed covariance

\[
V_{pq}
=
\begin{pmatrix}
aI&cZ\\
cZ&aI
\end{pmatrix},
\qquad
c^2=a^2-1,
\qquad
a>1.
\]

This is a physical pure Gaussian state correlating the observed occurrence with its opposite-momentum partner.

## Assignment test

Attempt to define a state-independent assignment by retaining the environment block \(aI\) and correlation block \(cZ\) while replacing the observed covariance by an arbitrary \(xI\).

Ordinary block positivity already requires

\[
xa-c^2\geq0,
\]

or

\[
\boxed{
x\geq a-\frac1a.
}
\]

For every integer \(a\geq2\), the physical observed vacuum \(x=1\) violates this condition.  Thus the fixed correlated assignment is not positive on the full observed state space.  Quantum uncertainty can only impose additional restrictions.

The checker verifies 63 source covariances, 63 vacuum assignment failures, and 2,205 compatibility decisions.

## Narrow result

\[
\boxed{
\text{At opposite-momentum anomalous support, no state-independent positive assignment extends the frozen correlation to arbitrary observed inputs.}
}
\]

Therefore the reduced evolution is not naturally a CP channel on the full observed state space.  It is typed on a compatibility domain determined by the initial correlation.

## Correct coefficient object

The appropriate object is an initial-correlation assignment/process tensor retaining:

- the observed occurrence \(p\);
- the supported partner \(-p\);
- their joint Gaussian covariance;
- admissible local interventions or marginal replacements;
- subsequent labelled Cut evolution.

Complete positivity remains valid for the global evolution and for interventions on the compatible joint object.  What fails is CP descent to an arbitrary reduced input after discarding the supported partner.

## Architectural consequence

The generic/supported split is now explicit:

\[
\text{generic split stratum}
\to
\text{positive scalar internal pushforward and CP observed channel},
\]

\[
\text{opposite-momentum correlation stratum}
\to
\text{compatibility-domain process tensor}.
\]

This is support-sensitive coefficient behavior on an existing labelled momentum-incidence support.  It does not require a new carrier divisor.

## Durable artifacts

- `research/benincasa/checkers/correlated_gaussian_assignment_domain.rs`
- `research/benincasa/results/correlated-gaussian-assignment-domain.json`
- `research/benincasa/correlated-gaussian-assignment-domain.md`

## Next falsifier

Construct the minimal Gaussian process-tensor Choi covariance for the pair \((p,-p)\) and one cubic interaction step.  Test positivity under all Gaussian interventions preserving the compatibility domain, and derive the restriction map back to Entry 1637's generic CP channel as \(c\to0\).  Failure of that degeneration would falsify the proposed supported coefficient object.
