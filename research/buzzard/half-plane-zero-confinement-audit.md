# Half-plane zero-confinement audit

## Conditional compiler

`MariciFormal/HalfPlaneZeroConfinement.lean` defines the exact pointwise
certificate sufficient for a control-theoretic RH route after centering the
critical line at the imaginary axis.

A `RightHalfPlaneFactorization completed` contains:

- a unit factor and selected response;
- equality `completed z = unit z * response z` on `Re z > 0`;
- nonvanishing of the unit there;
- strict positive-realness of the response there.

Lean proves that the completed scalar is zero-free in the right half-plane.
If it also satisfies reflection symmetry `completed (-z)=completed z`, every
zero has real part zero.

This is a conditional zero-confinement theorem, not a construction for xi.
The certificate intentionally does not call itself analytic: holomorphy,
domains, pole cancellation, boundary behavior, and source provenance remain
additional interfaces.

## Hostile adapter

The identity impedance `Z(z)=z` is strict positive-real on the right
half-plane. Its Cayley reflection `(z-1)/(z+1)` nevertheless vanishes at
`z=1`. Thus positivity of one typed response cannot be transported to
zero-freeness of another readout merely because a Cayley formula relates them.

## Attempted xi discharge

The current Grothendieck packets provide RH-equivalent Nevanlinna, Herglotz,
Stieltjes, and positivity formulations. They do not independently establish
the strict-positive-real factor required here. Using those equivalences as the
certificate field would assume an RH-equivalent premise. The source-derived
theta plant, authorized selected port, analytic factorization, and
zero-preserving identification with centered xi remain missing.

## Verification

Run from `research/buzzard/marici_formal`:

```powershell
lake env lean MariciFormal/HalfPlaneZeroConfinement.lean
lake build MariciFormal
```

No Git command or Marici site build is part of this audit.

The final targeted command exited zero without output or warnings in about 22
seconds. The project build completed successfully with 8800 jobs. An initial
targeted run remained silent for more than three minutes before interruption;
a heartbeat-bounded diagnostic run then exposed a misplaced contradiction
rewrite and a missing `noncomputable` marker for complex division. After those
defects were repaired, the timing returned to baseline. The project build also
had roughly a 90-second silent interval before reporting its two successful
jobs. These performance discontinuities are retained as tooling observations.
No placeholder or active-conjecture conclusion remains.
