# The Finite Sextics Form Eight Free Cyclic Occurrence Orbits

## Convention

Use the active cycle

\[
\sigma:
(X_1,X_2,X_3;P_1,P_2,P_3)
\longmapsto
(X_2,X_3,X_1;P_2,P_3,P_1)
\]

together with

\[
(a,b,c)\longmapsto(b,c,a).
\]

It sends

\[
\mathcal G_{12}\to\mathcal G_{23}\to\mathcal G_{31}\to\mathcal G_{12}
\]

and

\[
\mathfrak g_1\to\mathfrak g_2\to\mathfrak g_3\to\mathfrak g_1.
\]

This \(\sigma\) is the inverse of the \(\rho\) convention used in the earlier
three-chart packets,
\(\rho:(X_1,X_2,X_3)\mapsto(X_3,X_1,X_2)\).

## Exact orbit census

Transport each of Entry 802's eight \(\mathcal G_{12}\)-chart sextics by
simultaneous substitution of the external kinematics and its source labels.
Every labelled occurrence returns after exactly three steps.  Hence

\[
\boxed{
8\text{ free }C_3\text{ occurrence orbits}
=24\text{ labelled finite collision occurrences}.
}
\]

Every occurrence stabilizer is trivial.  No additional scalar transition
unit appears in the eliminated collision polynomial:

\[
\sigma^3(F_S)=F_S.
\]

This scalar statement deliberately does not determine the orientation sign
of a residue form or Gysin map; that remains Benincasa's geometric datum.

## Invariant scalar exception

Seven sextic representatives have scalar polynomial orbit size three.  The
representative from

\[
(\mathcal G_{23},\mathcal G_{31})
\quad\text{inside the }\mathcal G_{12}\text{ residue chart}
\]

produces a cyclically invariant external sextic.  Its **polynomial** stabilizer
has order three, while its **labelled occurrence** stabilizer remains trivial
because the residue chart and source labels still cycle.

Thus

\[
\boxed{
\text{scalar invariance}\neq\text{occurrence invariance}.
}
\]

This is precisely why the Gysin naturality test must retain chart and label
typing even when the external discriminant polynomial is unchanged.

## Correction to Entry 802's certificate

The orbit reconstruction exposed a substitution defect in the first Entry
802 artifact.  A single dictionary substitution could leave \(E\) inside the
marked-point replacements while the polynomial ring omitted \(E\).  The
factorizer then treated it as a coefficient.

The repaired procedure substitutes \((a,b)\) first and then imposes

\[
E=X_1+X_2+X_3.
\]

All eight resultants remain irreducible sextics.  Their corrected term counts
are

\[
54,\ 50,\ 40,\ 50,\ 40,\ 40,\ 40,\ 37.
\]

The JSON hashes and Entry 802 text have been repaired accordingly.

## Handoff to the geometric test

For each of the eight representatives, Benincasa need only construct one
local Kato/Gysin or vanishing-cycle map.  The remaining two occurrences are
then forced by \(\sigma\), provided the squares commute with the residue-chart
orientation and transition units.  The invariant scalar sextic is the
sharpest test: its polynomial is fixed, but its occurrence-labelled Gysin
object must still execute a nontrivial three-cycle.

## Verification

- repaired finite census:
  `research/nima/audit_generic_finite_marked_cm_collisions.py`;
- cyclic checker:
  `research/nima/audit_generic_finite_collision_cyclic_orbits.py`;
- orbit packet:
  `research/nima/generic-finite-collision-cyclic-orbits.json`.

Allocator claim: `seqclaim-7de3a2de708032a94e173905`.
