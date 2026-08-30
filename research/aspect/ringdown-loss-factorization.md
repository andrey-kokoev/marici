# Ringdown and cavity-loss factorization

## Does ringdown separate the loss loci?

Not in the ideal single-mode scalar cavity. Let mirror amplitude return be `m`
and internal amplitude survival be `eta`. Both the steady response and the
ringdown ratio depend on the same round-trip product

```text
rho = m eta.
```

The joint Jacobian of steady response and ringdown ratio with respect to
`(m,eta)` has rank one. A complete noiseless exponential decay provides many
time samples but only one static parameter combination.

This is a useful correction: a new time axis is not automatically a new
identification direction.

## What ringdown does add

Ringdown tests the single-exponential model. The checker freezes
`m=9/10`, `eta=4/5`, hence `rho=18/25`, and verifies five exact powers of
`rho`. It then perturbs one intermediate sample. The three successive ratios
become unequal, creating a fault syndrome for mode mixing, time-dependent
loss, detector memory, or model failure.

Thus ideal ringdown adds execution and fault evidence even when it adds no
static parameter rank.

## Smallest rank-raising port

Add a calibrated mirror-leakage record and the independently derived lossless
mirror relation

```text
L = 1 - m^2.
```

The Jacobian of `(rho,L)` with respect to `(m,eta)` has determinant `2m^2`, so
it is full rank on the positive chamber. In the frozen case, `L=19/100`
recovers `m=9/10`, after which `eta=rho/m=4/5`.

The positive chamber is essential: power leakage alone cannot select the sign
of an amplitude return. The mirror law and chamber must be derived before the
records are inverted.

If the mirror is not lossless, leakage no longer equals `1-m^2`; an independent
absorption or scattering port is then required. Naming an output detector a
“mirror monitor” does not authorize the lossless relation.

## Claim boundary

The result assumes a single scalar mode, known time step, positive amplitudes,
and a lossless calibrated mirror for the leakage port. Mode mixing, detector
convolution, uncertain input coupling, and mirror absorption are outside the
claim.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_ringdown_loss_factorization.py
```
