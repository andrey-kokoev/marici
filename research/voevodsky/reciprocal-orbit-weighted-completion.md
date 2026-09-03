# Reciprocal-orbit weighted completion

## Question

Does source decay suffice to complete finite cutoff fillers uniformly along a fixed reciprocal affine orbit?

## Claim boundary

The theorem is conditional on weighted source decay and applies to one orbit inside its decay strip. It is neither an unweighted nor a global spectral completion theorem.

## Weighted source and orbit

Let

\[
B_\epsilon=
\left\{c:\sum_r |c_r|H(r)^\epsilon<\infty\right\},
\]

and let \(K_w=\{sw:s\in[-1,1]\}\), with \(a=|\operatorname{Re}w|<\epsilon\). Then

\[
\sup_{z\in K_w}|H(r)^{-z}|
\leq H(r)^a
\leq H(r)^\epsilon.
\]

Consequently cutoff tails satisfy

\[
\sup_{z\in K_w}
\left|
\sum_{r\notin F_N}c_rH(r)^{-z}
\right|
\leq
\sum_{r\notin F_N}|c_r|H(r)^\epsilon
\longrightarrow0.
\]

Thus finite evaluations converge uniformly in \(C(K_w)\). Since reciprocal labels have equal height, one estimate controls both orientations.

## Boundary preservation

Endpoint evaluation is continuous in the orbit sup norm. Hence a boundary-null relation at every cutoff remains boundary-null in the limit. The graph norm

\[
\|c\|_{B_\epsilon}+\|E(c)\|_{C(K_w)}
\]

types the completed evaluation graph.

## Falsification fixture

For \(c_n=n^{-4}\), source exponent 2, and orbit width 1, exact rational tails verify uniform domination. At width 3 the evaluated tail is harmonic; every dyadic block is at least \(1/2\). This deliberate failure confirms that the strict strip condition cannot be removed by the proof.

## Disposition

Conditional completed filler descent, reciprocal uniformity, and boundary-null preservation hold on every fixed affine orbit strictly inside a supplied decay strip. Global spectral completion and unconditional source decay remain unproved.

## Verification

- `research/voevodsky/reciprocal-orbit-weighted-completion-v1.json`
- `research/voevodsky/checkers/check_reciprocal_orbit_weighted_completion.py`
- `research/voevodsky/results/reciprocal_orbit_weighted_completion.json`
