# The half factor is the primitive closure of four bitangent differences

The four critical lines of the reflection-adapted pencil are bitangents of the branch quartic. Their inverse images split as

\[
C_i^+\cup C_i^-,\qquad i=1,2,3,4,
\]

where each \(C_i^\pm\) is a \((-1)\)-curve and

\[
C_i^++C_i^-=-K_S.
\]

Define the component differences

\[
d_i=[C_i^+]-[C_i^-].
\]

The two components over one bitangent meet at its two tangency points, while components over distinct pencil lines meet at the corresponding one of the two points above the common pencil center. Consequently

\[
d_i^2=-6,
\qquad
d_i\cdot d_j=2\quad(i\ne j),
\qquad
d_1+d_2+d_3+d_4=0.
\]

The lattice generated directly by the four differences is not primitive. Its primitive closure contains

\[
\alpha_{12}=\frac{d_1+d_2}{2},
\quad
\alpha_{13}=\frac{d_1+d_3}{2},
\quad
\alpha_{14}=\frac{d_1+d_4}{2},
\]

with Gram matrix

\[
(\alpha_{1i}\cdot\alpha_{1j})=-2I_3.
\]

Thus the invariant algebraic lattice is

\[
E_7^+\cong A_1^3,
\]

and the raw component-difference lattice has index four in its primitive closure.

In the primitive \((\alpha_{12},\alpha_{13},\alpha_{14})\) frame, the four differences are

\[
\begin{aligned}
d_1&=(1,1,1),&d_2&=(1,-1,-1),\\
d_3&=(-1,1,-1),&d_4&=(-1,-1,1).
\end{aligned}
\]

This explains the source factor

\[
\tau\longmapsto-\frac12e_6.
\]

A single component difference is generally not twice a primitive root; halves become integral only in correlated sums of two split fibers. The factor \(1/2\) is therefore saturation geometry, not ambient torsion.

It also reveals the natural origin of a two-bit ambiguity: four component differences occupy an index-four sublattice of the primitive invariant lattice. The parity should be obtained by locating the source generators in this saturation quotient, not by choosing among abstract labels.

Certificate:

- `research/voevodsky/checkers/primitive_closure_of_split_fiber_differences.py`;
- `research/voevodsky/results/split_fiber_primitive_closure.json`.
