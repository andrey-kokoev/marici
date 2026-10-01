# Flat reference attachment and its holonomy gate

## Obligation and declared inputs

This addresses attachment transport and route compatibility before physical
readout. Keep the fixture's fixed invertible reference d4:A->B, r4=d4^-1,
the actual137 comparison matrices, and the two candidate endpoint policies.
Declare a port space V_v and an invertible frame P_v:A->V_v at each port.
These frames are coordinate identifications, not physical quantities derived
from the record count. This is a globally trivialized reference construction.

## Transport the one reference, rather than fit many references

For a record a:s->t with original matrix C_a:A->B, define

    a_tilde = P_t r4 C_a P_s^-1,
    d_a     = P_t P_s^-1,
    r_a     = P_s P_t^-1.

The decoding map on Hom(V_s,V_t) is

    decode(M) = d4 P_t^-1 M P_s.

It recovers C_a from a_tilde and the same fixed d4 from every d_a. Thus the
per-record references are copies of one specified reference under declared
transport; they are not independently fitted matrices. Both inverse equations
hold exactly in this invertible stratum.

For two records with a common target, the typed operation b_tilde r_b a_tilde
retains a's source. Its decoded value is exactly C_b r4 C_a. This realizes the
previous reference-return lift without changing the comparison response.

## Promotion with possibly different target ports

Normalize a member at its own target as the endomorphism a_tilde r_a. To promote
into a family target t_F, transport it by

    K_(t_F,t_a)=P_(t_F) P_(t_a)^-1.

Average the conjugated endomorphisms using retained member masses. Multiplying
that mean by d_F=P_(t_F)P_(s_F)^-1 gives the promoted comparison map. Its decoded
value is precisely the previously specified weighted mean C_F.

The checker carries this construction through both promotion rounds for both
endpoint candidates. It supplies typed transports between unlike target ports;
it does not silently add matrices living at different ports.

## Coordinate changes cannot tune the answer

For arbitrary invertible G_v, replace P_v by G_v P_v. Actual and reference maps
transform as G_t M G_s^-1, with the corresponding inverse transformation on
returns. Decoding yields the same original matrices. Promotion commutes with
this transformation as well.

Thus these port-frame choices cannot erase the previously measured difference
between the inherited-target and common-target generators. They supply a
coordinate-covariant realization, not a normalization knob or a physical gauge
group identification.

## The actual limitation is reference holonomy

Frame-generated reference maps telescope around every loop to the identity.
Local invertibility alone does not imply this. The checker uses an existing
two-edge cycle in the carrier, from ('a',0,0) to ('a',2,2) and back. Inserting a
nonidentity invertible shear H in one reference map preserves its local inverse
but makes the loop transport P_s H P_s^-1 nonidentity.

No passive frame change turns that loop into the identity: it only conjugates
its holonomy. Such reference data therefore cannot be represented by the above
single path-independent assignment of frames. One must either establish trivial
reference holonomy from the source or retain path-indexed transport/holonomy.
Flatness here concerns the reference attachments, not the actual comparison
matrices or their mixed rectangle responses.

## Result and scope

A complete flat attachment candidate now connects the fixed rung4 reference,
record ports, common-target composition, and promoted-family readouts. It is
coordinate-covariant and preserves all the checked matrix responses. The
reference value and global flatness are inputs; the intended endpoint generator
and physical metric remain unselected. No weak-return or nontrivial-bundle
extension is asserted.

## Verification

    python research/nima/checkers/check_flat_reference_attachment.py
    python research/aspect/scc/scc.py check nima-flat-reference-attachment

Exact rational tests cover local units, all retained and promoted values,
common-target pair composition, two promotion rounds, independent port-frame
changes, and an invertible but nonflat reference-loop control. Machine result:
`research/nima/results/flat-reference-attachment.json`.
