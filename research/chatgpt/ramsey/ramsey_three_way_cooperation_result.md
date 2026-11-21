# Genuine three-way cooperation resolves the phase-frustrated branch

ramsey_three_way_cooperation.py exhausts triples of vertex-disjoint individually invalid triangle-free two-edge switches over all ten regular catalogue representatives. 46,720 triples tested; 18 valid joint triples, of which13 have EVERY nonempty proper subset invalid. Every certified subset remains triangle-free; invalidity is an independent seven. Five irreducible triples start at Hall type191 and end at no-center type186. Type190 has none. Other irreducible counts: 182->182 two;183->186 one;185->186 one;186->191 two,->183 one,->185 one. No general connectivity claim follows.

Concrete source191 triple (catalogue vertices zero-based):
A removes (2,13),(12,16); adds (2,16),(12,13).
B removes (3,18),(10,19); adds (3,10),(18,19).
C removes (5,21),(9,17); adds (5,9),(17,21).
The three supports are pairwise disjoint. Root0 and its neighbor set are unchanged. Independent-seven counts: A=6, B=2, C=2, AB=6, AC=1, BC=3, ABC=0. All seven outputs were checked triangle-free; the final output has a verified isomorphism to type186.

This is directly related to the previously found phase frustration, not an unrelated example. Under the independently recovered generator and orbit numbering of ramsey_repair_orbit_obstruction.py, A is orbit12 phase0, B orbit13 phase1, C orbit13 phase2. The individual full-repair arcs (defect owner -> repairer) are only B->A and A->C. Neither A nor B individually repairs all C defects, but their combined added edges do (necessarily, since ABC is valid). Thus the final repair obligation is genuinely collective: C->{A,B}. It cannot be represented by pairwise full-repair edges alone.

Interpretation: nonzero phase drift obstructs two-way closure, but does NOT prevent higher-order cooperative repair. One six-defect switch and two differently phased two-defect switches close a valid triple. This confirms the original conjecture of irreducible three-way cooperation and shows why a hypergraph of repair obligations is needed. Pairwise repair results remain valid in their stated scope; do not generalize them into pairwise sufficiency for describing every valid composite operation.

Evidence: companion JSON stores one explicit example per source/target, all seven subset counts and obstruction witnesses, and final isomorphisms. The shared switches() helper now skips individually valid moves (rather than asserting none exist), allowing this test on non-Hall types; behavior on Hall types is unchanged.
