# Entry 498 — The Endpoint Conormal Jet Has Only Local Orbit Lifts

Entry 497 proposed projecting the derived endpoint jet backward into the
complete filtered orbit cokernel.  That operation is not defined: the
carrier-reduction morphism runs from the orbit presentation to the Koszul
target, not conversely.  The correct question is whether the target jet has
a global lift through that morphism.

For a \(q\)-generator, Entry 487 gives

\[
H_q=-{3\over2}m e_a,
\qquad
m=fL_1^{e_a}L_2^{e_b}.
\]

Every sector used by the complete orbit calculation has
\(e_a,e_b\ge1\).  At \(u=0\), the smallest plus-chart coefficient is

\[
m=f(b+1)a.
\]

To lift the endpoint jet \(-a^2e_a/8\), one must take

\[
f_-={a\over12(b+1)}.
\]

This is regular away from \(b=-1\), but is not a global polynomial source
coefficient.  The deck-conjugate chart similarly gives

\[
f_+={a\over12(1-b)},
\]

regular away from \(b=+1\).  Both map to the same target jet.  On their
overlap,

\[
f_--f_+=-{ab\over6(1-b^2)}.
\]

Thus

\[
\boxed{
-a^2e_a/8\text{ has local orbit lifts but no global polynomial lift.}
}
\]

## Consequence

The derived endpoint line cannot be identified with Entry 473's plus defect
by choosing an ordinary global representative.  Its natural source avatar
is the Čech obstruction to gluing the two endpoint-chart lifts.  The pole is
exactly along the divisor \(1-b^2=0\) whose conormal orientation produced
the invariant class in Entry 497.

This also explains why the generic ordinary even cokernel is flat in Entry
491 while the global filtered presentation has one defect: localization
solves the lift on either chart, but polynomial descent fails by one
endpoint-supported class.

The rank and character match with Entry 473 is now strengthened to a common
descent obstruction, but literal equality still requires evaluating the
Čech boundary in the finite filtered presentation.

## Next gate

Adjoin the two local coefficient columns to the Entry 473 matrix separately,
then compute the rank of their overlap difference after clearing
\(1-b^2\).  Test whether it kills exactly the unique plus defect at every
stable cutoff.  This is a forward source-to-target comparison and requires
no noncanonical inverse carrier map.

The local lift and overlap identities are checked by
`research/voevodsky/check_soft_axis_endpoint_jet_local_lift.py`.
