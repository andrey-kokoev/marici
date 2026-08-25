# An instrumented invariant score is still not a selector (WP58)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

The positive weak-basis-invariant functional

\[
C(H_u,H_d)=\operatorname{Tr}([H_u,H_d]^\dagger[H_u,H_d])
\]

has the exact up-spectral-frame form

\[
C=2\sum_{i<j}(u_i-u_j)^2|(H_d)_{ij}|^2.
\]

It descends under the full weak-basis group, is nonnegative, and for
nondegenerate (H_u) vanishes exactly on the commuting locus. Unlike the
deck-odd probe, its value is reconstructible from masses and CKM data, so its
readout has an experimental typing.

That still does not make it a selector. The source supplies no action or
dynamical principle that minimizes or stationarizes (C). Adding
"choose (C=0)" is an extra operation, and it predicts trivial CKM mixing,
contrary to the fitted ensemble. One nonzero off-diagonal (H_d) entry is the
smallest exact falsifier.

Thus WP58 separates three arrows: construct a distinguishing functional;
measure/reconstruct its value; impose an extremal law. Only the first two are
authorized here. Verification:
`uv run --with sympy python research/flavor/checkers/wp58_commutator_score_selector_gate.py`.
