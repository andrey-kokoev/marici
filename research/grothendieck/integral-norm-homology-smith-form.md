# The integral norm homology has universal Smith form

Epistemic-graph event: 1370.

## Smith reduction

Let `G` have order `d>1`, let `R` be a commutative ring, and let `I` be the
augmentation ideal in `R[G]`.  Ledger 1347 gives

`H_T=I/(dI+R(d*1-nu_G))`.

Choose the augmentation basis

`e_g=g-1`, for `g != 1`.

Then `I` is free of rank `d-1` and

`d*1-nu_G=-sum_(g != 1)e_g`.

The coefficient vector `(1,...,1)` is primitive.  An integral unimodular
change of basis sends it to the first basis vector.  Therefore

`H_T congruent (R/dR)^(d-2)`

as an `R`-module.  The isomorphism depends on an ordering and basis choice,
but the invariant-factor statement does not.  For `R=Z`, the Smith normal
form has one unit diagonal entry followed by `d-2` entries equal to `d`.

## Consequences

- The integral obstruction is independent of the multiplication law of `G`;
  only its order enters the underlying coefficient module.
- Each prime divisor of `d` appears simultaneously in
  `(Z/d)^(d-2)`, with its exact prime-power exponent retained.
- Base change to a field of characteristic dividing `d` gives dimension
  `d-2`; base change after inverting `d` gives zero.
- For `S3`, the integral norm-side homology is `(Z/6)^4`, whose reductions
  recover the four-dimensional characteristic-two and characteristic-three
  hostile controls.

The group law can still act on this quotient and can affect additional
representation-theoretic or Loewy structure.  The claim here is only the
underlying coefficient-module Smith form.

## Scope

This classifies the regular group-ring correspondence of Ledger 1347.  It
does not construct a physical chain pushforward or prove that a physical
readout retains the full integral torsion module.
