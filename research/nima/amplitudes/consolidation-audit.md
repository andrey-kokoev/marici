# Amplitude consolidation: first bounded audit

## Question

Can one live numerical evaluator result be independently reconstructed and
connected to a formal calculation, without promoting agreement to a proof of
the physical rules or of the whole Python implementation?

Operator direction: following the ten-turn expansion, the operator approved
pausing breadth for convention/reference review, independent reproduction,
and one actual Agda calculation. This changes search priority, not evidence.

## Claim boundary

Obligation classification: **forward realization** of a fixed source fixture
into an arithmetic calculation. No higher route-coherence or readout-descent
claim is made. This is not yet an instance of the existing native-boundary
comparison framework.

The selected source is `scalar_tree_baseline.py`: massless real phi^4,
all-incoming momenta, metric (+---), vertex -i lambda, propagator i/q^2,
amputated i M, lambda=3/5. Two vertices and one internal propagator give
M6=-lambda^2 sum(1/q^2). These Feynman rules remain physical inputs.

Independent bitmask enumeration in `scalar_six_bridge.py` finds ten labelled
unordered channels and M6=6/25. It agrees with all six recursive roots and a
distinct scaled sample. Missing-channel, double-count and sign hostiles differ.
The Python paths share Fraction arithmetic; this is not arithmetic-backend
independence.

The exported `ScalarSixFixture.agda` contains live momenta, coupling and result.
`ScalarSixKernel.agda` independently constructs label pairs, momentum sums,
Minkowski squares and integer reciprocal checks. `ScalarSixCertificate.agda`
verifies nullness, conservation, the ten propagators, reciprocal
identities, and 144/600=6/25 by normalization, without postulates. Export and
source hashes are recorded in `results/scalar-six-bridge.json`.

## Disposition

- Python discovery: **138 tests passed**, structured execution
  `structured_command_execution:e_11220_1790223564831360200_14`.
- Formal calculation: **fresh compiler check passed**, with `--safe`,
  `--cubical`, `--guardedness` and `--ignore-interfaces`. Receipt:
  `research/nima/results/agda-ScalarSixCertificate.json`.
- Compiler negative controls both fail for the intended arithmetic mismatch:
  result 7/25 gives `3600 != 4200`; propagator square 9 gives `8 != 9`.
  Both exit with code 42, not a missing-file or scope error. Combined receipt:
  `research/nima/results/scalar-six-formal-audit.json`.
- Reproduction: `pwsh -NoProfile -File research/nima/checkers/check_scalar_six_bridge.ps1`.
  It checks the live export, freshly compiles the positive certificate and
  requires the specific compiler diagnostics from the two negative controls.
- Execution provenance: MCP invocation initially failed or returned an empty
  zero exit even for a nonexistent input, which was NOT counted as success.
  The operator explicitly directed shell execution of the ps1 runner instead.
  That route actually invoked Agda, exposed missing guardedness and product
  imports, and passed after their repair. The earlier PATHEXT-only repair had
  failed and was removed; no complete cause of the MCP discrepancy is claimed.
- External-reference audit remains **open**. Local PDF searches did not supply
  a checked amplitude-convention source. No remembered equation or citation is
  counted as verification. The gravity phase convention in particular still
  needs an explicit map to an inspected reference convention.

The exporter remains untrusted, and the checked certificate covers only one
fixed fixture. It does not prove arbitrary-kinematics correctness, Python
semantics, Feynman rules, or the foundational physics.
Nothing was committed or published by this consolidation pass.
