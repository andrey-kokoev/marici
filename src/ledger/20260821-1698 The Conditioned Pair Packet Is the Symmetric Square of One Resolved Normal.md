# 1698 — The Conditioned Pair Packet Is the Symmetric Square of One Resolved Normal

## Extension falsifier

Entry 1697 produces one exceptional coefficient

\[
\xi_{ij}=\frac{c_ic_j}{b}
\]

for each conditioned labelled pair.  Test whether pair intersections require
independent extension data.

## Resolved normal

Write

\[
c_i=\sqrt b\,u_i.
\]

Then the complete exceptional packet is

\[
\boxed{
\Xi_{ij}=u_iu_j.
}
\]

Consequently `Xi` is the symmetric-square tensor

\[
\Xi=u\otimes u.
\]

Every rank-one minor vanishes:

\[
\Xi_{ij}\Xi_{kl}-\Xi_{il}\Xi_{kj}=0.
\]

The resolved square-root deck transformation is

\[
u\longmapsto-u,
\]

and therefore

\[
\Xi\longmapsto\Xi.
\]

## Narrow result

\[
\boxed{
\text{all exceptional conditioned-pair coefficients are components of one deck-invariant symmetric-square Rees grade.}
}
\]

No independent pair-intersection extension is required.  Occurrence labels
remain necessary to identify the tensor components, but their compatibility is
forced by the rank-one relations.

This gives a finite source-derived realization of the recurring Marici pattern

\[
\text{linear resolved normal}
\longrightarrow
\text{quadratic coarse invariant}.
\]

It is directly analogous in type—not yet by a constructed cross-sector map—to
the total-energy square-root modular coordinate of Entry 128.

## Durable artifacts

- `research/benincasa/checkers/symmetric_square_rees_pair_packet.rs`
- `research/benincasa/results/symmetric-square-rees-pair-packet.json`
- `research/benincasa/symmetric-square-rees-pair-packet.md`

## Next falsifier

Insert this symmetric-square exceptional tensor into the cubic Cut cocycle and
test its compatibility with the global time-root `Z_2`.  Determine whether the
deck-invariant second grade descends canonically while the first odd cumulant
retains the sign character.  Keep scalar regional polarity, contact
orientation, and time-root monodromy distinct.
