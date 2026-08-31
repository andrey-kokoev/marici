# The current Rees census cannot extract labelled generators

The physical half-twist census reports eight length-one invariant factors. Its
sparse backend returns relation ranks, from which the checker derives cokernel
dimensions and elementary-length multiplicities.

The interface serializes none of the data required for generator extraction:

- row or column basis transformations;
- labelled kernel or cokernel vectors;
- source descriptors for length-one representatives;
- replayable cross-prime generator matching.

Consequently the eight factors are multiplicities, not eight source objects.
They cannot be assigned connecting images or compared with \(\tau_p\) from the
current receipts.

Extraction requires a provenance-preserving exact or modular presentation
backend that returns labelled basis transformations, exact replay, and
cross-prime matching. Until that capability exists, the generator-extraction
leaf is interface-blocked rather than falsified.
