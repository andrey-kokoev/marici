# 2918 — The Bridge Face Has a Free First-Rees Carrier Lift

## Facet-containment audit

Entry 2913 identified the codimension-two bridge face.  Test every one of
Entry 2911's sixty-nine facets for containment of its thirteen source
vertices.

Exactly two facets contain the face:

\[
q_L=0,
\qquad
q_R=0.
\]

Their normal rows are independent and their normal Jacobian is one.  Thus the
bridge face is a genuine simple normal crossing, not a higher-concurrence or
hidden excess locus.

## Local canonical form

In the two normal coordinates, the canonical form has the source-normalized
expansion

\[
\Omega_G
=
\frac{dq_L}{q_L}\wedge\frac{dq_R}{q_R}
\wedge
\left(
\Omega_F+q_LA_L+q_RA_R+\cdots
\right).
\]

The leading coefficient \(\Omega_F\) is the join form of Entry 2913.  Since
the full canonical form exists, this leading residue has an actual lift off
the associated grade.

## Result

At Carrier level, the first-Rees module of the bridge face is a free rank-one
line over the two normal variables.  The mixed class of Entries 2914 and 2916
is therefore not killed by carrier normal torsion.

This result does not yet determine the moving-fiber coefficient lift.  Any
torsion or mixing with bulk elliptic periods must enter during coefficient
pushforward, not from the bridge incidence geometry.

## Next finite calculation

Derive the first \(q_L,q_R\) normal jets of the moving-fiber period map from
the localized twenty-one-variable contour.  Project those jets to the tensor
basis

\[
(1,F_L,F_R,F_LF_R)
\]

and the complementary bulk coefficient block.  Test whether the mixed column
is horizontal, torsion, or off-diagonally coupled.

## Durable artifacts

- `research/benincasa/check_bridge_face_first_rees_lift.py`
- `research/benincasa/bridge-face-first-rees-lift.json`
