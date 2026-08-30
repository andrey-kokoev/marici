# 2260 — The Equilateral Quadrupole Readout Is a Tight Frame

The three equilateral occurrence directions define three unit vectors in the
quadrupole plane.  Their Gram matrix is

\[
G_{ij}=\begin{cases}1&i=j,\\-1/2&i\ne j,\end{cases}
\]

with spectrum

\[
\left(\frac32,\frac32,0\right).
\]

Hence they form a tight frame for the two-dimensional shear plane:

\[
\sum_{i=1}^3q_iq_i^T=\frac32I_2.
\]

This explains why the quadrupole adapter is balanced across the three
occurrences.  No occurrence is preferred, and the two cyclotomic directions
have equal information weight.  The rank-three scalar-plus-shear matrix has
determinant \(-6\) in the integral scaled convention.

Thus the homogeneous triangle is not merely separable by anisotropy; its
native cyclic geometry supplies the optimal isotropic rank-two frame.

Verified by
`research/benincasa/checkers/quadrupole_information_geometry.rs`.
