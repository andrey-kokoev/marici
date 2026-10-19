# Three-context PN comparison family

## Frozen alternative contract

Keep the original coarse metric-unitary S, independently sourced geometric
C3 actions U_P,U_N, full fields and phase references fixed. Replace neither
geometric action. Instead explicitly enlarge the comparison presentation by
a retained context g in Z/3 and define

    S_g = U_N^g S U_P^(-g).

This is a different task from one fixed equivariant S. The known obstruction
to that fixed-map task remains active. Context is an external comparison index,
not three physical planes, an inferred spatial dimension or a new native move.

## Exact tests

Freshly replay the coarse PN construction and geometric source identities.
Evaluate all three full36-by-36 matrices using independent source actions.
Check S_3=S_0, U_N S_g=S_(g+1) U_P and all9 group-action compositions, plus
pairwise distinctness. Metric unitarity and projector-role exchange follow
for each S_g from freshly verified source identities and the factor certificate
for S; do not claim dense inverse products were evaluated when this was the
actual proof.

Compare the averaged map Sbar=(S_0+S_1+S_2)/3 with each retained context.
On the full source alignment space, U_P is identity. The target C3 average
on im(L_N) is N_N. Consequently

    Sbar G_P = S N_P,    Sbar (G_P-N_P)=0.

Check these rectangular identities exactly. A nonzero unit relative-alignment
input is carried with unit norm in every context but annihilated by Sbar;
therefore averaging is not an invertible or metric-unitary replacement.
The alignment rank drops3 to1. No claim about the total rank of Sbar on all36
components follows from this restriction alone.

For a source-defined orthonormal two-column relative basis, compute the three
context outputs. Every pairwise difference has target weighted Gram3I2; the
three directed consecutive differences sum to zero. This distinguishes a
closed orbit of unequal comparisons from equality of comparisons.

Use the actual anchored PN prepare/recover API on the three context packets
for one explicit unit relative input. Recover full fields; preserve the context
index separately. Each output has unit norm, the three output fields average
to zero, but their output self-comparison blocks do NOT average to the zero
packet. Averaging amplitudes and averaging quadratic comparisons are different
operations. Do not apply coherent prepare to a mixed packet and call it a
physical mixture without a separate type.

## Scope and next obligation

This constructs an equivariant family of comparison presentations, not an
invariant single map, physical sewing, a unique reference or native dynamics.
A canonical choice of one context, or a task/readout that legitimately forgets
context, requires a separate source-supported descent test. The family is
built from a previously chosen coarse S; its complement-frame choice is not
made canonical by taking the orbit.

Replay: `python research/strominger/checkers/check_cyclic_PN_presentation_family.py`.
Receipt: `results/cyclic-PN-presentation-family/verification.json`.
