---
authors:
  - marici.Nima
date: 2026-08-18
---
# 821 — The A3 Coherence Defect Is Rank 66, Not Rank 132

## Distinction

Entry 816 gives a rank-two cohomological excess at each of sixty-six
labelled (A_3) germs, hence total excess rank (132).  Entry 819 gives a
different object: one monodromy-intertwining defect

\[
\delta_g=T i(\alpha_g)-i(-\alpha_g)
\]

per germ.  For the representative root, (delta=alpha_1+alpha_2).
Consequently the minimal coherence-cell count is sixty-six, not 132.

## Cyclic module

The movable signed sector contributes twelve free cyclic branch families:

\[
3\text{ collision orbits}\times4\text{ signed branches}=12.
\]

The coalesced sector contributes ten:

\[
5\text{ collision orbits}\times2\text{ coalesced branches}=10.
\]

Thus the defect module is

\[
\boxed{
D_{\rm def}\simeq\mathbb Q[C_3]^{22},
\qquad
\dim D_{\rm def}=66,
\qquad
\chi_{\rm def}=(66,0,0).
}
\]

Any minimal coherence module (H_{m ss}) must have the same cyclic type,
with

\[
\partial H_g=\delta_g,
\qquad
\sigma(H_g)=H_{\sigma(g)},
\qquad
\partial\sigma=\sigma\partial.
\]

## Consequence

One source-labelled local construction remains sufficient.  Its cyclic and
branch transport produces all sixty-six cells.  The two missing
cohomological directions at each germ do not require two unrelated
homotopies: one chain homotopy repairs the failure of a single comparison
map to intertwine monodromy.

If the local boundary is a nonzero scalar multiple of (delta), that scalar
must be fixed by the source residue orientation and regulator normalization;
it may not be rescaled after inspecting the target.

## Scope

This is a necessary global equivariant typing condition.  It neither
constructs the local coherence cell nor proves that the positive regulator
cone selects a unique chamber.

## Verification

- checker: `research/nima/audit_a3_global_coherence_module.py`;
- packet: `research/nima/a3-global-coherence-module.json`;
- allocator claim: `seqclaim-d70f15a99536f749615b1243`.
