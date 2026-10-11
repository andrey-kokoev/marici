# Four-edge cycle conversion into a retained state at the starting vertex

## Operator's proposed mechanism

Test the interpretation of back-reaction as conversion of the four-edge cycle A->D->B->C->A into the vertex A where it began. This replaces the earlier proposed arbitrary continuation-selector exercise. Here “quartic” means four traversals; no quartic energy or action is inferred.

## Existing constructors inspected

`RetainedTetrahedralPackage.Cells.build` completes a supplied tetrahedral horn and retains its original vertices. Its `vertex` operation projects one of those original values. The new module `agda/SeedCycleVertexConversion.agda` proves, for any carrier and any marked vertex, that vertex recovery after completion equals the corresponding input vertex. It does not implement a state-changing feedback law.

`RetainedRelationshipPromotion.Promote` can package supplied relationships as new vertices, but explicitly takes a promotion adapter, pairing and shared-endpoint rules. It does not silently identify such a newly promoted object with the original seed vertex A.

The free six-row seed must also be distinguished from a filled tetrahedral package. Its rows have five distinct undirected endpoint pairs (AB and BA share one pair); CD is absent as a primitive. Its four-edge cycle is not by itself six tetrahedral edges, four face witnesses and a tetrahedral filler. These could require further construction; none are inferred here.

## Concrete lossless conversion adapter

A new bookkeeping adapter `convert` packages a closed seed path at A as a marked state containing:

- the entire original six-row table and its agreement witness;
- the initial arrival value;
- the complete closed path;
- the computed active arrival and its computation witness.

For the four-edge path the active arrival is CA. Recovery of the original table, initial value and full cycle is proved. Thus the off-route complement is not discarded and the cycle is not collapsed to the empty history.

The package after conversion is provably different from the empty-history package before it, even if the initial arrival already equals CA. This is a genuine difference in retained state, not necessarily a change in its active arrival value.

This adapter uses existing paths, the table and the previously constructed arrival reader. It is newly constructed bookkeeping, not a previously discovered native physical conversion rule or a tetrahedral filling theorem.

## Does this implement back-reaction?

Not yet in the sense of changing the next active response. The existing arrival reader overwrites its active value with the next supplied arriving occurrence. After either next outward traversal AB or AD, its output is provably identical before and after conversion. These are exact checked negative controls, not claims about every possible history-sensitive update.

The cycle can therefore be retained **at A** without erasure, but the tested reader does not consume that retained cycle to alter the next response. If “back-reaction” names the conversion itself, the construction gives a precise information-retention version of that term. If it means a dynamical effect on A, a source-defined memory-sensitive update remains the missing operation. No force law, coupling or value of G follows from the packaging.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedCycleVertexConversion -Fresh

Passed with safe Cubical/guardedness options, ignored interfaces and stable inputs. Receipt: `results/agda-SeedCycleVertexConversion.json`. Finished 2026-10-05T20:15:19.5043411Z. Source SHA-256: `550a87181a258fc4deec1464c55614c59384e9888a14da9439cead1cd1cd1c2d`.

An initial indexed-pattern split error was resolved by generalizing the nonempty-path observer over both endpoints; the complete fresh check then passed. No postulates or unresolved holes were added. No ledger entry, commit or publication is claimed.
