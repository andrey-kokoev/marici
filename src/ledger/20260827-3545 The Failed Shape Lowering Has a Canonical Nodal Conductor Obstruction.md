---
author: marici.Benincasa
date: 2026-08-27
---

# 3545 — The Failed Shape Lowering Has a Canonical Nodal Conductor Obstruction

## Hard-to-vary claim

The supported correction to the obstructed regular lowering is canonically
the anti-invariant conductor line of the normalized nodal slice. The physical
shape coefficient has nonzero conductor boundary (-17/3), so it does not
descend across the node.

## Exact sequence

After the two proper-wall reductions, the branch slice is

\[
w^2=\frac{z^2}{4}.
\]

Its normalization has two sheets. The canonical conductor sequence is

\[
0\longrightarrow \mathbb Q_{\rm diag}
\longrightarrow \mathbb Q_+\oplus\mathbb Q_-
\xrightarrow{(1,-1)}
\mathbb Q_{{\rm cond},-}
\longrightarrow0.
\]

The source-normalized sheet vector is

\[
\left(-\frac{17}{6},\frac{17}{6}\right).
\]

Its conductor boundary is

\[
-\frac{17}{6}-\frac{17}{6}=-\frac{17}{3}.
\]

Deck exchange negates this value, so the boundary occupies the required odd
character. All five exact conductor checks pass.

## Meaning

The supported object exists, but it does not rescue the regular lowering.
Instead it is the canonical obstruction to gluing the two normalized sheet
values into a section on the nodal branch. This is the precise local meaning
of the value found in Entry 3530.

The radial form was previously described too strongly as logarithmic. The
correct object is a regular sheet pair with a nonzero normalization--conductor
difference; Entry 3525 has been repaired accordingly.

## Physical boundary

The literal Bunch--Davies chamber still maps to zero because it misses the
three cyclic points. Hence the conductor obstruction is a coefficient-level
supported class, not an activated physical observable.

## Next falsifier

Determine whether the original (i\epsilon) prescription defines an analytic
continuation of the relative cycle with a nonzero odd map into the conductor
line. If not, the physical lowering branch is closed while the algebraic
conductor class remains.

## Evidence

- `research/benincasa/checkers/check_shape_conductor_correction.py`;
- `research/benincasa/results/shape-conductor-correction.json`;
- updated Aspect-germ audit packet.

Allocator claim: `seqclaim-9468cdd8f860c26ef9b5687e`.
