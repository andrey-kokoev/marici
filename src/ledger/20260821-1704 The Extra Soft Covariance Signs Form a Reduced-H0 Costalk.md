# 1704 — The Extra Soft Covariance Signs Form a Reduced-H0 Costalk

## Gysin/costalk falsifier

Entry 1703 finds `Z2^{c(H)}` component signs on the nonzero support graph `H`.
Determine whether the extra signs have a canonical description in the existing
Cut incidence calculus.

## Incidence calculation

Over `Z2`, the labelled graph boundary satisfies

\[
\operatorname{rank}\partial_1
=|V(H)|-c(H).
\]

Consequently

\[
H_0(H,\mathbb Z_2)
\cong\mathbb Z_2^{c(H)}.
\]

The generic connected sign specializes diagonally:

\[
\mathbb Z_2
\longrightarrow
H_0(H,\mathbb Z_2).
\]

Its cokernel is

\[
\boxed{
\widetilde H_0(H,\mathbb Z_2)
\cong\mathbb Z_2^{c(H)-1}.
}
\]

The exact checker constructs the labelled incidence matrices for every support
of every connected simple graph through six vertices and verifies this rank
formula.

## Narrow result

\[
\boxed{
\text{the additional soft covariance signs are the reduced-H0 costalk of the existing Cut support graph.}
}
\]

They are not merely an unexplained loss of transport, and they do not require a
new carrier stratum.  They are a support-sensitive coefficient costalk derived
from the frozen incidence boundary.

## Durable artifacts

- `research/benincasa/checkers/soft_sign_costalk.rs`
- `research/benincasa/results/soft-sign-costalk.json`
- `research/benincasa/soft-sign-costalk.md`

## Next falsifier

Compute specialization through a flag of nested zero-normal supports.  Test
whether reduced-H0 costalks compose by the standard long exact sequence of a
pair or require an excess coherence class at simultaneous softening.
