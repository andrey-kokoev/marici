# Immediate incidence does not determine viable switch templates

ramsey_local_switch_incidence_profiles.py compares all16 cyclic switch representatives in Hall191. The marked core consists of the four support vertices plus center0 and hub1 (deduplicated). Isomorphisms must preserve center/hub individually and distinguish removed from added edges.

Three increasingly strong profiles were tested:
1. Full induced adjacency on the marked core, including removed/added edge marks.
2. Additionally every pairwise common-neighbor count among core vertices.
3. Additionally the ENTIRE multiset of outside vertices' neighborhood signatures into the core. This records every edge from the outside into the core, up to permutation of externally indistinguishable vertices, but omits edges between outside vertices.

Even profile3 fails to distinguish viability. Mixed classes remain:
- orbit2 unextendable versus orbit5 extendable;
- orbit10 unextendable versus orbit12 extendable.
Thus local support geometry, all pairwise overlap counts, and even full external-to-core incidence do not suffice. The missing information is in the way external vertices are connected to one another (or equivalent global frame/repair data).

The second pair is especially sharp: SAME four physical support vertices and SAME added edges.
Unextendable orbit10: remove(2,12),(13,16); add(2,16),(12,13).
Extendable orbit12: remove(2,13),(12,16); add(2,16),(12,13).
The original support forms a red four-cycle. The two operations remove its two alternative opposite-edge pairs, adding the same missing pair. A symmetry of the marked local diagram, extendable to its outside incidence signatures, exchanges these choices. Nevertheless only the second can participate in any valid coalition in our candidate system.

The other collision is between root-involving switches:
orbit2 removes(0,2),(3,18), adds(0,18),(2,3);
orbit5 removes(0,2),(6,17), adds(0,17),(2,6).
Again their marked local diagrams and full external incidence signatures agree, but their extendability differs.

This is a precise obstruction to a proposed locality principle, not a proof that all useful structural criteria must enumerate global independent sets. A criterion involving the external wiring or its cyclic transport can still distinguish the cases. Likewise a fully marked C5 action contains more information than the static profiles tested here; the comparison does not discard that possibility.

The viable-template classifications come from the previously certified rule systems, not from fitting these profiles. The JSON retains every representative and profile-equivalence class. No completed coalition lookup was used to compute the incidence profiles themselves.
