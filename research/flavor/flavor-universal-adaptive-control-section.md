# Flavor universal adaptive control section

## Question

Does WP992's failure of every finite preregistered schedule persist if the
controls may depend on the faithfully reconstructed quotient point ((q,k))?

## Claim boundary

The claim is an exact section in formal invariant-control coordinates. It does
not assert that the quotient record, feedback channel, controls, reset, or
energy verification has a physical realization.

## Exact section

Write the controlled invariants as

\[
Q=q+u,\qquad R=k+v.
\]

Choose one fixed interior point in each of WP992's three preparation regions:

\[
(-1,0),\qquad (1,0),\qquad (0,1).
\]

They give the state-dependent control laws

\[
\begin{array}{c|cc}
\text{label}&u&v\\
\hline
\text{commuting}&-q-1&-k\\
\text{rank-two}&1-q&-k\\
\text{full-rank}&-q&1-k .
\end{array}
\]

Substitution makes the effective pair exactly the chosen interior point for
every (q,k>0). Hence a universal affine feedback section exists on the full
positive quotient. This removes WP992's unbounded-support obstruction for an
adaptive controller.

## Typing boundary

The section is a map from a prior quotient record and requested label to formal
control coordinates. It does not derive any of the physical arrows required to
execute that map:

\[
(q,k)\text{ measurement}
\longrightarrow
\text{feedback computation}
\longrightarrow
(u,v)\text{ actuation}
\longrightarrow
\text{reset and labelled energy verification}.
\]

The first record must be supplied by an admitted, calibrated realization of
WP991. The middle actuation must implement independent shifts of the invariant
coefficients rather than presentation coordinates. Measurement disturbance,
latency, reset, covariance, and the common-frame composition law remain
undeclared.

## Disposition

This construction is neither a source-generated selector nor a physical
instrument. It is an exact formal feedback section. The global control-geometry
obstruction is removed under perfect feedback; the unresolved obstruction is
the missing source-authorized apparatus composition.

## Smallest falsifier

The section fails physically if either:

1. two equivalent preparations produce inconsistent calibrated ((q,k))
   records; or
2. a commanded pair ((u,v)) does not realize
   (Q=q+u, R=k+v) within the declared uncertainty.

## Verification

- `research/flavor/checkers/wp993_universal_adaptive_control_section.py`
- `research/flavor/results/wp993_universal_adaptive_control_section.json`
