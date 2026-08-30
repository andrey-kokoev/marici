# The Betti boundary obstruction is basis-invariant

Epistemic-graph event: 1329.

## Theorem

Let `S_n:C_n(G)->C_n(H)` be the pairing-forced Betti candidate and set

`Omega_n=D_H,n S_n-S_(n-1) D_G,n`.

Under arbitrary invertible basis changes `P_G,n` and `P_H,n`, the matrices
transform by

`Omega'_n=P_H,n-1^(-1) Omega_n P_G,n`.

Hence the assertion `Omega_n=0`, its rank over a field, and its Smith
invariant factors over the integers are presentation-independent.  No
orientation-preserving relabelling or unimodular change of relative-stratum
basis can repair a genuine nonzero obstruction.

## Proof

In the new bases,

`D'_G,n=P_G,n-1^(-1)D_G,n P_G,n`,

`D'_H,n=P_H,n-1^(-1)D_H,n P_H,n`, and

`S'_n=P_H,n^(-1)S_n P_G,n`.

Substitution into `D'_H,n S'_n-S'_(n-1)D'_G,n` cancels the two intermediate
basis changes and yields the displayed formula.

## Falsifier and acquisition consequence

A witnessed pair `x in C_n(G)` and `lambda in C_(n-1)(H)^*` with

`lambda(Omega_n x) != 0`

is already a coordinate-free falsifier.  A future five-site acquisition need
not use a preferred global basis: source-labelled local strata and their
incidences suffice, provided the comparison maps are invertible and recorded.

Integral modular tests are one-sided.  A nonzero reduction of `Omega_n`
modulo any prime proves an integral obstruction.  Vanishing modulo one prime
does not prove integral vanishing, because every entry may be divisible by
that prime; exact integer matrices or enough divisibility information remain
necessary for a positive result.
