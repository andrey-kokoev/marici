# Comparison, forgetting, and records are distinct structures

Fresh safe Cubical Agda --ignore-interfaces check passes for `agda/ObserverDirectionRecords.agda`; log: `results/agda-direction-records.log`.

## Checked distinctions

1. A path comparison of indices gives an equivalence between their fibres. Such a comparison does not privilege a temporal direction.
2. For observation maps f:X→A and g:X→B, define Factors(f,g) as a postprocessing map A→B together with a pointwise witness that its composite with f equals g. Identity and composition are checked. If two source states are equal under f, they remain equal under g.
3. The identity observation on Bool factors to the constant Unit observation, but not conversely. The proof rules out ANY reconstruction satisfying both true and false cases. Both observation codomains are inhabited: mere positivity does not determine discriminating power or reversibility.
4. Any observe:X→Y admits a logical lossless refinement Recorded = Σ(y:Y) Σ(x:X) (observe(x)=y). Encoding and recovery form a checked equivalence X≃Recorded, and forgetting the record reproduces observe exactly. In the Bool→Unit example, retained records are distinct while their visible projections agree.

The record retains the full source and a comparison witness. This is deliberately a conservative existence construction, NOT a claim of a minimal record, bounded storage, accessible hidden information, physical reversibility, or free erasure. No inverse to the lossy visible projection is manufactured.

## What follows and what does not

There is a genuine mathematical asymmetry of recoverability once a lossy observation map is specified. No such asymmetry follows merely from positive support. A path can be invertible while a projection of information is not; these are different mathematical objects, so it is misleading to identify every drawn arrow with a temporal instruction.

Factorization supplies an information preorder relative to a specified common source. It is not an antisymmetric order as stated, and it is NOT a clock, a entropy law, causal precedence, or a statement that any real observer retains the proposed record. An arbitrary family need not have a global section; this construction does not override the previous local/global obstruction.

## Next

Connect the information-factorization definition to the actual restriction maps of our observation model, not just arbitrary functions. Test whether smaller support loses recoverable data and why duplicating access can be information-neutral on restricted images even though the enlarged codomain admits incompatible extra sections. Use a local common observation space only where it is specified; do not assume a universal global assignment. Geometric measure and physical records remain separate obligations.
