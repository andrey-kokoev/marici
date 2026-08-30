# Static linear port refinement cannot both add information and inherit every scalar null

## Result

Let `V` be a vector space, let `L: V -> k` be a nonzero scalar readout, and
let `M_i: V -> W_i` be linear refinement ports. If every scalar-null state is
dark at every refined port,

\[
\ker L\subseteq\ker M_i,
\]

then each port factors uniquely through the scalar readout:

\[
M_i=A_i\circ L
\]

for a linear map `A_i: k -> W_i`. In particular, the joint refined readout
contains no information beyond `L`.

Therefore a static linear monitor family cannot have both of the properties
we were asking it to have:

1. add separation power beyond the scalar theta readout;
2. become jointly dark at every scalar zero.

## Proof

Choose `v_0` with `L(v_0)=1`. Every `v` decomposes as

\[
v=L(v)v_0+\bigl(v-L(v)v_0\bigr),
\]

and the parenthesized term belongs to `ker L`. The kernel hypothesis gives

\[
M_i(v)=L(v)M_i(v_0).
\]

Defining `A_i(c)=cM_i(v_0)` proves the factorization. Uniqueness follows
because `L` is surjective onto the one-dimensional field.

## Theta consequence

Take the scalar port to be the aggregate commutator codiagonal and the
refined ports to be cell, moment, or incidence monitors of

\[
h_{a,t}(u)=k(u)\sinh(au)\sin(tu).
\]

If the refined ports genuinely reconstruct more of `h_{a,t}`, they cannot be
forced dark merely by the aggregate integral vanishing. Conversely, if every
scalar zero forces all of them dark by a linear static law, they are only
copies of the scalar port and cannot recover the bright off-seam packet.

The missing RH-strength operation is consequently not another static wall or
another monitor census. It must change the premise. Viable forms include:

- a source equation restricting admissible response packets before readout;
- a transport law carrying one null condition through a generated orbit of
  ports;
- a nonlinear conservation law whose zero set is smaller than a hyperplane;
- a derived comparison cell that couples ports and histories rather than
  merely listing them.

Categorically, adding objects and projections cannot create the required
action. One needs a morphism or higher coherence law that relates the scalar
kernel to the refined observation diagram on the source-admissible subobject.

## Falsifier and scope

Any proposed linear static refinement claiming both extra faithfulness and
automatic darkening at scalar zeros is falsified by this factorization
theorem. The result does not exclude a transport-generated family evaluated
on a restricted solution space, because there the scalar-null implication may
follow from independent dynamics rather than from linear readout geometry.

This is a no-go theorem for presentation-only enlargement, not a proof of RH.
