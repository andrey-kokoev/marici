# Executable Global Source Missing-Block Gate

## Result

The global normalization--Cech source remains unconstructed, but its construction
boundary is now executable. The checker
research/voevodsky/check_global_normalization_cech_source_gate.rs records the
known local packets separately and represents every absent comparison by a
typed MissingBlock value.

There is intentionally no default value, zero-matrix conversion, or multiplication
operation for MissingBlock. An absent geometric morphism therefore cannot be
silently interpreted as a zero block in a global differential.

## Earliest missing geometry

The first non-formal datum is the marked ringed-support correspondence

\[
  \{D03,x_1,x_3\}\rightsquigarrow v_+=\{x_1,x_3,x_5\},
\]

together with its reflected minus-side correspondence. Entry 105 proves that
literal pullback along the carrier gives zero while the local trace in entry 100
is nonzero, so ordinary restriction and a literal Cousin boundary cannot supply
this datum. The checker names the resulting typed obligation d_central_flip.

## Retained obligations

The executable gate lists seven unresolved blocks: occurrence/Rees and Tor/Cech
totalization differentials, the central-flip correspondence, two endpoint
comparisons, the full-log carrier comparison, and the central exceptional
two-to-one row.

Known packet ranks are emitted for audit while global source ranks remain
unknown. Global d-squared, Lz=b, Smith normal form, and the endpoint-fixed
mapping fiber therefore are not run.

## Scope

This is a construction-order invariant, not a nonexistence theorem. Filling
every finite block would yield at most a filtered chain candidate; it would not
by itself prove a six-functor kernel, extraordinary base change, properness,
physical parity, or a source identity.

Delegated read-only audits: run-1e3011cd00324c848dc4d5d0ef5035d7 and
run-fa505c830469430292b1a19a1e7502eb.
