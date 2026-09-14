# The total-energy thimble meets the fixed outer D4 arm

The local compound-\(D_4\) equation has quadratic factor

\[
q_2=\frac12\bigl((n')^2-s^2+3E^2\bigr).
\]

Take the site-symmetric transverse slice \(n'=0\). The resulting surface singularity is

\[
2XY=E(\sqrt3E-s)(\sqrt3E+s).
\]

This is the standard three-branch presentation of a \(D_4\) singularity. In its minimal resolution, the three distinct tangent factors

\[
E,
\qquad \sqrt3E-s,
\qquad \sqrt3E+s
\]

produce the three outer exceptional arms; the central exceptional curve joins them.

The source degeneration is specifically normal to the labelled divisor

\[
E=0.
\]

Accordingly, its based vanishing thimble follows the \(E\)-branch. In the simultaneous resolution its strict transform meets the **outer arm labelled by \(E\)**, rather than the central curve.

It therefore has nonzero image in

\[
D_4^\vee/D_4.
\]

Site exchange reverses the conductor tangent,

\[
s\mapsto-s.
\]

It swaps the two outer arms labelled by \(\sqrt3E-s\) and \(\sqrt3E+s\), while fixing the \(E\)-arm. Hence the total-energy thimble represents the unique nonzero triality-fixed class.

In the four-mark description, this is the diagonal pairing

\[
(++,--)\mid(+-, -+).
\]

Thus the geometry has selected an intrinsic parity class without fitting coefficients:

\[
[B]_{\rm geom}=\text{the diagonal }D_4\text{ discriminant class}.
\]

One normalization problem remains. Naming this class as a numerical pair in the ordered source coordinates \((e_6,v_{\rm alg})\) requires an integral Betti comparison for those two de Rham lines. Without that comparison, calling it specifically \((1,1)\), \((1,0)\), or \((0,1)\) would still be coordinate fitting. The invariant answer is the fixed outer-arm/diagonal-matching class.

Certificate:

- `research/voevodsky/checkers/d4_symmetric_slice_total_energy_arm.py`;
- `research/voevodsky/results/d4_symmetric_slice_total_energy_arm.json`.
