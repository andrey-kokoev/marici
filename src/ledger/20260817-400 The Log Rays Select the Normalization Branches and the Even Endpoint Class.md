---
id: 400
date: 2026-08-17
title: The Log Rays Select the Normalization Branches and the Even Endpoint Class
---

# The Log Rays Select the Normalization Branches and the Even Endpoint Class

Entry 399 produced two labelled endpoint rays with boundary
\[
 r_1-r_{D03}.
\]
The global normalization source has two sheet costalks
\(e_+,e_-\), reflection exchanges both ray labels and both sheet labels, and
the conductor quotient is the oriented difference
\[
 e_+-e_-.
\]

Any integral reflection-equivariant map from the ray permutation lattice to
the sheet permutation lattice has matrix
\[
 M(a,b)=
 \begin{pmatrix}a&b\\ b&a\end{pmatrix}.
\]
Compatibility with the exceptional boundary requires
\[
 M(a,b)(-1,1)^T=(1,-1)^T,
 \qquad b-a=1.
\]
Compatibility with the common normalized endpoint counit requires each
column to augment to one:
\[
 a+b=1.
\]
These equations have the unique integral solution
\[
 a=0,qquad b=1,qquad
 M=
 \begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Its determinant is \(-1\), so the comparison is unimodular. In the fixed
orientation convention,
\[
 r_{D03}\longmapsto e_-,
 \qquad
 r_1\longmapsto e_+.
\]
No half-difference, sheet section, or inversion of two is used.

## Endpoint mapping fiber

This matrix supplies the geometric connector cell absent from the earlier
hemisphere-only calculation. The previously conditional endpoint equation
\[
 2a+b=1
\]
now has its geometrically selected values \((a,b)=(0,1)\). Therefore the
endpoint-fixed mapping fiber is instantiated and
\[
 \boxed{p_{\partial,Q}=0\in\mathbb Z/2.}
\]
The polarity connecting homomorphism
\[
 H^1(D_3;\mathbb Z_{\rm or})\longrightarrow H^2(D_3;\mathbb Z)
\]
sends this class to zero, so the corresponding conductor Bockstein also
vanishes.

The earlier \(\mathbb Z/2\) torsor was real before a geometric connector
was supplied: the primitive hemisphere \(Q\)-row alone could not choose a
component. The log-ray boundary plus the normalized counit provides exactly
the missing second equation and selects the even component.

## Scope and next test

The conclusion uses the labelled positive exceptional interval, the fixed
conductor-difference orientation, and the normalized odd endpoint counit
already established in the local model. Within that scope the complete
three-road endpoint/\(Q\) mapping fiber now exists and its parity is fixed.

The next falsification tests are the promised global ones: extend the selected
component through the full dihedral \(D_8\) action and evaluate the Jordan
compatibility condition. Those tests are now well typed.

The executable audit is
research/voevodsky/check_log_ray_normalization_branch_identification.py.
