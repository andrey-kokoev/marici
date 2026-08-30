# Optical probe grammar admissibility

The tetrahedral frame is the unconstrained four-pure-state optimum, but the
frozen dual-rail source grammar does not contain an arbitrary state
preparation operation.

The declared path constructor prepares one named input rail, applies a fixed
balanced splitter, and then permits a calibrated relative phase. At the
post-splitter target interface its reachable Bloch vectors therefore have
zero Z coordinate:

    (cos(phi), sin(phi), 0).

No choice of phase reaches a tetrahedral vertex because every tetrahedral
vertex has absolute Z coordinate equal to one over the square root of three.
More strongly, any number of probes at this fixed post-splitter interface has
a zero Z column in the coherent-residue syndrome. Its rank is at most three.
The frozen grammar cannot diagnose relative-rail-phase residue at all.

The first missing constructor is a calibrated preparation selector that
presents both the unsplit rail pole and the balanced-splitter output at the
same typed target interface. With that selector, the admissible state set is
the two rail poles together with the full equator.

Within that enlarged but still fixed-splitter grammar, the optimal four-probe
frame is one pole and three equatorial states separated by one third of a
turn. Its Gram spectrum is

    (5 - sqrt(13))/2, 3/2, 3/2, (5 + sqrt(13))/2

and its condition number is

    sqrt((5 + sqrt(13)) / (5 - sqrt(13))),

approximately 2.48421.

The classification is finite. Zero poles gives no Z sensitivity. Three or
four poles leaves too few equatorial directions. Two distinct poles must be
opposite and its optimized two-equator branch has condition approximately
2.87100. The one-pole branch is minimized when its three equatorial vectors
are centered and isotropic, hence separated by one third of a turn.

A variable-ratio splitter is the next constructor. It reaches arbitrary
latitudes and therefore realizes the tetrahedral optimum with condition
square root of three.

Thus the conditioning ladder is:

1. fixed post-splitter locus: rank at most three;
2. calibrated bypass/selector: faithful constrained optimum, condition 2.48421;
3. variable-ratio splitter: tetrahedral optimum, condition square root of three.

No selector, variable splitter, physical execution, or interaction-net
promotion is inferred from algebraic availability.
