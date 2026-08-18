# Entry 499 — The Endpoint Mapping Cone Repairs Invariant Flatness

Entry 498 proposed inserting local lift columns into the finite presentation.
That has the wrong variance.  Entry 473's invariant defect is

\[
\delta_+(D)=2\dim C_{D,+}-\dim C^{(1)}_{D,+}=1.
\]

Thus the ordinary first-order cokernel is one dimension too small.  Adding
an exact-image column could only shrink it further.  The endpoint Čech class
must enter in the derived target degree of the mapping cone.

For every stable cutoff \(D=16,20,24,28\), Entry 473 gives

\[
\dim C_{D,+}=2D+1,
\qquad
\dim C^{(1)}_{D,+}=4D+1.
\]

The single deck-invariant endpoint conormal degree of Entry 497 changes the
derived first-order dimension to

\[
\dim C^{(1),\mathrm{der}}_{D,+}=4D+2.
\]

Consequently

\[
\boxed{
2(2D+1)-(4D+2)=0
}
\]

at every tested cutoff.  The mapping-cone correction restores exact
first-order flatness in the invariant character.

## Interpretation

This identifies the categorical location of Entry 473's constant defect:
it is the missing derived endpoint target degree.  It is not another exact
relation and not an ordinary torsion source class.  The sequence of Entries
491--498 constructs its coefficient object and shows why the ordinary
polynomial presentation omits it.

The statement is stronger than a bare rank match because the added degree is
already fixed independently by:

1. the principal conormal module;
2. the derived \(u\)-Bockstein;
3. derived endpoint base change;
4. deck-equivariant conormal orientation.

What remains unproved is the chain-level normalization of the comparison
with the complete filtered matrix.  Flatness alone cannot certify that map.

## Next gate

Build the explicit total differential containing the ordinary orbit matrix,
the two local lift maps, and their overlap boundary.  Verify \(d^2=0\) and
that deleting its single Čech target row recovers exactly the Entry 473
matrix.  This will turn the structural identification into a chain-level
one.

The cutoff audit is
`research/voevodsky/check_soft_axis_derived_plus_flatness.py`.
