# Actual cross-component contrast has a three-phase source recurrence

## Operation: reuse the registered successor

Start with the ACTUAL role-labelled LR and RL compositions, each containing
two unit-count words. Extend each by endpoint composition with the whole
original six-occurrence seed. This is the existing retained composition
operation, with both operands and parent bindings kept. Its word domains
agree with the registered successor for the first full period.

No new oscillator, selected signed input, fitted gain or evolution matrix
is inserted. Choosing to iterate this operation is still a declared
construction schedule, not a demonstrated autonomous physical interaction.

## Source-derived exact return

Endpoint counts evolve under the original seed incidence matrix

    M = [0 1 1 0]
        [1 0 0 1]
        [0 1 0 0]
        [1 0 0 0].

The initial difference of the two actual cross products is

    d0=(1,-1,-1,1).

Its successive readings are

    d1=(-2,2,-1,1),
    d2=(1,-1,2,-2),
    d3=d0.

Exactly `(M²+M+I)d0=0`, while neither d1 nor d2 equals d0. Thus this is the
primitive cube-root sector, with least period THREE, populated by the
actual source components rather than by an independently supplied mode.
The polynomial identity proves recurrence for all subsequent iterations;
the checker also composes and counts the retained words directly.

This closes a specific earlier gap: the nontrivial cyclic sector is reached
by actual component occurrence indicators and existing composition. It is
not a preparation inside the old fixed mean-zero resource bank.

## What returns, and what does not

| Quantity | Result |
|---|---|
|Raw role-difference endpoint profile|Exact period three|
|Total count in EACH role channel|2,3,5,8,13,21,34,...|
|Full retained words|Increasing word length and multiplicity; no return|
|Aggregate difference|Zero at every phase|
|Normalized spatial centroid difference|Not periodic; contrast divided by growing count|

In the existing tetrahedral chart, raw spatial contrast takes the values

    (0,0,4), (0,-6,-2), (0,6,-2).

Their squared Euclidean lengths are 16,40,40. This is not a rigid rotation
in that metric and does not establish constant physical oscillator energy.
After three extensions, the normalized centroid difference is one quarter
of its initial value because each channel now has eight words rather than
two. A periodic count difference must not be reported as periodic particle
motion.

## Clock meaning and remaining physical gate

There is now a source-generated three-phase combinatorial readout: current
raw endpoint contrast identifies the extension count modulo three. It does
not recover the number of complete cycles; retained histories supply that
additional construction information.

No physical duration per extension, frequency, clock energy, inertial mass
or autonomous scheduler has been derived. The native constructor can retain
and compute these objects under its explicit function admission, but a
constructor application is not automatically an elapsed physical tick.
The unchanged aggregate rung reader remains blind; the finer retained
endpoint reader sees the phase.

## Formal recurrence and timing boundary

`agda/TriangleSourceContrastClock.agda` now proves the recurrence for EVERY
iteration n. It computes the incidence action from the actual typed six
seed edges and the initial count difference from the native LR/RL joined
words. On the invariant sector `(a,-a,b,-b)`, the derived update is
`(a,b) -> (b-a,-a)`. The proof establishes its third return and rules out
first and second return for the actual initial contrast.

This is a formal source-incidence/count-reader theorem, not a formal proof
of arbitrary-length native path-family continuation. That latter adapter
is still covered by the direct finite retained-word tests.

A conditional scheduling control is decisive: if each newly extended word
in both channels were ONE sequential unit-duration event, the first full
phase cycle would take `2*(3+5+8)=32` units, while the second would take
`2*(13+21+34)=136`. Thus constant event duration under that schedule would
NOT make phase cycles isochronous. Parallel scheduling could differ; no
such timing rule is selected by the source constructor.

More generally, attaching time `t=n*tau` leaves every proved count identity
unchanged for any positive tau. Neither the formal theorem nor the original
composition interface supplies a dimensional constraint selecting tau.
A calibrated clock therefore needs a justified execution/timing law, not
another proof that the contrast repeats. The phase recurrence is now closed;
physical clock-rate selection is not.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module TriangleSourceContrastClock -Fresh
    uv run --with sympy python research/nima/checkers/check_triangle_source_contrast_clock.py

Fresh safe Cubical checking passes. 67 exact checks pass, including receipt
freshness and the conditional sequential timing control. Earlier component,
rung and spatial-reader checks rerun.
Receipts: `results/agda-TriangleSourceContrastClock.json` and
`results/triangle-source-contrast-clock.json`.
