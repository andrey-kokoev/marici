# Prime oscillator incidence packet

## Grothendieck source

This covers the convention-fixed finite-cutoff theorem in
`research/grothendieck/prime-oscillator-semigroup-incidence-kernel.md`.

## Formal objects

- `node label` represents `1/p_label`.
- `amplitude label` represents the nonzero critical prime amplitude,
  including any height phase.
- `semigroupIncidence node amplitude` has mode/label entry
  `amplitude(label) * node(label)^mode`.
- `det_semigroupIncidence` gives the amplitude product times the exact
  Vandermonde product.
- `det_semigroupIncidence_ne_zero` proves every finite cutoff has full rank
  from injective nodes and nonzero amplitudes.
- `bare_incidence_has_no_parameter_zero` is simultaneously the hostile: the
  bare incidence determinant cannot be the zero-bearing Xi determinant.

## Assumptions and coefficient type

The cutoff theorem is valid over an arbitrary field. It requires only:

- finitely many labels and modes of the same cardinality;
- injectivity of the semigroup nodes;
- nonvanishing of every column amplitude.

The theorem does not encode primality; distinct nonzero primes imply the
needed injectivity after the sector supplies the map `p -> 1/p`.

## Missing analytic interfaces

The infinite Hilbert--Schmidt theorem requires a typed prime enumeration,
the exact complex amplitude and oscillator normalization, and convergence of
the prime/geometric majorant. The commutator estimate needs unbounded
generator domains. Recovering the unsmoothed Euler Green term needs the
source-derived Schur complement. None is inferred from finite full rank.

Accordingly this file proves neither determinant class for the completed
operator, an Xi determinant, spectral zeros, nor RH.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
