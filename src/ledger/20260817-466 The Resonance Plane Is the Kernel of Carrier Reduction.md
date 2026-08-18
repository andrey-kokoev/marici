---
id: 466
date: 2026-08-17
title: The Resonance Plane Is the Kernel of Carrier Reduction
---

# The Resonance Plane Is the Kernel of Carrier Reduction

Benincasa Entry 465 closes the boundary-extension gate for the normalized odd
Cartier map.  The remaining specialization map must be typed correctly before
it is constructed.

At the frozen soft fiber, every exact-form image is divisible by (a^4).
Consequently there is a canonical linear map

\[
\frac{\mathbb Q[a,c]}{a^4\operatorname{im}D}
\longrightarrow
\frac{\mathbb Q[a,c]}{(a^4)},
\qquad c=b+1.
\]

Its kernel is

\[
\frac{(a^4)}{a^4\operatorname{im}D}
\simeq
a^4\left(
\frac{\mathbb Q[a,c]}{\operatorname{im}D}
\right),
\]

and Entry 449 identifies its basis as

\[
[a^4],qquad[a^{11}c].
\]

Thus the Euler-resonance plane is canonically a **kernel** of carrier
reduction.  It is not canonically a quotient of the complete exact cokernel,
and there is no derived projection onto it.

The cutoff dimensions make the sequence exact without residual terms.  At
total degree (D\ge12),

\[
\dim C_{\rm full}=4D,
\qquad
\dim C_{\rm carrier}=4D-2,
\qquad
\dim\ker=2.
\]

The two missing dimensions are exactly the restored divided resonances
((4,0)) and ((11,1)).

This changes the categorical formulation of the next gate.  One should not
seek a map from the full cokernel **onto** the length-three Cartier resonance
object.  The correct relative-support construction is the fiber of the map
from the weighted-Rees exact cokernel to the flat quartic carrier module.  Its
special fiber is the resonance plane, and Entries 464--465 predict its
Cartier-thickened nearby structure.

The next step is to lift this carrier-reduction sequence over the complete
weighted Rees family and test exactness there.  Any failure is then a precise
kernel, cokernel, or extension defect rather than an ambiguity of projection.

The executable audit is
research/voevodsky/check_soft_axis_resonance_kernel_sequence.py.
