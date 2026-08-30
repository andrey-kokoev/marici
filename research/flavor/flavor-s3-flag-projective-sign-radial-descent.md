# The cubic flag selector is sign- and radius-blind on its projective output: WP955

## Question

Do the cubic coefficient sign and doublet radius remain physical selector inputs after WP954's order parameter is mapped to the relational `Z2` flag and WP350 down ray?

## Projective flag map

For a nonzero standard-doublet vector `n`, define

\[
\Pi_n=\frac{nn^T}{n^Tn}.
\]

Let `d=(1,1,1)^T` and

\[
\Pi_V=I-\frac{dd^T}{3}
\]

be the projector onto the standard plane. The orthogonal down-line projector is

\[
\Pi_{\downarrow}(n)=\Pi_V-\Pi_n.
\]

Both maps satisfy

\[
\Pi_{\rho n}=\Pi_n,
\qquad
\Pi_{-n}=\Pi_n
\]

for every nonzero real `rho`. Therefore the derived flag and down ray are blind to radial magnitude and vector orientation.

At `n=(1,1,-2)^T`, the exact down-line projector is

\[
\Pi_{\downarrow}
=
\frac12
\begin{pmatrix}
1&-1&0\\
-1&1&0\\
0&0&0
\end{pmatrix},
\]

the projector onto `(1,-1,0)`.

## Opposite cubic orbits

WP954's minimum and maximum vector orbits are negatives of one another. After applying `Pi_n`, their sets of projective flags coincide exactly. Reversing the cubic coefficient therefore does not change the selected `Z2` flag orbit or the derived down coefficient lines.

The cubic sign would regain authority only if another coupling were odd in `n` rather than depending on its axis or orthogonal projector. Such a coupling is extra source structure and must be declared independently.

## Positive operation and boundary

Given an admitted relational identification between the coefficient standard plane and the flavor operator module, compression

\[
X\longmapsto\Pi_{\downarrow}X\Pi_{\downarrow}
\]

is a completely positive single-Kraus operation selecting the down line. It is not trace-preserving on the full module; its operational meaning is a conditional port or protected compression, not a complete detector channel.

This improves WP954's authority accounting but does not establish the identification with family-space Grams, the doublet's physical origin, the complex third projector ray, radial Yukawa amplitudes, stability under general `S3`-invariant completion, or a calibrated instrument. A zero cubic leaves the angular flag unselected, and nonlinear functions of the cubic can introduce additional extrema.

## Disposition

The minimal cubic flag template selects a projective `S3/Z2` orbit without requiring the sign or magnitude of the order parameter. The selector is more robust than its vector presentation suggested. The remaining source gate is the existence and coupling type of the standard doublet, not its orientation sign.

No parameter is assigned physical time. The smallest falsifier is an admitted odd-in-`n` coupling or completion whose projective minima are not the three transposition axes.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp955_s3_flag_projective_sign_radial_descent.py

Generated result: `research/flavor/results/wp955_s3_flag_projective_sign_radial_descent.json`.
