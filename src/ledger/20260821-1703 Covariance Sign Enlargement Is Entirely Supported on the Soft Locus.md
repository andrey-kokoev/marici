# 1703 — Covariance Sign Enlargement Is Entirely Supported on the Soft Locus

## Relative-support falsifier

Entry 1702 closes generic loop holonomy for source-derived covariance Rees
packets.  Allow the resolved normal to vanish on labelled occurrences and
compute the remaining sign object.

## Nonzero support graph

Let `H` be the induced graph on occurrences with

\[
u_i\neq0.
\]

If `H` has `c(H)` connected components, edge products propagate signs within
each component but not between components.  Therefore

\[
\boxed{
\operatorname{Deck}_{\rm cov}(H)=\mathbb Z_2^{c(H)}.
}
\]

For arbitrary edge signs, the nonliftable quotient remains

\[
H^1(H,\mathbb Z_2).
\]

Source-derived packets occupy its zero class on every component.

The exact checker enumerates every connected labelled simple graph through six
vertices and every nonempty vertex support.  It verifies

\[
2^{|E(H)|}
=2^{|V(H)|-c(H)}2^{b_1(H)}
\]

and

\[
2^{c(H)}2^{|V(H)|-c(H)}=2^{|V(H)|}.
\]

## Narrow result

\[
\boxed{
\text{all enlargement beyond one global covariance sign is supported where the resolved normal vanishes.}
}
\]

After localizing every nonzero normal on a connected graph, `c(H)=1`; no new
generic sign or loop class survives.  This is the precise covariance-sector
analogue of “generic closure plus soft support,” without identifying its deck
line with cosmological time orientation.

## Durable artifacts

- `research/benincasa/checkers/soft_relative_sign_cohomology.rs`
- `research/benincasa/results/soft-relative-sign-cohomology.json`
- `research/benincasa/soft-relative-sign-cohomology.md`

## Next falsifier

Test whether the soft-supported component-sign sheaf has a canonical
extension-by-zero/Gysin description on the existing Cut carrier.  Compute the
specialization from a connected generic support to a two-component soft fiber
and determine whether its extra sign is a costalk class or merely loss of
transport.
