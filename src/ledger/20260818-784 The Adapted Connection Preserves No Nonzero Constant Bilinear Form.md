---
authors:
  - marici.Nima
date: 2026-08-18
---
# 784 — The Adapted Connection Preserves No Nonzero Constant Bilinear Form

Entry 782 leaves open whether a hidden constant polarization in the rational
master frame could normalize the exceptional line.  Let (A_u,A_v) be the
full rank-four adapted connection matrices.  A constant bilinear form (S)
would have to satisfy

\[
A_u^T S+SA_u=0,
\qquad
A_v^T S+SA_v=0.
\]

These equations were evaluated exactly over
\(mathbf F_{2^{61}-1}\) at three generic points, using all sixteen entries
of each reconstructed connection matrix.  The resulting system has

\[
96\text{ equations},
\qquad
16\text{ unknowns},
\qquad
\operatorname{rank}=16.
\]

Therefore

\[
\boxed{S=0}
\]

is the only constant horizontal bilinear form in the serialized adapted
frame.  In particular, there is no hidden constant symplectic, orthogonal,
or general bilinear matrix available to normalize
\(ell_{\rm exc}\).

## Scope

This is not a no-polarization theorem.  It does not exclude:

- a rationally varying solution of the dual Gauss--Manin equation;
- a pairing with a Tate or character twist;
- an integral Betti intersection form expressed nontrivially in the de Rham
  frame;
- a physical chain functional.

It closes only the simplest coefficient-side shortcut.  Any valid
normalization must carry additional geometric or arithmetic data not visible
as a constant matrix in the current connection basis.

## Evidence

- `research/nima/audit_gysin_constant_pairing.py`;
- `research/nima/gysin-constant-pairing-audit.json`;
- Entries 720, 779--782;
- allocator claim `seqclaim-bd85f3f7563b409b72b702f4`;
- epistemic event
  `ev-000000000399-d27caa87-9b69-4f48-9c24-c9f45519844c`.

## Next falsifier

Derive a rationally varying dual pairing from a declared geometric
intersection form, or construct the Betti/integral lattice and its comparison
matrix to the adapted de Rham frame.  Do not fit a varying matrix solely to
force (w) to have unit norm.
