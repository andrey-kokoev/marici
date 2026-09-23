# The unbounded-query obstruction survives perfect filling coherence

## The stubborn question

Can the source-filling perspective remove the obstruction to a fixed finite representation supporting every future feasibility query? Test the existing owning zero-frame family, not an invented source.

Here a filling is an admitted refinement set J on H queried even coordinates. Each J defines a retained possibility carrier, rather than a unique microscopic tail measure. The owning spike/Farkas certificates determine the answer to each query exactly. The source history, current certificate and optimum are fixed across all fillings.

## Boundary-conditioned pencils

A partial query boundary specifies membership on k of the H coordinates. Its pencil has exactly 2^(H-k) admitted refinement fillings. Compatible partial boundaries glue by intersection of these pencils. Contradictory answers give an empty pencil.

For the owning H=10 family, the exhaustive construction yields:

- 1,024 admitted refinement fillings;
- 59,049 partial boundaries;
- 1,048,576 boundary/filling incidences;
- 1,180,980 one-query gluing checks;
- 393,660 contradictory extensions correctly rejected.

Every consistent boundary has a filling. All compositional refinements preserve the same witness set; there is no witness-switching or missing higher-arity constraint in this restricted cube family.

## The remaining obstruction

The fixed current numerical certificate has all 1,024 refinements in its fiber. Full query boundaries distinguish them individually. A different membership bit supplies a source-certified separating query. For arbitrary H, this gives 2^H distinctions and a lower bound of H retained bits.

Thus the strongest representation obstruction persists even with complete gluing coherence. It is a size obstruction of the query-distinguishable filling family, not an obstruction to existence or composition of fillings.

A compact formula can specify the whole Boolean family. It does not encode which member describes the retained evidence in a particular run. Leaving that member unknown supports set-valued answers; exact answers for the actual retained carrier require its distinctions to remain available. Boundary reorientation does not remove the separating queries when the entire declared language is transported with it.

## Structural synthesis

The filling perspective separates three failures:

1. empty fibers: no source realization;
2. incompatible sequential witness choices: no coherent path;
3. too many distinguishable admitted fillings: no representation within the fixed budget.

The present family has exact admission and composition, but exhibits the third failure for unbounded query horizons. This clarifies rather than dissolves the limitation. A general synthesis contract must admit either a growing presentation, restricted query scope, weaker answers, or a checked storage obstruction.

## Reproduction

    python research/voevodsky/checkers/check_query_budget_filling_space.py

Artifacts:

- `results/query-budget-filling-space-contract.json`
- `results/query-budget-filling-space.json`

The independent owning storage-obstruction verifier is freshly replayed before this construction. Finite checks corroborate the implementation; the arbitrary-H lower bound follows from the source-certified membership-query argument.
