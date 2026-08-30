# 1699 — Matching Z2 Parities Do Not Identify the Cubic, Conditioning, and Time-Root Covers

## Typing audit

Entry 1698 exhibits a square-root deck action on the resolved conditioning
normal.  Compare it with the cubic-flow reversal and the previously identified
cosmological time-root line.

## Two derived actions

The exact cubic orbit has

\[
t\longmapsto-t.
\]

Entries 1692--1693 give

\[
\kappa_3(-t)=-\kappa_3(t),
\qquad
\kappa_4(-t)=\kappa_4(t).
\]

The conditioning Rees cover instead has

\[
u\longmapsto-u,
\qquad
\Xi=u\otimes u\longmapsto\Xi.
\]

Thus both constructions display an odd resolved coordinate and an even second
grade.

## Missing comparison

The actions have different provenance:

- `t -> -t` reverses the cubic unitary orbit;
- `u -> -u` is the deck transformation of a covariance square root;
- the cosmological time-root line comes from compatible regional energy-root
  choices.

No source-derived morphism currently identifies these three local systems.

## Narrow result

\[
\boxed{
\text{the parity representations agree, but identifying the cubic, conditioning, and cosmological time-root covers is currently untyped.}
}
\]

The agreement is evidence for a reusable resolved-normal calculus, not for one
universal `Z_2` coefficient.  This preserves the distinction demanded by the
cosmology evidence partition.

## Durable artifacts

- `research/benincasa/checkers/distinct_z2_gradings.rs`
- `research/benincasa/results/distinct-z2-gradings.json`
- `research/benincasa/distinct-z2-gradings.md`

## Next falsifier

Search the frozen source for an actual specialization or comparison map from
the energy-root normal line to the Gaussian conditioning normal bundle.  If no
such map is present, keep the covers independent and test only functorial
compatibility of their even Rees grades on shared Cut strata.
