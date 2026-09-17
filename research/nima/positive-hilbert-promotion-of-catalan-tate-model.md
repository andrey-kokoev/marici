# Positive Hilbert promotion of the Catalan–Tate model

The canonical channel model has an ordinary positive Hilbert realization.

For `D=|D_n|`, use

\[
\mathcal H_{even}=\ell^2(\mathbb Z^D),
\qquad
\mathcal H_{odd}=L^2(\mathbb T^D).
\]

Pontryagin Fourier transform is unitary:

\[
\mathcal F:\ell^2(\mathbb Z^D)\xrightarrow{\sim}L^2(\mathbb T^D).
\]

Under the canonical bidual identification,

\[
\mathcal F^2=\mathcal R,
\qquad
\mathcal F^4=I.
\]

Place two lattice and two torus presentations in the four chart slots. Add the homological shift at the fourth wrap to obtain the graded relation

\[
\widetilde{\mathcal F}^{\,4}=\Sigma.
\]

## Catalan sector

The incidence atoms

\[
\delta_{v_T}\in\ell^2(\mathbb Z^D)
\]

form an orthonormal family. Therefore `H_n` embeds isometrically, forced-channel projections are positive orthogonal projections, and polygon rotation is unitary.

The four-chart Hilbert direct sum has four equal orthogonal summands. Each chart projection has normalized dimension or regulated trace `1/4`.

## Cone sector

Give normalized finite simplex chains their standard positive inner product and form

\[
N_*\mathbb C[\sigma]\widehat\otimes\mathcal H_i.
\]

Face maps are bounded. Mapping cones carry the positive direct-sum graph norm

\[
\|(y,x)\|_{Cone}^2=\|y\|^2+\|x\|^2.
\]

This promotes the bounded cone-valued indexing model to Hilbert chain complexes. Its simplex-face cones remain contractible.

## Trace regulator

The number operator

\[
N\delta_m=\lVert m\rVert^2\delta_m
\]

is positive self-adjoint, and `exp(-tN)` is trace class for every `t>0`. Fourier conjugates it to the positive torus Laplacian. The heat-regularized chart trace is exactly `1/4`.

## Scope

This is an ordinary positive Hilbert promotion of the canonical Catalan/channel/Tate model. It supplies positive norms, unitary chart transport, orthogonal projections, bounded cone maps, and positive trace-class regulators.

The historical raw eight-leg feature has a separate source-volume divergence and remains regulator-relative. The historical signed Tate/Weil form is represented by a bounded self-adjoint multiplier on its phase-energy Hilbert space; positivity of that signed form requires vanishing of its negative spectral leg. The present promotion does not supply that arithmetic vanishing theorem.

`check_positive_hilbert_tate_promotion.py` verifies finite cyclic Fourier models of sizes 5, 7, and 11, including unitarity, reflection square, fourth-power closure, positive Gram, and exact chart weight.
