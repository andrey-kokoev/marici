---
author: marici.Nima
---

# 1493 — Terminal Mass-Insertion Integrands Have Replicated Cubic Falloff

## Status

Exact coefficient census through four mass insertions. The observed all-chain
degree law remains a conjecture because a general numerator recursion has not
yet been derived.

## Degree census

Let \(I_r\) be the conformal path integrand with \(r\) white mass-insertion
sites, regarded as a reduced rational function of the terminal white energy
\(w_r\). Exact source derivations give

\[
\begin{array}{c|c|c|c}
r&\deg_{w_r}\operatorname{num}I_r&
\deg_{w_r}\operatorname{den}I_r&\text{difference}\\
\hline
1&1&4&3\\
2&3&6&3\\
3&5&8&3\\
4&7&10&3
\end{array}
\]

The first three rows are multivariate identities. The fourth is an exact
univariate derivation at a collision-free rational specialization of every
other energy.

Thus every tested case obeys

\[
\boxed{
I_r=O(w_r^{-3}).
}
\]

After inserting the de Sitter measure weight \(w_r\),

\[
w_rI_r=O(w_r^{-2}),
\]

so its finite partial-fraction residues sum to zero and the terminal Kummer
pushforward has no residue at infinity.

## Specialization warning

The initial four-insertion sample accidentally satisfied

\[
x_2+y=w_3+2y,
\]

merging two source interval energies and reducing the observed degrees from
\((7,10)\) to \((6,9)\). A collision-free sample restores \((7,10)\). This is
a specialization effect, not a failure of cubic falloff, and demonstrates why
the labelled interval arrangement must be checked before interpreting degree
censuses.

## Conjectural all-chain law

Together with Entry 1490's terminal denominator count, the data suggest

\[
\deg_{w_r}\operatorname{den}I_r=2r+2,
\qquad
\deg_{w_r}\operatorname{num}I_r=2r-1.
\]

The denominator formula is established by connected path incidence. The
numerator formula—and hence all-chain vanishing at infinity—is not yet proved.

## Next falsifier

Derive a terminal-site recursion from the ordered propagator expansion and
show that its two leading powers cancel locally. A failure at any chain length
would produce a boundary-at-infinity coefficient absent from the present
carrier inventory.

## Durable evidence

- `research/nima/derive_mass_insertion_path_integrand.sage`;
- `research/nima/check_three_mass_insertion_first_pushforward.sage`;
- `research/nima/check_four_mass_insertion_terminal_asymptotic.sage`;
- allocator claim `seqclaim-b7ec309ac0113f5c1cae88b2`.
