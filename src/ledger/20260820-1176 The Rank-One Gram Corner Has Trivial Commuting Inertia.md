---
title: "The Rank-One Gram Corner Has Trivial Commuting Inertia"
date: 2026-08-20
entry: 1176
status: active
sector: cosmology
---

# 1176 — The Rank-One Gram Corner Has Trivial Commuting Inertia

Sequence claim: `seqclaim-ba56ba64d85ff7e9934cd4b5`.

## Two-normal model

At a generic rank-one Gram point choose labelled normal parameters \(s,t\)
with

\[
G(s,t)=\operatorname{diag}(1,s,t),
\qquad
\operatorname{adj}(G)=\operatorname{diag}(st,t,s).
\]

The persistent-node normal form is

\[
\boxed{
W^2-stx_1^2-tx_2^2-sx_3^2=0.
}
\]

The three quadratic coefficients have labelled valuation vectors

\[
x_1:(1,1),
\qquad
x_2:(0,1),
\qquad
x_3:(1,0).
\]

These are exactly the two Gram normals and their intersection monomial; no
additional support equation occurs.

## Inertia

On the Kummer cover \(s=\alpha^2\), \(t=\beta^2\):

- the \(s\)-deck involution flips \((x_1,x_3)\);
- the \(t\)-deck involution flips \((x_1,x_2)\);
- their product flips \((x_2,x_3)\).

Every element flips two coordinates. Hence each acts with determinant
\(+1\) on the vanishing three-cycle:

\[
\boxed{T_s=T_t=T_{st}=1.}
\]

The deck actions are diagonal, so

\[
\boxed{[T_s,T_t]=0.}
\]

Thus the first iterated Gram corner has neither a new character nor a mixed
inertia commutator.

## Scope

This closes the semisimple inertia audit, not the full supported costalk.
At \(s=t=0\) the special equation is \(W^2=0\), so nilpotent Cartier length
or a supported extension could remain even though all generic monodromy
characters are trivial.

The support is nevertheless already typed:

\[
\boxed{
\{s=0\}\cup\{t=0\}\cup\{s=t=0\}
=
\text{existing labelled Gram-minor incidence corner}.
}
\]

## Next falsifier

Compute the derived special fiber of the two-normal quadratic family,
retaining the doubled equation \(W^2=0\). Compare its Cartier/Koszul
filtration with the existing two-face Gram-minor incidence cube. The target
is the supported extension or Tor class, not another monodromy census.

## Evidence

- `research/benincasa/checkers/four_site_qg_rank_one_gram_corner.py`
- `research/benincasa/results/four-site-qg-rank-one-gram-corner.json`
- Entries 1174--1175.
