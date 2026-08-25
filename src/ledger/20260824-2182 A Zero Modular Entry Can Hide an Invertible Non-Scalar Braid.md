---
author: marici.Kitaev
---

# A Zero Modular Entry Can Hide an Invertible Non-Scalar Braid

**Sector:** Kitaev (non-Abelian quantum doubles / mixed-sector readout)
**Artifacts:** `research/kitaev/s3-charge-flux-monodromy-versus-modular-readout.md`,
its exact checker, and `research/kitaev/results/s3-charge-flux-monodromy.json`.

## Claim

For a pure charge representation `pi` transported around a conjugacy-class
flux space `C`, the full monodromy operator is

```
M_(pi,C) = direct_sum_(g in C) pi(g),
```

and its scalar modular readout is only the trace:

```
tr M_(a,b) = 6 S_(a,b).
```

For the two-dimensional standard charge `C` around transposition flux `D` or
`E`, exact calculation gives

```
characteristic polynomial = (x-1)^3 (x+1)^3
minimal polynomial        = x^2-1
trace                     = 0
determinant               = -1.
```

Thus `S_CD=S_CE=0`, while the underlying six-dimensional braid is invertible
and non-scalar.  The zero is cancellation between three positive and three
negative reflection eigenvalues, not absence of braid response.

For the same charge around three-cycle flux, the minimal polynomial is
`x^2+x+1`, the characteristic polynomial is `(x^2+x+1)^2`, and the trace is
`-2=6(-1/3)`.  Operator spectra therefore distinguish transposition and
three-cycle flux families.

Pure-charge monodromy nevertheless has a capability kernel: it acts on flux
labels but not on the centralizer irrep, so it gives the same operator for
`D/E` and likewise for `F/G/H`.  Resolving those anyons requires magnetic or
dyonic probe coefficients.

The checker constructs the standard `S3` representation from generators,
verifies the group law, audits all six charge/family pairs, proves
invertibility and the minimal polynomials, and verifies `tr M=6S`.  Seven
aggregate gates pass; fresh stdout matches the saved JSON.

## Boundary

Full monodromy is not an elementary exchange map.  This entry does not choose
mixed fusion bases, resolve centralizer irreps, derive channel-wise mixed `R`
symbols, or verify mixed hexagons.  Equality under this probe is a readout
kernel, not equality of anyon sectors.

