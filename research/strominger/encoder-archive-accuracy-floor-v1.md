# The fixed floating archive cannot be an arbitrary-accuracy isometry target

## Question and falsified candidate

The operator requested falsification of the proposed terminating, optimized,
WG-composable encoder compiler. Test a concrete candidate prerequisite: use the
existing saved floating matrices as the literal target at every requested
accuracy, while compiling into exact metric-unitary control operations.

That candidate is false on the full archived encoder and ready embedding.
It is not a refutation of compilation toward the exact polar operator, nor of
the bright-sector-only specification. No optimizer or baseline-search algorithm
has yet been implemented or tested by this packet.

## Exact hostile

`checkers/check_encoder_archive_accuracy_floor.py` reads the saved NPY arrays
inside `neutron-comparison-memory.npz`, validates the archive against its receipt,
and treats each binary64 entry as its exact rational value. It uses only the
Python standard library, avoiding a floating recomputation of the defect.

For column j=2 (zero-based), let q be its exact squared Euclidean norm in the
archived whitened chart. It is not one. For any exact isometry V,

    ||A-V|| >= ||(A-V)e_j|| >= |sqrt(q)-1|
             = |q-1|/(sqrt(q)+1) > |q-1|/3,

where the checker verifies 0<q<4. This applies to the 45-by-45 archived encoder
and the 45-by-24 ready embedding, which share that column. The exact rational
lower bound is stored in the receipt; its decimal display is

    3.821116889741225e-16.

Therefore an error target of 1e-18 relative to these literal full matrices is
impossible for any exact isometry, regardless of control-word length. This is
a certified lower bound, not an optimal distance estimate.

An identity-matrix control has zero floor. A diagonal entry 1+1e-20 has a
nonzero rational floor although its binary64 conversion equals one. These
controls separate exact certification from a floating tolerance assertion.

## Consequence and remaining scope

The existing archive remains a useful numerical approximation and regression
fixture. It cannot serve as an exact arbitrary-accuracy target. A certified
compiler must target the exact source-defined polar operator and regenerate
certified approximations with precision depending on epsilon, explicitly
budgeting numerical error separately from word-synthesis error.

This does not falsify the higher-level existence conjecture, whose ideal target
was exact. Its optimization clause also still needs a named baseline, algorithm,
input family, and resource comparison before an implementation-level test is
possible. The present result rejects one concrete reuse strategy rather than
claiming that a precision defect refutes controllability.

## Verification

    python research/strominger/checkers/check_encoder_archive_accuracy_floor.py

Fresh execution exits 0 and records both requested 1e-18 accuracies as impossible
for the literal archive targets. Receipt:
`results/encoder-archive-accuracy-floor.json`. No numerical encoder rerun,
physical-control test, formal-kernel compilation, or optimizer comparison was
performed. Sources remain unchanged; no commit or push was made.
