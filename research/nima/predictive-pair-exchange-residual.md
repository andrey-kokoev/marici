# Same geometric/spin return, different retained exchange state

## Result

The prior exchange clue survives an operation-level comparison on actual proton
words. **56 exact checks pass**, after fresh replay of the existing port adapter,
phase bridge and proton spin binding.

Compare the two valid histories from joint endpoint (A,E):

    h = (AB, BC, CA)^2       -- six proton requests
    k = (AB, BC, CA)^4       -- twelve proton requests.

They have the same 60-state geometric prediction and identity spin action for
either lift sign. Nevertheless their existing carrier/record exchange actions
are different. The exact operator difference has **rank 2** and kernel dimension
20 on the full 22-dimensional exchange input space.

The unchanged unit AB-record preparation witnesses the difference. Both outputs
have the same conserved anchor and unit total exchange norm. Thus the difference
is not a changed energy budget or a newly tuned preparation.

This is a concrete history collision, not merely a signed aggregate of different
path families. It shows that the earlier geometric/spin state is not sufficient
for the attached exchange reading. It does not invalidate its sufficiency for
the original centroid observation.

## Existing operations reused

`check_seed_port_exchange_binding.py` supplies the actual six primitive-port
operators E_i, the 16-dimensional carrier metric H and normalized columns f_i.
Its six records are persistent channels, not newly initialized at each event.
The original conditional tail/head port selection remains a declared adapter.

Each arrow in h and k is executed in order in that same model. Both rung policies
retain the complete word and reproduce the exchange and mismatch readings after
recovery. No exchange action is invented for electron requests; this comparison
is restricted to the already bound proton ports.

## Closed mismatch dynamics, with exact reconstruction

Write F for the matrix of six port columns, y for the carrier and r for the six
record coordinates. Define

    a = y + F r,
    delta = r - F^T H y,
    K = I_6 + F^T H F.

The anchor a is conserved by each port exchange. The mismatch is the part that
actually evolves:

    delta' = (I_6 - K[:,i] e_i^T) delta.

For every one of the six ports, the checker verifies this recurrence as a matrix
identity on the entire exchange space. It also verifies the complete change of
coordinates, not just prediction of a selected scalar:

    r = K^-1 (delta + F^T H a),
    y = a - F r.

Encoding and decoding are two-sided inverses. In these coordinates every port
operator is exactly block diagonal, with identity on a and the displayed update
on delta. The mismatch update is involutive and preserves the positive metric
K^-1 inherited from the zero-anchor exchange sector.

Six mismatch coordinates therefore suffice for this attached exchange dynamics.
They have rank six as a readout of the full state. We do not claim minimality for
an unspecified reduced observable. The particular closed-word residual above
uses a rank-two part of this space; it is not claimed to excite all six directions.

## Revised structural picture

For the checked proton-only request domain:

    retained word
        -> geometric predictive state
        -> candidate spin action
        -> evolving exchange mismatch, with conserved anchor.

These are compatible readings of the same word, not asserted to be identical
physical operations. A geometric return can coexist with nonzero change of an
attached state. Full history remains provenance; the evolving mismatch supplies
the missing predictive information for the exchange; the constant anchor allows
reconstruction of its original variables.

This gives a useful refinement of the earlier 60-state quotient: once the
exchange observable is requested, its state must also be retained. Even with a
fixed initial preparation, the concrete collision rules out deriving that
exchange reading from geometric/spin return alone.

## What remains unselected

The comparison does not identify the exchange amplitudes with logical spin,
relative position or mediator variables of the contact-singlet model. The port
metric, feature interpretation and initial excitation remain inherited conditional
inputs. No electron-port extension, physical charge law, interaction schedule,
clock calibration or admission policy is added.

The next meaningful interface question is whether the existing contact/mediator
state has a source-supported map to this actual evolving record sector. Matching
dimensions or attaching arbitrary metadata would not establish that map.

## Reproduction

    OPENBLAS_NUM_THREADS=1 uv run --with sympy --with 'numpy>=2,<3' python research/nima/checkers/check_predictive_pair_exchange_residual.py

Receipt: `results/predictive-pair-exchange-residual.json`.
It contains the collision witness, exact residual rank, encoding/decoding matrices,
mismatch metric and all six reduced updates. New identities are exact symbolic
checks; the imported port adapter separately includes its documented floating-
point comparison with the old whitened fixture.
