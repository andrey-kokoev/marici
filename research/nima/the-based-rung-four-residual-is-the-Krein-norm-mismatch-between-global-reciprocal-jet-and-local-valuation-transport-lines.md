# The based rung-four residual is the Krein-norm mismatch between global reciprocal-jet and local valuation-transport lines

## Common based double

Let `b_z` be the retained nonzero corrected pair state with positive local
energy

\[
E_p(b_z)=\|b_z\|_p^2>0.
\]

Form the hyperbolic double

\[
\mathcal K_p=H_p\oplus H_p,
\qquad
J_p=\operatorname{diag}(I,-I).
\]

Two source-derived presentations of the same reciprocal pair are available.

## Global reciprocal-jet line

The first nonzero Xi jet obeys

\[
\tau_m(-\bar z)=(-1)^m\overline{\tau_m(z)}.
\]

After removal of the parity phase, the two reciprocal jet amplitudes have equal
norm. Thus the global functional equation selects a neutral line in the double:

\[
L_{\rm jet}(b_z)=
\operatorname{span}\{(b_z,e^{i\theta_m(z)}b_z)\},
\]

with

\[
[(b_z,e^{i\theta}b_z),(b_z,e^{i\theta}b_z)]_{J_p}=0.
\]

## Local valuation-transport line

The primewise reciprocal transport gives the weighted line

\[
L_{p,z}(b_z)
=
\operatorname{span}\{(b_z,p^{-z}b_z)\}.
\]

Its Krein norm is

\[
[(b_z,p^{-z}b_z),(b_z,p^{-z}b_z)]_{J_p}
=
\bigl(1-p^{-2\operatorname{Re}z}\bigr)E_p(b_z).
\]

This is exactly the final placewise Hermitian residual.

## Rung-four cell

The missing coherence is now a comparison of two based lines in the same
hyperbolic carrier:

\[
L_{\rm jet}(b_z)
\Longrightarrow
L_{p,z}(b_z).
\]

A `J_p`-isometric comparison exists only if the local line is neutral. Since
`E_p(b_z)>0`, this occurs exactly when

\[
\operatorname{Re}z=0.
\]

The first nonzero jet contributes the global equal-norm reciprocal
normalization; valuation transport contributes the transverse prime modulus;
the retained base contributes noncollapse.

## Claim boundary

This constructs the final residual as a metric mismatch between two
independently sourced line presentations. It does not construct the isometric
comparison cell. Existence of that cell is the rung-four filler and remains
equivalent to confinement.

## Finite falsifier

At one prime and one source vector, compare the two Gram matrices

\[
\begin{pmatrix}E_p&0\\0&E_p\end{pmatrix}
\quad\text{and}\quad
\begin{pmatrix}E_p&0\\0&p^{-2\operatorname{Re}z}E_p\end{pmatrix}.
\]

No `J_p`-isometry preserving the based first coordinate can identify their
selected lines off the seam.