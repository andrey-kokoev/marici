# Why the other switch orbits fail: absence of repair and phase drift

ramsey_repair_orbit_obstruction.py computes the DIRECTED repair relation before any combined-validity test. Write S -> T when T is vertex-disjoint from S and its added edges hit every independent seven created by S. This does NOT mean T is itself valid or that S+T has no joint-only obstructions.

Type190: fourteen of sixteen switch orbits have no repairer at all. The other two (indices7,10 in the deterministic script ordering) can only be repaired by orbit11, which itself has no repairer. Thus there is no reciprocal pair.

Type191: twelve of sixteen orbits have no repairer. The remaining orbit-level directed edges, with multiplicities per source switch, are:
6 -> 5(1),2(1),14(2),9(1),15(1)
12 -> 13(1)
13 -> 6(1),12(1),10(1)
14 -> 6(1).
Only orbit pairs {6,14} and {12,13} can possibly be reciprocal at orbit level. The first gives the five successful aligned pairs already studied.

The second is an instructive FALSE POSITIVE of quotienting away phase. Follow the unique repairer from a switch in orbit12 to orbit13, then the unique repairer back into orbit12. It returns at phase +1, not the starting switch. The C5 generator was independently recovered as a root-preserving graph automorphism. Equivariance then makes this a directed ten-cycle of repair obligations, not five reciprocal pairs. Reversing the generator changes sign, but nonzero drift is invariant.

Thus the complete finite exclusion mechanism is:
- no repairer for most orbits;
- repairers with no return for others;
- apparent two-way repair between two orbit families frustrated by nonzero cyclic return phase;
- one aligned orbit pair with actual reciprocal repairs.

This explains why a purely family-level repair graph overpredicts cooperation: the state must retain phase. It is a finite structural certificate based on explicitly computed obstruction families, not a general theorem that reciprocal repair suffices in arbitrary graphs. The aligned pair's joint validity remains separately checked. The directed ten-cycle is NOT automatically a valid ten-switch operation: adjacent support disjointness does not imply all ten supports are pairwise disjoint or that simultaneous updates are well defined.

Do not identify this repair-return phase with literal row swap, cage-path reversal, or earlier C5 transport merely because the group order agrees. It is a newly defined relation on candidate local edge switches.
