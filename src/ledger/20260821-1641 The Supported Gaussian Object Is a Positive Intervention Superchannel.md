# 1641 — The Supported Gaussian Object Is a Positive Intervention Superchannel

## Problem

Entry 1640 excludes an ordinary CP assignment channel for nonzero opposite-momentum correlation.  Construct the smallest correctly typed positive object without extending that correlation to arbitrary observed marginals.

## Source-defined object

Let (ho_{PE}\succeq0) be the frozen correlated state of the observed occurrence (P) and supported partner (E).  Given a local CP intervention

\[
\mathcal A(X)=\sum_rK_rXK_r^\dagger
\]

and a subsequent global evolution (U), define

\[
\boxed{
\mathfrak T_{\rho,U}(\mathcal A)
=
\operatorname{Tr}_E
\left[
U(\mathcal A\otimes\operatorname{id})(\rho_{PE})U^\dagger
\right].
}
\]

The input is an intervention on the existing correlated state, not a replacement marginal plus a fabricated assignment.

## Positivity

Writing (ho_{PE}=RR^\dagger), the state before partial trace is

\[
\sum_r UK_rR(UK_rR)^\dagger\succeq0.
\]

Partial trace preserves positivity.  Hence (mathfrak T_{\rho,U}) is a positive, indeed completely positive, supermap on local CP interventions.  This conclusion does not require a positive assignment on the full observed state space.

The finite checker verifies 64 correlated intervention/evolution cases and 72 exact product-degeneration identities.

## Product degeneration

For

\[
\rho_{PE}=\rho_P\otimes\rho_E,
\]

the same expression becomes

\[
\operatorname{Tr}_E
\left[
U(\mathcal A(\rho_P)\otimes\rho_E)U^\dagger
\right],
\]

which is the ordinary product reduced channel after intervention.  Thus the supported process object degenerates exactly to Entry 1637's generic channel type.

## Narrow result

\[
\boxed{
\text{The minimal supported coefficient object is a CP intervention superchannel on the frozen correlated pair.}
}
\]

This supplies the object demanded by Entries 1638–1640 and proves its abstract positivity and generic degeneration.  It strengthens H2: the carrier support is unchanged, while the coefficient type jumps from a channel to a process object on the correlated stratum.

It does not yet establish the renormalized continuum cubic evolution, a finite Gaussian Choi covariance for the non-Gaussian step, or complete positivity after an uncontrolled perturbative truncation.

## Durable artifacts

- `research/benincasa/checkers/correlated_intervention_superchannel.rs`
- `research/benincasa/results/correlated-intervention-superchannel.json`
- `research/benincasa/correlated-intervention-superchannel.md`

## Next falsifier

Replace the exact global (U) by the frozen second-order Dyson/Cut packet from Entries 1632–1634.  Test whether its real-plus-virtual truncated supermap remains positive on the compatible intervention cone.  Positivity of the exact unitary does not imply positivity of a finite perturbative truncation.
