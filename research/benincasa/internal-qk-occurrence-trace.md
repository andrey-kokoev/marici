# Internal (q/k) occurrence trace

## Frozen source pair

The middle statistical placement of Entry 1590 varies one of the two internal
propagators in the cubic self-energy:

\[
\delta G_q\,G_k
\qquad\text{or}\qquad
G_q\,\delta G_k,
\qquad
k=|p-q|.
\]

The source vertex

\[
(p^2+q^2+k^2)^2
\]

and the product of internal Wightman functions are symmetric under exchange
of the two internal labels.

## Source change of variables

On vector loop momentum, use

\[
\vec q\longmapsto\vec p-\vec q.
\]

This exchanges (qleftrightarrow k) and is an involution.  Its linear part
is (-I_3), so

\[
\det(-I_3)=-1,
\qquad
|\det(-I_3)|=1.
\]

The source loop integral uses the Lebesgue density (d^3q), hence the
substitution carries no minus sign.  The two labelled terms are equal for the
full momentum domain, or for a regulator/profile transported with the two
mode labels.

A cutoff imposed only on a fixed (q)-centred ball is not invariant under
this substitution and is not admissible evidence for the trace identity.

## Result

For a homogeneous isotropic state profile, the internal occurrence trace is

\[
\boxed{
\int d^3q\,
(\delta G_qG_k+G_q\delta G_k)
=2\int d^3q\,\delta G_qG_k,
}
\]

with all common source factors retained.

The factor (2) is an occurrence-orbit trace.  It is not a new coupling or
an adjustable symmetry factor.

## Next finite falsifier

Apply the endpoint-primitive recurrence to one representative
(delta G_qG_k), multiply by the derived trace coefficient (2), and audit
the nondecaying hard grades.  Repeat with a transported Hadamard profile to
ensure the regulator commutes with the involution.

