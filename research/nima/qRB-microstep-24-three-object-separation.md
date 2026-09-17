# qRB microstep 24: separate the three comparison objects

The source audit confirms the same discipline needed here: do not conflate

1. the absolute carrier/feature geometry;
2. the relative wall or boundary extension;
3. the transported physical readout.

The missing datum is an explicit interface from the relative boundary object to the absolute source carrier. In qRB terms this is the `B`-interface, not another `R`-identity.

A valid interface must preserve source labels, regulator typing, orientation, and the signed readout. Until it is supplied, the affine observer residual remains a typed lax boundary term rather than a positive bulk contribution.

Status: object separation closed; the relative-to-absolute boundary interface is the next substantive gate.
