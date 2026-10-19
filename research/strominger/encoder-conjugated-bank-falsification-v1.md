# A one-bank control reduction fails full-span coverage but not the polar task

## Question

Try to falsify constructive controllability by removing the preceding audit's
assumption of 60 independently selectable phase controls. Retain one existing
frame-zero continuous bank pulse, all 21 discrete native seam reflections,
all 21 discrete occurrence-memory writes, and native rotation. The stored bank
pulse is the first frame-zero entry (its label is retained in the receipt).

Every conjugating word V gives an available conditional software family
V exp(-i theta P) V^-1. This uses no new continuous seam/write phase actuator.
The physical availability of those operations and arbitrary switch schedules
is not inferred. Finite software composition and inverses are the tested policy.

## Risky test and actual residual

The stronger subclaim was that this reduced family already spans the previous
44-dimensional active space. It is false: exact invariant orbit closure has
rank **39**, not 44. The first checker execution failed its rank-44 assertion;
the final checker reports the actual rank and failed subclaim without changing
the operation vocabulary. This failure does not refute the original conjecture,
which allows all existing bank controls and requires only the encoder target.

The checker retains 39 independent actual conjugate directions and their words.
Echelon residuals are used only to decide independence, never as substituted
control directions. Each word is independently replayed and its metric norm
checked. Conjugating words have length at most six. Their nonorthogonality graph
is connected; the receipt retains a spanning tree with exact nonzero overlaps.

## Target-specific hostile

Compute the six-dimensional metric-orthogonal complement of that orbit span.
Every vector there has zero occurrence-memory component and satisfies Bx=0.
Consequently the polar encoder fixes the ENTIRE complement, not merely the
previous one-dimensional common fixed direction. This follows from its actual
polar form: W x=0 and N x=x for Bx=0.

Thus the lost five active dimensions do not create a target-separating fixed
space. Full 44-dimensional coverage was unnecessarily strong for this test.
Connected rank-one controls suggest a smaller controllability proof, but no Lie
algebra certificate or encoder word is claimed here.

## Disposition and verification

Falsified: one-bank conjugation reproduces all 44 active dimensions.
Not falsified: the actual polar encoder can be synthesized from existing controls.
Still missing: constructive synthesis, rigorous arbitrary-accuracy bounds, and
WG composition of its certificates. The physical-control interpretation is not
established by executable matrix operations.

    python research/strominger/checkers/check_encoder_conjugated_bank_controls.py

Fresh final execution exits 0, reporting rank 39, connected overlaps, maximum
word length six, and the polar-fixed complement. The final receipt explicitly
sets `full_active_span_test_passed` to false. Source receipts and checker are
hash-bound but predecessor suites were not rerun.

Artifacts:
- `checkers/check_encoder_conjugated_bank_controls.py`
- `results/encoder-conjugated-bank-controls.json`

This is an exact rational falsification audit, not an Agda or SCC certificate.
No graph publication, commit or push was performed.
