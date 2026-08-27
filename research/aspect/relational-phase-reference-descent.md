# Relational descent of an optical phase record

## Question

When is a sign-sensitive or phase-sensitive optical port a globally defined
observable rather than a gauge-dependent coordinate?

## Exact descent

Let a finite phase gauge act on the signal as `z -> g z`. A linear signal port
is gauge-odd and its orbit average vanishes. Direct intensity `|z|^2` is gauge
invariant, but deliberately deletes the phase.

Introduce a reference coefficient `lambda` in the dual character:

```text
z      -> g z
lambda -> lambda / g
q      = lambda z.
```

Then `q` is invariant under the simultaneous gauge action. Holding the admitted
reference fixed and reversing the target signal reverses `q`, so the descended
record remains sensitive to relative target phase.

The checker freezes `z=3+4i`, `lambda=2-i`, and the four phases
`{1,i,-1,-i}`. Every gauge representative gives the same relational record
`10+5i`, while the linear signal orbit averages to zero.

## Four hostiles

Orbit averaging a standalone linear phase port gives zero. This proves that
averaging repairs invariance by destroying the desired response.

Squaring a real sign signal gives `9` for both `+3` and `-3`. This also descends,
but loses the sign.

A gauge-trivial reference fails: multiplying the signal by the fixed number
`2` produces four different records over the four-element gauge orbit. A local
oscillator is not a reference merely because it is called one; its admitted
transformation law must cancel the signal character.

Finally, a bare sign-reference torsor `{+1,-1}` produces relational records
`{+3,-3}`. Without a source-derived trivialization or an authorized selector,
there is no canonical signed value. Choosing the convenient reference after
seeing the signal would be fitting a gauge section.

## Optical meaning

Balanced homodyne detection implements the relational pairing only when the
local oscillator has a physical phase lineage to the source or to an admitted
common clock. An independent free-running laser defines a changing relative
phase, not an absolute repair. Phase locking supplies a transport relation;
it does not make time or phase absolute.

The same logic governs the `q` versus `-q` spinor proposal. A controlled bypass
is useful only when its phase convention is physically tied to the controlled
implementation in the dual character. Otherwise the predicted sign is a
choice of representative.

## Claim boundary

The checker treats exact Z4 phase and Z2 sign gauges. It does not model phase
noise, reference preparation, detector noise, or nontrivial global topology of
the reference bundle.

## Verification

```text
python research/aspect/checkers/check_relational_phase_reference_descent.py
```
