# Xi-torsion lift iteration 6: opposite Fourier charts invert the delta--K assembly by a finite Hadamard transform

## Four source points

The pointed Clark orbit is

\[
S_0=\delta-\frac12K,
\qquad
S_1=\mathbf1-\frac12V,
\qquad
S_2=\delta+\frac12K,
\qquad
S_3=\mathbf1+\frac12V.
\]

All signs and normalizations are source-fixed by the Fourier orbit of `K_1`.
The complete bordered packet retains all four charts.

## Opposite-chart inversion

For a fixed regular first leg `f`, write

\[
y_j=T_{PB}^{\rm rig}(f\otimes S_j).
\]

Linearity gives

\[
T_{PB}^{\rm rig}(f\otimes\delta)
=\frac12(y_0+y_2),
\]

\[
T_{PB}^{\rm rig}(f\otimes K)
=y_2-y_0,
\]

and similarly

\[
T_{PB}^{\rm rig}(f\otimes\mathbf1)
=\frac12(y_1+y_3),
\]

\[
T_{PB}^{\rm rig}(f\otimes V)
=y_3-y_1.
\]

Thus forgetting the five-cell labels but retaining opposite Fourier charts is
invertible on the four-dimensional Clark sector. The inverse is a fixed finite
Hadamard-type matrix, hence continuous in every locally convex target topology.

No injectivity of `T_PB` itself is required: the statement recovers the four
**outputs**, which is exactly what is needed to descend the marked observer.

## Prime and completion compatibility

The inversion acts only in the finite chart index. It commutes with:

- prime and grade cutoffs;
- moving-seam translation;
- projective Köthe summation;
- spectral differentiation;
- passage to the analytic Silva germ topology.

Its operator constants are independent of the prime cutoff and shell width.
Therefore strictness of the marked delta endpoint observer descends to the
complete four-chart bordered packet.

## Forcing cell

The full pointed map also contains the forcing-reservoir summand
`f tensor Phi`. If the same forcing output is included in every chart, opposite
chart differences eliminate it:

\[
(y_2^{\rm full}-y_0^{\rm full})
=T_{PB}^{\rm rig}(f\otimes K),
\]

up to the displayed fixed normalization. Opposite sums contain the forcing
term and the delta output; the independently retained forcing channel separates
them. For `H_border` itself only the Clark primitive sector is used, so this
extra subtraction is unnecessary.

## Consequence for H-border

The marked lift of

\[
H_{\rm border}
=T_{PB}^{\rm rig}(e^{z\cdot}\otimes K_1)
\]

can now be recovered continuously from the unmarked complete four-chart packet:
first invert opposite charts to obtain the delta-labelled output, then apply
the endpoint exponential/Bohr observer from iteration 4.

Hence, under the already declared retention of all four Fourier charts, the
bordered synthesis

\[
J_B:K_B\to B_{\rm border}^{(4)}
\]

is a strict horizontal embedding onto its source-generated range.

## Scope of the result

This closes the occurrence-label descent gate. It does not yet identify the
bordered source range with the translated-theta scalar range from objective 1;
that identification is unnecessary if the torsion argument is formulated in
`coker(J_B)`.

The remaining task is to formulate the bordered cokernel with its induced
regular spectral connection and prove that its analytic graph topology is
Hausdorff and divisor-adically separated. Strictness of `J_B` now supplies the
closed-range input for that proof.