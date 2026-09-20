# Xi-torsion lift iteration 3: the bordered synthesis is well defined, but is not a fixed-translate system because shell width changes the atom

## Vector-valued synthesis

Let `lambda=(p,k)` denote a prime-power seam `c_lambda=k log p`, with its
source-prescribed shell `[a_lambda,b_lambda]` and frozen loading `omega_lambda`.
The natural bordered synthesis is

\[
J_B(c)(z)
=
\sum_\lambda c_\lambda\omega_\lambda
T_{PB}^{\rm rig}
\left(e^{z\cdot}\otimes K_{1,c_\lambda}
\right)_{[a_\lambda,b_\lambda]}.
\]

The prime-loaded moving-seam completion already gives absolute convergence in
the projective rigged dual under the frozen majorant. Hence `J_B` is a
well-defined continuous vector-valued synthesis on finite spectral compacta.
This supplies the correctly typed ambient map missing in iteration 2.

## Fixed-translate recovery does not transfer automatically

The scalar theta synthesis has one fixed atom translated to the distinct
positions `+-L_lambda`. Its Fourier transform therefore factors as

\[
\widehat\Phi(\xi)
\sum_\lambda d_\lambda e^{i\xi L_\lambda},
\]

which permits Bohr coefficient extraction.

For `J_B`, the atom changes with the shell geometry. Already the delta endpoint
coordinate at seam `c=b` is

\[
E_{e^{z\cdot},\delta_b}(z)
=
\frac12e^{zb}-\frac12e^{z(2a-b)}.
\]

Writing `ell=b-a`, this becomes

\[
E_{e^{z\cdot},\delta_b}(z)
=e^{za}\sinh(z\ell).
\]

Thus translation contributes `e^(za)`, but the atom also contains the
shell-width-dependent multiplier `sinh(z ell)`. The return coordinate similarly
contains

\[
e^{zb}\frac{1-e^{-2z\ell}}{2z}.
\]

Unless all shells have the same width, there is no common bordered atom to
factor out.

## Consequence for Fourier recovery

Distinct seam positions alone no longer prove injectivity or a continuous
inverse. A relation may involve both displacement phases and varying atom
multipliers. Bohr averaging isolates a frequency only after the multiplier has
been separated from the spectral variable, which is exactly what fails here.

The absolute-value component adds further polynomial and divided-Laplace
multipliers; it does not restore a fixed template.

## Horizontal bundle formulation

The proper source object is therefore a bundle of bordered fibers

\[
B_\lambda
=
B_{[a_\lambda,b_\lambda],c_\lambda},
\]

not one scalar common-history fiber. Define the labelled direct synthesis

\[
\widetilde J_B:
(c_\lambda)_\lambda
\longmapsto
(c_\lambda\omega_\lambda H_\lambda)_\lambda.
\]

This map retains labels and is recoverable coordinatewise whenever each
`H_lambda` is nonzero and its chosen observer has a quantitative lower bound.
Codiagonalization

\[
\Sigma_B:\bigoplus_\lambda B_\lambda\to B_{\rm border}
\]

is a separate map whose strictness cannot be borrowed from the fixed-theta
codiagonal.

## Exact next gate

Choose one source-derived bordered coordinate `ell_lambda` and prove a uniform
projective estimate

\[
|c_\lambda|e^{\delta L_\lambda}
\le
C_{\delta,\delta'}
q_{\delta'}\bigl(\widetilde J_Bc\bigr)
\]

before summation. Then analyze whether the complete family of endpoint/return
observers remains jointly faithful after `Sigma_B`.

The endpoint coordinate is the first candidate, but its multiplier
`sinh(z ell_lambda)` can vanish and its size depends on the shell width. A pair
of spectral observation lines may avoid individual zeros, yet a uniform lower
bound requires quantitative control of `ell_lambda`.

## Verdict

The bordered synthesis exists continuously in a labelled moving-fiber Köthe
bundle. It is not the translated fixed-atom synthesis used in iteration 1.
Objective 2 therefore reduces to a new nonuniform vector-valued interpolation
problem involving both seam positions and shell widths.