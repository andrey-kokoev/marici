# Correction: image pairing leaves a rank-one half-kernel

Pair the nonzero translation aliases with constants

\[
\frac{2}{2k\ell}=\frac1{k\ell},\qquad k\ge1.
\]

After extracting the two nearest reflected images, pair the farther reflected
aliases with constants

\[
\frac1{2k\ell}+\frac1{2(k+1)\ell},\qquad k\ge1.
\]

The constants do not cancel term by term. Their signed difference telescopes:

\[
\sum_{k\ge1}\left[
\frac1{k\ell}-\frac1{2k\ell}-\frac1{2(k+1)\ell}
\right]
=\frac1{2\ell}.
\]

On `L2(0,ell)`, the constant kernel `1/(2ell)` is rank one and has operator
norm `1/2`. The half-normalized Weil multiplier therefore incurs an additional
budget `1/4` unless an exact distributional derivation proves an opposite
local term. Zero mean of the odd extension does not by itself annihilate this
interval rank-one kernel after the direct/reflected reduction.

Accordingly, the presently safe full-image boundary budget is

\[
C_\partial\le
\frac\pi{\sqrt3}+\log2-\frac18,
\]

not `pi/sqrt(3)+log(2)-3/8`.
