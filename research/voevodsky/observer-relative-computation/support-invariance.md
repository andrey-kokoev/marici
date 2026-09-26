# Equivalent presentations versus duplicated access

Fresh safe Cubical Agda --ignore-interfaces check passes for agda/ObserverSupportInvariance.agda; output retained in results/agda-support-invariance.log.

For probes p:O→X and q:Q→X, an equivalence e:O≃Q plus actual comparisons h(o):p(o)=q(e(o)) induces equivalences of BOTH witnessed participation (dependent sums) and coherent observation (dependent products). An impossibility of observation transfers across this equivalence. We use the Cubical library's checked dependent sum/product equivalence constructions; the support equivalence alone does not specify how to compare fibres.

This is invariance of existence and retained structure, NOT equality of every witness under transport. A nontrivial h may permute observable values even when the support and access endpoints are unchanged. Nor does a homotopy equivalence of supports preserve a geometric area that has never been specified.

A checked counterexample distinguishes redundant presentation from independent access duplication. Restriction from one point to two disconnected accesses yields identical Bool values at both. The duplicated probe nevertheless admits (true,false), which cannot descend from a single-point observation. Supplying an agreement witness restores descent, and restricting the descended observation recovers the original two-point data.

Thus counting access positions is not automatically a measure of information or observer area. Multiplicity without compatibility changes the observation problem; redundancy with compatibility is a different construction. These statements are direction-free.

The current branch is complete for probe equivalence and the finite duplication/descent test. Next pursue the already open higher-overlap-coherence branch: for three observations, pairwise agreement witnesses themselves must be compared, rather than merely requiring pairwise inhabitation. This tests how the compatibility structure scales without installing a temporal order.
