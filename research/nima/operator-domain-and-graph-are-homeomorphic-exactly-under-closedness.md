# Operator domain and graph are homeomorphic exactly under closedness

For an operator `A:D(A) subset X -> Y`, give the domain its graph topology, defined by

\[
\|x\|_A=\bigl(\|x\|_X^2+\|Ax\|_Y^2\bigr)^{1/2}.
\]

Then

\[
j_A:D(A)_A\to\operatorname{Graph}(A),
\qquad x\mapsto(x,Ax)
\]

is an isometric homeomorphism onto the graph with its product-subspace topology. Its inverse is the first projection. If `A` is closed and `X,Y` are complete, both sides are complete.

For a finite family `(A_i)`, the same statement holds for the joint graph norm and the diagonal graph map whenever the family is jointly closed. For closable families it holds after taking the closure of the operator family, provided the graph closure has no nonzero vertical vectors.

## Correction to the source-pulled construction

Merely retaining the source coordinate in

\[
Kx=(x,(A_ix)_i)
\]

does not prove that projection from the closure of `K(D_0)` is injective. A sequence can satisfy

\[
x_n\to0,
\qquad A_ix_n\to y_i\ne0,
\]

producing a vertical graph vector `(0,(y_i))`. Excluding this is exactly joint closability.

Therefore the previously proposed source-pulled `L/O` completion is a faithful graph presentation only conditionally on joint closability of

\[
U_4,\quad M_aU_4,\quad OU_4,\quad OM_aU_4
\]

in the chosen source and target topologies. The finite checker proves a finite-dimensional model, not this infinite-dimensional gate.

## Exact and conditional candidates

The analytic `L/O` graph built from closed multiplier and retained closed observation is an exact homeomorphic presentation of its graph domain. The broader arithmetic source-pulled graph remains conditional until joint closability is established.

Thus graph replacement is a valid presentation principle, but it must never be used to manufacture closedness or faithfulness by definition.
