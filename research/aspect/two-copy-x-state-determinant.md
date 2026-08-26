# Two-copy optical determinant observable

## Question

Can the X-state determinant be measured as one linear expectation rather than
reconstructed from several separately estimated quantities?

## Construction

Take two synchronized copies of the two-port polarization state. On the
two-copy basis, define an observable with population-sector weight `+1/2` on
`|01,10>` and `|10,01>`, and coherence-exchange weight `-1/2` between
`|00,11>` and `|11,00>`.

Its expectation on two identical copies is

```text
b c - |z|^2.
```

The nuisance X-state coherence `w` does not contribute. A negative expectation
is therefore exactly the NPT determinant condition for the labelled corner
coherence.

## Why this is a different instrument

The five-setting instrument reconstructs four ingredients and applies a
nonlinear classical decision. The two-copy observable moves that nonlinearity
into physical composition: products of one-copy matrix elements become linear
expectations on two copies.

The observable has only three outcomes, with spectrum contained in
`{-1/2, 0, +1/2}`. This gives a single bounded record and removes the need to
propagate separate population and quadrature intervals.

## Optical frontier

A candidate implementation uses a synchronized source of two entangled pairs,
interference between corresponding copy modes, and number-resolved coincidence
detection to distinguish the population and coherence-exchange spectral
sectors. This packet proves the target observable, not that passive linear
optics can realize its complete spectral measurement deterministically.

That realizability question is now decisive. Even if realizable, two copies
are consumed per trial and four-photon rates may erase any statistical gain.
The immediate benefit is reduced setting and calibration complexity, not a
claimed reduction in source emissions.

## Verification

Run:

```text
python research/aspect/checkers/check_two_copy_x_state_determinant.py
```

The checker uses exact Gaussian-rational arithmetic, verifies the full complex
coherence identity on the asymmetric hostile, freezes the observable spectrum,
and confirms cancellation of nuisance `w`.
