# Explicit seed binding: center transfer is not the literal row swap

ramsey_center_transfer_seed_binding.py constructs the affine BRNN matching output directly, identifies it with catalogue191 by verified graph isomorphism, transports all five cooperative switches back into the actual seed output coordinates, and compares their result with the independently constructed row-swapped matching output.

Output coordinates: root0; ground-label vertices1..6 correspond to [12,13,14,23,24,34]; duad vertices7..21. These are NOT Hall cage vertex numbers0..29.

The unique fixed ground label of the intrinsic C5 is the selected affine hub14, represented by output vertex3. Under the catalogue isomorphism root0->0 and vertex3->1, forced by the unique center and the C5-fixed neighbor. The full cooperative operation therefore transfers the Hall center from root0 to the HUB NEIGHBOR3.

Literal row swap acts on output vertices by fixing root0 and permuting ground labels by (1,0,2,3,5,4), with induced action on duads. It also fixes hub vertex3. Its output has unique Hall center0. It removes five red edges and adds five. The transported five-switch operation has unique Hall center3; it removes ten red edges and adds ten. These are different labeled transformations, with invariantly different behavior of the distinguished center. A common relabeling cannot erase this distinction while preserving the root mark.

Moreover, literal boundary marks do not retain their original incidence roles after the center transfer. Original entry flag (0,16) is output selected duad7 in partition triple [7,17,20]; exit flag (7,29) is selected duad14 in triple [11,14,16]. The new center3 has neighborhood [0,8,12,16,17,18]. Thus entry triple vertex17 and exit triple vertex16 become new ground-label vertices, not duad vertices. Neither marked triple remains a partition into duads in the new presentation. This is an explicit type change, not just a numeric mismatch.

Conclusion: the cooperative full-orbit operation is a change of incidence presentation centered at the old hub neighbor. It is NOT the original BRNN row flip. Comparing it to an incidence duality would require an explicit retyping and transport of boundary flags; preserving all literal old marks is impossible. No identification with the earlier endpoint-exchanging cage maps follows merely from involutivity or shared C5 symmetry.

The verified vertex map, five transported switches, edge-change counts and boundary-mark checks are in the companion JSON. Next conceptual task, if pursuing a unified duality: define an object with BOTH a graph and a chosen center, and separate row action (center-preserving between matching outputs) from cooperative transfer (changes center and incidence roles). Do not treat the graph alone as recording the comparison frame.
