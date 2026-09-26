# Restriction versus repetition: a checked information comparison

Fresh safe Cubical Agda --ignore-interfaces check passed for `agda/ObserverRestrictionInformation.agda`; log: `results/agda-restriction-information.log`. It imports the actual earlier observation restriction operator, rather than merely repeating an analogous definition.

## Established

For any specified local probe, take its section type as Source. Full observation factors to any restriction; nested restriction factors through the intermediate restriction. These are maps on possible sections and do NOT assert that this Source is inhabited, or that an arbitrary ambient family has a global section.

Two concrete inhabited cases distinguish changes in support:

1. Source = Bool→Bool, representing two independent Bool accesses. Restricting to the true-labelled access loses the false-labelled value. Two source observations collide, and Agda rejects any reconstruction satisfying all source observations.
2. Source = Unit→Bool. Restricting along Bool→Unit duplicates the single access. Both maps factor through one another on this source, so duplication neither adds nor loses recoverable source information. Nevertheless the output type Bool→Bool admits disagreement that no duplicated source ever produces. Information-equivalent observation maps need not have equivalent complete output types.

Neither conclusion assigns geometric area to support cardinality or temporal direction to factorization.

## A boundary discovered in the definition

The Factors relation requires postprocessing on the ENTIRE declared output type. With an empty Source, an observation into Unit and another into Empty preserve every source collision vacuously. Yet no total factor exists, because Unit→Empty is impossible. Thus collision preservation cannot be substituted for total factorization, and unachievable outputs can affect the comparison.

This is an explicit degenerate counterexample, not a claim that every inhabited observer has this problem. It matters because local/global obstructions can make a purported common section space empty. Positivity must not be silently presumed in an argument about all probes.

## Next: actual admissible outputs

Investigate observation images, keeping two constructions distinct:

- proof-relevant fibres retaining the source witness (the preceding Recorded construction); these can restore the very information the observer forgot;
- mere admissibility of an output, which hides the source witness while retaining the output itself.

Test the distinction on strict forgetting and the unused-output counterexample before treating image-level comparison as a better foundational information notion. Membership truncation would be an explicit observer operation, NOT a silent quotient of the underlying witness-bearing structure. General higher descent remains a separate obligation.
