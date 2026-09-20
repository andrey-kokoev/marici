# Xi-torsion lift iteration 5: atomic coefficient extraction is continuous only on the marked five-cell carrier, not on the unmarked distribution target

## Continuity audit

Iteration 4 used an atomic endpoint projection. On an ordinary distribution
space this projection is not continuous. A delta distribution is a limit of
smooth mollifiers in the distribution topology, while all mollifiers have zero
atomic coefficient. Hence no continuous map

\[
\mathcal S'\to\mathbb C
\]

can extract the coefficient of `delta_b` on an unrestricted distributional
neighborhood.

Singular order is detectable microlocally, but coefficient extraction is not a
continuous linear projection in the bare `S'` topology.

## Where the projection is valid

The rigged crossing is not defined on arbitrary second legs. Its admitted
carrier is the finite-dimensional marked space

\[
M_5=\operatorname{span}(\Phi,\mathbf1,\delta_0,K,V).
\]

On `M_5`, coefficient projections onto the declared basis cells are continuous.
The source point

\[
K_1=\delta_0-\frac12K
\]

has a fixed, independently derived decomposition. Translation moves the marked
`delta_0` cell to `delta_c`, and Fourier transport permutes the marked cells:

\[
\delta_0\leftrightarrow\mathbf1,
\qquad
K\mapsto V\mapsto-K.
\]

Therefore the correct observer is not “take the atomic part of an unmarked
output distribution.” It is “retain the `delta` occurrence label through the
partial-transpose crossing.”

## Marked bordered target

Define the refined target before adding the five contributions:

\[
B_{\rm border}^{\rm mark}
=
\bigoplus_{s\in\{\Phi,1,\delta,K,V\}}B_s,
\]

with assembly

\[
\Sigma_5:B_{\rm border}^{\rm mark}\to B_{\rm border}.
\]

The restricted crossing lifts canonically coordinatewise because its partial-
transpose definition evaluates each declared second-leg cell separately. On
this marked target, projection to the translated delta cell is continuous,
cutoff-diagonal, and Fourier-covariant after permuting cell labels.

The endpoint exponential observer from iteration 4 is consequently rigorous
on `B_border^mark`.

## What is not proved

The published complete bordered packet is assembled after applying the linear
combination `delta-(1/2)K`. Unless it retains `Sigma_5` as a marked graph map,
the delta projection does not descend to `B_border`.

A cancellation between delta and `K` outputs can therefore be invisible in the
unmarked topology even though the source decomposition was canonical. Fourier
covariance does not fix this: in the next chart the delta cell becomes the
constant cell, so “atomic singularity” is not an invariant description.

## Revised strictness statement

The vector-valued synthesis

\[
J_B^{\rm mark}:K_B\to B_{\rm border}^{\rm mark}
\]

has a continuous coefficient-recovery observer through its delta-labelled
endpoint coordinate. Thus it is a strict topological embedding onto its range.
It is horizontal because parameter differentiation acts on the regular first
leg and does not mix the five occurrence labels.

Descent to the unmarked codiagonal requires one more theorem:

\[
\Sigma_5\text{ is injective and strict on }
\operatorname{im}J_B^{\rm mark}.
\]

This is a finite-cell cancellation problem coupled to the infinite arithmetic
labels, not a distributional regularity statement.

## Consequence for H-border

The independently constructed `H_border` has a canonical marked lift because
it is defined from the specific source point `K_1`. Therefore objective 2 is
proved in the marked five-cell bordered category. It is not yet proved after
forgetting the occurrence label through `Sigma_5`.

## Next executable test

Use the explicit shell formulas to test whether the delta and absolute-value
endpoint outputs can cancel after all four Fourier charts are retained. Joint
four-chart injectivity of `Sigma_5` on the two-dimensional `span(delta,K)`
source sector would close the descent gate.