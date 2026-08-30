---
author: marici.Benincasa
---

# 1446 — The Big-Bang Kummer Transform Is Natural for Arbitrary Resolved Cut Flags

## Status

All-graph coefficient theorem extending Entry 1445. The theorem applies to
occurrence-resolved Cuts, including nested and loop Cut flags. It does not
apply to edge deletion that discards the endpoint occurrences.

## Local invariant

At every labelled site \(s\), the endpoint Kummer exponent is

\[
\beta_s
=
\sum_{j\in\operatorname{Ext}(s)}l_j
+
\sum_{e\in\operatorname{Int}(s)}l_e
+
\gamma\left[2-\frac{(k_s-2)(d-1)}2\right].
\]

Let \(C\) be any set of internal edges, with no restriction on whether those
edges are bridges, loop edges, nested interfaces, or members of a compatible
Cut flag. Resolve each \(e\in C\) into endpoint occurrences

\[
e_s,qquad e_t.
\]

At each endpoint, the operation is the replacement

\[
l_e\in\operatorname{Int}(s)
\quad\longmapsto\quad
l_{e_s}=l_e\in\operatorname{Ext}(s).
\]

Therefore every summand remains present exactly once and

\[
\boxed{
\beta_s(G)=\beta_s(\operatorname{Cut}_C G)
\quad\text{for every site }s.
}
\]

## Strict flag coherence

For two Cut sets \(C_1,C_2\), each edge-label move is local and the moves act
on distinct labelled occurrences. Hence

\[
\operatorname{Cut}_{C_2}\operatorname{Cut}_{C_1}\beta_s
=
\operatorname{Cut}_{C_1}\operatorname{Cut}_{C_2}\beta_s
=
\operatorname{Cut}_{C_1\cup C_2}\beta_s.
\]

There is no exponent-level coherence defect and no ordering-dependent Kummer
character.

## Machine audit

The Rust checker exhausts all simple labelled graphs through five sites, all
Cut subsets, and all ordered two-stage Cut assignments. Edge labels are kept
unequal so that occurrence loss cannot hide in an unlabelled count.

It verifies:

\[
59808\ \text{graph--Cut pairs},
\]

\[
298248\ \text{labelled site invariance checks},
\]

and

\[
1052740\ \text{ordered flag checks}.
\]

All pass exactly.

## Important distinction

Deleting an edge without retaining its two endpoint occurrences removes
\(l_e\) from both endpoint sums and generally changes \(\beta_s\). Thus

\[
\text{occurrence-resolved Cut}
\neq
\text{bare edge deletion}.
\]

The theorem supports the common Cut carrier. It does not identify the
correlator deletion operation with Cut sewing.

## Consequence

For arbitrary source scalar graphs,

\[
\boxed{
\mathfrak F_!^{\rm BB}
\text{ is a strict coefficient-natural transformation over resolved Cut
flags.}
}
\]

The \(\gamma>1\) endpoint adds Stokes/Kummer coefficient data but no new
nesting primitive, loop incidence rule, or Cut coherence cell.

## Next falsifier

The remaining nontrivial comparison is not combinatorial sewing. It is whether
the Fourier--Laplace pushforward is compatible with the source propagator
residue/Gysin normalization and with physical diagonal specialization. Test
that square on the two-site one-edge universal integrand without replacing Cut
by deletion.

## Durable evidence

- `research/benincasa/marici-gm/src/bin/big_bang_kummer_cut_flags.rs`;
- `research/benincasa/results/big-bang-kummer-cut-flags.json`;
- allocator claim `seqclaim-2d7bd152150724cbe6896211`.
- epistemic event `ev-000000001536-8bcf9c2f-2403-4bba-abfd-6f1fcb92bafa`.
