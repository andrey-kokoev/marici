# Exact selector-frontier matrix (WP59)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

Five gates define a genuine physical selector:

- **D**: descent on the original full weak-basis quotient;
- **P**: proper reduction of the admissible `physical16` family;
- **A**: independent source authorization of that reducing operation;
- **I**: typed physical implementation or instrument;
- **E**: survival on the complete fitted ensemble.

| Candidate | D | P | A | I | E | First failure |
|---|---:|---:|---:|---:|---:|---|
| physical readouts | yes | no | yes | yes | yes | P |
| generation-exchange deck probe | no | no | yes | no | yes | D |
| one-loop RG transport | yes | no | yes | no | yes | P |
| spectral conditional expectation | yes | yes | no | no | no | A |
| relational reference port | no | no | no | no | yes | D |
| discrete-CP chart vacua | no | no | no | no | yes | D |
| mixed Gram-word complement | yes | no | yes | yes | yes | P |
| positive commutator score | yes | no | yes | yes | yes | P |

No row passes all five gates. The matrix locates the first nonfaithful or
unauthorized arrow rather than merging distinct failure modes:

- readouts, invariant words, and scores separate but do not reduce;
- RG transports invertibly;
- deck and discrete-phase probes remain presentation data;
- a reference port changes the experiment;
- spectral pinching has a proper image, but the reducing channel is neither
  dynamically authorized nor instrumented and its locus fails experiment.

The sharp next target is therefore narrow: a source action or threshold
boundary law whose induced quotient map has a proper image, with normalization
frozen independently of the IR fit and a typed physical realization.

Verification:
`python research/flavor/checkers/wp59_selector_frontier_matrix.py`.
