# Anchoring the five marking transports

The ambiguity is exactly a cyclic reflection parameter, not five unrelated maps. In the actual affine output coordinates, the selected-duad orbit is
[7,20,14,11,19].
Assign coordinates0..4 in that order. The original entry selected-duad vertex7 has coordinate0, exit selected-duad vertex14 has coordinate2. Each of the five marking transports K acts on this orbit as t -> c-t, and every c in F5 occurs exactly once. This is independently verified in ramsey_mark_transport_anchor.py/JSON.

Three distinct operational conventions each select a unique transport:
- keep selected entry vertex fixed: c=0;
- keep selected exit vertex fixed: c=4;
- exchange selected entry and exit vertices: c=2.
No transport fixes both selected boundary vertices. In general, exchanging distinct orbit marks a,b requires c=a+b; fixing a requires c=2a. These descriptions do not depend on choosing an orientation or origin for the cyclic coordinates. However choosing which convention to require IS additional operational information.

The reciprocal selected-duad-exchange convention picks phase4 in the stored transport list. It carries the original entry selected vertex7 and partition[7,17,20] to selected14 and NEW partition[2,14,20]. It carries the original exit selected14 and partition[11,14,16] to selected7 and NEW partition[1,7,19]. These are valid flags in the new-center presentation by the verified graph isomorphism. They are not the literal old opposite flags: the old partition triples do not preserve their types under center change.

Thus one can define a deterministic marked-center transfer by specifying the unordered pair of selected boundary duads and requiring them to exchange. This removes the phase ambiguity and is reversible, since K is an involution. On the row-related state the coherent convention is transported by K_R=RKR, which exchanges the row images of the same marked pair. This is a well-defined added operational rule, not a deduction that the original BRNN strings mandated it.

The broader lesson is to distinguish: (i) canonical unmarked graph update T; (ii) equivariant fivefold torsor of marking transports; (iii) a marking/reciprocity convention selecting one element. Pinning a single selected duad is enough to select a reflection, but entry pinning, exit pinning and reciprocal exchange are different choices. A full old flag cannot simply be held fixed as a typed object, because its partition contains a vertex that becomes a new label.
