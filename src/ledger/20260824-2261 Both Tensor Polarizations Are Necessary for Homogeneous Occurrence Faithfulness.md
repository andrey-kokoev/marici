# 2261 — Both Tensor Polarizations Are Necessary for Homogeneous Occurrence Faithfulness

The scalar port plus either single tensor polarization has rank two, not three.
In the scaled equilateral convention:

\[
q_+=(2,-1,-1),
\qquad
q_\times=(0,-1,1).
\]

With only the plus port, the invisible occurrence packet is

\[
(0,1,-1).
\]

With only the cross port, it is

\[
(-2,1,1).
\]

Both are also annihilated by the scalar sum.  Adding both polarizations gives

\[
\det
\begin{pmatrix}
1&2&0\\
1&-1&-1\\
1&-1&1
\end{pmatrix}
=-6,
\]

so the blind line disappears.

Therefore two independent tensor-polarization ports are necessary and
sufficient for faithful homogeneous occurrence readout.  A detector exposing
only one polarization causes a precise rank-one readout loss even though the
Carrier and source coefficient packet remain complete.

Verified by
`research/benincasa/checkers/quadrupole_information_geometry.rs`.
