# v107: principal road-Cech support reduction

The physical-principal-Cech packet reduces the remaining principal-wall diagram
by support. D2 and D3 are disjoint from the physical closure, as are all three
pairwise incidence supports Z12, Z13, and Z23. Their literal chain maps vanish;
the D1 corner maps vanish as well.

`rzk/135-principal-road-cech-support-reduction.rzk.md` records that the sole
remaining principal road-Cech arrow is the D1 soft nearby-cycle
specialization. The source packet does not supply its analytic continuation.
Thus the road-Cech completion problem is now localized to one map rather than a
full three-wall diagram.

A fresh Symbolica executable replay was attempted, both through Cargo and the
existing debug binary, but the runtime aborted with stack overflow. The packet
is therefore retained as supplied evidence with this replay limitation
explicit. The Rzk summary passes all eight declarations with no assumptions.
