# Betti boundary defects obey a Leibniz law under quotient composition

Epistemic-graph event: 1330.

## Composition theorem

Let `q:G->H` and `r:H->J` be composable quotient data.  Assume perfect
pairings force degreewise Betti candidates and coefficient pullback is
strictly compositional, so uniqueness gives

`S_(r q)=S_r S_q`.

Writing `Omega_q=D_H S_q-S_q D_G`, one has

`Omega_(r q)=Omega_r S_q+S_r Omega_q`.

Indeed, insert and subtract `S_r D_H S_q` between
`D_J S_r S_q` and `S_r S_q D_G`.  Thus the boundary defect is a derivation on
the category of pairing-forced correspondences.

## Consequences

- If both stages are physical chain maps, their composite is a chain map.
- A defect in either stage propagates unless it is killed by the adjacent
  forced map or cancels the transported defect of the other stage.
- Therefore a passing composite does **not** certify either constituent.
- If `S_r` is injective and `Omega_r S_q=0`, then nonzero `Omega_q` survives.
  Dually, if `S_q` is surjective and `S_r Omega_q=0`, then nonzero `Omega_r`
  survives on an image representative.

The last two statements are useful only with their stated side condition;
without it, cancellation is real.

## Smallest hostile cancellation

Take rank-one two-term complexes with boundary scalars

`D_G=0`, `D_H=1`, `D_J=0`,

and take both degree components of `S_q` and `S_r` to be the identity.  Then

`Omega_q=1`, `Omega_r=-1`, but `Omega_(r q)=0`.

The composite passes solely because the two transported defects cancel.  It
is therefore invalid to test a five-site multi-bit collapse only at the
terminal quotient and infer that every one-bit physical specialization
exists.

## Five-site acquisition rule

For a filtration collapsing branch bits one at a time, retain each
stagewise boundary packet and compute every `Omega`.  The terminal
commutator is a consistency check, not a replacement for the stagewise
tests.  This remains separate from the presently unavailable physical
relative-chain matrices identified in Ledger 1314.
