# Sinh/cosine defect-weight packet

## Grothendieck source

This formalizes the sign-theoretic core of
`research/grothendieck/theta-defect-velocity-two-copy-sinh-cosine-form.md`.

## Formal objects

- `radialSinhWeight y S = S*sinh(y*S)` is the sum-coordinate factor.
- `radialSinhWeight_nonnegative` proves its universal nonnegative sign for
  outward height `y>=0`.
- `radialSinhWeight_positive` gives strict positivity when `y>0` and `S!=0`.
- `cosineReadout x D` is the relative-coordinate oscillation.
- the two hostile theorems show that positive source and radial weights can
  still produce a negative cosine band and negative combined contribution.

## Assumptions and coefficient type

These order statements are over the real numbers and use the standard real
hyperbolic sine and cosine. No theta density or measure is assumed.

## Missing analytic interfaces

The exact two-copy integral formula requires a normalized even completed
theta density, integrability of the product, justified differentiation under
the integral, the `(u,v)` to `(S,D)` change of variables and Jacobian, and the
even-source pairing. The boundary acceleration identity additionally needs
second differentiation and its relation to `A`, `A'`, and `A''`.

Most importantly, radial positivity does not orient the oscillatory integral.
A source-derived modular/prime transport pairing across `S` and arithmetic
labels remains missing. Fixed-sum Fourier positivity, Hermite--Biehler
orientation, Laguerre positivity, and RH are not asserted.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
